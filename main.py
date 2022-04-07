from database import get_db
from fastapi import FastAPI, Depends
import logging

import os
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from typing import Optional

from models.Book import Book
from models.Course import Course 
from models.Gradedepartment import Gradedepartment

from schemas.Book import Book as SchemaBook
from schemas.Course import Course as SchemaCourse
from schemas.Gradedepartment import Gradedepartment as SchemaGradedepartment


PATH = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()


@app.get("/")
def get_index():
    return FileResponse(os.path.join(PATH, 'templates', 'index.html'))


@app.get("/books/")
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{id}")
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Book).filter(Book.id == id).first()

@app.get("/courses/")
def get_all_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@app.get("/courses/{id}")
def get_course_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Course).filter(Course.id == id).first()

@app.get("/gradedepartments/")
def get_all_gradedepartments(db: Session = Depends(get_db)):
    return db.query(Gradedepartment).all()

@app.get("/gradedepartments/{id}")
def get_gradedepartment_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Gradedepartment).filter(Gradedepartment.id == id).first()

