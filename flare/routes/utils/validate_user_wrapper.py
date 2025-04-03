from fastapi import Depends
from typing import Annotated

from flare.domain.domain import Domain
from flare.domain.entities.user_entity import User
from python_utils.auth import oauth2_scheme


def validate_user_wrapper(domain: Domain):
    async def validate_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
        return domain.validate_user(token)
    return validate_user
