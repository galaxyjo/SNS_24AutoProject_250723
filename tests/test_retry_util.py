# tests/test_retry_util.py

import pytest
from modules.common.retry_util import retry


def test_retry_success():
    def func():
        return "success"

    assert retry(func) == "success"


def test_retry_eventual_success():
    counter = {"tries": 0}

    def func():
        if counter["tries"] < 2:
            counter["tries"] += 1
            raise ValueError("Try again")
        return "done"

    assert retry(func, retries=3) == "done"


def test_retry_failure_raises():
    def fail():
        raise RuntimeError("fail always")

    with pytest.raises(RuntimeError, match="fail always"):
        retry(fail, retries=2, delay=0.1)
