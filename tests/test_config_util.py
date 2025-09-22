import json
import os
import tempfile

from modules.common.config_util import load_config, get_config_value


def test_load_config_valid():
    temp_file = tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8", suffix=".json"
    )
    json.dump({"key": "value"}, temp_file)
    temp_file.close()

    config = load_config(temp_file.name)
    assert config == {"key": "value"}

    os.remove(temp_file.name)


def test_load_config_missing_file():
    config = load_config("non_existing_file.json")
    assert config == {}


def test_get_config_value_exists():
    config = {"timeout": 30}
    assert get_config_value(config, "timeout") == 30


def test_get_config_value_default():
    config = {}
    assert get_config_value(config, "retry", default=5) == 5
