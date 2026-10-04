from sqlalchemy import Column, Integer, String, Numeric

from app.database.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    project_name = Column(String(200), nullable=False)
    department_id = Column(Integer)
    budget = Column(Numeric(12, 2))
    status = Column(String(50))