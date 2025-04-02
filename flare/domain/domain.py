from flare.domain.command_context import CommandContext
from flare.domain.commands.search_command import search_command
from python_utils.domain import CommandContextCreator, Domain as BaseDomain



class Domain(BaseDomain[CommandContext]):
    def __init__(
        self,
        command_context_creator: CommandContextCreator[CommandContext],
    ) -> None:
        super().__init__(command_context_creator)

        self.search = self._bind_command(search_command)
