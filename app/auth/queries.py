from sqlmodel import select, Session
from .models import User


def register_user(data: User, session: Session):
    user = User(**data.dict())
    session.add(user)
    session.commit()
    return user

def get_users(session: Session):
    query = session.exec(select(User)).all()
    return query