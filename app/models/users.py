from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.engine import Base


class User(Base):
    __tablename__ = 'user_account'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    # follows: Mapped[list['User']] = relationship()
