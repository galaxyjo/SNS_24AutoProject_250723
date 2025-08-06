# tests/test_account_runner.py

import pytest
from unittest.mock import patch, AsyncMock
from modules.account_runner import run_account, run_all_accounts


@patch("modules.core.main_features.execute_account", new_callable=AsyncMock)
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "sid, acc_id, expected_status",
    [
        ("TESTSID1", "account_01", "success"),
        ("TESTSID2", "account_02", "fail"),
    ],
)
async def test_run_account(mock_execute_account, sid, acc_id, expected_status):
    if expected_status == "success":
        mock_execute_account.return_value = "ok"
    else:
        async def raise_exception(*args, **kwargs):
            raise Exception("fail")
        mock_execute_account.side_effect = raise_exception

    result = await run_account(sid, acc_id)

    assert isinstance(result, dict)
    assert result["session_id"] == sid
    assert result["account"] == acc_id
    assert result["status"] == expected_status
    assert "message" in result


@patch("modules.account_runner.run_account", new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_run_all_accounts(mock_run_account):
    async def fake_run_account(session_id, acc_id):
        return {
            "session_id": session_id,
            "account": acc_id,
            "status": "success",
            "message": "ok"
        }

    mock_run_account.side_effect = fake_run_account

    result = await run_all_accounts("TEST_SESSION")

    assert result is not None
    assert isinstance(result, dict)
    assert "account_01" in result
    assert result["account_01"]["status"] == "success"
    assert result["account_01"]["message"] == "ok"
