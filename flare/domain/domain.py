from flare.domain.command_context import CommandContext
from flare.domain.commands.get_video_with_formats_command import get_video_with_formats_command
from flare.domain.commands.refresh_access_token_command import refresh_access_token_command
from flare.domain.commands.end_stream_command import end_stream_command
from flare.domain.commands.search_command import search_command
from flare.domain.commands.signin_command import signin_command
from flare.domain.commands.signup_command import signup_command
from flare.domain.commands.stream_command import stream_command
from flare.domain.commands.validate_user_command import validate_user_command
from python_utils.domain import CommandContextCreator, Domain as BaseDomain




class Domain(BaseDomain[CommandContext]):
    def __init__(
        self,
        command_context_creator: CommandContextCreator[CommandContext],
    ) -> None:
        super().__init__(command_context_creator)

        self.end_stream = self._bind_command(end_stream_command)
        self.get_video_with_formats = self._bind_command(get_video_with_formats_command)
        self.refresh_access_token = self._bind_command(refresh_access_token_command)
        self.search = self._bind_command(search_command)
        self.signin = self._bind_command(signin_command)
        self.signup = self._bind_command(signup_command)
        self.stream = self._bind_command(stream_command)
        self.validate_user = self._bind_command(validate_user_command)
