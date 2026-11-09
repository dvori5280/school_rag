
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("OpenAI API key was found.")
else:
    print("OpenAI API key is not configured yet.")
