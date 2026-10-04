from app.rag.rag_chain import ask_question


question = "How many days can employees work from home?"

answer = ask_question(question)


print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)