import pytest
from modules.common.common_5 import get_first_element

def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a", "b"]) == "a"
    assert get_first_element([]) is None
    assert get_first_element(None) is None
