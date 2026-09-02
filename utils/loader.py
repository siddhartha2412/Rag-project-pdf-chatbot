import pymupdf
from pathlib import Path


def load_pdf(pdf_path):
    """
    Read every page from a PDF and return :
    - the full extracted text
    - page-wise information (for metadata later)
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"{pdf_path} not found.")
       
    pages = []
    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            pages.append(page.get_text())
    text = "\n\n".join(pages)
    return text
    