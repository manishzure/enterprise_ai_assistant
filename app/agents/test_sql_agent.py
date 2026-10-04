from app.agents.sql_agent import ask_sql_question


question = "Which employee has the highest salary?"


result = ask_sql_question(question)


print("\nQuestion:")
print(result["question"])

print("\nGenerated SQL:")
print(result["sql"])

print("\nDatabase Result:")
print(result["result"])

print("\nFinal Answer:")
print(result["answer"])
