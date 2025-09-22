from modules.common.type_check_util import (
    is_iterable,
    is_number,
    is_string,
    is_dict,
    is_list,
    is_tuple,
)


def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable("abc")
    assert not is_iterable(123)


def test_is_number():
    assert is_number(5)
    assert is_number(3.14)
    assert not is_number(True)
    assert not is_number("5")


def test_is_string():
    assert is_string("hello")
    assert not is_string(5)


def test_is_dict():
    assert is_dict({})
    assert not is_dict([])


def test_is_list():
    assert is_list([1, 2])
    assert not is_list((1, 2))


def test_is_tuple():
    assert is_tuple((1, 2))
    assert not is_tuple([1, 2])
