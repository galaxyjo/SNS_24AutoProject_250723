# tests/test_string_cleaner.py
import pytest
from modules.common import string_cleaner


def test_remove_special_chars():
    assert string_cleaner.remove_special_chars("Hello, World!") == "Hello World"
    assert string_cleaner.remove_special_chars("123$%^abc") == "123abc"
    assert string_cleaner.remove_special_chars("A B\tC\nD") == "A B\tC\nD"


def test_normalize_whitespace():
    assert string_cleaner.normalize_whitespace("A  B\tC\nD") == "A B C D"
    assert string_cleaner.normalize_whitespace("   Hello   World   ") == "Hello World"


def test_clean_string():
    assert string_cleaner.clean_string("  Hello,\nWorld!  ") == "Hello World"
    assert string_cleaner.clean_string("A  B$%^ C") == "A B C"
