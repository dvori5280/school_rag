
from pathlib import Path
from llama_index.core import SimpleDirectoryReader

data_dir = Path(__file__).parent / "data"

documents = SimpleDirectoryReader(
    input_dir=str(data_dir),
    required_exts=[".txt"]
).load_data()

print(f"Loaded {len(documents)} documents")
