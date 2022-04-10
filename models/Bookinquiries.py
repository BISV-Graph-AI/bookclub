from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import Column
from database import Base


class Bookinquiries(Base):
    __tablename__ = "bookinquiries"
        
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    buyorsell = Column(String)
    isbn13s = Column(String)
    createdat = Column(DateTime)
