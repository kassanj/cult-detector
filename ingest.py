"""
Run this once to embed your cult documents into ChromaDB.
Documents are chunked, embedded, and stored locally in ./chroma_db
Subsequent runs skip already-embedded documents.

Run:
    python3 ingest.py

To re-ingest all documents, delete the ./chroma_db directory.
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from data.cult_docs import CULT_DOCUMENTS

load_dotenv()

CHROMA_PATH = "./chroma_db"


def ingest():
    print("🔍 Starting document ingestion...")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",   # fast + cheap, good quality
        chunk_size=100,                   # batch size for parallel embedding
    )

    # Convert to LangChain Document format
    documents = [
        Document(
            page_content=doc["text"],
            metadata={
                "id": doc["id"],
                "category": doc["category"],
                "source": doc["source"],
            }
        )
        for doc in CULT_DOCUMENTS
    ]

    # Check if DB already exists
    if os.path.exists(CHROMA_PATH):
        print("📦 ChromaDB exists — adding any new documents only...")
        vectorstore = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings,
            collection_name="cult_docs"
        )
        existing_ids = set(vectorstore.get()["ids"])
        new_docs = [d for d in documents if d.metadata["id"] not in existing_ids] # only add new documents
        if new_docs:
            vectorstore.add_documents(new_docs)
            print(f"✅ Added {len(new_docs)} new documents")
        else:
            print("✅ All documents already ingested")
   
    # if the database does not exist, create it
    else:
        print("🆕 Creating new ChromaDB...")
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=CHROMA_PATH,
            collection_name="cult_docs"
        )
        print(f"✅ Ingested {len(documents)} documents into ChromaDB")

    print(f"📍 Vector store location: {CHROMA_PATH}")
    return vectorstore


if __name__ == "__main__": # run the script when the file is executed directly
    ingest()