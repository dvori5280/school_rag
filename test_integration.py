
from pathlib import Path
import chromadb

from llama_index.vector_stores.chroma import ChromaVectorStore

# Connect to the existing local ChromaDB
db_path = Path(__file__).parent / "chroma_db"

client = chromadb.PersistentClient(path=str(db_path))

# Access the collection we already created
collection = client.get_collection(
    name="school_documents"
)

# Connect ChromaDB to LlamaIndex
vector_store = ChromaVectorStore(
    chroma_collection=collection
)

print("LlamaIndex and ChromaDB connected successfully!")
print("Collection:", collection.name)
print("Stored items:", collection.count())
