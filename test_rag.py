
from utils.rag_pipeline import answer_question


question = "What is probability?"

answer = answer_question(question)

print("\nQuestion:")
print(question)



print("\nAnswer:")
print(answer)