# tests/test_common_34.py

import os
import pytest
from modules.common import common_34 as c34

def test_save_and_load(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"a": 1, "b": 2}
    c34.save_json_file(data, str(test_file))
    loaded = c34.load_json_file(str(test_file))
    assert loaded == data

def test_load_file_not_exist(tmp_path):
    test_file = tmp_path / "non_exist.json"
    with pytest.raises(FileNotFoundError):
        c34.load_json_file(str(test_file))
