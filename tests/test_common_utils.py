# tests/test_common_utils.py

import pytest
from modules.common.common_utils import (
    get_list_element,
    is_numeric,
    calculate_area,
    SimpleDictStore,
    ensure_path_exists,
)
import os


# ✅ get_list_element 테스트
def test_get_list_element_valid():
    assert get_list_element([10, 20, 30], 1) == 20

def test_get_list_element_index_error():
    with pytest.raises(IndexError):
        get_list_element([1, 2], 5)

def test_get_list_element_type_error():
    with pytest.raises(TypeError):
        get_list_element("not a list", 0)


# ✅ is_numeric 테스트
@pytest.mark.parametrize("val", ["123", 456, "3.14", 0.0])
def test_is_numeric_true(val):
    assert is_numeric(val) is True

@pytest.mark.parametrize("val", ["abc", None, {}, []])
def test_is_numeric_false(val):
    assert is_numeric(val) is False


# ✅ calculate_area 테스트
def test_calculate_area():
    assert calculate_area(5.0, 4.0) == 20.0


# ✅ SimpleDictStore 테스트
def test_simple_dict_store():
    store = SimpleDictStore()
    store.add_entry("a", 1)
    assert store.get_entry("a") == 1

    store.remove_entry("a")
    assert store.get_entry("a") is None

    store.add_entry("b", 2)
    store.clear_entries()
    assert store.get_all_entries() == {}


# ✅ ensure_path_exists 테스트
def test_ensure_path_exists_tmp(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("test")
    ensure_path_exists(str(path))  # should not raise

def test_ensure_path_exists_fail():
    with pytest.raises(FileNotFoundError):
        ensure_path_exists("nonexistent/path.txt")
