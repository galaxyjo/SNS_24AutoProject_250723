# tests/test_logical_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import pytest
from modules.common.logical_util import coalesce, is_truthy, is_falsy


@pytest.mark.parametrize(
    "args,expected",
    [
        ((None, None, "a", "b"), "a"),
        ((None, 0, "x"), 0),
        ((None, None, None), None),
        ((False, None, True), False),
        (("first", "second"), "first"),
    ],
)
def test_coalesce(args, expected):
    assert coalesce(*args) == expected


@pytest.mark.parametrize(
    "val,expected",
    [
        (True, True),
        (1, True),
        ("x", True),
        ([0], True),
        (False, False),
        (None, False),
        ("", False),
        ([], False),
        (0, False),
    ],
)
def test_is_truthy(val, expected):
    assert is_truthy(val) == expected


@pytest.mark.parametrize(
    "val,expected",
    [
        (True, False),
        (False, True),
        (None, True),
        ("", True),
        ([], True),
        (1, False),
        ("x", False),
    ],
)
def test_is_falsy(val, expected):
    assert is_falsy(val) == expected
