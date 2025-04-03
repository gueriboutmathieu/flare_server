# Flare server

Another youtube frontend alternative.

To use Flare, check the frontend apps:
- [web app](https://github.com/gueriboutmathieu/flare_app.git)

## Install locally

First, you need [uv](https://github.com/astral-sh/uv) to be installed.

If you are on NixOs, you need a FHS compliant environment, check [nix-ld](https://github.com/nix-community/nix-ld).

This project uses python 3.11.
```shell
uv python install 3.11
```

Then, setup venv and activate it :
```shell
uv venv
source .venv/bin/activate
```

Finally, install dependencies :
```shell
uv sync
```

## Environment variables
Create a `.env` file with these variables:
```
SQL_USER=user
SQL_PASSWORD=password
SQL_HOST=localhost
SQL_PORT=55432
SQL_DATABASE=flare
AUTH_SECRET_KEY=<your secret key>
AUTH_PUBLIC_KEY=<your public key>
YOUTUBE_API_KEY=<your youtube api key>
```

## Run locally
Run postgresql database:
```shell
docker compose up -d
```

In order to run migrations, you may need to export your env vars:
```shell
set -a
source .env
set +a
```

Run migrations:
```shell
alembic upgrade head
```

Run the app:
```shell
python flare/app.py
```

## Run the tests
```shell
pytest tests
```

## Run Coverage
```shell
coverage run -m pytest tests
coverage report -m
```

## Contribute
This will install pre-commit hook to run multiple checks, ruff and pyright before committing.
```shell
pre-commit install
```

## License
This project is licensed under the GNU General Public License v3.0 (GPL v3).
You are free to use, modify, and distribute this software, as long as any distributed version is also licensed under GPLv3.
This software is provided "as is", without warranty of any kind.
See the [LICENSE](LICENSE) file for more details.
