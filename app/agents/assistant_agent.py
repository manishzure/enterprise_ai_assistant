from langchain_ollama import ChatOllama

from app.agents.router_agent import classify_question
from app.agents.planner_agent import create_plan
from app.agents.sql_agent import ask_sql_question
from app.rag.rag_chain import ask_question


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


def ask_assistant(question: str):

    category = classify_question(question)

    # --------------------------------------------------
    # SQL
    # --------------------------------------------------

    if category == "SQL":

        result = ask_sql_question(question)

        return {
            "category": "SQL",
            "answer": result["answer"],
            "sql": result["sql"]
        }


    # --------------------------------------------------
    # RAG
    # --------------------------------------------------

    elif category == "RAG":

        answer = ask_question(question)

        return {
            "category": "RAG",
            "answer": answer
        }


    # --------------------------------------------------
    # BOTH
    # --------------------------------------------------

    elif category == "BOTH":

        # Step 1: Split the question
        plan = create_plan(question)

        sql_question = plan["sql_question"]
        rag_question = plan["rag_question"]


        # Step 2: Ask database question
        sql_result = ask_sql_question(sql_question)


        # Step 3: Ask document question
        rag_result = ask_question(rag_question)


        # Step 4: Combine both results
        combined_prompt = f"""
You are an enterprise AI assistant.

The user asked:

{question}

The question required information from both
the company database and company documents.

DATABASE INFORMATION:

Database sub-question:
{sql_question}

SQL Query:
{sql_result["sql"]}

Database Result:
{sql_result["result"]}


COMPANY DOCUMENT INFORMATION:

Document sub-question:
{rag_question}

Document Information:
{rag_result}


Instructions:

1. Answer the original user question.
2. Combine the database and document information.
3. Use only the information provided above.
4. Do not invent information.
5. If some information is missing, clearly say so.
6. Give a concise and clear answer.
7. Do not mention internal implementation details.

Final Answer:
"""

        response = llm.invoke(combined_prompt)

        answer = response.content.strip()


        return {
            "category": "BOTH",
            "answer": answer,
            "sql": sql_result["sql"]
        }


    else:

        raise ValueError(
            f"Unsupported category: {category}"
        )