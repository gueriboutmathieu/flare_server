import os

from flare.config.youtube_config import YoutubeConfig


def test_youtube_config():
    os.environ["YOUTUBE_API_KEY"] = "test_api_key"

    youtube_config = YoutubeConfig()
    assert youtube_config.api_key == "test_api_key"
