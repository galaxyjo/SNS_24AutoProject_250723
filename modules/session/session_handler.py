# modules/session/session_handler.py

from datetime import datetime, timedelta

__all__ = ["login", "is_expired", "refresh_token", "SessionState"]


class SessionState:
    def __init__(self):
        self.token = None
        self.expires_at = None

    def set_token(self, token: str, expires_in_sec: int = 3600):
        self.token = token
        self.expires_at = datetime.utcnow() + timedelta(seconds=expires_in_sec)

    def is_valid(self) -> bool:
        return (
            self.token is not None
            and self.expires_at
            and self.expires_at > datetime.utcnow()
        )


state = SessionState()


def login(username: str = "admin", password: str = "password") -> str:
    state.set_token("access_token_123", 3600)
    return state.token


def is_expired() -> bool:
    return not state.is_valid()


def refresh_token() -> str:
    state.set_token("access_token_456", 3600)
    return state.token
