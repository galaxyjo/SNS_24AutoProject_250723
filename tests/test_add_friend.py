# tests/test_add_friend.py

import builtins
from modules.actions import add_friend


def test_add_friend_prints_username(monkeypatch):
    printed = []

    def fake_print(msg):
        printed.append(msg)

    monkeypatch.setattr(builtins, "print", fake_print)
    add_friend.add_friend("john_doe")

    assert printed == ["[FRIEND REQUEST] → john_doe"]
