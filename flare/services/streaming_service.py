from subprocess import Popen, PIPE
from typing import cast, Optional, TypedDict
from yt_dlp import YoutubeDL


class VideoFormat(TypedDict):
    url: str
    acodec: Optional[str]
    vcodec: str
    abr: int
    height: int

class VideoInfo(TypedDict):
    formats: list[VideoFormat]


class StreamingService:
    def __init__(self):
        self.yt_dlp_client = YoutubeDL(
            {
                "quiet": True,
                "no_warnings": True,
            }
        )

    def _get_best_streams(self, video_id: str) -> tuple[str, str]:
        video_info = cast(VideoInfo, self.yt_dlp_client.extract_info(video_id, download=False))  # pyright: ignore
        formats = video_info["formats"]

        audio_formats = [audio_format for audio_format in formats if audio_format.get("vcodec") == "none" and audio_format.get("acodec") not in [None, "none"]]
        audio_url = max(audio_formats, key=lambda x: x.get("abr", 0))["url"]

        video_formats = [video_format for video_format in formats if video_format.get("vcodec") != "none" and video_format.get("acodec") in [None, "none"]]
        video_url = max(video_formats, key=lambda x: x.get("height", 0))["url"]

        return audio_url, video_url

    def stream(self, video_id: str) -> Popen[bytes]:
        audio_url, video_url = self._get_best_streams(video_id)

        ffmpeg_command = [
            "ffmpeg",
            "-i", video_url,
            "-i", audio_url,
            "-c", "copy",
            "-f", "mp4",
            "-movflags", "frag_keyframe+empty_moov",
            "pipe:1",
        ]

        return Popen(ffmpeg_command, stdout=PIPE)
