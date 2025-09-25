# tests/test_browser_core.py
import pytest
from modules.common.browser_core import (
    Browser,
    BrowsingContext,
    ClientWindowManager,
)


def test_browser_info_and_secure():
    b = Browser("TestBrowser")
    assert b.get_info() == "Browser: TestBrowser"
    assert b.is_secure() is True


def test_browsing_context_children():
    parent = BrowsingContext("p1")
    child = BrowsingContext("c1", "p1")
    parent.add_child(child)
    assert len(parent.get_children()) == 1
    assert isinstance(parent.get_children()[0], BrowsingContext)


def test_client_window_manager_add_and_get():
    mgr = ClientWindowManager()
    mgr.add_window("user1", {"x": 10, "y": 20, "width": 100, "height": 200, "state": "open", "active": True})
    windows = mgr.get_windows("user1")
    assert len(windows) == 1
    assert windows[0].x == 10
    assert windows[0].active is True


def test_client_window_manager_remove_user_context():
    mgr = ClientWindowManager()
    mgr.add_window("user2", {"x": 1, "y": 1, "width": 50, "height": 50, "state": "min", "active": False})
    assert "user2" in mgr.user_contexts
    mgr.remove_user_context("user2")
    assert "user2" not in mgr.user_contexts
    with pytest.raises(Exception):
        mgr.remove_user_context("default")
