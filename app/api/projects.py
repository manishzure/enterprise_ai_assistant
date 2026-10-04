from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.project import Project
from app.schemas.project import ProjectResponse


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# Get all projects
@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    return projects


# Get project by ID
@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project