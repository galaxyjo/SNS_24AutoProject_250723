
    # from .unicode import unicode
    __all__ = ["basestring", "olddict", "oldstr", "long", "unicode"]
    __all__ = []
    basestring = __builtin__.basestring
    dict = __builtin__.dict
    from .basestring import basestring
    from .olddict import olddict
    from .oldstr import oldstr
    import __builtin__
    long = __builtin__.long
    long = int
    str = __builtin__.str
    unicode = __builtin__.unicode
    unicode = str
- ``basestring``: equivalent to ``(str, bytes)`` in ``isinstance`` checks
- ``dict``: with list-producing .keys() etc. methods
- ``long``: alias of Py3 int with ``L`` suffix in the ``repr``
- ``str``: bytes-like, but iterating over them doesn't product integers
- ``unicode``: alias of Py3 str with ``u`` prefix in the ``repr``
"""
else:
Forward-ports of types from Python 2 for use with Python 3:
from past import utils
if utils.PY2:
