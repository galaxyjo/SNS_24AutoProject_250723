# C:\SNS_24AutoProject_250723\tests\test_pprint_util_custom.py

import pytest
from modules.pprint_util_custom import PrettyPrinter


def test_dict_formatting_sorted():
    printer = PrettyPrinter(indent=2, sort_dicts=True)
    sample = {"z": 1, "a": 2}
    result = printer.pformat(sample)
    assert isinstance(result, str)
    assert result.index("a") < result.index("z")


def test_dict_formatting_unsorted():
    printer = PrettyPrinter(indent=2, sort_dicts=False)
    sample = {"z": 1, "a": 2}
    result = printer.pformat(sample)
    assert isinstance(result, str)
    # insertion order assumed in Python 3.7+


def test_format_with_invalid_object():
    class BadObject:
        def __repr__(self):
            raise ValueError("boom")

    printer = PrettyPrinter()
    value, is_readable, is_recursive = printer.format(BadObject(), {}, 10, 0)
    assert value == "<bad value>"
    assert is_readable is True
    assert is_recursive is False


def test_safe_key_and_value():
    printer = PrettyPrinter()

    class BadKey:
        def __str__(self):
            raise ValueError("bad key")

    class BadValue:
        def __str__(self):
            raise ValueError("bad value")

    d = {BadKey(): BadValue()}
    result = printer._format_dict(d)
    assert result == {"<bad key>": "<bad value>"}


def test_format_list_with_bad_value():
    printer = PrettyPrinter()

    class BadValue:
        def __str__(self):
            raise ValueError("bad value")

    result = printer._format_list([1, BadValue()])
    assert result == ["1", "<bad value>"]
