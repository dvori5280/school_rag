
from pathlib import Path
from dotenv import load_dotenv
import chromadb

from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding

project_dir = Path(__file__).parent
load_dotenv(project_dir / ".env")

# Connect to the existing ChromaDB database
client = chromadb.PersistentClient(
    path=str(project_dir / "chroma_db")
)

collection = client.get_or_create_collection(
    name="school_documents"
)

def retrieve_documents(question):
    if collection.count() == 0:
        return []

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    embed_model = OpenAIEmbedding(
        model="text-embedding-3-small"
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model
    )

    retriever = index.as_retriever(
        similarity_top_k=3
    )

    return retriever.retrieve(question)
