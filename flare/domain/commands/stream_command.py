from subprocess import Popen

from flare.domain.command_context import CommandContext


def stream_command(command_context: CommandContext, video_id: str) -> Popen[bytes]:
    return command_context.streaming_service.stream(video_id)
