
                    _load_lexers(modname)
                _load_lexers(modname)
                _load_lexers(module_name)
                if name not in _lexer_cache:
                matches.append((_lexer_cache[name], filename))
                matches.append((cls, filename))
                matching_lexers.add(lexer)
                primary[lexer] = False
                primary[lexer] = True
            _load_lexers(info[0])
            _load_lexers(module_name)
            _text = _text.decode(inencoding or "utf8")
            _text, _ = guess_decode(_text)
            best_lexer[:] = (rv, lexer)
            cls = _lexer_cache[info[1]]
            exec(f.read(), custom_namespace)
            if _fn_matches(fn, filename):
            if name not in _lexer_cache:
            pass
            raise ClassNotFound(f"no valid {lexername} class found in {filename}")
            return _lexer_cache[name]
            return _lexer_cache[name](**options)
            return cls
            return cls(**options)
            return cls.analyse_text(code) + bonus, cls.__name__
            return get_lexer_by_name(ft, **options)
            return getattr(self, COMPAT[name])
            return lexer(**options)
            setattr(self, name, cls)
            yield lexer.name, lexer.aliases, lexer.filenames, lexer.mimetypes
        "find_lexer_class",
        "get_lexer_by_name",
        "get_lexer_for_filename",
        "guess_lexer",
        "load_lexer_from_file",
        # - analyse score
        # - is primary filename pattern?
        # - last resort: class name
        # - priority
        # And finally instantiate it with the options
        # decode it, since all analyse_text functions expect unicode
        # explicit patterns get a bonus
        # gets turned into 0.0.  Run scripts/detect_missing_analyse_text.py
        # print "Possible lexers, after sort:", matches
        # Retrieve the class `lexername` from that namespace
        # sort by:
        # The class _always_ defines analyse_text because it's included in
        # the Lexer class.  The default implementation returns None which
        # This empty dict will contain the namespace for the exec'd file
        # to find lexers which need it overridden.
        _lexer_cache[cls.name] = cls
        bonus = "*" not in filename and 0.5 or 0
        cls = getattr(mod, lexer_name)
        cls, filename = info
        code = guess_decode(code)
        custom_namespace = {}
        else:
        except ClassNotFound:
        for filename in cls.filenames:
        for filename in filenames:
        for filename in lexer.alias_filenames:
        for filename in lexer.filenames:
        for lexer in find_plugin_lexers():
        if _alias.lower() in aliases:
        if _alias.lower() in cls.aliases:
        if _mime in cls.mimetypes:
        if _mime in mimetypes:
        if cls.name == name:
        if code:
        if inencoding:
        if info:
        if lexername not in custom_namespace:
        if name == lname:
        if name in COMPAT:
        if name not in _lexer_cache:
        if rv == 1.0:
        if rv > best_lexer[0]:
        inencoding = options.get("inencoding", options.get("encoding"))
        info = LEXERS.get(name)
        lexer_class = custom_namespace[lexername]
        matches.sort(key=get_rating)
        module_name, name = LEXERS[key][:2]
        pattern = _pattern_cache[glob] = re.compile(fnmatch.translate(glob))
        raise
        raise AttributeError(name)
        raise ClassNotFound("no lexer matching the text found")
        raise ClassNotFound(f"cannot read {filename}: {err}")
        raise ClassNotFound(f"error when loading custom lexer: {err}")
        raise ClassNotFound(f"no lexer for alias {_alias!r} found")
        raise ClassNotFound(f"no lexer for filename {_fn!r} found")
        raise ClassNotFound(f"no lexer for filename {fn!r} found")
        result.append((rv, lexer))
        return (t[0], primary[t[1]], t[1].priority, t[1].__name__)
        return _lexer_cache[name]
        return cls.priority + bonus, cls.__name__
        return lexer_class(**options)
        return matches[-1][0]
        return matching_lexers.pop()(**options)
        return pattern.match(fn)
        rv = lexer.analyse_text(_text)
        try:
        with open(filename, "rb") as f:
        yield _lexer_cache[name]
        yield from find_plugin_lexers()
        yield item[1:]
    """
    """Automatically import lexers."""
    """Get a lexer for a filename.
    """Load a lexer (and all others in the module too)."""
    """Load a lexer from a file.
    """Return a generator of tuples in the form ``(name, aliases,
    """Return an iterator over all lexer classes."""
    """Return whether the supplied file name fn matches pattern filename."""
    "LeanLexer": "Lean3Lexer",
    "Python3Lexer": "PythonLexer",
    "Python3TracebackLexer": "PythonTracebackLexer",
    # continue with lexers from setuptools entrypoints
    # lookup builtin lexers
    # try to get a vim modeline first
    .. versionadded:: 2.2
    :exc:`pygments.util.ClassNotFound` is raised if no lexer thinks it can
    [
    ]
    `text`. For that, the :meth:`.analyse_text()` method of every known lexer
    + list(COMPAT)
    + list(LEXERS)
    aliases list. The lexer is given the `options` at its
    are also returned.  Otherwise, only builtin ones are considered.
    As :func:`guess_lexer()`, but only lexers which have a pattern in `filenames`
    as the second argument to this function.
    best_lexer = [0.0, None]
    class is called with the text as argument, and the lexer which returned the
    def __getattr__(self, name):
    def __init__(self, *args, **kwargs): pass
    def get_rating(info):
    def type_sort(t):
    directory, which contains a Lexer class. By default, it expects the
    except ClassNotFound:
    except Exception as err:
    except OSError as err:
    figure out which one is more appropriate.
    filenames, mimetypes)`` of all know lexers.
    fn = basename(_fn)
    for cls in find_plugin_lexers():
    for item in LEXERS.values():
    for key in sorted(LEXERS):
    for lexer in _iter_lexerclasses():
    for lexer in matching_lexers:
    for lexer_name in mod.__all__:
    for modname, name, _, _, mimetypes in LEXERS.values():
    for modname, name, _, filenames, _ in LEXERS.values():
    for module_name, lname, aliases, _, _ in LEXERS.values():
    for module_name, name, aliases, _, _ in LEXERS.values():
    found.
    ft = get_filetype_from_buffer(_text)
    handle the content.
    highest value will be instantiated and returned.
    If *plugins* is true (the default), plugin lexers supplied by entrypoints
    if ft is not None:
    if glob not in _pattern_cache:
    if isinstance(code, bytes):
    if len(matching_lexers) == 1:
    if matches:
    If multiple lexers match the filename pattern, use ``analyse_text()`` to
    If multiple lexers match the filename pattern, use their ``analyse_text()``
    if name in _lexer_cache:
    if not _alias:
    if not best_lexer[0] or best_lexer[1] is None:
    if not isinstance(_text, str):
    if not matching_lexers:
    if not res:
    if plugins:
    instantiating it.
    instantiation.
    is equivalent to running eval on the input file.
    is found.
    Lexer to be name CustomLexer; you can specify your own class name
    Like `get_lexer_by_name`, but does not instantiate the class.
    list. The lexer is given the `options` at its instantiation.
    matches = []
    matching `fn`. The lexer is given the `options` at its
    matching_lexers = set()
    methods to figure out which one is more appropriate.
    mod = __import__(module_name, None, None, ["__all__"])
    or `alias_filenames` that matches `filename` are taken into consideration.
    primary = {}
    Raise :exc:`pygments.util.ClassNotFound` if no lexer for that filename
    raise ClassNotFound(f"no lexer for alias {_alias!r} found")
    raise ClassNotFound(f"no lexer for mimetype {_mime!r} found")
    Raises ClassNotFound if there are any problems importing the Lexer.
    res = find_lexer_class_for_filename(_fn, code)
    result = []
    result.sort(key=type_sort)
    return _pattern_cache[glob].match(fn)
    Return a `Lexer` subclass instance that has `mime` in its mimetype
    Return a `Lexer` subclass instance that has a filename pattern
    Return a `Lexer` subclass instance that's guessed from the text in
    Return an instance of a `Lexer` subclass that has `alias` in its
    return best_lexer[1](**options)
    return res(**options)
    return result[-1][1](**options)
    Return the `Lexer` subclass that has `alias` in its aliases list, without
    Return the `Lexer` subclass that with the *name* attribute as given by
    Returns None if not found.
    the *name* argument.
    This method expects a file located relative to the current working
    try:
    Users should be very careful with the input, because this method
    Will raise :exc:`pygments.util.ClassNotFound` if no lexer with that alias is
    Will raise :exc:`pygments.util.ClassNotFound` if not lexer for that mimetype
