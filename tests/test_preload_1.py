import os
import json
import tempfile
import pytest
from modules.common import preload_1


def test_get_preload_path():
    path = preload_1.get_preload_path("sample.json")
    assert path.endswith("sample.json")


def test_load_preload_data_success():
    with tempfile.TemporaryDirectory() as tmpdir:
        preload_file = os.path.join(tmpdir, "preload.json")
        with open(preload_file, "w", encoding="utf-8") as f:
            json.dump({"a": 1, "b": 2}, f)

        result = preload_1.load_preload_data(preload_file)
        assert isinstance(result, dict)
        assert result["a"] == 1


def test_load_preload_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        preload_1.load_preload_data("nonexistent.json")


def test_get_preload_value_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        preload_file = os.path.join(tmpdir, "preload.json")
        with open(preload_file, "w", encoding="utf-8") as f:
            json.dump({"token": "abc123"}, f)

        value = preload_1.get_preload_value("token", path=preload_file)
        assert value == "abc123"


def test_get_preload_value_not_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        preload_file = os.path.join(tmpdir, "preload.json")
        with open(preload_file, "w", encoding="utf-8") as f:
            json.dump({}, f)

        value = preload_1.get_preload_value("missing", default="none", path=preload_file)
        assert value == "none"
