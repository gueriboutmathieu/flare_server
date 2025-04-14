from flare.domain.command_context import CommandContext
from flare.domain.entities.video_entity import Video


def get_video_with_formats_command(command_context: CommandContext, video_id: str) -> Video:
    return command_context.search_service.get_video_with_formats(video_id)
