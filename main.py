from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import repository, entity, schema
from database import SessionLocal, engine

entity.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todo_create/")
def get_todo(todo: schema.TodoBase, db: Session = Depends(get_db)):
    db_user = repository.create_todo(db, todo=todo)
    if not db_user:
        raise HTTPException(status_code=400, detail="no data")
    return db_user


# @app.get("/todo_read/", response_model=List[schema.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = repository.get_users(db, skip=skip, limit=limit)
#     return users


