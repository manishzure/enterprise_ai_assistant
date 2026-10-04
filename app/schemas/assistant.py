from pydantic import BaseModel


class AssistantQuestion(BaseModel):
    question: str


class AssistantResponse(BaseModel):
    category: str
    answer: str
    sql: str | None = None