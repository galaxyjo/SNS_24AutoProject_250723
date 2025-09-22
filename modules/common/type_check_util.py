def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def is_number(obj):
    return isinstance(obj, (int, float, complex)) and not isinstance(obj, bool)


def is_string(obj):
    return isinstance(obj, str)


def is_dict(obj):
    return isinstance(obj, dict)


def is_list(obj):
    return isinstance(obj, list)


def is_tuple(obj):
    return isinstance(obj, tuple)
