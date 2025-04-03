from fastapi import FastAPI, HTTPException

from flare.domain.domain import Domain
from flare.domain.entities.user_tokens import UserTokens
from flare.domain.exceptions.user_exceptions import UserConstraintException, UserNotFoundException
from python_utils.auth import AuthException


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/signup")
    async def signup(public_key: str, username: str, password: str) -> UserTokens:  # pyright: ignore[reportUnusedFunction]
        try:
            user_tokens = domain.signup(public_key, username, password)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e)) from e
        except UserConstraintException as e:
            raise HTTPException(status_code=403, detail=str(e)) from e
        return user_tokens

    @fastapi_app.post("/signin")
    async def signin(username: str, password: str) -> UserTokens:  # pyright: ignore[reportUnusedFunction]
        try:
            user_tokens = domain.signin(username, password)
        except UserNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e)) from e
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e)) from e
        return user_tokens
