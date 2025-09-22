# C:\SNS_24AutoProject_250723\tests\test_six_util_custom.py

from modules.six_util_custom import SixWrapper


def test_wrapper_basic():
    wrapper = SixWrapper()
    result = wrapper.wrap("test")
    assert result == "<wrapped>test</wrapped>"


def test_wrapper_empty_input():
    wrapper = SixWrapper()
    result = wrapper.wrap("")
    assert result == "<wrapped></wrapped>"


def test_unwrap_basic():
    wrapper = SixWrapper()
    wrapped = wrapper.wrap("hello")
    assert wrapper.unwrap(wrapped) == "hello"


def test_unwrap_passthrough_when_not_wrapped():
    wrapper = SixWrapper()
    raw = "not_wrapped"
    # unwrap은 래핑되지 않은 경우 원문을 그대로 반환해야 한다.
    assert wrapper.unwrap(raw) == raw


def test_wrap_then_unwrap_empty_string():
    wrapper = SixWrapper()
    wrapped_empty = wrapper.wrap("")
    # "<wrapped></wrapped>"에서 언래핑 시 빈 문자열이어야 한다.
    assert wrapper.unwrap(wrapped_empty) == ""
