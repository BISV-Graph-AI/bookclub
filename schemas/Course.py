from pydantic import BaseModel


class Course(BaseModel):
    name: str

    class Config:
        orm_mode = True
