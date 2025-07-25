
                    "'{}' must be a list of strings (got {!r})".format(option, val)
                    continue
                    yield package
                "'{}' must be a {} (got `{}`)".format(option, what, val)
                # down there, even if the parent was excluded.
                # Keep searching subdirectories, as there may be more packages
                # Should this package be included?
                # Skip directory trees that are not valid packages
                )
                cls._build_filter("ez_setup", "*__pycache__", *exclude),
                cls._build_filter(*include),
                convert_path(where),
                dirs.append(dir)
                full_path = os.path.join(root, dir)
                if "." in dir or not cls._looks_like_package(full_path):
                if include(package) and not exclude(package):
                ok = all(isinstance(v, str) for v in val)
                ok = False
                package = rel_path.replace(os.path.sep, ".")
                raise DistutilsOptionError(
                rel_path = os.path.relpath(full_path, where)
            """
            # Copy dirs to iterate over it, then empty dirs.
            )
            _incl = "dependency_links", "setup_requires"
            all_dirs = dirs[:]
            cls._find_packages_iter(
            dirs[:] = []
            Disable finalize_options to avoid building the working set.
            distutils.core.Distribution.__init__(self, filtered)
            else:
            filtered = {k: attrs[k] for k in set(_incl) & set(attrs)}
            for dir in all_dirs:
            if isinstance(val, list):
            if not ok:
            raise DistutilsOptionError(
            Ref #2158.
            return
            return default
            setattr(self, option, default)
            setattr(self, option, re.split(r",\s*|\s+", val))
        """
        """Does a directory look like a package?"""
        """Return a list all Python packages found within directory 'where'
        "foo bar baz", "foo,bar,baz", and "foo,   bar baz" all become
        )
        ["foo", "bar", "baz"].
        _Command.__init__(self, dist)
        A minimal version of a distribution for supporting the
        All the packages found in 'where' that pass the 'include' filter, but
        as a wildcard in the names, such that 'foo.*' will exclude all
        be converted to the appropriate local path syntax.
        cmd = _Command.reinitialize_command(self, command, reinit_subcommands)
        Construct the command for dist, updating
        currently a string, we split it either on /,\s*/ or /\s+/, so
        def finalize_options(self):
        dist.fetch_build_eggs(dist.setup_requires)
        elif isinstance(val, str):
        elif not isinstance(val, str):
        else:
        'exclude' is a sequence of package names to exclude; '*' can be used
        fetch_build_eggs interface.
        files = map(make_rel, files)
        for base, dirs, files in os.walk(path, followlinks=True)
        for file in files
        for root, dirs, files in os.walk(where, followlinks=True):
        Given a list of patterns, return a callable that will be true only if
        if val is None:
        'include' is a sequence of package names to include.  If it's
        make_rel = functools.partial(os.path.relpath, start=dir)
        not the 'exclude' filter.
        os.path.join(base, file)
        r"""Ensure that 'option' is a list of strings.  If 'option' is
        return cmd
        return lambda name: any(fnmatchcase(name, pat=pat) for pat in patterns)
        return list(
        return os.path.isfile(os.path.join(path, "__init__.py"))
        return True
        return val
        shell style wildcard patterns just like 'exclude'.
        should be supplied as a "cross-platform" (i.e. URL-style) path; it will
        specified, all found packages will be included.  'include' can contain
        specified, only the named packages will be included.  If it's not
        subpackages of 'foo' (but not 'foo' itself).
        the input matches at least one of the patterns.
        val = getattr(self, option)
        vars(cmd).update(kw)
        vars(self) with any keyword parameters.
        vars(self).update(kw)
        'where' is the root directory which will be searched for packages.  It
       def __init__(self, attrs):
      """
    """
    """Treat this string as-is (https://en.wikipedia.org/wiki/Sic)"""
    "Command",
    "Distribution",
    "Extension",
    "find_namespace_packages",
    "find_packages",
    "Require",
    "setup",
    "SetuptoolsDeprecationWarning",
    # Honor setup.cfg's options.
    # Make sure we have any requirements needed to interpret 'attrs'.
    # Note: do not use `setuptools.Distribution` directly, as
    # our PEP 517 backend patch `distutils.core.Distribution`.
    )
    @classmethod
    @staticmethod
    __doc__ = _Command.__doc__
    _install_setup_requires(attrs)
    class MinimalDistribution:
    command_consumes_arguments = False
    def __init__(self, *args, **kwargs): pass
    def __init__(self, dist, **kw):
    def _build_filter(*patterns):
    def _ensure_stringlike(self, option, what, default=None):
    def _find_packages_iter(cls, where, exclude, include):
    def _looks_like_package(path):
    def ensure_string_list(self, option):
    def find(cls, where=".", exclude=(), include=("*",)):
    def reinitialize_command(self, command, reinit_subcommands=0, **kw):
    dist = MinimalDistribution(attrs)
    dist.parse_config_files(ignore_option_errors=True)
    files = _find_all_simple(dir)
    Find all files under 'dir' and return the list of full filenames.
    Find all files under 'path'
    Generate a list of all Python packages found within a directory
    if dir == os.curdir:
    if dist.setup_requires:
    results = (
    return distutils.core.setup(**attrs)
    return filter(os.path.isfile, results)
    return list(files)
    Unless dir is '.', return full filenames with dir prepended.
"""Extensions to the 'distutils' for large or complex distributions"""
# Apply monkey patches
]
__all__ = [
__version__ = setuptools.version.__version__
_Command = monkey.get_unpatched(distutils.core.Command)
bootstrap_install_from = None
class Command:
class PackageFinder:
class PEP420PackageFinder:
class sic:
def _find_all_simple(path):
def _install_setup_requires(attrs):
def findall(dir=os.curdir):
def setup(**attrs):
find_namespace_packages = PEP420PackageFinder.find
find_packages = PackageFinder.find
from . import monkey
from ._deprecation_warning import SetuptoolsDeprecationWarning
from distutils.errors import DistutilsOptionError
from distutils.util import convert_path
from fnmatch import fnmatchcase
from setuptools.depends import Require
from setuptools.dist import Distribution
from setuptools.extension import Extension
import _distutils_hack.override  # noqa: F401
import distutils.core
import functools
import os
import re
import setuptools.version
monkey.patch_all()
setup.__doc__ = distutils.core.setup.__doc__
