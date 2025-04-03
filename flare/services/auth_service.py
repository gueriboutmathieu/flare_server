from fastapi import Depends, HTTPException
from jwt import decode  # pyright: ignore
from typing import Annotated
from uuid import UUID

from flare.domain.entities.user_entity import User
from python_utils.auth import Auth, AuthException, oauth2_scheme


class AuthService(Auth):
    def __init__(self, secret_key: str, public_key: str):
        token_data_keys = ["user_id", "username", "password"]
        super().__init__(secret_key, public_key, token_data_keys)

    async def validate_user(
        self, token: Annotated[str, Depends(oauth2_scheme)]
    ) -> User:
        try:
            self.validate_token(token)
        except AuthException:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        payload = decode(token, self.secret_key, algorithms=[self.algorithm])
        if all(key not in payload for key in self.token_data_keys):
            raise HTTPException(
                status_code=401, detail="Missing required data in token"
            )

        user_id = payload.get("user_id")
        username = payload.get("username")
        password = payload.get("password")
        return User(UUID(user_id), username, password)
