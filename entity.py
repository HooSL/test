from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    seq = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    age = Column(String, nullable=False)