# tests/test_common_4.py

import pytest
from modules.common import common_4 as c4

def test_is_even_true():
    assert c4.is_even(2) is True
    assert c4.is_even(0) is True

def test_is_even_false():
    assert c4.is_even(1) is False
    assert c4.is_even(3) is False
