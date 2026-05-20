"""
Simple RAG chain for cult likelihood analysis.
No optimizations — just the core pattern clearly laid out:

1. Take user input
2. Search ChromaDB for relevant documents
3. Stuff documents into a prompt
4. Send to LLM
5. Parse structured output
"""

import asyncio
from typing import AsyncIterator # for asyncio
from dotenv import load_dotenv # load environment variables

from langchain_openai import ChatOpenAI, OpenAIEmbeddings # LLM
from langchain_community.vectorstores import Chroma # vector store
from langchain_core.prompts import ChatPromptTemplate # prompt
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field # output schema
from langchain_community.cache import InMemoryCache # cache
from langchain.globals import set_llm_cache # to set the cache

# set the cache
set_llm_cache(InMemoryCache())
load_dotenv()

CHROMA_PATH = "./chroma_db"


# ── STEP 1: DEFINE WHAT YOU WANT BACK ────────────────────────────
# Pydantic schema tells the LLM exactly what JSON to return
class CultEvidence(BaseModel):
    indicator: str = Field(description="The specific cult indicator found")
    source: str = Field(description="The source document this came from")
    severity: str = Field(description="low | medium | high")

class CultAnalysis(BaseModel):
    score: int = Field(description="Cult likelihood score 0-100")
    verdict: str = Field(description="Deadpan one-line verdict")
    indicators_found: list[CultEvidence] = Field(description="Specific evidence found")
    closest_cult_match: str = Field(description="The real group this most resembles")
    advice: str = Field(description="Deadpan advice for the person")
    safe_to_leave: bool = Field(description="Whether leaving seems psychologically safe")


# ── STEP 2: WRITE THE PROMPT ──────────────────────────────────────
SYSTEM_PROMPT = """You are a deadpan cult analysis system with encyclopedic knowledge
of high-control groups. You analyze descriptions with clinical detachment and mild concern.

You have been provided with retrieved evidence from cult research literature.
Use ONLY this evidence to support your analysis — cite sources directly.

Scoring guide:
0-20:   Normal group with minor quirks
21-40:  Mildly concerning. Worth monitoring.
41-60:  Several red flags. Proceed with caution.
61-80:  Strong cult indicators. Document everything.
81-100: Textbook cult. Exit strategy recommended.

Tone: deadpan, clinical, mildly alarmed. Never dramatic. Never funny on purpose.
The humor comes from the absolute seriousness with which you treat absurd situations.

Return ONLY valid JSON matching the schema. No preamble. No markdown."""

HUMAN_PROMPT = """Analyze this group or situation for cult indicators:

DESCRIPTION:
{description}

RETRIEVED EVIDENCE FROM CULT RESEARCH:
{retrieved_docs}

Respond with JSON only."""


# ── STEP 3: LOAD THE VECTOR STORE ────────────────────────────────
# ChromaDB was populated by ingest.py
# Now we load it and create a retriever
def get_retriever():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name="cult_docs"
    )

    # as_retriever() turns the vector store into something the chain can call
    # search_type="mmr" means use the Maximum Marginal Relevance algorithm to return the most relevant documents
    # feeding the model a diverse set of source documents results in more comprehensive, well-rounded, and informative answers
    # k=6 means return the 6 most relevant documents
    # fetch_k=20 means fetch 20 documents from the vector store
    # lambda_mult=0.7 means use 0.7 as the lambda multiplier
    retriever = vectorstore.as_retriever(
        # search_kwargs={"k": 6}
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20,
            "lambda_mult": 0.7
        }
    )

    return retriever


# ── STEP 4: FORMAT RETRIEVED DOCS FOR THE PROMPT ─────────────────
# The retriever returns Document objects
# This turns them into a readable string for the prompt
def format_docs(docs) -> str:
    return "\n\n".join([
        f"[SOURCE: {doc.metadata.get('source', 'Unknown')}]\n"
        f"[CATEGORY: {doc.metadata.get('category', 'Unknown')}]\n"
        f"{doc.page_content}"
        for doc in docs
    ])


# ── STEP 5: BUILD THE CHAIN ──────────────────────────────
def build_chain():
    """
    Builds the chain.

    The flow: description → retriever → format docs → prompt → LLM
    Returns the chain.
    """

    # Load the retriever
    retriever = get_retriever()

    # Set up the LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.1,
        streaming=True,
    ).with_structured_output(CultAnalysis)

    # Set up the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT)
    ])

    # Define a function to retrieve and format the documents
    def retrieve_and_format(inputs):
        docs = retriever.invoke(inputs["description"])
        return {
            "description": inputs["description"],
            "retrieved_docs": format_docs(docs)
        }

    # Build the chain using LCEL pipe syntax
    # RunnableLambda is used to apply a function to the input
    # | is used to chain the functions together
    chain = (
        RunnableLambda(retrieve_and_format)
        | prompt
        | llm
    )

    return chain

# ── STEP 6: RUN THE SYNCHRONOUS CHAIN ──────────────────────────────
# Only used for testing
def analyze(description: str) -> dict:
    """
    Takes a description, returns cult analysis.
    """
    chain = build_chain()
    analysis = chain.invoke({"description": description})
    if isinstance(analysis, CultAnalysis):
        return analysis.model_dump()
    return analysis


# ── STEP 6: RUN THE ASYNC CHAIN ──────────────────────────────
# Only used for the API 
async def analyze_async(description: str) -> dict:
    """
    Takes a description, returns cult analysis.
    """
    chain = build_chain()
    analysis = await chain.ainvoke({"description": description})
    if isinstance(analysis, CultAnalysis):
        return analysis.model_dump()
    return analysis

# ── STEP 6: RUN THE STREAMING CHAIN ──────────────────────────────
# Only used for streaming responses in the API
async def analyze_stream(description: str) -> AsyncIterator[str]:
    """
    Streams tokens as they generate.
    Used when request.stream = True in app.py.
    """
    chain = build_chain()
    async for chunk in chain.astream({"description": description}):
        if isinstance(chunk, CultAnalysis):
            yield chunk.model_dump_json()
        else:
            yield str(chunk)
        await asyncio.sleep(0.03)  # ← add this — 30ms delay between chunks

# ── QUICK TEST ────────────────────────────────────────────────────
if __name__ == "__main__":


    test = "My startup has weekly all-hands where the CEO shares his vision \
            for humanity. Questioning the roadmap is called 'not being a \
            builder mindset'. We work weekends because we're 'changing the world'."

    # print("Analyzing...\n")
    # result = analyze(test)

    # print(f"CULT SCORE: {result['score']}/100")
    # print(f"VERDICT:    {result['verdict']}")
    # print(f"RESEMBLES:  {result['closest_cult_match']}")
    # print(f"ADVICE:     {result['advice']}")
    # print(f"\nINDICATORS:")
    # for i in result['indicators_found']:
    #     print(f"  [{i['severity'].upper()}] {i['indicator']}")
    #     print(f"  Source: {i['source']}")

    # print("Testing sync version...\n")
    # result = analyze(test)
    # print(f"SYNC  → Score: {result['score']}/100 | {result['verdict']}\n")
 
    # print("Testing async version...\n")
    # # asyncio.run() creates the event loop needed to run async from a script
    # result_async = asyncio.run(analyze_async(test))
    # print(f"ASYNC → Score: {result_async['score']}/100 | {result_async['verdict']}\n")
 
    # print("Both versions return identical results — difference is under the hood.")

    # print("\nTesting streaming version...\n")

    # async def test_stream():
    #     async for chunk in analyze_stream(test):
    #         print(chunk, end="", flush=True)
    #     print()  # newline at the end

    # asyncio.run(test_stream())