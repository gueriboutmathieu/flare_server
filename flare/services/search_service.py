import requests
from datetime import datetime
from typing import cast, TypedDict

from flare.domain.entities.channel_entity import Channel
from flare.domain.entities.playlist_entity import Playlist
from flare.domain.entities.search_result import SearchResult
from flare.domain.entities.search_type import SearchType
from flare.domain.entities.video_entity import Video
from flare.utils.parse_iso_duration import parse_iso_duration
from python_utils.loggers import get_logger


logger = get_logger(__name__)


class Thumbnail(TypedDict):
    url: str

class ThumbnailQualities(TypedDict):
    default: Thumbnail
    medium: Thumbnail
    high: Thumbnail

class VideoSearchResultId(TypedDict):
    kind: str
    videoId: str

class VideoSearchResultSnippet(TypedDict):
    title: str
    thumbnails: ThumbnailQualities
    channelId: str
    channelTitle: str
    publishedAt: str

class VideoSearchResult(TypedDict):
    id: VideoSearchResultId
    snippet: VideoSearchResultSnippet

class PlaylistSearchResultId(TypedDict):
    kind: str
    playlistId: str

class PlaylistSearchResultSnippet(TypedDict):
    title: str
    thumbnails: ThumbnailQualities
    channelId: str
    channelTitle: str
    publishedAt: str

class PlaylistSearchResult(TypedDict):
    id: PlaylistSearchResultId
    snippet: PlaylistSearchResultSnippet

class ChannelSearchResultId(TypedDict):
    kind: str
    channelId: str

class ChannelSearchResultSnippet(TypedDict):
    title: str
    description: str
    thumbnails: ThumbnailQualities
    publishedAt: str

class ChannelSearchResult(TypedDict):
    id: ChannelSearchResultId
    snippet: ChannelSearchResultSnippet

class VideoContentDetails(TypedDict):
    duration: str

class VideoStatistics(TypedDict):
    viewCount: str

class VideoMetadataResponse(TypedDict):
    contentDetails: VideoContentDetails
    statistics: VideoStatistics

class PlaylistContentDetails(TypedDict):
    itemCount: int

class PlaylistMetadataResponse(TypedDict):
    contentDetails: PlaylistContentDetails

class ChannelStatistics(TypedDict):
    subscriberCount: str
    videoCount: str

class ChannelMetadataResponse(TypedDict):
    statistics: ChannelStatistics

class SearchService:
    def __init__(self, api_key: str):
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.api_key = api_key

    def search(self, query: str, search_type: SearchType) -> list[SearchResult]:
        params = {
            "q": query,
            "type": search_type,
            "part": "snippet",
            "maxResults": 50,
            "key": self.api_key
        }
        response = requests.get(f"{self.base_url}/search", params=params).json()

        search_results: list[SearchResult] = []
        for youtube_search_result in response["items"]:
            search_result_type = SearchType[youtube_search_result["id"]["kind"].replace("youtube#", "").upper()]  # pyright: ignore[reportTypedDictNotRequiredAccess]

            match search_result_type:
                case SearchType.VIDEO:
                    video_search_result = cast(VideoSearchResult, youtube_search_result)
                    title = video_search_result["snippet"]["title"]
                    thumbnail_url = video_search_result["snippet"]["thumbnails"]["high"]["url"]
                    video_id = video_search_result["id"]["videoId"]
                    channel_id = video_search_result["snippet"]["channelId"]
                    channel_title = video_search_result["snippet"]["channelTitle"]
                    raw_published_at = video_search_result["snippet"]["publishedAt"].replace("Z", "+00:00")
                    published_at = datetime.fromisoformat(raw_published_at)
                    url = f"https://www.youtube.com/watch?v={video_id}"
                    duration, view_count = self._get_video_metadata(video_id)

                    search_results.append(
                        Video(
                            video_id,
                            title,
                            url,
                            channel_title,
                            thumbnail_url,
                            duration,
                            view_count,
                            published_at,
                            None,
                            channel_id,
                        )
                    )
                case SearchType.PLAYLIST:
                    playlist_search_result = cast(PlaylistSearchResult, youtube_search_result)
                    playlist_id = playlist_search_result["id"]["playlistId"]
                    title = playlist_search_result["snippet"]["title"]
                    channel_title = playlist_search_result["snippet"]["channelTitle"]
                    channel_id = playlist_search_result["snippet"]["channelId"]
                    thumbnail_url = playlist_search_result["snippet"]["thumbnails"]["high"]["url"]
                    raw_published_at = playlist_search_result["snippet"]["publishedAt"].replace("Z", "+00:00")
                    published_at = datetime.fromisoformat(raw_published_at)
                    url = f"https://www.youtube.com/playlist?list={playlist_id}"
                    video_count = self._get_playlist_video_count(playlist_id)

                    search_results.append(
                        Playlist(
                            playlist_id,
                            title,
                            url,
                            channel_title,
                            thumbnail_url,
                            video_count,
                            published_at,
                            channel_id,
                        )
                    )
                case SearchType.CHANNEL:
                    channel_search_result = cast(ChannelSearchResult, youtube_search_result)
                    channel_id = channel_search_result["id"]["channelId"]
                    title = channel_search_result["snippet"]["title"]
                    description = channel_search_result["snippet"]["description"]
                    thumbnail_url = channel_search_result["snippet"]["thumbnails"]["high"]["url"]
                    raw_published_at = channel_search_result["snippet"]["publishedAt"].replace("Z", "+00:00")
                    published_at = datetime.fromisoformat(raw_published_at)
                    url = f"https://www.youtube.com/channel/{channel_id}"
                    video_count, subscriber_count = self._get_channel_metadata(channel_id)

                    search_results.append(
                        Channel(
                            channel_id,
                            title,
                            description,
                            url,
                            thumbnail_url,
                            video_count,
                            subscriber_count,
                            published_at,
                        )
                    )
                case _:
                    pass
        return search_results
    
    def _get_video_metadata(self, video_id: str) -> tuple[int, int]:
        params = {
            "id": video_id,
            "part": "contentDetails,statistics",
            "key": self.api_key
        }
        response = requests.get(f"{self.base_url}/videos", params=params).json()["items"][0]
        video_metadata_response = cast(VideoMetadataResponse, response)
        duration = parse_iso_duration(video_metadata_response["contentDetails"]["duration"])
        view_count = int(video_metadata_response["statistics"]["viewCount"])
        return duration, view_count
    
    def _get_playlist_video_count(self, playlist_id: str) -> int:
        params = {
            "id": playlist_id,
            "part": "contentDetails",
            "key": self.api_key
        }
        response = requests.get(f"{self.base_url}/playlists", params=params).json()["items"][0]
        playlist_metadata_response = cast(PlaylistMetadataResponse, response)
        return playlist_metadata_response["contentDetails"]["itemCount"]
    
    def _get_channel_metadata(self, channel_id: str) -> tuple[int, int]:
        params = {
            "id": channel_id,
            "part": "statistics",
            "key": self.api_key
        }
        response = requests.get(f"{self.base_url}/channels", params=params).json()["items"][0]
        channel_metadata_response = cast(ChannelMetadataResponse, response)
        video_count = int(channel_metadata_response["statistics"]["videoCount"])
        subscriber_count = int(channel_metadata_response["statistics"]["subscriberCount"])
        return video_count, subscriber_count
