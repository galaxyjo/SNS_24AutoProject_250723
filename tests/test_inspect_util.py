# tests/test_inspect_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

from modules.common.inspect_util import get_function_name, get_caller_name, is_lambda


def regular_function():
    return "hello"


def test_get_function_name_regular():
    assert get_function_name(regular_function) == "regular_function"


def test_get_function_name_lambda():
    f = lambda x: x + 1
    assert get_function_name(f) == "<lambda>"


def test_get_function_name_non_callable():
    assert get_function_name(1234) == "<not-callable>"


def test_get_caller_name_returns_self():
    def caller():
        return get_caller_name(level=1)  # self

    assert caller() == "caller"


def test_get_caller_name_default_level():
    def wrapper():
        return get_caller_name()  # should return test name

    name = wrapper()
    assert name.startswith("test_")


def test_is_lambda_with_lambda():
    f = lambda x: x
    assert is_lambda(f) is True


def test_is_lambda_with_normal_function():
    assert is_lambda(regular_function) is False
