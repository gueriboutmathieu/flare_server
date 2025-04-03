from flare.domain.command_context import CommandContext
from flare.domain.entities.user_tokens import UserTokens


def signin_command(
    command_context: CommandContext,
    username: str,
    password: str,
) -> UserTokens:
    user = command_context.user_repository.get_by_name_and_password(username, password)

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
