from fastapi import HTTPException

from flare.domain.command_context import CommandContext
from flare.domain.entities.user_entity import User
from flare.domain.exceptions.user_exceptions import UserNotFoundException


def validate_user_command(command_context: CommandContext, token: str) -> User:
    user_id = command_context.auth_service.validate_user(token)

    try:
        user = command_context.user_repository.get_or_raise(user_id)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

    return user
