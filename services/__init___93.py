
    -------
    ----------
                "class must derive from BaseException, not %s" % tp.__name__
                exc = tp()
                exc = tp(*value)
                exc = tp(value)
                exc = value
                locs = frame.f_locals
                raise TypeError("instance exception may not have a separate value")
                return bytes(s)
                return f(*args, **kwargs).encode(encoding=encoding)
                return newbytes(obj)
                return newdict(obj)
                return newint(obj)
                return newstr(obj)
                return next(self._iter).upper()
                return obj
                return s.encode("latin-1")
                return self
                return type.__new__(cls, name, (), d)
                self._iter = iter(iterable)
            "raise __python_future_raise_from_exc from __python_future_raise_from_cause"
            # Already a new type
            # and the second object must be None.
            # constructor is used as the exception value.
            # exc = exc.__name__
            # exception.
            # exec(execstr, myglobals, mylocals)
            # execstr = "e = " + _repr_strip(exc) + "()"
            # If the first object is a class, it becomes the type of the
            # If the first object is an instance, the type of the exception
            # is an instance of the class, the instance becomes the exception
            # is the class of the instance, the instance itself is the value,
            # list for the class constructor; if it is None, an empty argument
            # list is used, and any other object is treated as a single argument
            # myglobals, mylocals = _get_caller_globals_and_locals()
            # The second object is used to determine the exception value: If it
            # to the constructor. The instance so created by calling the
            # Upcast
            # value. If the second object is a tuple, it is used as the argument
            )
            @as_native_str(encoding='ascii')
            @functools.wraps(f)
            _, _, traceback = sys.exc_info()
            assert type(obj) in [newbytes, newstr]
            def __init__(self, iterable):
            def __iter__(self):
            def __next__(self):
            def __repr__(self):
            def wrapper(*args, **kwargs):
            del frame
            e = exc
            e = exc()
            e.__cause__ = cause
            e.__cause__ = cause()
            e.__cause__ = None
            e.__cause__.__traceback__ = sys.exc_info()[2]
            e.__suppress_context__ = True
            elif isinstance(value, tuple):
            elif native_type == dict:
            elif native_type == int:
            elif native_type == long:
            elif native_type == unicode:
            elif value is None:
            else:
            exc = tp
            frame = sys._getframe(1)
            globs = frame.f_globals
            if isinstance(s, str):
            if isinstance(value, tp):
            if locs is None:
            if native_type == str:  # i.e. Py2 8-bit str
            if value is not None:
            locs = globs
            object.__setattr__(e.__cause__, "__traceback__", sys.exc_info()[2])
            pass
            raise exc.with_traceback(tb)
            raise EXCEPTION from CAUSE
            raise TypeError(
            raise TypeError("exception causes must derive from BaseException")
            return "".join(s)
            return bytes(s)
            return bytes(s, "latin-1")
            return filename.encode("utf-8")
            return meta(name, bases, d)
            return obj
            return s
            return s.encode("latin-1")
            return wrapper
           if this_bases is None:
        - iteritems, iterkeys, itervalues
        - viewitems, viewkeys, viewvalues
        """
        """Execute code in a namespace."""
        "__dict__" in dir(cls) or hasattr(cls, "__slots__")
        # instance (e.g. IndexError('my message here')? If so, pass the
        # Is either arg an exception class (e.g. IndexError) rather than
        # name of the class undisturbed through to "raise ... from ...".
        # Upcast only if the type is already a native (non-future) type
        # We pass the exception and cause along with other globals
        # when we exec():
        )
        * binary_type: str in Python 2, bytes in Python 3
        * class_types: (type, types.ClassType) in Python 2, type in Python 3
        * integer_types: (int, long) in Python 2, int in Python 3
        * string_types: basestring in Python 2, str in Python 3
        * text_type: unicode in Python 2, str in Python 3
        @implements_iterator
        _, _, traceback = sys.exc_info()
        _name_re = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*$")
        >>> from future.builtins import bytes
        >>> from future.builtins import int
        >>> from future.builtins import str
        >>> from numbers import Integral
        >>> isinstance(obj, bytes)
        >>> isinstance(obj, int)
        >>> isinstance(obj, Integral)
        >>> isinstance(obj, str)
        A function that matches the Python 2.x ``raise`` statement. This
        allows re-raising exceptions with the cls value and traceback on
        class BaseForm:
        class Form:
        class FormType:
        class MyClass:
        class to receive bound method
        class UppercasingIterator:
        cls.__str__ = lambda self: self.__unicode__().encode("utf-8")
        cls.__unicode__ = cls.__str__
        cls.next = cls.__next__
        def encoder(f):
        del cls.__next__
        e.__context__ = sys.exc_info()[1]
        e.__suppress_context__ = False
        elif cause is None:
        elif isinstance(cause, BaseException):
        elif isinstance(tp, type) and not issubclass(tp, BaseException):
        elif locs is None:
        else:
        Equivalent to:
        exec("""exec code in globs, locs""")
        exec(execstr, myglobals, mylocals)
        execstr = (
        from __future__ import unicode_literals
        from a byte string, and make a byte string.
        from future.types import newbytes  # to avoid a circular import
        from future.types.newbytes import newbytes
        from future.types.newdict import newdict
        from future.types.newint import newint
        from future.types.newstr import newstr
        func = obj.items
        func = obj.keys
        func = obj.values
        function to be bound as method
        if exc.__traceback__ is not tb:
        if globs is None:
        if isinstance(cause, type) and issubclass(cause, Exception):
        if isinstance(exc, type) and issubclass(exc, Exception):
        if isinstance(filename, unicode):
        if isinstance(s, bytes):
        if isinstance(s, str):
        if isinstance(s, unicode):
        if isinstance(tp, BaseException):
        if issubclass(native_type, type(obj)):
        if traceback == Ellipsis:
        import re
        keys, values.
        myglobals = myglobals.copy()
        myglobals, mylocals = _get_caller_globals_and_locals()
        myglobals["__python_future_raise_from_cause"] = cause
        myglobals["__python_future_raise_from_exc"] = exc
        name of method on class instance
        native_type = type(native(obj))
        on Python 3. (See PEP 3134).
        Python 2 and 3.
        raise e
        raise exc
        raise exc.with_traceback(traceback)
        return a / b
        return a // b
        return all(isidentifier(a) for a in s.split("."))
        return b.decode(encoding)
        return bool(_name_re.match(s))
        return bytes([s])
        return chr(s)
        return cls
        return d.items()
        return d.values()
        return encoder
        return filename
        return lambda f: f
        return list(d.items())
        return list(d.values())
        return list(filter(*args, **kwargs))
        return list(map(*args, **kwargs))
        return list(range(*args, **kwargs))
        return list(zip(*args, **kwargs))
        return native(b)
        return newbytes(s)
        return obj
        return obj.__native__()
        return ord(s)
        return r
        return r[1:-1]
        return s
        return s.encode(encoding)
        return s.isidentifier()
        return str(s)
        return t
        return unicode(t).encode(encoding)
        setattr(cls, name, func)
        setattr(cls, name, types.MethodType(func, None, cls))
        Take a text string, a byte string, or a sequence of characters taken
        Take an integer and make a 1-character byte string
        Take the result of indexing on a byte string and make an integer
        These use the original method if available, otherwise they use items,
        unicode_literals" is in effect.
        Use this to create a Py2 native string when "from __future__ import
      def __new__(cls, name, this_bases, d):
      https://github.com/mitsuhiko/jinja2/blob/master/LICENSE)
      this may be shadowed by imports from future.builtins)
     __init__ = type.__init__
    """
    """Bind a method to class, python 2 and python 3 compatible.
    """Use this only if compatibility with Python versions before 2.7 is
    "as_native_str",
    "binary_type",
    "bind_method",
    "bord",
    "bstr",
    "bytes_to_native_str",
    "class_types",
    "encode_filename",
    "ensure_new_type",
    "exec_",
    "get_next",
    "getexception",
    "implements_iterator",
    "integer_types",
    "is_new_style",
    "isbytes",
    "isidentifier",
    "isint",
    "isnewbytes",
    "istext",
    "iteritems",
    "iterkeys",
    "itervalues",
    "lfilter",
    "listitems",
    "listvalues",
    "lmap",
    "lrange",
    "lzip",
    "native",
    "native_bytes",
    "native_str",
    "native_str_to_bytes",
    "old_div",
    "PY2",
    "PY26",
    "PY3",
    "PYPY",
    "python_2_unicode_compatible",
    "raise_",
    "raise_with_traceback",
    "reraise",
    "string_types",
    "text_to_native_str",
    "text_type",
    "tobytes",
    "viewitems",
    "viewkeys",
    "viewvalues",
    "with_metaclass",
    # list-producing versions of the major Python iterating functions
    # only python 2 has an issue with bound/unbound methods
    # Python 2
    # Python 2-builtin ranges produce lists
    # Python 3
    )
    * ``implements_iterator``
    * ``native_str_to_bytes`` and ``bytes_to_native_str``
    * ``native_str``: always equal to the native platform string object (because
    * ``python_2_unicode_compatible``
    * ``with_metaclass``
    * bchr(c):
    * bind_method: binds functions to classes
    * bord(c)
    * Django
    * iterable method compatibility:
    * Jinja2 (BSD licensed: see
    * lists: lrange(), lmap(), lzip(), lfilter()
    * Pandas compatibility module pandas.compat
    * raise_from()
    * raise_with_traceback()
    * six.py by Benjamin Peterson
    * tobytes(s)
    * types:
    ...         return u'Unicode string: \u5b54\u5b50'
    ...     def __str__(self):
    ... class MyClass:
    __call__ = type.__call__
    __init__ comes back from type etc.).
    ``long``.
    >>> @python_2_unicode_compatible
    >>> a = MyClass()
    >>> from builtins import str, bytes, int
    >>> from future.builtins import str
    >>> from future.utils import python_2_unicode_compatible
    >>> native(bytes(b'ABC'))
    >>> native(int(10**20))
    >>> native(str(u'ABC'))
    >>> print(a)
    >>> print(str(a))
    >>> str(a) == a.encode('utf-8').decode('utf-8')
    >>> type(native(bytes(b'ABC')))
    >>> type(native(int(10**20)))
    >>> type(native(str(u'ABC')))
    >>> type(native(u'ABC'))
    100000000000000000000L
    2. Under Python 3, this decorator is a no-op.
    A decorator that defines __unicode__ and __str__ methods under Python
    A decorator to turn a function or method call that returns text, i.e.
    A function equivalent to the str.isidentifier method on Py3
    after this import:
    and, on a Unicode-enabled terminal with the right fonts, these both print the
    ASCII.)
    b'ABC'
    be pesky in some circumstances, such as when using inheritance.  Use this
    behaviour on Py2.7 as on Py3.
    binary_type = bytes
    binary_type = str
    bytes
    caller_frame = inspect.stack()[2]
    Chinese characters for Confucius::
    class metaclass:
    class_types = (type, types.ClassType)
    class_types = (type,)
    cls : type
    def __init__(self, *args, **kwargs): pass
    def bchr(s):
    def bord(s):
    def bstr(s):
    def bytes_to_native_str(b, encoding="utf-8"):
    def bytes_to_native_str(b, encoding=None):
    def ensure_new_type(obj):
    def exec_(code, globs=None, locs=None):
    def get_next(x): return x.__next__
    def get_next(x): return x.next
    def lfilter(*args, **kwargs):
    def listitems(d):
    def listvalues(d):
    def lmap(*args, **kwargs):
    def lrange(*args, **kwargs):
    def lzip(*args, **kwargs):
    def native_str_to_bytes(s, encoding="utf-8"):
    def native_str_to_bytes(s, encoding=None):
    def raise_(tp, value=None, tb=None):
    def raise_from(exc, cause):
    def raise_with_traceback(exc, traceback=Ellipsis):
    def text_to_native_str(t, encoding="ascii"):
    def text_to_native_str(t, encoding=None):
    def tobytes(s):
    Deprecated. Tests whether an object is a Py3 ``int`` or either a Py2 ``int`` or
    Deprecated. Use::
    DEPRECATED: import ``old_div`` from ``past.utils`` instead.
    dict.iteritems
    division``.
    dummy classes into the final MRO.
    dummy metaclass for one level of class instantiation that replaces
    else:
    Encodes to latin-1 (where the first 256 chars are the same as
    Equivalent to ``a / b`` on Python 2 without ``from __future__ import
    equivalent to ininstance(obj, newbytes)
    Equivalent to the result of ``type(obj)  == type(newbytes)``
    exec(
    exec_ = getattr(builtins, "exec")
    Existing native types on Py2 will be returned unchanged:
    for one level to something closer to type (that's why __call__ and
    From jinja2/_compat.py. License: BSD.
    func : function
    func = getattr(obj, "iteritems", None)
    func = getattr(obj, "iterkeys", None)
    func = getattr(obj, "itervalues", None)
    func = getattr(obj, "viewitems", None)
    func = getattr(obj, "viewkeys", None)
    func = getattr(obj, "viewvalues", None)
    Function for iterating over dictionary items with the same set-like
    Function for iterating over dictionary keys with the same set-like
    Function for iterating over dictionary values with the same set-like
    Function from jinja2/_compat.py. License: BSD.
    function to test for whether a class is new-style. (Python 3 only has
    if dotted:
    if hasattr(obj, "__native__"):
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
    if not func:
    if not PY3:
    if PY3:
    if r.startswith("'") and r.endswith("'"):
    if traceback == Ellipsis:
    import __builtin__
    import builtins
    in other words, it is REALLY a newbytes instance, not a Py2 native str
    Instead of using this function, you can use:
    integer_types = (int, long)
    integer_types = (int,)
    Is there an alternative to frame hacking here?
    itself with the actual metaclass.  Because of internal type checks
    lfilter = __builtin__.filter
    lmap = __builtin__.map
    long
    lrange = __builtin__.range
    lzip = __builtin__.zip
    method returning unicode text and apply this decorator to the class, like
    myglobals = caller_frame[0].f_globals
    mylocals = caller_frame[0].f_locals
    name : basestring
    new-style classes.)
    None
    Note that this does not cover subclasses of newbytes, and it is not
    object?
    On Py2, returns a newbytes type, ignoring the ``encoding`` argument.
    On Py2, returns the corresponding native Py2 types that are
    On Py3, returns an encoded string.
    On Py3, this is a no-op: native(obj) -> obj
    Parameters
    Passes kwargs to method."""
    Python 2.7 has both new-style and old-style classes. Old-style classes can
    r = repr(mystring)
    raise exc, None, traceback
    raise tp, value, tb
    required. Otherwise, prefer viewitems().
    required. Otherwise, prefer viewkeys().
    required. Otherwise, prefer viewvalues().
    return cls
    return func(**kwargs)
    return hasattr(cls, "__class__") and (
    return isinstance(obj, bytes)
    return isinstance(obj, numbers.Integral)
    return isinstance(obj, str)
    return metaclass("temporary_class", None, {})
    return myglobals, mylocals
    return sys.exc_info()[1]
    return type(obj).__name__ == "newbytes"
    Returns
    Returns the globals and locals of the calling frame.
    Returns the string without any initial or final quotes.
    string_types = (basestring,)
    string_types = (str,)
    superclasses for backported objects from Py3:
    text_type = str
    text_type = unicode
    The following idiom is equivalent:
    the following is ``True`` on both Python 3 and 2::
    The implementation comes from django.utils.encoding.
    Then, after this import:
    This has the advantage over six.with_metaclass of not introducing
    This requires a bit of explanation: the basic idea is to make a
    this::
    To support Python 2 and 3 with a single code base, define a __str__
    TODO: generalize this to other objects (like arrays etc.)
    True
    u'ABC'
    unicode
    unicode, into one that returns a native platform str.
    Use as a decorator like this::
    Use it as a decorator like this::
    Use it like this::
    we also need to make sure that we downgrade the custom metaclass
"""
""".strip()
# ``bytes`` are redefined on Py2 by ``from future.builtins import *``.
# Defined here for backward compatibility:
# Definitions from pandas.compat and six.py follow:
# Deprecated alias for backward compatibility with ``future`` versions < 0.11:
# Implementation of exec_ is from ``six``:
# listvalues and listitems definitions from Nick Coghlan's (withdrawn)
# PEP 496:
# The native platform string and bytes types. Useful because ``str`` and
###
]
__all__ = [
A selection of cross-compatible functions for Python 2 and 3.
def _get_caller_globals_and_locals():
def _repr_strip(mystring):
def as_native_str(encoding="utf-8"):
def bind_method(cls, name, func):
def encode_filename(filename):
def getexception():
def implements_iterator(cls):
def is_new_style(cls):
def isbytes(obj):
def isidentifier(s, dotted=False):
def isint(obj):
def isnewbytes(obj):
def istext(obj):
def iteritems(obj, **kwargs):
def iterkeys(obj, **kwargs):
def itervalues(obj, **kwargs):
def native(obj):
def old_div(a, b):
def python_2_unicode_compatible(cls):
def raise_(tp, value=None, tb=None):
def raise_with_traceback(exc, traceback=Ellipsis):
def viewitems(obj, **kwargs):
def viewkeys(obj, **kwargs):
def viewvalues(obj, **kwargs):
def with_metaclass(meta, *bases):
else:
except AttributeError:
if PY3:
If traceback is not passed, uses sys.exc_info() to get traceback."""
import copy
import functools
import inspect
import numbers
import sys
import types
native_bytes = bytes
native_str = str
native_str_to_bytes.__doc__ = """
PY2 = sys.version_info[0] == 2
PY26 = sys.version_info[0:2] == (2, 6)
PY27 = sys.version_info[0:2] == (2, 7)
PY3 = sys.version_info[0] >= 3
PY34_PLUS = sys.version_info[0:2] >= (3, 4)
PY35_PLUS = sys.version_info[0:2] >= (3, 5)
PY36_PLUS = sys.version_info[0:2] >= (3, 6)
PY37_PLUS = sys.version_info[0:2] >= (3, 7)
PY38_PLUS = sys.version_info[0:2] >= (3, 8)
PY39_PLUS = sys.version_info[0:2] >= (3, 9)
PYPY = hasattr(sys, "pypy_translation_info")
raise_with_traceback.__doc__ = """Raise exception with existing traceback.
reraise = raise_
Some of the functions in this module come from the following sources:
This module also defines these decorators:
This module exports useful functions for 2/3 compatible code:
tobytes.__doc__ = """
try:
