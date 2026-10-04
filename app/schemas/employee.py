from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department_id: int | None = None
    salary: Decimal | None = None
    joining_date: date | None = None
    manager_id: int | None = None

    model_config = ConfigDict(from_attributes=True)