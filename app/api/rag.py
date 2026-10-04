from fastapi import APIRouter

from app.rag.rag_chain import ask_question
from app.schemas.rag import RAGQuestion, RAGResponse


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.post("/ask", response_model=RAGResponse)
def ask_rag(request: RAGQuestion):

    answer = ask_question(request.question)

    return {
        "answer": answer
    }