from database import *
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

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
BOOK_HEADER = 'title,author,publisher,isbn13,requirement,price,image'
BOOK_HEADER_ARRAY = BOOK_HEADER.split(',')


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def book_retrieve_util(query):
    print(query)
    results = get_results(query)
    ret_list = []
    for result in results:
        ret_dict = {}
        for header_index, header in enumerate(BOOK_HEADER_ARRAY):
            ret_dict[BOOK_HEADER_ARRAY[header_index]] = result[header_index]
        ret_list.append(ret_dict)
    return ret_list

@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    #return FileResponse(os.path.join(PATH, 'templates', 'index.html'))

@app.get("/books")
def get_all_books(g: int, c: str):
    query = """
    SELECT DISTINCT {}
    FROM GDS_COURSES_BOOKS MAP
    JOIN BOOKS B ON MAP.BOOKS_ID = B.ID 
    WHERE MAP.GRADEDEPARTMENTS_ID = {} 
    """.format(BOOK_HEADER, str(g))
    if (c.strip() != ''):
        query += " AND COURSES_ID IN (" + c + ")"
    query += ";"
    return book_retrieve_util(query)

@app.get("/search")
def search_books(q: str):
    query = """
    SELECT DISTINCT {}
    FROM BOOKS
    """.format(BOOK_HEADER)
    if (q is not None and len(q) > 2):
        query += "WHERE TITLE ILIKE '%" + q + "%'"
    query += ';'
    return book_retrieve_util(query)


@app.get("/books/{id}")
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Book).filter(Book.id == id).first()

@app.get("/courses/")
def get_all_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@app.get("/courses/{id}")
def get_course_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Course).filter(Course.id == id).first()

@app.get("/courses_by_gdid/{gdid}")
def get_courses_by_gdid(gdid: int, db: Session = Depends(get_db)):
    results = get_results("SELECT DISTINCT COURSES_ID, C.NAME FROM GDS_COURSES MAP JOIN COURSES C ON MAP.COURSES_ID = C.ID WHERE GRADEDEPARTMENTS_ID = " + str(gdid) + " ORDER BY 2;")
    ret_list = []
    for result in results:
        ret_dict = {}
        ret_dict['id'] = result[0]
        ret_dict['name'] = result[1]
        ret_list.append(ret_dict)
    return ret_list

@app.get("/gradedepartments/")
def get_all_gradedepartments(db: Session = Depends(get_db)):
    return db.query(Gradedepartment).all()

@app.get("/gradedepartments/{id}")
def get_gradedepartment_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Gradedepartment).filter(Gradedepartment.id == id).first()

