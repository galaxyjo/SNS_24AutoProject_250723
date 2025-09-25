import importlib
import pytest


def test_module_loads_without_error():
    try:
        importlib.import_module("modules.common.common_28")
    except Exception as e:
        pytest.fail(f"모듈 로딩 실패: {e}")


from modules.common.common_utils import is_numeric


@pytest.mark.parametrize("value,expected", [
    ("123", True),
    ("45.67", True),
    ("-89", True),
    ("abc", False),
    ("", False),
    (None, False),
    (123, True),
    (45.6, True),
])
def test_is_numeric(value, expected):
    assert is_numeric(value) == expected
