import uvicorn

from flare.config.auth_config import AuthConfig
from flare.config.postgresql_config import PostgresqlConfig
from flare.config.youtube_config import YoutubeConfig
from flare.domain.domain import Domain
from flare.repositories.user_repository import UserRepository
from flare.routes.fastapi_app import FastapiApp
from flare.services.auth_service import AuthService
from flare.services.search_service import SearchService
from flare.services.streaming_service import StreamingService
from python_utils.loggers import get_logger
from python_utils.sqlalchemy_postgresql_engine_wrapper import SqlAlchemyPostgresqlEngineWrapper



# Logger
logger = get_logger(__name__)


# Configs
auth_config = AuthConfig()
postgresql_config = PostgresqlConfig()
youtube_config = YoutubeConfig()


# Services
auth_service = AuthService(auth_config.secret_key, auth_config.public_key)
search_service = SearchService(youtube_config.api_key)
streaming_service = StreamingService()


# SQLAlchemyEngineWrapper
sqlalchemy_postgresql_engine_wrapper = SqlAlchemyPostgresqlEngineWrapper(
    sql_user=postgresql_config.sql_user,
    sql_password=postgresql_config.sql_password,
    sql_host=postgresql_config.sql_host,
    sql_port=postgresql_config.sql_port,
    sql_database=postgresql_config.sql_database,
    pool_size=5
)
sqlalchemy_session = sqlalchemy_postgresql_engine_wrapper.create_session()


# Repositories
user_repository = UserRepository(sqlalchemy_session, logger)


class CommandContext:
    def __init__(self):
        self.auth_service = auth_service
        self.search_service = search_service
        self.streaming_service = streaming_service
        self.sqlalchemy_session = sqlalchemy_session
        self.user_repository = user_repository

    def commit(self):
        self.sqlalchemy_session.commit()

    def rollback(self):
        self.sqlalchemy_session.rollback()



bound_domain = Domain(CommandContext)
fastapi_app = FastapiApp(bound_domain)


def run_server():
    uvicorn.run(fastapi_app.app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run_server()
