import pytest
from modules.common import text_block_util


def test_dedent_block():
    input_text = "    line1\n        line2\n    line3"
    expected = "line1\n    line2\nline3"
    assert text_block_util.dedent_block(input_text) == expected


def test_trim_block():
    input_text = "\n\nline1\nline2\n\n"
    expected = "line1\nline2"
    assert text_block_util.trim_block(input_text) == expected


def test_remove_duplicate_lines():
    input_text = "a\nb\na\nc\nb"
    expected = "a\nb\nc"
    assert text_block_util.remove_duplicate_lines(input_text) == expected
