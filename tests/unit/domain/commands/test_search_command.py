import pytest  # pyright: ignore  # noqa
from pytest_mock import MockerFixture

from flare.domain.commands.search_command import search_command
from flare.domain.entities.channel_entity import Channel
from flare.domain.entities.playlist_entity import Playlist
from flare.domain.entities.search_type import SearchType
from flare.domain.entities.video_entity import Video
from tests.unit.fixtures import MockedCommandContext, channel, playlist, video  # pyright: ignore  # noqa


def test_search_command(mocker: MockerFixture, channel: Channel, playlist: Playlist, video: Video):  # noqa
    context = MockedCommandContext()
    search_results = [channel, playlist, video]
    mocker.patch.object(context.search_service, "search", return_value=search_results)
    assert search_command(context, "never+gonna+give+you+up", SearchType.ALL) == search_results
