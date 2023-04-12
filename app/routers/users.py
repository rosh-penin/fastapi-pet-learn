from fastapi import APIRouter
from sqlalchemy import select

from schemas.users import UserScheme
from models.users import User
from engine import Session

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def get_all_users():
    return Session().scalars(select(User)).all()


@router.post('/')
def create_user(user: UserScheme):
    with Session.begin() as session:
        try:
            db_user = User(**user.create())
            session.add(db_user)
        except Exception:
            session.rollback()
            raise
    return user
