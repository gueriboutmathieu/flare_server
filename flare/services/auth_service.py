from fastapi import HTTPException
from jwt import decode  # pyright: ignore
from uuid import UUID

from python_utils.auth import Auth, AuthException


class AuthService(Auth):
    def __init__(self, secret_key: str, public_key: str):
        token_data_keys = ["user_id", "username", "password"]
        super().__init__(secret_key, public_key, token_data_keys)

    def validate_user(self, token: str) -> UUID:
        try:
            self.validate_token(token)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e))
        payload = decode(token, self.secret_key, algorithms=[self.algorithm])
        if all(key not in payload for key in self.token_data_keys):
            raise HTTPException(status_code=401, detail="Missing required data in token")

        user_id = UUID(payload.get("user_id"))
        return user_id
