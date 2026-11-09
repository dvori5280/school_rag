
import truststore
truststore.inject_into_ssl()



from pathlib import Path
from dotenv import load_dotenv
from llama_index.embeddings.openai import OpenAIEmbedding

# Load the API key from .env
load_dotenv(Path(__file__).parent / ".env")

# Use the embedding model we selected
embed_model = OpenAIEmbedding(
    model="text-embedding-3-small"
)

# Send a short test sentence
embedding = embed_model.get_text_embedding(
    "שלום, זהו משפט בדיקה של בית ספר אופק."
)

print("OpenAI connection successful!")
print("Embedding dimensions:", len(embedding))
