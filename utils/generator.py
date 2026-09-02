from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question: str, context: str):

    prompt = f"""
        You are a helpful assistant answering questions based on a provided document.

        Use ONLY the information given in the context.

        If the answer is not present in the context, say:
        "I don't know based on the provided document."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text