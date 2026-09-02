from utils.embedder import embed_query
from utils.vectordb import collection


def retrieve(
        question: str,
        pdf_name : str,
        top_k: int = 3):
    query_embedding = embed_query(question)

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = top_k,
        where = {
            "source":pdf_name
        }
    )

    return results



