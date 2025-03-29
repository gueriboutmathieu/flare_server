import uvicorn

from flare.config.postgresql_config import PostgresqlConfig
from flare.domain.domain import Domain
from flare.routes.fastapi_app import FastapiApp
from python_utils.loggers import get_logger
from python_utils.sqlalchemy_postgresql_engine_wrapper import SqlAlchemyPostgresqlEngineWrapper


# Logger
logger = get_logger(__name__)


# Configs
postgresql_config = PostgresqlConfig()


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


class CommandContext:
    def __init__(self):
        self.sqlalchemy_session = sqlalchemy_session

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
