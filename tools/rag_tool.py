import chromadb
from chromadb.utils import embedding_functions
import os

# Setup ChromaDB client and collection
client = chromadb.PersistentClient(path="./vector_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="research_docs",
    embedding_function=embedding_fn
)

def add_to_vectordb(texts: list[str], ids: list[str] = None):
    if not texts:
        return
    if ids is None:
        ids = [f"doc_{i}" for i in range(len(texts))]
    collection.upsert(documents=texts, ids=ids)

def search_vectordb(query: str, n_results: int = 3) -> str:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    docs = results["documents"][0]
    if not docs:
        return ""
    return "\n".join(docs)