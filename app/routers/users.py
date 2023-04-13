from fastapi import APIRouter
from sqlalchemy import select

from app.schemas.users import UserScheme
from app.models.users import User
from app.engine import Session

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
            db_user = User(**user.dict())
            session.add(db_user)
            print(db_user.__dict__)
        except Exception:
            session.rollback()
            raise
    return db_user.__dict__
