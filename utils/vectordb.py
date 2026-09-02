import chromadb

client = chromadb.PersistentClient(
    path=  "database"
)

collection = client.get_or_create_collection(
    name = "pdf_chunks"
)


def store_documents(
    documents: list[dict],
    pdf_name: str
):

    ids = []
    texts = []
    embeddings = []
    metadatas = []

    for i,doc in enumerate(documents):

        ids.append(f"{pdf_name}_chunk_{i}")

        texts.append(doc["text"])

        embeddings.append(doc["embedding"])

        metadatas.append(
            {
                "source":pdf_name,
                "chunk":i
            }
        )
    collection.add(
        ids = ids,
        documents= texts,
        embeddings=embeddings,
        metadatas=metadatas
    )