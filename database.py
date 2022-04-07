from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgres://qxlwehffsjoldk:50d2815916dbc44c0b33b307d73cc136ee3b87e9c95b861d5dbec8fde8352f24@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d25t8boh3a6en5'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        print(str(err))
        db.close()
