from fastapi import APIRouter, HTTPException

from app.agents.sql_agent import ask_sql_question
from app.schemas.sql import SQLQuestion, SQLResponse


router = APIRouter(
    prefix="/sql",
    tags=["SQL"]
)


@router.post("/ask", response_model=SQLResponse)
def ask_sql(request: SQLQuestion):

    try:
        result = ask_sql_question(request.question)

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail="Failed to process SQL question."
        )