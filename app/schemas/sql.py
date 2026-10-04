from pydantic import BaseModel


class SQLQuestion(BaseModel):
    question: str


class SQLResponse(BaseModel):
    question: str
    sql: str
    result: str
    answer: str
    