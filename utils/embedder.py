from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(chunks: list[str]) -> list[dict]:
    """
    Generate embeddings for document chunks.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    documents = []

    for chunk, embedding in zip(chunks, embeddings):
        documents.append({
            "text": chunk,
            "embedding": embedding.tolist()
        })

    return documents


def embed_query(question: str):
    """
    Generate embedding for a user question.
    """

    embedding = model.encode(
        question,
        convert_to_numpy=True
    )

    return embedding.tolist()