from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    department_id: int | None = None
    budget: Decimal | None = None
    status: str | None = None

    model_config = ConfigDict(from_attributes=True)