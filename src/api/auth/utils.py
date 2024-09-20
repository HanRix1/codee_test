import time
from uuid import UUID

import jwt

from settings import AuthSettings, get_settings

setting: AuthSettings = get_settings(AuthSettings)


def token_response(token: str):
    return {"access_token": token}


def sign_jwt(user_id: UUID) -> dict[str, str]:
    payload = {"user_id": user_id.hex, "expires": time.time() + 600}
    token = jwt.encode(payload, setting.secret, algorithm=setting.algorithm)

    return token_response(token)


def decode_jwt(token: str) -> dict[str, str]:
    try:
        decoded_token = jwt.decode(
            token, setting.secret, algorithms=[setting.algorithm]
        )
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
