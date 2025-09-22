import os
import tempfile
import pytest
from modules.common import json_checker


def test_is_valid_json_string_true():
    valid_json = '{"name": "John", "age": 30}'
    assert json_checker.is_valid_json_string(valid_json) is True


def test_is_valid_json_string_false():
    invalid_json = '{"name": "John", "age": 30'  # missing closing brace
    assert json_checker.is_valid_json_string(invalid_json) is False


def test_is_valid_json_file_true():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json") as tmp:
        tmp.write('{"foo": "bar"}')
        tmp_path = tmp.name
    try:
        assert json_checker.is_valid_json_file(tmp_path) is True
    finally:
        os.remove(tmp_path)


def test_is_valid_json_file_false():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json") as tmp:
        tmp.write('{"foo": ')
        tmp_path = tmp.name
    try:
        assert json_checker.is_valid_json_file(tmp_path) is False
    finally:
        os.remove(tmp_path)


def test_is_valid_json_file_not_exist():
    assert json_checker.is_valid_json_file("non_existing_file.json") is False
