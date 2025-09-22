# tests/test_pickle_serializer.py

import pytest
from modules import pickle_serializer


def test_dumps_and_loads_basic():
    obj = {"a": 1, "b": [1, 2, 3]}
    data = pickle_serializer.dumps(obj)
    result = pickle_serializer.loads(data)
    assert result == obj


def test_dumps_returns_bytes():
    obj = [1, 2, 3]
    data = pickle_serializer.dumps(obj)
    assert isinstance(data, bytes)


def test_loads_invalid_data_raises():
    with pytest.raises(Exception):
        pickle_serializer.loads(b"not a pickle")
