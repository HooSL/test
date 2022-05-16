from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    user_name: str
    age: str

class User(UserBase):
    seq: int

    class Config:
        orm_mode = True