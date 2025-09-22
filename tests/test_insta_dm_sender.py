# tests/test_insta_dm_sender.py

import pytest
from modules.sns import insta_dm_sender


def test_send_dm_success():
    assert insta_dm_sender.send_dm("user123", "Hello!") is True


def test_send_dm_failure_empty_user():
    assert insta_dm_sender.send_dm("", "Message") is False


def test_send_dm_failure_empty_message():
    assert insta_dm_sender.send_dm("user123", "") is False


def test_send_dm_exception():
    assert insta_dm_sender.send_dm("user123", "fail") is False


def test_get_dm_message_template_valid():
    assert (
        insta_dm_sender.get_dm_message_template(1)
        == "Check out our new product launch!"
    )


def test_get_dm_message_template_invalid():
    assert insta_dm_sender.get_dm_message_template(99) == "Invalid template index."


def test_should_send_dm_true():
    user = {"is_active": True, "is_blocked": False}
    assert insta_dm_sender.should_send_dm(user) is True


def test_should_send_dm_false_blocked():
    user = {"is_active": True, "is_blocked": True}
    assert insta_dm_sender.should_send_dm(user) is False


def test_main_dm_dispatcher_count():
    users = [
        {"user_id": "u1", "is_active": True, "is_blocked": False, "template_index": 0},
        {
            "user_id": "u2",
            "is_active": True,
            "is_blocked": False,
            "template_index": 3,
        },  # fail-test
        {"user_id": "u3", "is_active": False, "is_blocked": False, "template_index": 0},
    ]
    count = insta_dm_sender.main_dm_dispatcher(users)
    assert count == 1  # Only u1 should succeed
