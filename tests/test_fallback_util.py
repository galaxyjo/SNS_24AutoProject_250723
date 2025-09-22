from modules.common.fallback_util import fallback, fallback_dict


def test_fallback():
    assert fallback("A", "B") == "A"
    assert fallback(None, "B") == "B"
    assert fallback(None, None) is None


def test_fallback_dict():
    d = {"x": 1}
    assert fallback_dict(d, "x", 99) == 1
    assert fallback_dict(d, "y", 99) == 99
    assert fallback_dict({}, "x", "default") == "default"
    assert fallback_dict(None, "x", 0) == 0
