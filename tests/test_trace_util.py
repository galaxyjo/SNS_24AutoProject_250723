import pytest
from modules.common.trace_util import get_stack_trace_str


def test_get_stack_trace_str():
    try:
        raise ValueError("Test error")
    except Exception as e:
        trace = get_stack_trace_str(e)
        assert isinstance(trace, str)
        assert "ValueError" in trace
        assert "Test error" in trace
