from utils.retriever import retrieve

question = "What is probability?"

results = retrieve(
    question,
    pdf_name="Probability.pdf",
    top_k=3
)

print("\nRetrieved Chunks:\n")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"--- Chunk {i} ---")
    print(document)
    print()