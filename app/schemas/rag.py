from pydantic import BaseModel


class RAGQuestion(BaseModel):
    question: str


class RAGResponse(BaseModel):
    answer: str