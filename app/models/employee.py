from sqlalchemy import Column, Integer, String, Numeric, Date
from app.database.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    department_id = Column(Integer)
    salary = Column(Numeric(10, 2))
    joining_date = Column(Date)
    manager_id = Column(Integer)