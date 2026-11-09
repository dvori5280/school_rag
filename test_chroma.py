
from pathlib import Path
import chromadb

# Create a local database folder
db_path = Path(__file__).parent / "chroma_db"

# Connect to ChromaDB
client = chromadb.PersistentClient(path=str(db_path))

# Create a collection if it doesn't exist
collection = client.get_or_create_collection(
    name="school_documents"
)

print("ChromaDB connected successfully!")
print("Collection name:", collection.name)
print("Number of stored items:", collection.count())
