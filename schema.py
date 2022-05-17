from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

# 해야할 일
class TodoBase(BaseModel):
    comment: str
    score: int
    is_active: int


class Todo(TodoBase):
    seq: int

    class Config:
        orm_mode = True