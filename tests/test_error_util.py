# tests/test_error_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import pytest

from modules.common.error_util import extract_exception_message, format_exception_trace


def test_extract_message_with_custom_error():
    class CustomError(Exception):
        pass

    err = CustomError("Something went wrong")
    msg = extract_exception_message(err)
    assert msg == "Something went wrong"


def test_extract_message_empty_error():
    class SilentError(Exception):
        def __str__(self):
            return ""

    err = SilentError()
    msg = extract_exception_message(err, default="No details")
    assert msg == "No details"


def test_extract_message_fallback_to_classname():
    class SilentError(Exception):
        def __str__(self):
            return ""

    err = SilentError()
    msg = extract_exception_message(err)
    assert msg == "SilentError"


def test_extract_message_none():
    msg = extract_exception_message(None, default="Fallback")
    assert msg == "Fallback"


def test_format_exception_trace_output_contains_message():
    try:
        1 / 0
    except ZeroDivisionError as e:
        trace = format_exception_trace(e)
        assert "ZeroDivisionError" in trace
        assert "1 / 0" in trace
        assert "Traceback" in trace
