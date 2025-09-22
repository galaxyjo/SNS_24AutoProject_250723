import pytest
from modules.common import regex_util


def test_match_pattern_valid():
    assert regex_util.match_pattern(r"\d+", "123abc").group() == "123"


def test_match_pattern_invalid_pattern():
    assert regex_util.match_pattern(r"[", "123abc") is None


def test_match_pattern_empty_input():
    assert regex_util.match_pattern("", "text") is None
    assert regex_util.match_pattern(r"\d+", "") is None


def test_search_pattern_valid():
    assert regex_util.search_pattern(r"[a-z]+", "123abc456").group() == "abc"


def test_search_pattern_invalid_pattern():
    assert regex_util.search_pattern(r"(", "test") is None


def test_search_pattern_empty_input():
    assert regex_util.search_pattern("", "abc") is None
    assert regex_util.search_pattern(r"[a-z]+", "") is None


def test_is_valid_pattern():
    assert regex_util.is_valid_pattern(r"\w+")
    assert not regex_util.is_valid_pattern(r"[")
