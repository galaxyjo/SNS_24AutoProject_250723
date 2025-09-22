# tests/test_dm_echo.py

from modules.dm.echo import handle_dm


def test_handle_dm_refund():
    assert handle_dm("refund please") == "We will process your refund."


def test_handle_dm_default():
    assert handle_dm("hello bot") == "Thank you for your message."


def test_handle_dm_empty():
    assert handle_dm("") == "No input"
