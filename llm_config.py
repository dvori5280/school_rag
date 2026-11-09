
from pathlib import Path
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

def get_llm():
    return OpenAI(
        model="gpt-5-mini",
        temperature=1
    )
