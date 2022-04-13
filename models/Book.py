from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import Column
from database import Base


class Book(Base):
    __tablename__ = "books2021"
        
    id = Column(Integer, primary_key=True)
    title = Column(String)
    requirement = Column(String)
    author = Column(String)
    isbn13 = Column(String)
    schoolisbn13 = Column(String)
    isbn10 = Column(String)
    schoolisbn10 = Column(String)
    editioncopyright = Column(String)
    publisher = Column(String)
    image = Column(String)
    price = Column(Integer)
