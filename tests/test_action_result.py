# tests/test_action_result.py

import pytest
from modules.dm.action_result import ActionResult


def test_successful_action_result():
    result = ActionResult(success=True)
    assert result.is_successful() is True
    assert result.describe() == "Action succeeded"


def test_failed_action_result_with_reason():
    result = ActionResult(success=False, reason="Invalid input")
    assert result.is_successful() is False
    assert result.describe() == "Action failed: Invalid input"


def test_failed_action_result_without_reason():
    result = ActionResult(success=False)
    assert result.is_successful() is False
    assert result.describe() == "Action failed: Unknown reason"


def test_action_result_with_detail():
    result = ActionResult(success=True, detail={"key": "value"})
    assert result.detail == {"key": "value"}
