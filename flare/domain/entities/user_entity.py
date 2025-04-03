from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from python_utils.entity import Entity


class User(Entity):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(init=True, primary_key=True)
    name: Mapped[str] = mapped_column(init=True)
    password: Mapped[str] = mapped_column(init=True)
