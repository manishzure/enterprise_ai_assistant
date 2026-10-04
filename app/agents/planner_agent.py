from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


def create_plan(question: str):

    prompt = f"""
You are a planning assistant for an enterprise AI system.

The user's question requires information from both:

1. A PostgreSQL database
2. Company documents

Split the user's question into two smaller questions.

Return exactly:

SQL: <database question>
RAG: <document question>

Rules:

- SQL must only contain the database-related part.
- RAG must only contain the company-document-related part.
- Do not answer the questions.
- Do not write SQL.
- Do not add explanations.
- Always provide both lines.

User question:

{question}

Plan:
"""

    response = llm.invoke(prompt)

    plan = response.content.strip()

    sql_question = ""
    rag_question = ""

    for line in plan.splitlines():

        line = line.strip()

        if line.upper().startswith("SQL:"):
            sql_question = line[4:].strip()

        elif line.upper().startswith("RAG:"):
            rag_question = line[4:].strip()

    if not sql_question:
        raise ValueError("Planner failed to create SQL question.")

    if not rag_question:
        raise ValueError("Planner failed to create RAG question.")

    return {
        "sql_question": sql_question,
        "rag_question": rag_question
    }