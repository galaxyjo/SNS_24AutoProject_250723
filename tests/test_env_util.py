import os
import pytest
from modules.common import env_util


def test_get_env_variable_existing(monkeypatch):
    monkeypatch.setenv("TEST_KEY", "test_value")
    assert env_util.get_env_variable("TEST_KEY") == "test_value"


def test_get_env_variable_default(monkeypatch):
    monkeypatch.delenv("NON_EXISTENT_KEY", raising=False)
    assert env_util.get_env_variable("NON_EXISTENT_KEY", "default") == "default"


@pytest.mark.parametrize("value", ["1", "true", "yes", "TRUE", "Yes"])
def test_is_env_true_positive(monkeypatch, value):
    monkeypatch.setenv("BOOL_KEY", value)
    assert env_util.is_env_true("BOOL_KEY") is True


@pytest.mark.parametrize("value", ["0", "false", "no", "", "random"])
def test_is_env_true_negative(monkeypatch, value):
    monkeypatch.setenv("BOOL_KEY", value)
    assert env_util.is_env_true("BOOL_KEY") is False


def test_set_env_variable(monkeypatch):
    env_util.set_env_variable("NEW_KEY", "new_value")
    assert os.environ["NEW_KEY"] == "new_value"
