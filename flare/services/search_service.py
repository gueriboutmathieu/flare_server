from datetime import datetime
from typing import cast, Optional, TypedDict
from yt_dlp import YoutubeDL

from flare.domain.entities.audio_format import AudioFormat
from flare.domain.entities.playlist import Playlist
from flare.domain.entities.video_entity import Video
from flare.domain.entities.video_format import VideoFormat
from python_utils.loggers import get_logger


logger = get_logger(__name__)


class Thumbnail(TypedDict):
    url: str
    width: int
    height: int


class Format(TypedDict):
    format_id: str
    url: str
    acodec: Optional[str]
    vcodec: str
    protocol: str
    abr: Optional[int]
    height: int
    width: int
    fps: int


class VideoSearchResult(TypedDict):
    id: str
    title: str
    thumbnails: list[Thumbnail]
    channel_id: str
    channel: str
    duration: int
    view_count: int
    upload_date: str
    formats: list[Format]


class SearchService:
    def __init__(self):
        self.search_client = YoutubeDL({
            "quiet": True,
            "no_warnings": True,
            "skip_download": "True",
            "extract_flat": "in_playlist",
            "default_search": "ytsearch50",
        })
        self.formats_client = YoutubeDL({
            "quiet": True,
            "no_warnings": True,
            "skip_download": "True",
        })

    def search(self, query: str) -> list[Video]:
        search_results: list[VideoSearchResult] = self.search_client.extract_info(query)["entries"]

        videos: list[Video] = []
        for search_result in search_results:
            video_id = search_result["id"]
            title = search_result["title"]
            thumbnail_url = max(search_result["thumbnails"], key=lambda x: x.get("height", 0))["url"]
            channel_id = search_result["channel_id"]
            channel_title = search_result["channel"]
            duration = search_result["duration"]
            view_count = search_result["view_count"]

            videos.append(
                Video(
                    video_id,
                    title,
                    thumbnail_url,
                    channel_id,
                    channel_title,
                    duration,
                    view_count,
                    None,
                    [],
                    [],
                )
            )

        return videos

    def get_video_with_formats(self, video_id: str) -> Video:
        video = cast(VideoSearchResult, self.formats_client.extract_info(video_id))
        formats = video["formats"]

        video_id = video["id"]
        title = video["title"]
        thumbnail_url = max(video["thumbnails"], key=lambda x: x.get("height", 0))["url"]
        channel_id = video["channel_id"]
        channel_title = video["channel"]
        duration = video["duration"]
        view_count = video["view_count"]
        upload_date = datetime.strptime(video["upload_date"], "%Y%m%d")

        audio_formats: list[AudioFormat] = []
        audio_candidates = [
            audio_format for audio_format in formats
            if audio_format.get("acodec") not in [None, "none"]
            and "drc" not in audio_format.get("format_id")
            and audio_format.get("abr") not in [None, "none"]
        ]
        best_aac = max(
            [audio_format for audio_format in audio_candidates if audio_format.get("acodec") != "opus"],
            key=lambda x: int(x.get("abr", 0) or 0)
        )
        best_opus = max(
            [audio_format for audio_format in audio_candidates if audio_format.get("acodec") == "opus"],
            key=lambda x: int(x.get("abr", 0) or 0)
        )
        audio_formats.append(
            AudioFormat(
                best_aac["format_id"],
                best_aac["url"],
                best_aac.get("acodec") or "",
                best_aac.get("abr") or 0,
            )
        )
        audio_formats.append(
            AudioFormat(
                best_opus["format_id"],
                best_opus["url"],
                best_opus.get("acodec") or "",
                best_opus.get("abr") or 0,
            )
        )

        video_candidates = [
            video_format for video_format in formats
            if video_format.get("vcodec") not in [None, "none"]
            and video_format.get("protocol") == "https"
            and video_format.get("acodec") in [None, "none"]
        ]
        video_formats = [
            VideoFormat(
                video_format["format_id"],
                video_format["url"],
                video_format["vcodec"],
                video_format["height"],
                video_format["width"],
                video_format["fps"],
            )
            for video_format in video_candidates
        ]

        return Video(
            video_id,
            title,
            thumbnail_url,
            channel_id,
            channel_title,
            duration,
            view_count,
            upload_date,
            audio_formats,
            video_formats,
        )

    def get_channel_videos(self, channel_id: str) -> list[Video]:
        return []

    def get_channel_playlists(self, channel_id: str) -> list[Playlist]:
        return []

    def get_playlist_videos(self, playlist_id: str) -> list[Video]:
        return []
