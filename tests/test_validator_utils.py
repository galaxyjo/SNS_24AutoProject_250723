# tests/test_validator_utils.py
# ✅ pytest 기반 테스트

import pytest
from modules.common import validator_utils


def test_check_wraps_preserves_metadata():
    def f(x): return x
    wrapped = validator_utils.check_wraps(f)
    assert wrapped.__name__ == "f"
    assert wrapped(42) == 42


def test_ensure_not_none():
    assert validator_utils.ensure_not_none("abc") == "abc"
    with pytest.raises(ValueError):
        validator_utils.ensure_not_none(None, "test")


def test_safe_getattr_and_setattr():
    class Dummy: pass

    d = Dummy()
    validator_utils.safe_setattr(d, "x", 123)
    assert validator_utils.safe_getattr(d, "x") == 123

    assert validator_utils.safe_getattr(d, "y", "default") == "default"
