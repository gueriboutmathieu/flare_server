from subprocess import PIPE, Popen
from typing import Optional, TypedDict
from yt_dlp import YoutubeDL

from flare.domain.exceptions.stream_exceptions import StreamNotFoundException


class Format(TypedDict):
    url: str
    acodec: Optional[str]
    vcodec: str
    protocol: str
    abr: int
    height: int

class VideoInfo(TypedDict):
    formats: list[Format]


class StreamingService:
    def __init__(self):
        self.yt_dlp_client = YoutubeDL(
            {
                "quiet": True,
                "no_warnings": True,
            }
        )
        self.streams: dict[str, Popen[bytes]] = {}

    def stream(self, video_id: str, start_at: int, audio_url: str, video_url: str, container: str) -> Popen[bytes]:
        ffmpeg_command = [
            "ffmpeg",
            "-ss", str(start_at),
            "-i", audio_url,
            "-ss", str(start_at),
            "-i", video_url,
            "-c", "copy",
            "-f", container,
            "-map", "0:a",
            "-map", "1:v",
            "-c:a", "copy",
            "-c:v", "copy",
        ]

        if container == "mp4":
            ffmpeg_command += ["-movflags", "frag_keyframe+empty_moov"]

        ffmpeg_command += ["pipe:1"]

        subprocess = Popen(ffmpeg_command, stdout=PIPE)
        self.streams[video_id] = subprocess

        return subprocess

    def end_stream(self, video_id: str) -> None:
        if video_id not in self.streams.keys():
            raise StreamNotFoundException

        self.streams[video_id].kill()
        del self.streams[video_id]
