
            "`math` module (Deprecated Numpy 1.25). Replace usages of "
            "`np.lib.math` is a deprecated alias for the standard library "
            "`numpy.lib.math` with `math`",
            "Arrayterator class use numpy.lib.Arrayterator.",
            "function, it should be available in the main numpy namespace, "
            "in NumPy 2.0. Replace usages of numpy.lib.emath with "
            "module {!r} has no attribute " "{!r}".format(__name__, attr)
            "numpy.emath.",
            "numpy.lib.arrayterator submodule is now private. To access "
            "numpy.lib.emath was an alias for emath module that was removed "
            "otherwise check the NumPy 2.0 migration guide.",
            DeprecationWarning,
            f"numpy.lib.{attr} is now private. If you are using a public "
            name=None,
            stacklevel=2,
        "arraypad",
        "arraysetops",
        "function_base",
        "histograms",
        "index_tricks",
        "nanfunctions",
        "polynomial",
        "shape_base",
        "twodim_base",
        "type_check",
        "ufunclike",
        "utils",
        )
        raise AttributeError(
        return math
        warnings.warn(
    "add_docstring",
    "add_newdoc",
    "array_utils",
    "Arrayterator",
    "introspect",
    "mixins",
    "npyio",
    "NumpyVersion",
    "scimath",
    "stride_tricks",
    "tracemalloc_domain",
    # Warn for deprecated/removed aliases
    ):
    elif attr == "arrayterator":
    elif attr == "emath":
    elif attr in (
    else:
    if attr == "math":
    import math
    import warnings
"""
# load module names. See https://github.com/networkx/networkx/issues/5838
# Note: recfunctions and (maybe) format are public too, but not imported
# numpy.lib namespace members
# Private submodules
# Public submodules
(e.g. ``random``, ``fft``, ``linalg``, ``ma``).
]
__all__ = [
``numpy.lib`` is mostly a space for implementing functions that don't
``numpy.lib``'s private submodules contain basic functions that are used by
add_newdoc.__module__ = "numpy.lib"
belong in core or in another NumPy submodule with a clear purpose
def __getattr__(attr):
del PytestTester
from . import array_utils
from . import introspect
from . import mixins
from . import npyio
from . import scimath
from . import stride_tricks
from ._arrayterator_impl import Arrayterator
from ._version import NumpyVersion
from numpy._core._multiarray_umath import add_docstring, tracemalloc_domain
from numpy._core.function_base import add_newdoc
from numpy._pytesttester import PytestTester
other public modules and are useful to have in the main name-space.
test = PytestTester(__name__)
