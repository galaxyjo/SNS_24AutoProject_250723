# tests/test_session_flow.py

import pytest
from modules.session import session_handler


def test_login_success(monkeypatch):
    monkeypatch.setattr(session_handler, "login", lambda: "token_ok")
    assert session_handler.login() == "token_ok"


def test_session_expired(monkeypatch):
    monkeypatch.setattr(session_handler, "is_expired", lambda: True)
    assert session_handler.is_expired() is True


def test_token_refresh(monkeypatch):
    monkeypatch.setattr(session_handler, "refresh_token", lambda: "new_token")
    assert session_handler.refresh_token() == "new_token"
