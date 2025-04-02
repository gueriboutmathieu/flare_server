from flare.domain.command_context import CommandContext
from flare.domain.entities.search_result import SearchResult
from flare.domain.entities.search_type import SearchType


def search_command(command_context: CommandContext, query: str, search_type: SearchType) -> list[SearchResult]:
    results = command_context.search_service.search(query, search_type)
    return results
