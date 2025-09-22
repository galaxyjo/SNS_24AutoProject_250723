# tests/test_path_util.py

import os
import pytest
from modules.common import path_util


def test_get_filename():
    assert path_util.get_filename("/a/b/c.txt") == "c.txt"


def test_get_directory():
    assert path_util.get_directory("/a/b/c.txt") == "/a/b"


def test_join_paths():
    assert path_util.join_paths("a", "b", "c.txt") == os.path.join("a", "b", "c.txt")


def test_split_extension():
    name, ext = path_util.split_extension("file.tar.gz")
    assert name == "file.tar"
    assert ext == ".gz"


def test_is_absolute():
    assert path_util.is_absolute("/usr/bin") is True
    assert path_util.is_absolute("relative/path") is False
