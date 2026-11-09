
from pathlib import Path

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

# Step 1: Locate the documents
data_dir = Path(__file__).parent / "data"

# Step 2: Load the documents
documents = SimpleDirectoryReader(
    input_dir=str(data_dir),
    required_exts=[".txt"]
).load_data()

print(f"Loaded {len(documents)} documents")

# Step 3: Configure the chunking method
splitter = SentenceSplitter(
    chunk_size=256,
    chunk_overlap=50
)

# Step 4: Split documents into chunks
nodes = splitter.get_nodes_from_documents(documents)

# Step 5: Display the results
print(f"Created {len(nodes)} chunks")

for i, node in enumerate(nodes, start=1):
    print(f"\nChunk {i}")
    print("Source:", node.metadata.get("file_name"))
    print("Characters:", len(node.text))


from html import escape

# Create an HTML preview of all chunks
html_content = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>School RAG - Chunks Preview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            direction: rtl;
            margin: 30px;
            background: #f5f7fa;
        }
        .chunk {
            background: white;
            padding: 20px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 10px;
        }
        .content {
            white-space: pre-wrap;
            line-height: 1.8;
        }
    </style>
</head>
<body>
<h1>בדיקת חלוקת המסמכים ל-Chunks</h1>
"""

for i, node in enumerate(nodes, start=1):
    source = escape(node.metadata.get("file_name", "Unknown"))
    content = escape(node.text)

    html_content += f"""
    <div class="chunk">
        <h2>מקטע {i}</h2>
        <p><strong>קובץ מקור:</strong> {source}</p>
        <div class="content">{content}</div>
    </div>
    """

html_content += "</body></html>"

preview_path = Path(__file__).parent / "chunks_preview.html"

preview_path.write_text(html_content, encoding="utf-8")

print("Created chunks_preview.html")
