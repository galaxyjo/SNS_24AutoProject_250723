import time
import pytest
from modules.common.decorator_util import timing_decorator, retry_on_exception


def test_timing_decorator():
    @timing_decorator
    def slow_function():
        time.sleep(0.2)
        return "done"

    result = slow_function()
    assert result == "done"
    assert slow_function.last_runtime >= 0.2


def test_retry_on_exception_success_after_retry():
    call_count = {"count": 0}

    @retry_on_exception(max_retries=3, exceptions=(ValueError,), delay=0.05)
    def flaky():
        if call_count["count"] < 2:
            call_count["count"] += 1
            raise ValueError("temporary failure")
        return "success"

    assert flaky() == "success"
    assert call_count["count"] == 2


def test_retry_on_exception_exceeds_max_retries():
    @retry_on_exception(max_retries=2, exceptions=(ValueError,), delay=0.05)
    def always_fail():
        raise ValueError("always fails")

    with pytest.raises(ValueError):
        always_fail()
