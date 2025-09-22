
f"\nAt Date: {base}"
            f"\nExpected: {expected}\nActual: {actual}\nFor Offset: {offset})"
        ) from err
        assert actual == expected
        assert actual_apply == expected
        assert actual_swapped == expected
        f"\nAt Date: {date}"
        f"\nExpected: {expected}\nActual: {actual}\nFor Offset: {offset})"
        raise AssertionError(
    )
    actual = offset + base
    actual = offset.is_on_offset(date)
    actual_apply = offset._apply(base)
    actual_swapped = base + offset
    assert actual == expected, (
    except AssertionError as err:
    FRI = 4
    MON = 0
    SAT = 5
    SUN = 6
    THU = 3
    try:
    TUE = 1
    WED = 2
"""
Assertion helpers and base class for offsets tests
class WeekDay:
def assert_is_on_offset(offset, date, expected):
def assert_offset_equal(offset, base, expected):
from __future__ import annotations

pass
