# modules/session/token_flow.py

from time import time


def generate_token(user_id: str) -> str:
    return f"token_for_{user_id}"


def validate_token(token: str) -> bool:
    return token.startswith("token_for_")


def refresh_token(token: str) -> dict:
    return {
        "access_token": f"new_{token}",
        "expires_in": 3600,
        "created_at": int(time()),
    }


def get_token_expiry(token_data: dict) -> int:
    return token_data.get("created_at", 0) + token_data.get("expires_in", 0)


def is_token_valid(token_data: dict) -> bool:
    return get_token_expiry(token_data) > int(time())
