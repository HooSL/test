from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


# 해야할 일
class Todo(Base):
    __tablename__ = "todo"

    seq = Column(Integer, primary_key=True, index=True, Auto_Increment=True)
    comment = Column(String, Not_Null=True)
    score = Column(Integer, Not_Null=True)
    datetime = Column(TIMESTAMP, Not_Null=True, default='CURRENT_TIMESTAMP')
    is_active = Column(Integer, default=False)
