# C:\SNS_24AutoProject_250723\tests\test_manual_import.py

# tests/test_manual_import.py

import pytest
from modules.manual_import import SomeClass, some_function, config


def test_some_class_double():
    obj = SomeClass(5)
    assert obj.double() == 10


def test_some_function_addition():
    assert some_function(2, 3) == 5
    assert some_function(-1, 1) == 0


def test_config_keys():
    assert "retry" in config
    assert "timeout" in config
    assert config["retry"] == 3
    assert config["timeout"] == 10
