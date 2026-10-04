from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


def classify_question(question: str) -> str:

    prompt = f"""
You are a routing assistant for an enterprise AI system.

Your job is to classify the user's question into exactly ONE of these categories:

SQL
RAG
BOTH

Use these rules:

SQL:
Use SQL when the question requires information from the PostgreSQL database.

Examples:
- How many employees are there?
- Which employee has the highest salary?
- Which department has the most employees?
- Show projects with budget greater than 100000.

RAG:
Use RAG when the question requires information from company documents or policies.

Examples:
- How many paid leaves do employees get?
- What is the work from home policy?
- What is the expense policy?
- What are the employee benefits?

BOTH:
Use BOTH when the question requires information from both the PostgreSQL database and company documents.

Example:
- Which department has the highest average salary and what is the leave policy?

Return ONLY one word:
SQL
RAG
or
BOTH

User question:
{question}

Category:
"""

    response = llm.invoke(prompt)

    category = response.content.strip().upper()

    allowed_categories = {
        "SQL",
        "RAG",
        "BOTH"
    }

    if category not in allowed_categories:
        raise ValueError(
            f"Invalid routing category: {category}"
        )

    return category