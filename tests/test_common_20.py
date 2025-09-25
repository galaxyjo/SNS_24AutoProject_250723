# tests/test_common_20.py

import importlib
import pytest

def test_module_loads_without_error():
    try:
        importlib.import_module("modules.common.common_20")
    except Exception as e:
        pytest.fail(f"모듈 로딩 실패: {e}")
