"""Tests for the SSLHandler module."""

import pytest
from modules.ssl_handler import SSLHandler


@pytest.mark.parametrize(
    "domain,expected",
    [
        ("www.google.com", True),
        ("expired.badssl.com", False),  # Known invalid SSL
    ],
)
def test_verify_ssl_domains(domain, expected):
    """Test SSL verification for valid and invalid domains."""
    handler = SSLHandler()
    result = handler.verify_ssl(domain)
    assert result == expected
