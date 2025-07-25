
-----
                    mod.__package__ = fullname
                    mod.__package__ = fullname.rpartition(".")[0]
                    mod.__path__ = []
                # required by PEP 302
                else:
                if self.is_package(fullname):
                logger.debug("Autoconverting %s", fullname)
                mod = imp.new_module(fullname)
                mod = super().load_module(fullname)
                mod.__file__ = self.path
                mod.__loader__ = self
                py2_detect_fixers, {"print_function": True}
                self._exec_transformed_module(mod)
                sys.modules[fullname] = mod
            )
            0, _hook
            allparts.insert(0, parts[0])
            allparts.insert(0, parts[1])
            break
            convert = False
            convert = True
            else:
            if self._convert_needed():
            install_hooks()
            logger.debug("Autoconverting %s", self.name)
            logger.debug("Py2Fixer could not find %s", fullname)
            mod = sys.modules[fullname]
            path = parts[0]
            raise
            remove_hooks()
            return None
            RTs._rt = RefactoringTool(myfixes)
            RTs._rt_py2_detect = RefactoringTool(py2_detect_fixers)
            RTs._rtp = RefactoringTool(myfixes, {"print_function": True})
            RTs._rtp_py2_detect = RefactoringTool(
            self._exec_transformed_module(module)
            source = transform(source, pathname)
            super().exec_module(module)
        """
        # The above fixers made changes, so we conclude it's Python 2 code
        )  # insert at beginning. This could be made a parameter
        Call this before using the refactoring tools to create them on demand
        chunks.append(dir1)
        code = compile(source, pathname, "exec")
        elif any(fullname.startswith(path) for path in self.include_paths):
        elif parts[1] == path:  # sentinel for relative paths
        else:
        exclude_paths = (exclude_paths,)
        exec(code, module.__dict__)
        fullname = self.name
        if any(fullname.startswith(path) for path in self.exclude_paths):
        if detect_python2(source, pathname):
        if dir1 != dir2:
        if e.msg != "bad input" or e.value != "=":
        if fullname in sys.modules:
        if needed.
        if None in [RTs._rt, RTs._rtp]:
        if None in [RTs._rt_py2_detect, RTs._rtp_py2_detect]:
        if not loader:
        if not self.hooks_were_installed:
        if not spec:
        if parts[0] == path:  # sentinel for absolute paths
        if present at the leftmost side of the full package name, would
        if self._convert_needed():
        if self.hooks_were_installed:
        include_paths = (include_paths,)
        install_hooks()
        loader = PathFinder.find_module(fullname, path)
        loader.__class__ = PastSourceFileLoader
        loader.exclude_paths = self.exclude_paths
        loader.include_paths = self.include_paths
        logger.debug("Detected Python 2 code: {}".format(pathname))
        logger.debug("Detected Python 3 code: {}".format(pathname))
        logger.debug("Running exec_module for %s", module)
        logger.debug("Running find_module: (%s, %s)", fullname, path)
        logger.debug("Running find_spec: (%s, %s, %s)", fullname, path, target)
        logger.debug("Running load_module for %s", fullname)
        parts = os.path.split(path)
        Pass in a sequence of module names such as 'plotrique.plotting' that,
        Pass in a sequence of strings such as 'mymodule' that, if
        PathFinder,
        pathname = self.path
        present at the leftmost side of the full package name, would cause
        remove_hooks()
        return convert
        return False
        return loader
        return mod
        return self
        return spec
        return True
        self.base_exclude_paths = ["future", "past"]
        self.exclude_paths += paths
        self.exclude_paths = copy.copy(self.base_exclude_paths)
        self.found = None
        self.hooks_were_installed = detect_hooks()
        self.include_paths += paths
        self.include_paths = []
        source = self.get_source(self.name)
        SourceFileLoader,
        spec = PathFinder.find_spec(fullname, path, target)
        spec.loader.__class__ = PastSourceFileLoader
        spec.loader.exclude_paths = self.exclude_paths
        spec.loader.include_paths = self.include_paths
        specify the module to be transformed from Py2 to Py3.
        sys.meta_path.insert(
        sys.meta_path.remove(_hook)
        the module not to undergo any source transformation.
        tree = RTs._rt.refactor_string(source, pathname)
        tree = RTs._rt_py2_detect.refactor_string(source, pathname)
        tree = RTs._rtp.refactor_string(source, pathname)
    """
    "lib2to3.fixes.fix_apply",
    "lib2to3.fixes.fix_basestring",
    "lib2to3.fixes.fix_except",
    "lib2to3.fixes.fix_exec",
    "lib2to3.fixes.fix_execfile",
    "lib2to3.fixes.fix_exitfunc",
    "lib2to3.fixes.fix_filter",
    "lib2to3.fixes.fix_funcattrs",
    "lib2to3.fixes.fix_getcwdu",
    "lib2to3.fixes.fix_has_key",
    "lib2to3.fixes.fix_idioms",
    "lib2to3.fixes.fix_import",
    "lib2to3.fixes.fix_intern",
    "lib2to3.fixes.fix_isinstance",
    "lib2to3.fixes.fix_long",
    "lib2to3.fixes.fix_methodattrs",
    "lib2to3.fixes.fix_ne",
    "lib2to3.fixes.fix_next",
    "lib2to3.fixes.fix_nonzero",  # TODO: add a decorator for mapping __bool__ to __nonzero__
    "lib2to3.fixes.fix_numliterals",  # turns 1L into 1, 0755 into 0o755
    "lib2to3.fixes.fix_paren",
    "lib2to3.fixes.fix_print",
    "lib2to3.fixes.fix_raise",  # uses incompatible with_traceback() method on exceptions
    "lib2to3.fixes.fix_raw_input",
    "lib2to3.fixes.fix_reduce",
    "lib2to3.fixes.fix_renames",
    "lib2to3.fixes.fix_repr",
    "lib2to3.fixes.fix_standarderror",
    "lib2to3.fixes.fix_sys_exc",
    "lib2to3.fixes.fix_throw",
    "lib2to3.fixes.fix_tuple_params",
    "lib2to3.fixes.fix_types",
    "lib2to3.fixes.fix_ws_comma",
    "lib2to3.fixes.fix_xrange",
    "lib2to3.fixes.fix_xreadlines",
    # _hook.debug = debug
    # could optimise a bit for only doing str(tree) if
    # For Python >=3.4
    # For Python 3.3
    # From stage 1:
    # From stage 2:
    # getattr(tree, 'was_changed', False) returns True
    # if that's better for you
    # lib2to3 likes a newline at the end
    # 'lib2to3.fixes.fix_buffer',    # perhaps not safe. Test this.
    # 'lib2to3.fixes.fix_callable',  # not needed in Py3.2+
    # 'lib2to3.fixes.fix_dict',        # TODO: add support for utils.viewitems() etc.
    # 'lib2to3.fixes.fix_dict',        # TODO: add support for utils.viewitems() etc. and move to stage2
    # 'lib2to3.fixes.fix_future',    # we don't want to remove __future__ imports
    # 'lib2to3.fixes.fix_imports',   # called by libfuturize.fixes.fix_future_standard_library
    # 'lib2to3.fixes.fix_imports2',  # we don't handle this yet (dbm)
    # 'lib2to3.fixes.fix_input',
    # 'lib2to3.fixes.fix_itertools',
    # 'lib2to3.fixes.fix_itertools_imports',
    # 'lib2to3.fixes.fix_map',
    # 'lib2to3.fixes.fix_metaclass', # causes SyntaxError in Py2! Use the one from ``six`` instead
    # 'lib2to3.fixes.fix_operator',    # we will need support for this by e.g. extending the Py2 operator module to provide those functions in Py3
    # 'lib2to3.fixes.fix_set_literal',  # this is unnecessary and breaks Py2.6 support
    # 'lib2to3.fixes.fix_unicode',   # strips off the u'' prefix, which removes a potentially helpful source of information for disambiguating unicode/byte strings
    # 'lib2to3.fixes.fix_urllib',
    # 'lib2to3.fixes.fix_zip',
    # makes any implicit relative imports explicit. (Use with ``from __future__ import absolute_import)
    # present = any([hasattr(hook, 'PY2FIXER') for hook in sys.meta_path])
    # return _hook
    # return present
    # See the comments on :class:future.standard_library.RenameImport.
    # This implementation uses lib2to3,
    # unambiguously detect whether the import hook is installed:
    # We add this attribute here so remove_hooks() and install_hooks() can
    # We could return the hook when there are ways of configuring it
    # you can override and use something else
    )
    ...     import mypy2module
    @staticmethod
    _hook.exclude(exclude_paths)
    _hook.include(include_paths)
    _rt = None
    _rt_py2_detect = None
    _rtp = None
    _rtp_py2_detect = None
    + list(fixes.lib2to3_fix_names_stage1)
    + list(fixes.lib2to3_fix_names_stage2)
    + list(fixes.libfuturize_fix_names_stage2)
    >>>     import requests     # or others that support Py2/3
    >>> # ...
    >>> # etc.
    >>> autotranslate(['mypackage1', 'mypackage2'])
    >>> autotranslate('mypackagename')
    >>> from past import translation
    >>> from past.translation import autotranslate
    >>> from past.translation import remove_hooks
    >>> import http.client
    >>> import requests        # py2/3 compatible anyway
    >>> remove_hooks()
    >>> translation.install_hooks()
    >>> with translation.hooks():
    >>> with translation.suspend_hooks():
    A namespace for the refactoring tools. This avoids creating these at
    Acts as a context manager. Use like this:
    allparts = []
    An import hook class that uses lib2to3 for source-to-source translation of
    assert len(include_paths) + len(exclude_paths) > 0, "Pass at least one argument"
    chunks = []
    def __enter__(self):
    def __exit__(self, *args):
    def __init__(self):
    def __init__(self, *args, **kwargs): pass
    def _convert_needed(self):
    def _exec_transformed_module(self, module):
    def exclude(self, paths):
    def exec_module(self, module):
    def find_module(self, fullname, path=None):
    def find_spec(self, fullname, path=None, target=None):
    def include(self, paths):
    def load_module(self, fullname):
    def setup():
    def setup_detect_python2():
    else:
    enable = sys.version_info[0] >= 3  # enabled for all 3.x+
    except ParseError as e:
    exclude_paths = []
    for dir1, dir2 in zip(path1, path2):
    from importlib.machinery import (
    Hence we have two possible refactoring tool implementations.
    if _hook in sys.meta_path:
    if enable and _hook not in sys.meta_path:
    if isinstance(exclude_paths, str):
    if isinstance(include_paths, str):
    if source != str(tree)[:-1]:  # remove added newline
    If the hooks were disabled before the context, they are not installed when
    import imp
    import importlib as imp
    include_paths = []
    left.
    list(fixes.libfuturize_fix_names_stage1)
    path1 = splitall(s1)
    path2 = splitall(s2)
    PathFinder = None
    Py2 code to Py3.
    PY2FIXER = True
    return _hook in sys.meta_path
    return allparts
    return os.path.join(*chunks)
    return str(tree)[:-1]  # remove added newline
    Returns a bool indicating whether we think the code is Py2
    Returns the longest common substring to the two strings, starting from the
    Returns True if the import hooks are installed, False if not.
    RTs.setup()
    RTs.setup_detect_python2()
    source += "\n"
    SourceFileLoader = object
    Split a path into all components. From Python Cookbook.
    the context is left.
    the module level, which slows down the module import. (See issue #117).
    There are two possible grammars: with or without the print statement.
    try:
    while True:
"""
#
#         _syslibprefix = getattr(sys, 'base_prefix', sys.prefix)
#         _syslibprefix = sys.real_prefix
#     # In a non-pythonv virtualenv, sys.real_prefix points to the installed Python.
#     # In a pythonv venv, sys.base_prefix points to the installed Python.
#     # Outside a virtual environment, sys.prefix points to the installed Python.
#     else:
#     if hasattr(sys, 'real_prefix'):
# _stdlibprefix = common_substring(math.__file__, urllib.__file__)
# ``conda`` environments:
# ``math`` and ``urllib``.
# alias
# imp was deprecated in python 3.6
# Instead, we use the portion of the path common to both the stdlib modules
# process any files there (they will already be Python 3).
# The following method is used by Sanjay Vinip in uprefix. This fails for
# to it. If the diff is empty, it's Python 3 code.
# We detect whether the code is Py2 or Py3 by applying certain lib2to3 fixers
# We need to find a prefix for the standard library, as we don't want to
)
]
_hook = Py2Fixer()
==================
Author: Ed Schofield.
autotranslate = install_hooks
class hooks:
class PastSourceFileLoader:
class Py2Fixer:
class RTs:
class suspend_hooks:
def common_substring(s1, s2):
def detect_hooks():
def detect_python2(source, pathname):
def install_hooks(include_paths=(), exclude_paths=()):
def remove_hooks():
def splitall(path):
def transform(source, pathname):
dependencies still only support Python 2.x.
else:
except ImportError:
from lib2to3.pgen2.parse import ParseError
from lib2to3.refactor import RefactoringTool
from libfuturize import fixes
hook is invoked as follows:
if sys.version_info >= (3, 6):
if sys.version_info[:2] < (3, 4):
import copy
import logging
import os
import sys
Inspired by and based on ``uprefix`` by Vinay M. Sajip.
It is intended to assist users in migrating to Python 3.x even if some
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
myfixes = (
Once your Py2 package is installed in the usual module search path, the import
Or:
past.translation
print statements into functions, etc.
py2_detect_fixers = [
The ``past.translation`` package provides an import hook for Python 3 which
transparently runs ``futurize`` fixers over Python 2 code on import to convert
try:
Usage
You can unregister the hook using::
