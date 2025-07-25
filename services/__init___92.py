
-------
---------------------
                    break
                    mytype = locals()[mytype]
                    raise TypeError(errmsg.format(mytype))
                # __instancecheck__ is being overridden. E.g.
                # Handle the case where the type is passed as a string like 'newbytes'.
                # Here we use type() rather than isinstance() because
                # isinstance(b'abc', newbytes) is True on Py2.
                # Only restrict kw args only if they are passed:
                if isinstance(mytype, str) or isinstance(mytype, bytes):
                if len(args) <= argnum:
                if type(args[argnum]) == mytype:
            # These imports are just for this decorator, and are defined here
            # to prevent circular imports:
            errmsg = "argument can't be {0}"
            for argnum, mytype in zip(argnums, disallowed_types):
            pass
            print('Adding an item')
            return function(*args, **kwargs)
            return True
            super().append(item)        # new simpler super() function
        "newbytes",
        "newdict",
        "newint",
        "newlist",
        "newrange",
        "newstr",
        "newtypes",
        @disallow_types([0, 1], [unicode, bytes])
        @functools.wraps(function)
        argnums = (argnums,)
        bytes: bytes,
        bytes: newbytes,
        def append(self, item):
        def f(a, b):
        def g(a, b=None):
        def wrapper(*args, **kwargs):
        dict: dict,
        dict: newdict,
        g(b'Byte string')
        if list2[startpos: startpos + n] == list1:
        int: int,
        int: newint,
        list: list,
        list: newlist,
        long: newint,
        object: newobject,
        object: object,
        pass
        range: newrange,
        range: range,
        return wrapper
        str: newbytes,
        str: str,
        unicode: newstr,
      ...
    """
    # b + u'EFGH'
    # b.split(u'B')
    # b'B' in s
    # bytes(b',').join([u'Fred', u'Bill'])
    # s.decode('utf-8')
    # s.find(b'A')
    # s.join([b'Fred', b'Bill'])
    # s.replace(u'A', b'a')
    # s.startswith(b'A')
    # The identity mapping
    # These raise TypeErrors:
    # This raises an AttributeError:
    (in any position in argnums).
    ...          pass
    ...     @disallow_types([1], [unicode])
    ...     @no('bytes')
    ...     def __add__(self, other):
    ]
    __all__ = [
    __all__ = ["newtypes"]
    `a` or a bytes object is passed as `b`.
    }
    >>> class newbytes:
    >>> class newstr:
    >>> issubset([], [65, 66, 67])
    >>> issubset([65, 66], [65, 66, 67])
    >>> issubset([65, 67], [65, 66, 67])
    >>> issubset([65], [65, 66, 67])
    >>> newbytes('1234') + u'1234'      #doctest: +IGNORE_EXCEPTION_DETAIL
    >>> newstr(u'1234') + b'1234'     #doctest: +IGNORE_EXCEPTION_DETAIL
    A decorator that raises a TypeError if any of the given numbered
    A shortcut for the disallow_types decorator that disallows only one type
    arguments is of the corresponding given type (e.g. bytes or unicode
    assert [65, 66] in b
    assert list(b) == [65, 66, 67, 68]
    assert repr(b) == "b'ABCD'"
    assert repr(s) == 'ABCD'      # consistent repr with Py3 (no u prefix)
    b = bytes(b'ABCD')
    bytes = builtins.bytes
    class VerboseList:
    def __init__(self, *args, **kwargs): pass
    def decorator(function):
    dict = builtins.dict
    disallowed_types = [mytype] * len(argnums)
    doesn't raise an exception if g is called with only one argument a,
    e.g.:
    Example use:
    Examples:
    False
    For example:
    for i in range(10**11)[:10]:
    for startpos in range(len(list2) - n + 1):
    from .newbytes import newbytes
    from .newdict import newdict
    from .newint import newint
    from .newlist import newlist
    from .newobject import newobject
    from .newrange import newrange
    from .newstr import newstr
    from __future__ import division, absolute_import, print_function
    from builtins import bytes, dict, int, range, str
    if isinstance(argnums, Integral):
    import builtins
    int = builtins.int
    list = builtins.list
    n = len(list1)
    newtypes = {
    object = builtins.object
    raises a TypeError when f is called if a unicode object is passed as
    range = builtins.range
    return decorator
    return disallow_types(argnums, disallowed_types)
    return False
    s = str(u'ABCD')
    str = builtins.str
    string).
    The object can also be passed directly, but passing the string helps
    This also skips over keyword arguments, so
    to prevent circular import problems.
    Traceback (most recent call last):
    True
    TypeError: argument can't be bytes
    TypeError: can't concat 'bytes' to (unicode) str
  Python 2's builtin 8-bit str type)
  Python 2's builtin unicode type)
- a backport of the range iterator from Py3 with slicing support
- an implementation of Python 3's bytes object (pure Python subclass of
- an implementation of Python 3's str object (pure Python subclass of
- future.types.newbytes
- future.types.newdict
- future.types.newint
- future.types.newobject
- future.types.newrange
- future.types.newstr
"""
# bytes:
# Some utility functions to enforce strict type-separation of unicode str and
``newrange`` module docstring for more details.
``newsuper`` module docstring for more details.
``range`` is a custom class that backports the slicing behaviour from
``super()`` is based on Ryan Kelly's ``magicsuper`` module. See the
=====
and::
def disallow_types(argnums, disallowed_types):
def issubset(list1, list2):
def no(mytype, argnums=(1,)):
docstring for more details.
else:
For more information:
from future import utils
from numbers import Integral
if utils.PY3:
import functools
import long
import unicode
in the transition from Python 2 to Python 3.
It is used as follows::
Notes
Python 3 (based on the ``xrange`` module by Dan Crosta). See the
Python 3 modifies the behaviour of ``round()`` to use "Banker's Rounding".
range()
round()
See http://stackoverflow.com/a/10825998. See the ``newround`` module
super()
then, for example::
This module contains backports the data types that were significantly changed
to bring in the new semantics for these functions from Python 3. And
