from app.agents.planner_agent import create_plan


question = """
Which department has the highest average salary
and what is the work from home policy?
"""


result = create_plan(question)


print("=" * 70)
print("SQL QUESTION")
print("=" * 70)

print(result["sql_question"])


print("\n" + "=" * 70)
print("RAG QUESTION")
print("=" * 70)

print(result["rag_question"])