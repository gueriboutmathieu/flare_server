import pytest
from datetime import datetime
from logging import Logger
from sqlalchemy.orm import Session

from flare.domain.command_context import CommandContext
from flare.domain.entities.channel_entity import Channel
from flare.domain.entities.playlist_entity import Playlist
from flare.domain.entities.video_entity import Video
from flare.repositories.user_repository import UserRepository
from flare.services.auth_service import AuthService
from flare.services.search_service import SearchService
from flare.services.streaming_service import StreamingService


class MockedCommandContext(CommandContext):
    def __init__(self) -> None:
        self._auth_service = AuthService("", "")
        self._search_service = SearchService("")
        self._streaming_service = StreamingService()
        self._user_repository = UserRepository(Session(), Logger(__name__))

    @property
    def auth_service(self):
        return self._auth_service

    @property
    def search_service(self):
        return self._search_service

    @property
    def streaming_service(self):
        return self._streaming_service

    @property
    def user_repository(self):
        return self._user_repository

    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass


@pytest.fixture
def video():
    return Video(
        id="dQw4w9WgXcQ",
        title="Rick Astley - Never Gonna Give You Up (Official Music Video)",
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        channel_title="Rick Astley",
        thumbnail_url="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
        duration=213,
        view_count=1641139516,
        channel_id="channel_id",
        playlist_id=None,
        published_at=datetime.fromisoformat("2009-10-25T06:57:33+00:00"),
    )


@pytest.fixture
def playlist():
    return Playlist(
        id="PLE0hg-LdSfycrpTtMImPSqFLle4yYNzWD",
        title="'Never Gonna Give You Up' Rick Astley Playlist",
        url="https://www.youtube.com/playlist?list=PLE0hg-LdSfycrpTtMImPSqFLle4yYNzWD",
        channel_title="just.rick_6",
        thumbnail_url="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
        video_count=59,
        published_at=datetime.fromisoformat("2023-04-13T10:50:20+00:00"),
        channel_id="UCnJIsk6daK5Qym0dCR7UC4g",
    )


@pytest.fixture
def channel():
    return Channel(
        id="UCuAXFkgsw1L7xaCfnd5JJOw",
        title="Rick Astley",
        description="Never: The Autobiography - Out now.",
        url="https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
        thumbnail_url="https://yt3.ggpht.com/K2ecE5j90a_DFzugHo0bW98vFlIQ1JJgs9mbcav7RGy1t7adJRnd2jaIv-oc6XzTRvDdWlFCAfc=s800-c-k-c0xffffffff-no-rj-mo",
        video_count=310,
        subscriber_count=4310000,
        published_at=datetime.fromisoformat("2015-02-01T16:32:30+00:00"),
    )
