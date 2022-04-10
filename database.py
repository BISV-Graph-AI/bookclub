from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")  # or other relevant config var
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        print('get_db Exception: ' + str(err))
        db.close()

def get_engine_connect():
    engine_connect = None
    try:
        engine_connect = engine.connect() 
    except Exception as err:
        print('get_engine_connect Exception: ' + str(err))
        engine_connect = None
    return engine_connect

def get_results(query):
    results = None 
    try:
        engine_connect = get_engine_connect()
        if (engine_connect is not None):
            with engine_connect as conn:
                statement = text(query)
                results = conn.execute(statement)
    except Exception as err:
        print('get_results Exception: ' + str(err))
        results = None 
    return results
