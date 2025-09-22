# tests/test_main_features.py

import pytest
import builtins
from modules.core import main_features


def test_init_core(monkeypatch):
    monkeypatch.setattr("builtins.print", lambda *a, **k: None)
    result = main_features.init_core()
    assert result == "core_init_ok"


@pytest.mark.asyncio
async def test_run_all_mocked(monkeypatch):
    called = {}

    async def mock_runner(session_id):
        called["session"] = session_id

    monkeypatch.setattr(main_features.account_runner, "run_all_accounts", mock_runner)
    await main_features.run_all("test_sess")
    assert called["session"] == "test_sess"


@pytest.mark.asyncio
async def test_execute_account_dummy():
    result = await main_features.execute_account("s1", "a1")
    assert result == "ok"


def test_run_finished_error():
    with pytest.raises(main_features.RunFinishedError):
        raise main_features.RunFinishedError("끝났습니다")


def test_current_task_returns_none():
    assert main_features.current_task() is None
