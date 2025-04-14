from flare.domain.command_context import CommandContext
from flare.domain.entities.video_entity import Video


def search_command(command_context: CommandContext, query: str) -> list[Video]:
    videos = command_context.search_service.search(query)



    return videos
