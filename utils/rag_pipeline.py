from utils.retriever import retrieve
from utils.generator import generate_answer


def answer_question(question: str, top_k: int = 3) -> str:
    """
    Retrieve relevant chunks and generate an answer.
    """

    results = retrieve(
        question,
        top_k=top_k
    )

    chunks = results["documents"][0]

    context = "\n\n".join(chunks)

    answer = generate_answer(
        question,
        context
    )

    return answer