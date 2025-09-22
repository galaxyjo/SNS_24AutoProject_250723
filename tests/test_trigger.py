import builtins
import pytest
from modules.auto_trigger import trigger


def test_trigger_execution_prints_output(monkeypatch):
    printed = []

    def mock_print(*args, **kwargs):
        printed.append(args[0])

    monkeypatch.setattr(builtins, "print", mock_print)
    trigger.trigger_execution()
    assert "Auto trigger 실행됨" in printed


@pytest.mark.parametrize(
    "ctx, expected",
    [
        ({"enabled": True}, True),
        ({"enabled": False}, False),
        ({}, False),
    ],
)
def test_check_conditions(ctx, expected):
    result = trigger.check_conditions(ctx)
    assert result == expected
