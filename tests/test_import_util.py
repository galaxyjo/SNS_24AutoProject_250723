# tests/test_import_util.py

import types
import pytest
from modules.common import import_util


def test_dynamic_import_success():
    math_module = import_util.dynamic_import("math")
    assert isinstance(math_module, types.ModuleType)
    assert hasattr(math_module, "sqrt")


def test_dynamic_import_failure():
    result = import_util.dynamic_import("nonexistent_module_xyz123")
    assert result is None


def test_import_from_success():
    sqrt_fn = import_util.import_from("math", "sqrt")
    assert sqrt_fn is not None
    assert sqrt_fn(16) == 4.0


def test_import_from_failure():
    obj = import_util.import_from("math", "not_a_real_function")
    assert obj is None


def test_is_module_available_true():
    assert import_util.is_module_available("math") is True


def test_is_module_available_false():
    assert import_util.is_module_available("nonexistent_module_xyz123") is False
