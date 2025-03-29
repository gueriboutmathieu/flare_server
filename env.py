import os
from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool

from python_utils.entity import Entity

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None and not os.getenv(
    "IS_RUNNING_PYTHON_TESTS", False
):
    fileConfig(config.config_file_name)

target_metadata = Entity.metadata

# set the database url in config using environment variables
sql_user = os.environ.get("SQL_USER")
sql_password = os.environ.get("SQL_PASSWORD")
sql_host = os.environ.get("SQL_HOST")
sql_port = os.environ.get("SQL_PORT")
sql_database = os.environ.get("SQL_DATABASE")
if not sql_user or not sql_password or not sql_host or not sql_port or not sql_database:
    raise ValueError(
        "SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT and SQL_DATABASE environment variables must be set"
    )
db_url = f"postgresql+psycopg2://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"
config.set_main_option("sqlalchemy.url", db_url)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        connection.execution_options(isolation_level="AUTOCOMMIT")
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
