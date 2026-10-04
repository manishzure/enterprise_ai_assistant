from fastapi import FastAPI

from app.api.employees import router as employee_router
from app.api.departments import router as department_router
from app.api.projects import router as project_router
from app.api.rag import router as rag_router
from app.api.sql import router as sql_router
from app.api.assistant import router as assistant_router


app = FastAPI(
    title="Enterprise AI Data Assistant",
    version="1.0.0"
)


app.include_router(employee_router)
app.include_router(department_router)
app.include_router(project_router)
app.include_router(rag_router)
app.include_router(sql_router)
app.include_router(assistant_router)




@app.get("/")
def home():
    return {
        "message": "Enterprise AI Data Assistant"
    }


@app.get("/about")
def about():
    return {
        "project": "Enterprise AI Data Assistant",
        "version": "1.0"
    }