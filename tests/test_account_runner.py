import pytest
from modules.account_runner import run_all_accounts


def test_run_all_accounts_executes():
    try:
        result = run_all_accounts("test_session")
        assert result is None or result is not False
    except Exception as e:
        pytest.fail(f"run_all_accounts raised an exception: {e}")
