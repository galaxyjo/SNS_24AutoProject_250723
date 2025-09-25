import importlib
import pytest

def test_module_loads_without_error():
    importlib.import_module("modules.common.common_29")

def test_has_no_top_level_execution():
    with open("modules/common/common_29.py", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().startswith("print(") or "if __name__" in line:
            pytest.fail("Top-level execution or print found.")
