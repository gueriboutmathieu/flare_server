from python_utils.env_vars import EnvVar


class GoogleConfig:
    def __init__(self) -> None:
        self.api_key = EnvVar[str]("GOOGLE_API_KEY", cast_fct=str).value
