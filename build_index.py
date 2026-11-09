
import truststore
truststore.inject_into_ssl()

from pathlib import Path
from dotenv import load_dotenv
import chromadb

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding

# Project paths
project_dir = Path(__file__).parent
data_dir = project_dir / "data"
db_dir = project_dir / "chroma_db"

# Load API key
load_dotenv(project_dir / ".env")

# Load school documents
documents = SimpleDirectoryReader(
    input_dir=str(data_dir),
    required_exts=[".txt"]
).load_data()

print(f"Loaded {len(documents)} documents")

# Split documents into chunks
splitter = SentenceSplitter(
    chunk_size=256,
    chunk_overlap=50
)

nodes = splitter.get_nodes_from_documents(documents)
print(f"Created {len(nodes)} chunks")

# Connect to ChromaDB
client = chromadb.PersistentClient(path=str(db_dir))
collection = client.get_or_create_collection(
    name="school_documents"
)

print(f"Existing chunks in ChromaDB: {collection.count()}")



# Prevent duplicate indexing
if collection.count() > 0:
    print("Database already contains data. Skipping indexing.")
else:
    print("Database is empty. Ready to create embeddings.")

    embed_model = OpenAIEmbedding(
        model="text-embedding-3-small"
    )

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
        embed_model=embed_model
    )

    print("Index created successfully!")
    print(f"Stored chunks: {collection.count()}")
