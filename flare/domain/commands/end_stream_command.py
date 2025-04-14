from flare.domain.command_context import CommandContext


def end_stream_command(command_context: CommandContext, video_id: str) -> None:
    command_context.streaming_service.end_stream(video_id)
