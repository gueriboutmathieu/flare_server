source .venv/bin/activate
set -a
source ./.env
set +a
docker compose up -d
alembic upgrade head
