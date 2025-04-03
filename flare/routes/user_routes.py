from fastapi import Depends, FastAPI

from flare.domain.domain import Domain
from flare.domain.entities.user_entity import User
from flare.routes.dtos.user_dto import UserDto
from flare.routes.utils.validate_user_wrapper import validate_user_wrapper


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.get("/current_user")
    async def current_user(user: User = Depends(validate_user_wrapper(domain))) -> UserDto:  # pyright: ignore[reportUnusedFunction]
        return UserDto(id=user.id, name=user.name)
