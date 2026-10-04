from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


response = llm.invoke(
    "Explain employee leave policy in simple words."
)


print(response.content)