"""
)
:copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
__all__ = (
_lexer_cache = {}
_pattern_cache = {}
}
~~~~~~~~~~~~~~~
class _automodule:
COMPAT = {
def _fn_matches(fn, glob):
def _iter_lexerclasses(plugins=True):
def _load_lexers(module_name):
def find_lexer_class(name):
def find_lexer_class_by_name(_alias):
def find_lexer_class_for_filename(_fn, code=None):
def get_all_lexers(plugins=True):
def get_lexer_by_name(_alias, **options):
def get_lexer_for_filename(_fn, code=None, **options):
def get_lexer_for_mimetype(_mime, **options):
def guess_lexer(_text, **options):
def guess_lexer_for_filename(_fn, _text, **options):
def load_lexer_from_file(filename, lexername="CustomLexer", **options):
del newmod.newmod, newmod.oldmod, newmod.sys, newmod.types
from os.path import basename
from pip._vendor.pygments.lexers._mapping import LEXERS
from pip._vendor.pygments.modeline import get_filetype_from_buffer
from pip._vendor.pygments.plugin import find_plugin_lexers
from pip._vendor.pygments.util import ClassNotFound, guess_decode
import fnmatch
import re
import sys
newmod = _automodule(__name__)
newmod.__dict__.update(oldmod.__dict__)
oldmod = sys.modules[__name__]
Pygments lexers.
pygments.lexers
sys.modules[__name__] = newmod
