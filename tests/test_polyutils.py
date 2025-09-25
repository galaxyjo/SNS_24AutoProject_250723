# tests/test_polyutils.py

from modules.common.polyutils import parse_name, get_domain, format_url, generate_uid


def test_parse_name():
    assert parse_name("  John  ") == "John"

def test_get_domain():
    assert get_domain("user@example.com") == "example.com"

def test_format_url():
    assert format_url(" HTTP://Example.COM ") == "http://example.com"

def test_generate_uid():
    assert generate_uid("john", "example.com") == "john_example.com"
