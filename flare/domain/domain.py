from flare.domain.command_context import CommandContext
from flare.domain.commands.search_command import search_command
from flare.domain.commands.signin_command import signin_command
from flare.domain.commands.signup_command import signup_command
from flare.domain.commands.validate_user_command import validate_user_command
from python_utils.domain import CommandContextCreator, Domain as BaseDomain




class Domain(BaseDomain[CommandContext]):
    def __init__(
        self,
        command_context_creator: CommandContextCreator[CommandContext],
    ) -> None:
        super().__init__(command_context_creator)

        self.search = self._bind_command(search_command)
        self.signin = self._bind_command(signin_command)
        self.signup = self._bind_command(signup_command)
        self.validate_user = self._bind_command(validate_user_command)
