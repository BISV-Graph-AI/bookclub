import datetime
from pydantic import BaseModel


class Bookinquiries(BaseModel):
    name: str
    email: str
    buyorsell: str
    isbn13s: str
    createdat: datetime.datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
