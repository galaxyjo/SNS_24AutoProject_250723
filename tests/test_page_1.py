# tests/test_page_1.py

import pytest
from modules.common.page_1 import paginate


def test_paginate_normal_case():
    items = list(range(1, 21))
    assert paginate(items, page_size=5, page_number=2) == [6, 7, 8, 9, 10]


def test_paginate_first_page():
    items = list(range(10))
    assert paginate(items, page_size=3, page_number=1) == [0, 1, 2]


def test_paginate_last_partial_page():
    items = list(range(7))
    assert paginate(items, page_size=3, page_number=3) == [6]


def test_paginate_out_of_range_page():
    items = list(range(5))
    assert paginate(items, page_size=2, page_number=4) == []


def test_paginate_invalid_page_size():
    with pytest.raises(ValueError):
        paginate([1, 2, 3], page_size=0, page_number=1)


def test_paginate_invalid_page_number():
    with pytest.raises(ValueError):
        paginate([1, 2, 3], page_size=2, page_number=0)
