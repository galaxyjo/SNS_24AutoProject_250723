import os
import pytest
from modules.common import file_util

TEST_FILE = "tests/temp_test_file.txt"
TEST_DIR = "tests/temp_test_dir"


def setup_module(module):
    os.makedirs(TEST_DIR, exist_ok=True)
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("hello")


def teardown_module(module):
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(TEST_DIR):
        os.rmdir(TEST_DIR)


def test_file_exists():
    assert file_util.file_exists(TEST_FILE) is True
    assert file_util.file_exists("nonexistent.txt") is False


def test_dir_exists():
    assert file_util.dir_exists(TEST_DIR) is True
    assert file_util.dir_exists("nonexistent_dir") is False


def test_get_file_size():
    assert file_util.get_file_size(TEST_FILE) > 0
    assert file_util.get_file_size("nonexistent.txt") == -1


def test_read_file():
    content = file_util.read_file(TEST_FILE)
    assert content == "hello"


def test_write_file():
    test_path = "tests/write_test.txt"
    file_util.write_file(test_path, "data")
    with open(test_path, encoding="utf-8") as f:
        assert f.read() == "data"
    os.remove(test_path)
