import os

from dotenv import load_dotenv
from urllib.parse import quote_plus

from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama


load_dotenv()


# --------------------------------------------------
# 1. PostgreSQL connection
# --------------------------------------------------

DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")


database_uri = (
    f"postgresql+psycopg://{DB_USER}:"
    f"{quote_plus(DB_PASSWORD)}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


db = SQLDatabase.from_uri(database_uri)


# --------------------------------------------------
# 2. Ollama LLM
# --------------------------------------------------

llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


# --------------------------------------------------
# 3. Test function
# --------------------------------------------------

def ask_sql_question(question: str):

    # ---------------------------------------------
    # 1. Get database schema
    # ---------------------------------------------

    schema = db.get_table_info()


    # ---------------------------------------------
    # 2. Generate SQL
    # ---------------------------------------------

    sql_prompt = f"""
You are a SQL assistant.

You have access to a PostgreSQL database.

Database schema:

{schema}

User question:

{question}

Write ONLY the SQL query needed to answer the question.

Rules:
- Only generate SELECT queries.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, or CREATE queries.
- Do not explain the query.
- Do not use markdown.
- Do not use ```sql.

SQL:
"""

    response = llm.invoke(sql_prompt)

    sql_query = response.content.strip()

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()


    # ---------------------------------------------
    # 3. Safety check
    # ---------------------------------------------

    if not sql_query.lower().startswith("select"):
        raise ValueError(
            "Only SELECT queries are allowed."
        )


    # ---------------------------------------------
    # 4. Execute SQL
    # ---------------------------------------------

    result = db.run(sql_query)


    # ---------------------------------------------
    # 5. Ask LLM to explain result
    # ---------------------------------------------

    answer_prompt = f"""
You are an enterprise database assistant.

Answer the user's question using the SQL result below.

User question:
{question}

SQL query:
{sql_query}

Database result:
{result}

Rules:
- Answer using only the database result.
- Do not invent information.
- Give a concise and clear answer.
- Do not mention internal prompts or implementation details.

Answer:
"""

    answer_response = llm.invoke(answer_prompt)

    answer = answer_response.content.strip()


    return {
        "question": question,
        "sql": sql_query,
        "result": result,
        "answer": answer
    }