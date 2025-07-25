
---------
---------------------
----------------------------
-----------------------------
-----------------------------------
                            "\nhttps://numpy.org/devdocs/building/index.html"
                            "\nIf you compiled yourself, more information is available at:"
                            "\nOtherwise report this to the vendor "
                            "Polyfit sanity test emitted a warning, most likely due "
                            "that provided NumPy.\n\n{}\n".format(error_message)
                            "to using a buggy Accelerate backend."
                        # Ignore other warnings, they may not be relevant (see gh-25433).
                        )
                        error_message = f"{_wn.category.__name__}: {_wn.message}"
                        msg = (
                        raise RuntimeError(msg)
                    "`numpy.distutils` is not available from " "Python 3.12 onwards",
                    if _wn.category is exceptions.RankWarning:
                    name=None,
                    use_hugepage = 0
                "`np.chararray` is deprecated and will be removed from "
                "`numpy.array_api` is not available from " "numpy 2.0 onwards",
                "by incorrect BLAS library being linked in, or by mixing "
                "corresponding NumPy scalar.",
                "numpy issues for similar problems."
                "or bytes dtype instead.",
                "package managers (pip, conda, apt, ...). Search closed "
                "pass simple sanity checks. This can be caused for example "
                "The current Numpy installation ({!r}) fails to "
                "the main namespace in the future. Use an array with a string "
                )
                del _wn
                DeprecationWarning,
                f"`np.{attr}` was removed in the NumPy 2.0 release. "
                f"{__expired_attributes__[attr]}",
                f"In the future `np.{attr}` will be defined as the "
                for _wn in w:
                FutureWarning,
                if kernel_version < (4, 6):
                import numpy.distutils as distutils
                kernel_version = os.uname().release.split(".")[:2]
                kernel_version = tuple(int(v) for v in kernel_version)
                name=None,
                raise AssertionError
                raise AttributeError(
                return distutils
                stacklevel=2,
                use_hugepage = 0
                use_hugepage = 1
            "array_api",
            "compat",
            "conftest",
            "distutils",
            "matlib",
            "matrixlib",
            "module {!r} has no attribute " "{!r}".format(__name__, attr)
            "NPY_PROMOTION_STATE was a temporary feature for NumPy 2.0 "
            "tests",
            "transition and is ignored after NumPy 2.2.",
            "version",
            # And future warnings for those that will change, but also give
            # If there is an issue with parsing the kernel version,
            # See: #16679 for related discussion.
            # set use_hugepage to 0. Usage of LooseVersion will handle
            # the AttributeError
            # the kernel version parsing better, but avoided since it
            # This is not Linux, so it should not matter, just enable anyway
            # Throw runtime error, if the test failed Check for warning and error_message
            # will increase the import time.
            )
            _ = polyfit(x, y, 2, cov=True)
            _mac_os_check()
            c = array([3.0, 2.0, 1.0])
            del w
            else:
            except ValueError:
            globals()[ta] = getattr(_core, ta)
            if "distutils" in __numpy_submodules__:
            if len(w) > 0:
            if not abs(x.dot(x) - float32(2.0)) < 1e-5:
            import numpy.char as char
            import numpy.core as core
            import numpy.ctypeslib as ctypeslib
            import numpy.dtypes as dtypes
            import numpy.exceptions as exceptions
            import numpy.f2py as f2py
            import numpy.fft as fft
            import numpy.linalg as linalg
            import numpy.ma as ma
            import numpy.matlib as matlib
            import numpy.polynomial as polynomial
            import numpy.random as random
            import numpy.rec as rec
            import numpy.strings as strings
            import numpy.testing as testing
            import numpy.typing as typing
            msg = (
            pass
            raise AttributeError(
            raise AttributeError(__former_attrs__[attr], name=None)
            raise RuntimeError(msg.format(__file__)) from None
            return char
            return char.chararray
            return core
            return ctypeslib
            return dtypes
            return exceptions
            return f2py
            return fft
            return linalg
            return ma
            return matlib
            return polynomial
            return random
            return rec
            return strings
            return testing
            return typing
            stacklevel=2,
            try:
            use_hugepage = 1
            use_hugepage = int(use_hugepage)
            UserWarning,
            warnings.warn(
            x = linspace(0, 2, 5)
            x = ones(2, dtype=float32)
            y = polyval(c, x)
        "    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations"
        """
        "`np.{n}` was a deprecated alias for the builtin `{n}`. "
        "additional information."
        "char",
        "core",
        "ctypeslib",
        "details and guidance see the original release note at:\n"
        "Doing this will not modify any behavior and is safe. {extended_msg}\n"
        "dtypes",
        "exceptions",
        "f2py",
        "fft",
        "If you specifically wanted the numpy scalar type, use `np.{}` here."
        "lib",
        "linalg",
        "ma",
        "module 'numpy' has no attribute '{n}'.\n"
        "or `np.int32` to specify the precision. If you wish to review "
        "polynomial",
        "random",
        "rec",
        "strings",
        "test",
        "testing",
        "The aliases was originally deprecated in NumPy 1.20; for more "
        "To avoid this error in existing code, use `{n}` by itself. "
        "typing",
        "When replacing `np.{}`, you may wish to use e.g. `np.int64` "
        "your current use, check the release note link for "
        # Warn for expired attributes
        ("complex", _specific_msg.format("complex128")),
        ("float", _specific_msg.format("float64")),
        ("int", _int_extended_msg.format("int")),
        ("object", ""),  # The NumPy scalar only exists by name.
        ("str", _specific_msg.format("str_")),
        )
        __numpy_submodules__
        | {"emath", "show_config", "__version__", "__array_namespace_info__"}
        | set(_core.__all__)
        | set(_mat.__all__)
        | set(lib._arraypad_impl.__all__)
        | set(lib._arraysetops_impl.__all__)
        | set(lib._function_base_impl.__all__)
        | set(lib._histograms_impl.__all__)
        | set(lib._index_tricks_impl.__all__)
        | set(lib._nanfunctions_impl.__all__)
        | set(lib._npyio_impl.__all__)
        | set(lib._polynomial_impl.__all__)
        | set(lib._shape_base_impl.__all__)
        | set(lib._stride_tricks_impl.__all__)
        | set(lib._twodim_base_impl.__all__)
        | set(lib._type_check_impl.__all__)
        | set(lib._ufunclike_impl.__all__)
        | set(lib._utils_impl.__all__)
        }
        abs,
        achieved during test suite runs, and it is useful to catch those early.
        array,
        elif attr == "array_api":
        elif attr == "char":
        elif attr == "core":
        elif attr == "ctypeslib":
        elif attr == "distutils":
        elif attr == "dtypes":
        elif attr == "exceptions":
        elif attr == "f2py":
        elif attr == "fft":
        elif attr == "ma":
        elif attr == "matlib":
        elif attr == "polynomial":
        elif attr == "random":
        elif attr == "rec":
        elif attr == "strings":
        elif attr == "testing":
        elif attr == "typing":
        elif use_hugepage is None:
        else:
        except AssertionError:
        except AttributeError:
        except ValueError:
        float32,
        from . import exceptions
        from pathlib import Path
        had a bug fix which probably fixed this:
        https://github.com/torvalds/linux/commit/7cf91a98e607c2f935dbcc177d70011e95b8faff
        if attr == "chararray":
        if attr == "linalg":
        if attr in __expired_attributes__:
        if attr in __former_attrs__:
        if attr in __future_scalars__:
        if sys.platform == "linux" and use_hugepage is None:
        import warnings
        is slow and thus better avoided. Specifically kernel version 4.6
        its source directory; please exit the numpy source tree, and relaunch
        linspace,
        msg = """Error importing numpy: you should not try to import numpy from
        n: _msg.format(n=n, extended_msg=extended_msg) for n, extended_msg in _type_info
        ones,
        pass
        polyfit,
        polyval,
        public_symbols -= {
        public_symbols = globals().keys() | __numpy_submodules__
        Quick Sanity check for Mac OS look for accelerate build bugs.
        Quick sanity checks for common bugs caused by environment.
        raise AttributeError(
        raise ImportError(msg) from e
        results under specific runtime conditions that are not necessarily
        return [str(Path(__file__).with_name("_pyinstaller").resolve())]
        return list(public_symbols)
        return use_hugepage
        See https://github.com/numpy/numpy/issues/8577 and other
        similar bug reports.
        Testing numpy polyfit calls init_dgelsd(LAPACK)
        There are some cases e.g. with wrong BLAS ABI that cause wrong
        try:
        use_hugepage = os.environ.get("NUMPY_MADVISE_HUGEPAGE", None)
        warnings.warn(
        We usually use madvise hugepages support, but on some old kernels it
        with warnings.catch_warnings(record=True) as w:
        your python interpreter from there."""
    # (experimental label) are not added here, because `from numpy import *`
    # __getattr__. Note that `distutils` (deprecated) and `array_api`
    # Allow distributors to run custom init code before importing numpy._core
    # Filter out Cython harmless warnings
    # Give a warning if NumPy is reloaded or imported on a sub-interpreter
    # import with `from numpy import *`.
    # it is tidier organized.
    # must not raise any warnings - that's too disruptive.
    # Note that this will currently only make a difference on Linux
    # NOTE: It's still under discussion whether these aliases
    # now that numpy core module is imported, can initialize limits
    # probably wait for NumPy 1.26 or 2.0.
    # public submodules are imported lazily, therefore are accessible from
    # Pytest testing
    # should be removed.
    # Some of these could be defined right away, but most were aliases to
    # Tell PyInstaller where to find hook-numpy.py
    # the Python objects and only removed in NumPy 1.24.  Defining them should
    # TODO: Remove the environment variable entirely now that it is "weak"
    # We build warning messages for former attributes
    # We do this from python, since the C-module may not be reloaded and
    # When defined, these should possibly not be added to `__all__` to avoid
    )
    ]
    __all__ = list(
    __array_api_version__ = "2023.12"
    __former_attrs__ = {
    __future_scalars__ = {"str", "bytes", "object"}
    __NUMPY_SETUP__
    __NUMPY_SETUP__ = False
    __numpy_submodules__ = {
    _core.getlimits._register_known_types()
    _core.multiarray._multiarray_umath._reload_guard()
    _core.multiarray._set_madvise_hugepage(hugepage_setup())
    _int_extended_msg = (
    _msg = (
    _sanity_check()
    _specific_msg = (
    _type_info = [
    }
    Basic functions used by several sub-packages.
    Core FFT routines
    Core Linear Algebra Tools
    Core Random Tools
    def __dir__():
    def __getattr__(attr):
    def _mac_os_check():
    def _pyinstaller_hooks_dir():
    def _sanity_check():
    def hugepage_setup():
    del _mac_os_check
    del _sanity_check
    del hugepage_setup
    del PytestTester
    del ta
    Enhancements to distutils with support for
    except ImportError as e:
    for ta in ["float96", "float128", "complex192", "complex256"]:
    Fortran compilers support and more (for Python <= 3.11)
    from . import _core
    from . import lib
    from . import matrixlib as _mat
    from ._core import (
    from .lib._polynomial_impl import (
    from numpy._pytesttester import PytestTester
    if os.environ.get("NPY_PROMOTION_STATE", "weak") != "weak":
    if sys.platform == "darwin":
    NumPy testing tools
    NumPy version string
    pass
    Polynomial tools
    Run numpy unittests
    Show numpy build configuration
    sys.stderr.write("Running from numpy source directory.\n")
    test = PytestTester(__name__)
    try:
    warnings.filterwarnings("ignore", message="numpy.dtype size changed")
    warnings.filterwarnings("ignore", message="numpy.ndarray size changed")
    warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
  ... # doctest: +SKIP
  >>> help(np.sort)
  >>> import numpy as np
  >>> x = 42
  >>> x = x + 1
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation
"""
# If a version with git hash was stored, use that instead
# procedure itself in a reliable manner.
# Remove symbols imported for internal use
# We first need to detect if we're being called as part of the numpy setup
(e.g., `np.sort`).  In-place versions of these functions are often
__version__
``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow
``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view
`IPython <https://ipython.org>`_, an advanced Python shell with
`the NumPy homepage <https://numpy.org>`_.
=====
available as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.
Available subpackages
Code snippets are indicated by three greater-than signs::
Copies vs. in-place operation
del os, sys, warnings
distutils
Documentation is available in two forms: docstrings provided
down the list.  To view the docstring for a function, use
else:
examples into the shell.  To see which functions are available in `numpy`,
except NameError:
Exceptions to this rule are documented.
fft
For some objects, ``np.info(obj)`` may provide additional help.  This is
from ._expired_attrs_2_0 import __expired_attributes__
How to use the documentation
if __NUMPY_SETUP__:
import os
import sys
import warnings
instructions.
lib
linalg
Most of the functions in `numpy` return a copy of the array argument
np.info() function does.
NumPy
numpy as np`.  Then, directly past or use the ``%cpaste`` magic to paste
of the help() page.  Ufuncs are implemented in C, not Python, for speed.
particularly true if you see the line "Help on ufunc object:" at the top
polynomial
Provides
random
show_config
Start IPython and import `numpy` usually under the alias ``np``: `import
TAB-completion and introspection capabilities.  See below for further
test
testing
The docstring examples assume that `numpy` has been imported as ``np``::
The native Python help() does not know how to view their help, but our
the source code).
try:
type ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use
Use the built-in ``help`` function to view a function's docstring::
Utilities
Viewing documentation using IPython
We recommend exploring the docstrings using
with the code, and a loose standing reference guide, available from
