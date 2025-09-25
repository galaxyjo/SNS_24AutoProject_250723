import os
import configparser
import tempfile
import pytest
from modules.common.my_configparser import get_config, get_env_value, set_env_value


@pytest.fixture
def temp_config_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.ini') as f:
        f.write("[test_section]\nkey=value\n")
        f.flush()
        yield f.name
    os.remove(f.name)


def test_get_config_with_valid_file(temp_config_file):
    config = get_config(temp_config_file)
    assert isinstance(config, configparser.ConfigParser)


def test_get_env_value_existing_key(temp_config_file):
    value = get_env_value("test_section", "key", temp_config_file)
    assert value == "value"


def test_get_env_value_non_existing_key(temp_config_file):
    value = get_env_value("test_section", "non_existing_key", temp_config_file)
    assert value is None


def test_set_env_value_adds_new_key(temp_config_file):
    set_env_value("test_section", "new_key", "new_value", temp_config_file)
    config = get_config(temp_config_file)
    assert config.get("test_section", "new_key") == "new_value"


def test_set_env_value_adds_new_section(temp_config_file):
    set_env_value("new_section", "new_key", "new_value", temp_config_file)
    config = get_config(temp_config_file)
    assert config.get("new_section", "new_key") == "new_value"
