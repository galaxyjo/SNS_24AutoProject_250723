# tests/manual/session/test_token_flow.py

import pytest
from modules.session import token_flow
from time import time


def test_generate_token():
    token = token_flow.generate_token("user123")
    assert token == "token_for_user123"


def test_validate_token():
    assert token_flow.validate_token("token_for_user123") is True
    assert token_flow.validate_token("invalid_token") is False


def test_refresh_token():
    old_token = "token_for_user123"
    new_token_data = token_flow.refresh_token(old_token)
    assert new_token_data["access_token"].startswith("new_token_for_")
    assert new_token_data["expires_in"] == 3600
    assert "created_at" in new_token_data


def test_get_token_expiry():
    token_data = {"created_at": 1000, "expires_in": 3600}
    assert token_flow.get_token_expiry(token_data) == 4600


def test_is_token_valid():
    valid_token_data = {"created_at": int(time()) - 100, "expires_in": 3600}
    expired_token_data = {"created_at": int(time()) - 5000, "expires_in": 100}
    assert token_flow.is_token_valid(valid_token_data) is True
    assert token_flow.is_token_valid(expired_token_data) is False
