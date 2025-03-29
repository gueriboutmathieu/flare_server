from python_utils.env_vars import EnvVar


class PostgresqlConfig:
    def __init__(self) -> None:
        self.sql_user = EnvVar[str]("SQL_USER", cast_fct=str).value
        self.sql_password = EnvVar[str]("SQL_PASSWORD", cast_fct=str).value
        self.sql_host = EnvVar[str]("SQL_HOST", cast_fct=str).value
        self.sql_port = EnvVar[int]("SQL_PORT", cast_fct=int).value
        self.sql_database = EnvVar[str]("SQL_DATABASE", cast_fct=str).value
