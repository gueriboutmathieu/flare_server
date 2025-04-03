from uuid6 import uuid7

from flare.domain.command_context import CommandContext
from flare.domain.entities.user_entity import User
from flare.domain.entities.user_tokens import UserTokens


def signup_command(
    command_context: CommandContext,
    public_key: str,
    username: str,
    password: str,
) -> UserTokens:
    command_context.auth_service.validate_public_key(public_key)

    user = User(
        id=uuid7(),
        name=username,
        password=password,
    )
    command_context.user_repository.create(user)

    access_token = command_context.auth_service.create_access_token(
        {
            "user_id": str(user.id),
            "username": user.name,
            "password": user.password,
        }
    )
    refresh_token = command_context.auth_service.create_refresh_token(
        {
            "user_id": str(user.id),
            "username": user.name,
            "password": user.password,
        }
    )

    return UserTokens(access_token, refresh_token)
