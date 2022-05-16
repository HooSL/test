from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import repository as r

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user_insert/")
def read_users(user:schema.UserBase, db:Session = Depends(get_db)):
    r.create_user(db=db, user=user)
    return user

@app.get("/user_list/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = r.get_user(db, skip=skip, limit=limit)
    return user