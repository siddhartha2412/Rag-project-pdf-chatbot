import streamlit as st

from utils.retriever import retrieve
from utils.generator import generate_answer
from utils.loader import load_pdf
from utils.chunker import chunk_text
from utils.embedder import embed_text
from utils.vectordb import store_documents

from pathlib import Path


st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📚"
)

st.title("📚 PDF RAG Chatbot")
st.caption("Upload a PDF and ask questions about it.")


# -------------------------
# PDF Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
    key="pdf_uploader"
)


if uploaded_file is not None:

    if (
        "processed_pdf" not in st.session_state
        or st.session_state.processed_pdf != uploaded_file.name
    ):

        temp_path = "uploaded.pdf"

        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        text = load_pdf(temp_path)

        chunks = chunk_text(text)

        with st.spinner("Creating embeddings..."):
            documents = embed_text(chunks)

        pdf_name = Path(uploaded_file.name).name

        store_documents(
            documents,
            pdf_name
        )

        st.session_state.processed_pdf = uploaded_file.name
        st.session_state.pdf_name = pdf_name


        st.success(
            f"✅ {pdf_name} processed successfully! "
            f"{len(chunks)} chunks stored."
        )


# -------------------------
# Chat History
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# -------------------------
# Chat Input
# -------------------------

question = st.chat_input(
    "Ask something about the PDF..."
)


if question:

    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    results = retrieve(
        question,
        pdf_name = st.session_state.pdf_name
        )

    context = "\n\n".join(
        results["documents"][0]
    )


    answer = generate_answer(
        question,
        context
    )


    with st.chat_message("assistant"):
        st.write(answer)


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })