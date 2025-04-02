from python_utils.env_vars import EnvVar


class YoutubeConfig:
    def __init__(self) -> None:
        self.api_key = EnvVar[str]("YOUTUBE_API_KEY", cast_fct=str).value
