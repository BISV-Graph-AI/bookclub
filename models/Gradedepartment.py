from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import Column
from database import Base


class Gradedepartment(Base):
    __tablename__ = 'gradedepartments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
