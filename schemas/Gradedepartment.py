from pydantic import BaseModel


class Gradedepartment(BaseModel):
    name: str

    class Config:
        orm_mode = True
