from flare.domain.command_context import CommandContext


def refresh_access_token_command(command_context: CommandContext, refresh_token: str) -> str:
    return command_context.auth_service.refresh_access_token(refresh_token)
