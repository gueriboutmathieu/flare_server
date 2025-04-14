from subprocess import Popen

from flare.domain.command_context import CommandContext
from python_utils.loggers import get_logger


logger = get_logger(__name__)


def stream_command(
    command_context: CommandContext,
    video_id: str,
    start_at: int,
    audio_url: str,
    video_url: str,
    container: str,
) -> Popen[bytes]:
    return command_context.streaming_service.stream(video_id, start_at, audio_url, video_url, container)
