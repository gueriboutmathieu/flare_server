from python_utils.env_vars import EnvVar


class AuthConfig:
    def __init__(self) -> None:
        self.secret_key = EnvVar[str]("AUTH_SECRET_KEY", cast_fct=str).value
        self.public_key = EnvVar[str]("AUTH_PUBLIC_KEY", cast_fct=str).value
