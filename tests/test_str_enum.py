# tests/test_str_enum.py
# UTF-8 (no BOM), LF
from __future__ import annotations

import json
import pytest

from modules.common.str_enum import StrEnum
from enum import auto


class Color(StrEnum):
    RED = auto()  # -> "red"
    GREEN = "green"  # explicit
    BLUE = auto()  # -> "blue"


def test_auto_and_explicit_values():
    assert Color.RED.value == "red"
    assert Color.GREEN.value == "green"
    assert Color.BLUE.value == "blue"
    assert str(Color.RED) == "red"


def test_names_and_values_helpers():
    assert Color.names() == ["RED", "GREEN", "BLUE"]
    assert Color.values() == ["red", "green", "blue"]
    assert Color.has_name("RED") is True
    assert Color.has_name("red") is False
    assert Color.has_name("rEd", casefold=True) is True
    assert Color.has_value("green") is True
    assert Color.has_value("Green") is False
    assert Color.has_value("gReEn", casefold=True) is True


def test_from_any_accepts_instance():
    assert Color.from_any(Color.RED) is Color.RED


@pytest.mark.parametrize(
    "inp,expected",
    [
        ("RED", Color.RED),
        ("red", Color.RED),
        ("ReD", Color.RED),
        ("GREEN", Color.GREEN),
        ("green", Color.GREEN),
        ("gReEn", Color.GREEN),
        ("BLUE", Color.BLUE),
        ("blue", Color.BLUE),
    ],
)
def test_from_any_string_name_or_value_casefold(inp, expected):
    assert Color.from_any(inp) is expected


def test_from_any_case_sensitive_mode():
    # exact matches only when casefold=False
    assert Color.from_any("red", casefold=False) is Color.RED
    with pytest.raises(ValueError):
        Color.from_any("ReD", casefold=False)  # no case-insensitive matching here
    assert Color.from_any("GREEN", casefold=False) is Color.GREEN
    # name must be exact when casefold=False
    with pytest.raises(ValueError):
        Color.from_any("Green", casefold=False)


def test_from_any_default_and_errors():
    # default returned on unknown
    assert Color.from_any("chartreuse", default=Color.GREEN) is Color.GREEN
    # None with default
    assert Color.from_any(None, default=Color.BLUE) is Color.BLUE
    # None without default -> error
    with pytest.raises(ValueError):
        Color.from_any(None)
    # unknown without default -> error
    with pytest.raises(ValueError):
        Color.from_any("unknown-color")


def test_json_serialization_helper():
    assert Color.RED.to_json() == "red"
    # ensure it plays nice with json default hook
    payload = {"color": Color.BLUE.to_json()}
    s = json.dumps(payload)
    assert s == '{"color": "blue"}'


def test_invalid_non_string_value_for_member_definition():
    with pytest.raises(TypeError):
        # type: ignore[misc, assignment]
        class Bad(StrEnum):
            X = 1  # non-string -> TypeError

        _ = Bad  # silence linter
