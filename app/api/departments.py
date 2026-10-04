from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.department import Department
from app.schemas.department import DepartmentResponse


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


# Get all departments
@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):

    departments = db.query(Department).all()

    return departments


# Get department by ID
@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department