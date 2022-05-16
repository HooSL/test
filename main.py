from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import repository as r

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def read_users(user:schema.UserBase, db:Session = Depends(get_db)):
    r.create_user(db=db, user=user)
    return user