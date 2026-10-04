from fastapi import APIRouter, HTTPException

from app.agents.assistant_agent import ask_assistant
from app.schemas.assistant import (
    AssistantQuestion,
    AssistantResponse
)


router = APIRouter(
    prefix="",
    tags=["Assistant"]
)


@router.post("/ask", response_model=AssistantResponse)
def ask(request: AssistantQuestion):

    try:
        result = ask_assistant(request.question)

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        print("Assistant error:", e)

        raise HTTPException(
            status_code=500,
            detail="Failed to process the question."
        )