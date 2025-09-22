# tests/test_string_util.py

import pytest
from modules.common.string_util import (
    is_blank,
    normalize_whitespace,
    safe_lower,
    safe_upper,
    truncate,
    remove_accents,
    to_slug,
    to_snake_case,
    to_camel_case,
    strip_html,
    split_words,
    join_non_empty,
)


def test_is_blank():
    assert is_blank(None)
    assert is_blank("   \t")
    assert not is_blank("x")


def test_normalize_whitespace():
    assert normalize_whitespace("  a   b \n  c ") == "a b c"
    text = "  a   b \n\n  c\t\t d "
    assert (
        normalize_whitespace(text, keep_newlines=True) == "a b \n c d"
    )  # ← 수정된 기대값


def test_safe_lower_upper():
    assert safe_lower(None) == ""
    assert safe_upper(None) == ""
    assert safe_lower("AbC") == "abc"
    assert safe_upper("AbC") == "ABC"


def test_truncate():
    assert truncate("abcdef", 10) == "abcdef"
    assert truncate("abcdef", 5) == "abcd…"
    assert truncate("abcdef", 1) == "…"
    with pytest.raises(ValueError):
        truncate("abc", -1)


def test_remove_accents():
    assert remove_accents("Café") == "Cafe"
    assert remove_accents("áéíóú") == "aeiou"
    assert remove_accents(None) == ""


def test_to_slug():
    assert to_slug("Hello, World!") == "hello-world"
    assert to_slug("한글 테스트", allow_unicode=False) == ""
    assert to_slug("한글 테스트", allow_unicode=True) == "한글-테스트"


def test_to_snake_case():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello world-text") == "hello_world_text"
    assert to_snake_case("") == ""


def test_to_camel_case():
    assert to_camel_case("hello_world test") == "helloWorldTest"
    assert to_camel_case("hello_world test", upper_first=True) == "HelloWorldTest"
    assert to_camel_case("") == ""


def test_strip_html():
    assert strip_html("<b>Hi</b> &amp; bye") == "Hi & bye"
    assert strip_html(None) == ""


def test_split_words_and_join():
    assert split_words("  a   b  c ") == ["a", "b", "c"]
    assert split_words(None) == []
    joined = join_non_empty(["", "a", None, "b", "  "], sep=",")
    assert joined == "a,b"
