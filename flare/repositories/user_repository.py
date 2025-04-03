from logging import Logger
from sqlalchemy.orm import Session

from flare.domain.entities.user_entity import User
from flare.domain.exceptions.user_exceptions import UserConstraintException, UserNotFoundException
from python_utils.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class UserRepositoryException(Exception):
    def __init__(self, message: str = "User repository exception") -> None:
        super().__init__(message)


class UserRepository(SQLAlchemyCRUDRepository[User]):
    def __init__(self, session: Session, logger: Logger) -> None:
        super().__init__(
            session=session,
            entity_class=User,
            logger=logger,
            default_exception=UserRepositoryException,
            not_found_exception=UserNotFoundException,
            constraint_exception=UserConstraintException
        )

    def get_by_name_and_password(self, name: str, password: str) -> User:
        user = self.session.query(User).filter(User.name == name, User.password == password).first()
        if user is None:
            raise UserNotFoundException()
        return user
