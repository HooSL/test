from sqlalchemy.orm import Session

import entity, schema

def create_user(db: Session, user: schema.UserBase):
    db_user = entity.User(
        user_name=user.user_name, 
        age=user.age
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.User).offset(skip).limit(limit).all()




# def get_list(db: Session):
#     db.query(entity.User).all()
