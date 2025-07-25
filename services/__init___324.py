
                return type.__new__(cls, name, (), d)
            pass
            return meta(name, bases, d)
           if this_bases is None:
        class BaseForm:
        class Form:
        class FormType:
        return a / b
        return a // b
        return obj
        return obj.__native__()
      def __new__(cls, name, this_bases, d):
     __init__ = type.__init__
    """
    __call__ = type.__call__
    __init__ comes back from type etc.).
    >>> # The old_div() function behaves like Python 2's / operator
    >>> # without "from __future__ import division"
    >>> from past.builtins import str, dict
    >>> from past.utils import old_div
    >>> native(str(b'ABC'))   # Output on Py3 follows. On Py2, output is 'ABC'
    >>> old_div(3, 2)    # like 3/2 in Py2
    >>> old_div(3, 2.0)  # like 3/2.0 in Py2
    >>> type(native(b'ABC'))
    >>> type(native(str(b'ABC')))
    0
    1.5
    b'ABC'
    bytes
    class metaclass:
    def __init__(self, *args, **kwargs): pass
    division``.
    dummy classes into the final MRO.
    dummy metaclass for one level of class instantiation that replaces
    else:
    Equivalent to ``a / b`` on Python 2 without ``from __future__ import
    Existing native types on Py3 will be returned unchanged:
    for one level to something closer to type (that's why __call__ and
    Function from jinja2/_compat.py. License: BSD.
    if hasattr(obj, "__native__"):
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
    itself with the actual metaclass.  Because of internal type checks
    On Py2, this is a no-op: native(obj) -> obj
    On Py3, returns the corresponding native Py3 types that are
    return metaclass("temporary_class", None, {})
    superclasses for forward-ported objects from Py2:
    This has the advantage over six.with_metaclass of not introducing
    This requires a bit of explanation: the basic idea is to make a
    TODO: generalize this to other objects (like arrays etc.)
    Use it like this::
    we also need to make sure that we downgrade the custom metaclass
"""
# An alias for future.utils.old_div():
__all__ = ["PY3", "PY2", "PYPY", "with_metaclass", "native", "old_div"]
compatibility in Py3.
def native(obj):
def old_div(a, b):
def with_metaclass(meta, *bases):
For example:
import numbers
import sys
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] >= 3
PYPY = hasattr(sys, "pypy_translation_info")
Various non-built-in utility functions and definitions for Py2
