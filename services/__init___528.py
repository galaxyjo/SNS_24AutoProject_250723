
                    _load_formatters(modname)
                _load_formatters(module_name)
                if name not in _formatter_cache:
                return _formatter_cache[name](**options)
                return cls(**options)
            _load_formatters(info[0])
            cls = _formatter_cache[info[1]]
            exec(f.read(), custom_namespace)
            if _fn_matches(fn, filename):
            if name not in _formatter_cache:
            raise ClassNotFound(f"no valid {formattername} class found in {filename}")
            return _formatter_cache[name]
            return cls
            setattr(self, name, cls)
        # And finally instantiate it with the options
        # Retrieve the class `formattername` from that namespace
        # This empty dict will contain the namespace for the exec'd file
        _formatter_cache[cls.name] = cls
        cls = getattr(mod, formatter_name)
        custom_namespace = {}
        for filename in cls.filenames:
        for filename in filenames:
        formatter_class = custom_namespace[formattername]
        if alias in aliases:
        if alias in cls.aliases:
        if formattername not in custom_namespace:
        if info:
        if info[1] not in _formatter_cache:
        info = FORMATTERS.get(name)
        pattern = _pattern_cache[glob] = re.compile(fnmatch.translate(glob))
        raise
        raise AttributeError(name)
        raise ClassNotFound(f"cannot read {filename}: {err}")
        raise ClassNotFound(f"error when loading custom formatter: {err}")
        raise ClassNotFound(f"no formatter found for name {_alias!r}")
        return formatter_class(**options)
        return pattern.match(fn)
        with open(filename, "rb") as f:
        yield _formatter_cache[info[1]]
        yield formatter
    """
    """Automatically import formatters."""
    """Load a formatter (and all others in the module too)."""
    """Lookup a formatter by alias.
    """Return a generator for all formatter classes."""
    """Return whether the supplied file name fn matches pattern filename."""
    "get_all_formatters",
    "get_formatter_by_name",
    "get_formatter_for_filename",
    "load_formatter_from_file",
    # NB: this returns formatter classes, not info like get_all_lexers().
    (by default, CustomFormatter). Users should be very careful with the input, because
    .. versionadded:: 2.2
    :exc:`pygments.util.ClassNotFound` is raised if there are any errors loading
    alias is found.
    aliases list. The formatter is given the `options` at its instantiation.
    cls = find_formatter_class(_alias)
    def __getattr__(self, name):
    def __init__(self, *args, **kwargs): pass
    except ClassNotFound:
    except Exception as err:
    except OSError as err:
    fn = basename(fn)
    for _, cls in find_plugin_formatters():
    for _, formatter in find_plugin_formatters():
    for _name, cls in find_plugin_formatters():
    for formatter_name in mod.__all__:
    for info in FORMATTERS.values():
    for modname, name, _, filenames, _ in FORMATTERS.values():
    for module_name, name, aliases, _, _ in FORMATTERS.values():
    given the `options` at its instantiation.
    if cls is None:
    if glob not in _pattern_cache:
    is found.
    matching `fn`. The formatter is given the `options` at its instantiation.
    mod = __import__(module_name, None, None, ["__all__"])
    raise ClassNotFound(f"no formatter found for file name {fn!r}")
    return _pattern_cache[glob].match(fn)
    Return a :class:`.Formatter` subclass instance that has a filename pattern
    Return a `Formatter` subclass instance loaded from the provided file, relative
    Return an instance of a :class:`.Formatter` subclass that has `alias` in its
    return cls(**options)
    Returns None if not found.
    The file is expected to contain a Formatter class named ``formattername``
    the formatter.
    this method is equivalent to running ``eval()`` on the input file. The formatter is
    to the current directory.
    try:
    Will raise :exc:`pygments.util.ClassNotFound` if no formatter for that filename
    Will raise :exc:`pygments.util.ClassNotFound` if no formatter with that
"""
:copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
] + list(FORMATTERS)
__all__ = [
_formatter_cache = {}  # classes by name
_pattern_cache = {}
~~~~~~~~~~~~~~~~~~~
class _automodule:
def _fn_matches(fn, glob):
def _load_formatters(module_name):
def find_formatter_class(alias):
def get_all_formatters():
def get_formatter_by_name(_alias, **options):
def get_formatter_for_filename(fn, **options):
def load_formatter_from_file(filename, formattername="CustomFormatter", **options):
del newmod.newmod, newmod.oldmod, newmod.sys, newmod.types
from os.path import basename
from pip._vendor.pygments.formatters._mapping import FORMATTERS
from pip._vendor.pygments.plugin import find_plugin_formatters
from pip._vendor.pygments.util import ClassNotFound
import fnmatch
import re
import sys
newmod = _automodule(__name__)
newmod.__dict__.update(oldmod.__dict__)
oldmod = sys.modules[__name__]
Pygments formatters.
pygments.formatters
sys.modules[__name__] = newmod
