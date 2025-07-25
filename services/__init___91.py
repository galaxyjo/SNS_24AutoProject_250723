
-----------
                    for subfolder in FUTURE_SOURCE_SUBFOLDERS
                    os.path.exists(os.path.join(folder, subfolder))
                    return sys.modules[name]
                "library: %s" % stdlib_paths
                "Multiple locations found for the Python standard "
                # Found it. Remove it.
                # There's a problem importing the system module. E.g. the
                # This could be e.g. moves.
                # winreg module is not available except on Windows.
                [
                ]
                __import__(m)
                break
                flog.debug("Package {} has no __path__.".format(package))
                flog.debug("What to do here?")
                if name in sys.modules:
                module = __import__(m, level=0)
                pass
                path = package.__path__
                sys.path.remove(folder)
            "builtins",
            "future",
            "libfuturize",
            "libpasteurize",
            "past",
            #             del sys.modules[key]
            #             pass
            #         except KeyError:
            #         try:
            #     if key == m or key.startswith(m + '.'):
            # Delete the module and any submodules from sys.modules:
            # for key in list(sys.modules):
            # ignore it.
            # module.__future_module__ = True
            # New name. Look up the corresponding old (Py2) name:
            # This seems to happen on travis-ci.org. Very strange. We'll try to
            # Treat the first bit as a package
            )
            ):
            and "site-packages" not in modpath[0]
            continue
            dbm.gnu = gnu
            dbm.ndbm = ndbm
            del sys.meta_path[i]
            del sys.modules[modulename]
            except AttributeError:
            except ImportError:
            except ImportError:  # e.g. winreg
            flog.debug("Deleting (Py2) {} from sys.modules".format(modulename))
            flog.warn(
            from future.moves.dbm import gnu
            from future.moves.dbm import ndbm
            if all(
            if i == 0:
            install_hooks()
            modpath[0].startswith(is_py2_stdlib_module.stdlib_path)
            module = self._find_and_load_module(name)
            module = self._find_and_load_module(oldname)
            modules.append(importlib.import_module(sofar))
            old_to_new.values()
            oldname = self.new_to_old[name]
            package = self._find_and_load_module(packagename, path)
            packagename = bits.pop(0)
            pass
            prefix = "future.backports"
            prefix = "future.moves"
            raise NotImplementedError("Dotted module names are not supported")
            remove_hooks()
            return
            return output
            return output[0]
            return self
            return sys.modules[name]
            return True
            scrubbed[modulename] = sys.modules[modulename]
            setattr(modules[i - 1], part, modules[i])
            sofar = ".".join(parts[: i + 1])
            sys.modules["dbm.gnu"] = gnu
            sys.modules["dbm.ndbm"] = ndbm
            sys.modules[m] = self.old_sys_modules[m]
            try:
        """
        # because `builtins` won't have been installed in site-packages by setup.py:
        # Before v0.12: Was: if fullname in set(self.old_to_new) | new_base_names:
        # Choose the first one arbitrarily
        # client.blah = blah
        # Disallow dotted module names like http.client:
        # Ensure we import the system module:
        # etc.
        # flog.debug('Entering hooks context manager')
        # flog.debug('Exiting hooks context manager')
        # Handles hierarchical importing: package.module.module2
        # If several, choose one arbitrarily to raise an exception about
        # In any case, make it available under the requested (Py3) name
        # Look for the future source folder:
        # newmod.__future_module__ = True
        # Restore sys.path and sys.modules:
        # restore_sys_modules(self.scrubbed)
        # Return the next-most top-level module after future.backports / future.moves:
        # scrub_future_sys_modules()
        # self.scrubbed = scrub_future_sys_modules()
        # self.scrubbed = scrub_py2_sys_modules()
        # The presence of all these indicates we've found our source folder,
        # Then http.client = client
        # top-level package:
        # We look up the module in sys.modules because __import__ just returns the
        ), "Ambiguity in renaming (handler not implemented)"
        ):
        ]
        __import__(newmodname)
        __import__(oldmodname)
        >>> # etc.
        >>> conn = http.client.HTTPConnection(...)
        >>> from future.backports import http.client
        >>> from future.backports import module
        >>> from future.backports import module_name
        >>> from future.backports.module import submodule
        >>> from future.backports.module_name import symbol_names[0], ...
        >>> from future.moves import module_name
        >>> from future.moves.module_name import symbol_names[0], ...
        >>> from module_name import symbol_names[0], symbol_names[1], ...
        >>> http = import_('http.client')
        >>> http = import_('http.server')
        >>> HTTPConnection = from_import('http.client', 'HTTPConnection')
        >>> HTTPServer = from_import('http.server', 'HTTPServer')
        >>> import module_name
        >>> module.submodule = submodule
        >>> package_name = import_(module_name)
        >>> response = urllib.request.urlopen('http://mywebsite.com')
        >>> urllib = import_('urllib.request')
        >>> urlopen, urlparse = from_import('urllib.request', 'urlopen', 'urlparse')
        assert len(args) > 0
        assert len(both) == 0 and len(set(old_to_new.values())) == len(
        bits = name.split(".")
        both = set(old_to_new.keys()) & set(old_to_new.values())
        dbm.dumb = dumb
        elif name in self.new_to_old:
        else:
        except ImportError:
        Finds and loads it. But if there's a . in the name, handles it
        first = list(clash)[0]
        flog.debug("Detected.")
        flog.debug("Not detected.")
        for folder in self.old_sys_path:
        for i, part in enumerate(parts):
        for i, part in reversed(list(enumerate(parts))):
        for m in self.module_names:
        for m in set(self.old_sys_modules.keys()) - set(sys.modules.keys()):
        for m in TOP_LEVEL_MODULES:
        from future.moves.dbm import dumb
        from future.moves.test import support
        FUTURE_SOURCE_SUBFOLDERS = [
        if "backport" in kwargs and bool(kwargs["backport"]):
        if (
        if any(["." in m for m in self.module_names]):
        if backport:
        if fullname in new_base_names:
        if hasattr(hook, "RENAMER"):
        if is_py2_stdlib_module(module):
        if len(output) == 1:
        if name in sys.modules:
        if not len(set(stdlib_paths)) == 1:
        if not modulename in sys.modules:
        if not self.hooks_were_installed:
        if self.hooks_were_installed:
        if sys.version_info[0] < 3:
        import dbm
        import queue
        import Queue as queue
        import test
        install_hooks()
        is_py2_stdlib_module.stdlib_path = stdlib_paths[0]
        modpath = os.path.split(m.__file__)
        module = importlib.import_module(prefix + "." + module_name)
        module = sys.modules[modulename]
        module_info = imp.find_module(name, path)
        modules = []
        name = bits[0]
        names. E.g. {'ConfigParser': 'configparser', 'cPickle': 'pickle'}
        new_base_names = {s.split(".")[0] for s in self.new_to_old}
        newmod = sys.modules[newmodname]
        obj = getattr(oldmod, oldobjname)
        oldmod = sys.modules[oldmodname]
        output = [getattr(module, name) for name in symbol_names]
        parts = prefix.split(".") + module_name.split(".")
        pass
        Pass in a dictionary-like object mapping from old names to new
        path = None
        properly.
        raise ImportError("future module {} clashes with Py2 module".format(first))
        remove_hooks()
        return
        return __import__(module_name)
        return {}
        return False
        return imp.load_module(name, *module_info)
        return module
        return modules[2]
        return None
        return self
        return True
        scrub_future_sys_modules()
        self.hooks_were_installed = detect_hooks()
        self.module_names = args
        self.new_to_old = {new: old for (old, new) in old_to_new.items()}
        self.old_sys_modules = copy.copy(sys.modules)
        self.old_sys_path = copy.copy(sys.path)
        self.old_to_new = old_to_new
        setattr(newmod, newobjname, obj)
        stdlib_files = [contextlib.__file__, os.__file__, copy.__file__]
        stdlib_paths = [os.path.split(f)[0] for f in stdlib_files]
        sys.meta_path.append(newhook)
        sys.modules["dbm.dumb"] = dumb
        sys.modules["test.support"] = support
        sys.modules[name] = module
        sys.path = self.old_sys_path
        test.support = support
        try:
        while len(bits) > 1:
    """
    "__builtin__": "builtins",
    "_dummy_thread",
    "_markupbase",
    "_thread",
    "_winreg": "winreg",
    "builtins",
    "ConfigParser": "configparser",
    "copy_reg": "copyreg",
    "copyreg",
    "dbm",
    "dummy_thread": "_dummy_thread" if sys.version_info < (3, 9) else "_thread",
    "future.moves._markupbase": "_markupbase",
    "future.moves.html": "html",
    "future.moves.http": "http",
    "future.moves.socketserver": "socketserver",
    "future.moves.xmlrpc": "xmlrpc",
    "html",
    "http",
    "multiprocessing.queues": "multiprocessing",
    "pickle",
    "queue",
    "Queue": "queue",
    "repr": "reprlib",
    "reprlib",
    "socketserver",
    "test",
    "thread": "_thread",
    "tkinter",
    "urllib",
    "winreg",
    "xmlrpc",
    #          ('urllib', 'error', 'future.moves.urllib', 'error'),
    #          ('urllib', 'parse', 'future.moves.urllib', 'parse'),
    #          ('urllib', 'request', 'future.moves.urllib', 'request'),
    #          ('urllib', 'response', 'future.moves.urllib', 'response'),
    #          ('urllib', 'robotparser', 'future.moves.urllib', 'robotparser'),
    #     import test
    #     return
    #     sys.py2_modules['test'] = None
    # (and it exists on Py2.6+).
    # 'abc': 'collections.abc',   # for Py33
    # Add it unless it's there already
    # anydbm and whichdb are handled by fix_imports2
    # 'anydbm': 'dbm',   # causes infinite import loop
    # 'BaseHTTPServer': 'http.server',
    # 'CGIHTTPServer': 'http.server',
    # 'commands': 'subprocess',
    # 'Cookie': 'http.cookies',
    # 'cookielib': 'http.cookiejar',
    # 'cPickle': 'pickle',
    # 'cStringIO': 'io',  # there's a new io module in Python 2.6
    # 'dbhash': 'dbm.bsd',
    # 'dbm': 'dbm.ndbm',
    # 'Dialog': 'tkinter.dialog',
    # Different RenameImport classes are created when importing this module from
    # different source files. This causes isinstance(hook, RenameImport) checks
    # 'DocXMLRPCServer': 'xmlrpc.server',
    # 'dumbdbm': 'dbm.dumb',
    # easily:
    # except ImportError:
    # Explicit is better than implicit. In the future the interface should
    # 'FileDialog': 'tkinter.filedialog',
    # function call. Left as is for now for backward compatibility with
    # 'future.backports.email': 'email',    # for use by urllib
    # 'future.backports.test': 'test',  # primarily for renaming test_support to support
    # 'future.backports.urllib': 'urllib',
    # 'future.utils.six.moves.html': 'html',
    # 'future.utils.six.moves.http': 'http',
    # 'future.utils.six.moves.urllib': 'urllib',
    # 'gdbm': 'dbm.gnu',
    # Hack for urllib so it appears to have the same structure on Py2 as on Py3
    # 'htmlentitydefs' : 'html.entities',
    # 'HTMLParser' : 'html.parser',
    # 'httplib': 'http.client',
    # if hasattr(install_aliases, 'run_already'):
    # import dbm
    # install_aliases.run_already = True
    # Loop backwards, so deleting items keeps the ordering:
    # Not all Python installations have test module. (Anaconda doesn't, for example.)
    # Patch the dbm module so it appears to have the same structure on Py2 as on Py3
    # Patch the test module so it appears to have the same structure on Py2 as on Py3
    # probably change so that scrubbing the import hooks requires a separate
    # Python 2.6 doesn't have importlib in the stdlib, so it requires
    # remove_hooks() and install_hooks() can find instances of these classes
    # 'robotparser' : 'urllib.robotparser',
    # 'ScrolledText': 'tkinter.scrolledtext',
    # Set re.ASCII to a zero constant. stat.ST_MODE just happens to be one
    # 'SimpleDialog': 'tkinter.simpledialog',
    # 'SimpleHTTPServer': 'http.server',
    # 'SimpleXMLRPCServer': 'xmlrpc.server',
    # 'StringIO': 'io',   # ditto
    # sys.py2_modules['dbm'] = dbm
    # sys.py2_modules['test'] = test
    # that provides StringIO and BytesIO
    # the backported ``importlib`` package from PyPI as a dependency to use
    # The re module has no ASCII flag in Py2, but this is the default.
    # this function:
    # This is no use, since "import urllib.request" etc. still fails:
    # 'Tix': 'tkinter.tix',
    # 'tkColorChooser': 'tkinter.colorchooser',
    # 'tkCommonDialog': 'tkinter.commondialog',
    # 'Tkconstants': 'tkinter.constants',
    # 'Tkdnd': 'tkinter.dnd',
    # 'tkFileDialog': 'tkinter.filedialog',
    # 'tkFont': 'tkinter.font',
    # 'Tkinter': 'tkinter',
    # 'tkMessageBox': 'tkinter.messagebox',
    # 'tkSimpleDialog': 'tkinter.simpledialog',
    # to produce inconsistent results. We add this RENAMER attribute here so
    # try:
    # 'ttk': 'tkinter.ttk',
    # 'urlparse' : 'urllib.parse',
    # v0.11.x.
    # 'whichdb': 'dbm',  # causes infinite import loop
    ("base64", "decodebytes", "base64", "decodestring"),
    ("base64", "encodebytes", "base64", "encodestring"),
    ("collections", "ChainMap", "future.backports.misc", "ChainMap"),
    ("collections", "Counter", "future.backports.misc", "Counter"),
    ("collections", "OrderedDict", "future.backports.misc", "OrderedDict"),
    ("collections", "UserDict", "UserDict", "UserDict"),
    ("collections", "UserList", "UserList", "UserList"),
    ("collections", "UserString", "UserString", "UserString"),
    ("functools", "cmp_to_key", "future.backports.misc", "cmp_to_key"),
    ("itertools", "count", "future.backports.misc", "count"),
    ("itertools", "filterfalse", "itertools", "ifilterfalse"),
    ("itertools", "zip_longest", "itertools", "izip_longest"),
    ("math", "ceil", "future.backports.misc", "ceil"),
    ("multiprocessing", "SimpleQueue", "multiprocessing.queues", "SimpleQueue"),
    ("re", "ASCII", "stat", "ST_MODE"),
    ("reprlib", "recursive_repr", "future.backports.misc", "recursive_repr"),
    ("subprocess", "check_output", "future.backports.misc", "check_output"),
    ("subprocess", "getoutput", "commands", "getoutput"),
    ("subprocess", "getstatusoutput", "commands", "getstatusoutput"),
    ("sys", "intern", "__builtin__", "intern"),
    (Note that currently import hooks are disabled for modules like these
    (This was need prior to v0.16.0 because the presence of a configparser
    ...     import http.client
    ``future`` v1.0.
    >>>     import requests     # incompatible with ``future``'s standard library hooks
    >>> # ...
    >>> from future import standard_library
    >>> import http.client
    >>> import requests
    >>> standard_library.install_hooks()
    >>> with standard_library.hooks():
    >>> with standard_library.suspend_hooks():
    A class for import hooks mapping Py3 module names etc. to the Py2 equivalents.
    A context-manager that prevents standard library modules like configparser
    Acts as a context manager. Saves the state of sys.modules and restores it
    Acts as a context manager. Use like this:
    Add any previously scrubbed modules back to the sys.modules cache,
    after the 'with' block.
    aliases for better Py3 compatibility.
    and this on Py2:
    assert len(set(RENAMES.values()) & set(sys.builtin_module_names)) == 0
    assert not detect_hooks()
    but only if it's safe to do so.
    clash = set(sys.modules) & set(scrubbed)
    continue to be accessible in the current namespace but not from any
    Currently this function is unneeded, as we are not attempting to provide import hooks
    def __enter__(self):
    def __exit__(self, *args):
    def __init__(self, *args):
    def __init__(self, old_to_new):
    def _find_and_load_module(self, name, path=None):
    def find_module(self, fullname, path=None):
    def load_module(self, name):
    Deprecated.
    Deprecated. Use install_hooks() instead. This will be removed by
    Deprecated. Use remove_hooks() instead. This will be removed by
    else:
    Equivalent to this on Py3:
    Example use:
    except ImportError:
    except that it also handles dotted module names such as ``http.client``
    except that it also handles dotted module names such as ``http.client``.
    flog.debug("Detecting hooks ...")
    flog.debug("Installing hooks ...")
    flog.debug("sys.meta_path is now: {}".format(sys.meta_path))
    flog.debug("sys.meta_path was: {}".format(sys.meta_path))
    flog.debug("Uninstalling hooks ...")
    folder would otherwise have prevented setuptools from running on Py3. Maybe
    for i, hook in list(enumerate(sys.meta_path))[::-1]:
    for modulename in REPLACED_MODULES & set(RENAMES.keys()):
    for modules with ambiguous names: email, urllib, pickle.
    for newmodname, newobjname, oldmodname, oldobjname in MOVES:
    For this to work, http.client will be scrubbed from sys.modules after the
    from being imported from the local python-future source folder on Py3.
    from collections import OrderedDict, Counter, ChainMap     # even on Py2.6
    from collections import UserDict, UserList, UserString
    from future import standard_library
    from future.backports.urllib import error
    from future.backports.urllib import parse
    from future.backports.urllib import request
    from future.backports.urllib import response
    from future.backports.urllib import robotparser
    from itertools import filterfalse, zip_longest
    from multiprocessing import SimpleQueue
    from subprocess import check_output              # even on Py2.6
    from subprocess import getoutput, getstatusoutput
    from sys import intern
    if hasattr(m, "__file__"):
    if len(clash) != 0:
    if len(sys.py2_modules) != 0:
    if m.__name__ in sys.builtin_module_names:
    if not "stdlib_path" in is_py2_stdlib_module.__dict__:
    if not detect_hooks():
    if present:
    if PY3:
    if scrub_sys_modules:
    If the hooks were disabled before the context, they are not installed when
    import _dummy_thread
    import _markupbase
    import _thread
    import builtins
    import collections.abc  # on Py33
    import copyreg
    import dbm
    import dbm.dumb
    import dbm.gnu
    import email
    import html, html.parser, html.entities
    import http, http.client, http.server
    import http.cookies, http.cookiejar
    import imp
    import importlib
    import importlib as imp
    import pickle
    import pickle     # should (optionally) bring in cPickle on Python 2
    import queue
    import reprlib
    import socketserver
    import test.support
    import urllib
    import urllib.parse, urllib.request, urllib.response, urllib.error, urllib.robotparser
    import winreg    # on Windows only
    import xmlrpc.client, xmlrpc.server
    imported modules (like requests).
    install_aliases()
    install_hooks()
    it's not needed any more?)
    module. This function imports the module compatibly on Py2 and Py3 and
    modules with the same names (like urllib or email).
    Monkey-patches the standard library in Py2.6/7 to provide
    newhook = RenameImport(RENAMES)
    Note that this would be a SyntaxError in Python:
    On Py2, equivalent to this if backport=False:
    On Py3, equivalent to this:
    or to this if backport=True:
    or:
    Pass a (potentially dotted) module name of a Python 3 standard library
    present = any([hasattr(hook, "RENAMER") for hook in sys.meta_path])
    remove_hooks()
    Removes any Python 2 standard library modules from ``sys.modules`` that
    RENAMER = True
    return {}
    return False
    return present
    return scrubbed
    returns the top-level module.
    Returns True if the import hooks are installed, False if not.
    scrubbed = {}
    standard_library.install_aliases()
    sys.meta_path.
    sys.modules.update(scrubbed)
    sys.modules["urllib.error"] = error
    sys.modules["urllib.parse"] = parse
    sys.modules["urllib.request"] = request
    sys.modules["urllib.response"] = response
    sys.modules["urllib.robotparser"] = robotparser
    sys.py2_modules = {}
    sys.py2_modules["email"] = email
    sys.py2_modules["pickle"] = pickle
    sys.py2_modules["urllib"] = urllib
    the context is left.
    The effect then is like this:
    Then:
    This function installs the future.standard_library import hook into
    This function removes the import hook from sys.meta_path.
    This may not be reliable on all systems.
    Tries to infer whether the module m is from the Python 2 standard library.
    try:
    urllib.error = error
    urllib.parse = parse
    urllib.request = request
    urllib.response = response
    urllib.robotparser = robotparser
    Use as follows:
    Use like this:
    with ambiguous names anyway ...)
    'with' block. That way the modules imported in the 'with' block will
    with exclude_local_folder_imports(*TOP_LEVEL_MODULES):
    would interfere with Py3-style imports using import hooks. Examples are
"""
#
#               mkarg
#               module but these fns are missing: getstatus, mk2arg,
#             return self
#             return sys.modules[name]
#             self.path = path
#         flog.warning("Imported deprecated module %s", name)
#         if fullname in self.module_names:
#         if name in sys.modules:
#         module = imp.load_module(name, *module_info)
#         module_info = imp.find_module(name, self.path)
#         return module
#         return None
#         self.module_names = args
#         sys.modules[name] = module
#     def __init__(self, *args):
#     def find_module(self, fullname, path=None):
#     def load_module(self, name):
#     install_hooks()
#   dbm
#   email
#   html
#   http
#   pickle (fast one)
#   re:         needs an ASCII constant that works compatibly with Py3
#   subprocess: should provide getoutput and other fns from commands
#   test
#   tkinter
#   urllib
#   xmlrpc
# (New module name, new object name, old module name, old object name)
# ``sys.modules`` cache in order to support "import urllib" meaning two
# A minimal example of an import hook:
# As of v0.12, this no longer happens implicitly:
# builtin modules names:
# by the application.
# class WarnOnImport:
# contexts. So we require explicit imports for these modules.
# different contents in a significant way (e.g. submodules) are:
# different things (Py2.7 urllib and backported Py3.3-like urllib) in different
# etc: see lib2to3/fixes/fix_imports.py
# Harmless renames that we can insert.
# if not PY3:
# imp was deprecated in python 3.6
# It is complicated and apparently brittle to mess around with the
# Keys: Py2 / real module names
# Make a dedicated logger; leave the root logger to be configured
# potential clashes between the old and new names:
# Sanity check for is_py2_stdlib_module(): We aren't replacing any
# The following module names are not present in Python 2.x, so they cause no
# The modules that are defined under the same names on Py3 but with
# These modules need names from elsewhere being added to them:
# Values: Py3 / simulated module names
(The renamed modules and functions are still available under their old
]
_formatter = logging.Formatter(logging.BASIC_FORMAT)
_handler = logging.StreamHandler()
_handler.setFormatter(_formatter)
}
}  # add email and dbm when we support it
And then these normal Py3 imports work on both Py3 and Py2::
assert len(set(RENAMES.values()) & set(REPLACED_MODULES)) == 0
class exclude_local_folder_imports:
class hooks:
class RenameImport:
class suspend_hooks:
def __init__(self, *args, **kwargs): pass
def cache_py2_modules():
def detect_hooks():
def disable_hooks():
def enable_hooks():
def from_import(module_name, *symbol_names, **kwargs):
def import_(module_name, backport=False):
def import_top_level_modules():
def install_aliases():
def install_hooks():
def is_py2_stdlib_module(m):
def remove_hooks(scrub_sys_modules=False):
def restore_sys_modules(scrubbed):
def scrub_future_sys_modules():
def scrub_py2_sys_modules():
else:
flog = logging.getLogger("future_stdlib")
flog.addHandler(_handler)
flog.setLevel(logging.WARN)
from future.utils import PY2, PY3
http://docs.pythonsprints.com/python3_porting/py-porting.html)::
if not hasattr(sys, "py2_modules"):
if PY2:
if sys.version_info >= (3, 6):
import contextlib
import copy
import logging
import os
import sys
It is designed to be used as follows::
Limitations
MOVES = [
names on Python 2.)
names.
Python 3 reorganized the standard library (PEP 3108). This module exposes
RENAMES = {
REPLACED_MODULES = {
several standard library modules to Python 2 under their new Python 3
This is a cleaner alternative to this idiom (see
TOP_LEVEL_MODULES = [
We don't currently support these modules, but would like to::
