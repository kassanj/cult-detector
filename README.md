# 🔍 Is This a Cult?
### RAG-Powered Cult Likelihood Analyzer

Describe any group, company culture, or social dynamic.
Get back a scored likelihood with cited evidence from cult research literature.

## Demo

> Input: "My startup requires 80hr weeks. The CEO is called The Visionary.
>  Questioning the roadmap is called 'not having a builder mindset.'"

> Output: CULT SCORE: 74/100
> VERDICT: Several indicators consistent with high-control organizational culture.
> RESEMBLES: NXIVM (corporate phase, pre-indictment)
> ADVICE: Document everything. Maintain outside relationships.

## Technical Architecture

- **RAG**: ChromaDB vector store with MMR retrieval over curated cult research corpus
- **LangChain LCEL**: Composable chain with RunnableParallel for performance
- **LangSmith**: Full observability — every run traced, latency per step, token costs
- **Structured output**: Pydantic schema enforced via JsonOutputParser

## Stack

Python · LangChain · LangSmith · ChromaDB · OpenAI · FastAPI

## Setup

#### 1. Clone / create repo
`git clone https://github.com/YOU/cult-detector && cd cult-detector`

#### 2. Install
`pip install -r requirements.txt`

#### 3. Environment
`cp .env.example .env`  # fill in your keys

#### 4. Embed documents (once)
`python3 ingest.py`

#### 5. Test in CLI
`python3 main.py`

#### 6. Start API
`uvicorn app:app --reload`

#### 7. View traces
https://smith.langchain.com → your project → every run logged

#### 8. Run evals
`python3 evaluation/eval.py`

#### 9. Push
`git add . && git commit -m "feat: cult detector" && git push`

