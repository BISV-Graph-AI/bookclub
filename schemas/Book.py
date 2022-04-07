from pydantic import BaseModel


class Book(BaseModel):
    title: str
    requirement: str
    author: str
    isbn13: str
    schoolisbn13: str
    isbn10: str
    schoolisbn10: str
    editioncopywright: str
    publisher: str
    image: str
    price: int

    class Config:
        orm_mode = True
