from sklearn.metrics import SCORERS
from sqlalchemy.orm import Session

import entity, schema


# 해야할 일
def get_todo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schema.TodoBase):
    db_todo = entity.Todo(
        comment = todo.comment,
        score = todo.score,
        is_active = todo.is_active
        )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo