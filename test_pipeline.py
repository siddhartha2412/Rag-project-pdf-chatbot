from pathlib import Path

from utils.loader import load_pdf
from utils.chunker import chunk_text
from utils.embedder import embed_text
from utils.vectordb import store_documents

pdf_path = "data/Probability.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(text)

documents = embed_text(chunks)

pdf_name = Path(pdf_path).name

store_documents(documents,pdf_name)

print("✅ PDF stored successfully in ChromaDB.")