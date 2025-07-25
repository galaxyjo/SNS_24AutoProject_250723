
            "The `np._core.MachAr` is considered private API (NumPy 1.24)",
            DeprecationWarning,
            stacklevel=2,
        "numpy in {}. One method of fixing this is to repeatedly uninstall "
        "numpy until none is found, then reinstall this version."
        "Something is wrong with the numpy installation. "
        "While importing we detected an older version of "
        )
        __version__,
        del os.environ[envkey]
        env_added.append(envkey)
        exc,
        import warnings
        os.environ[envkey] = "1"
        return _machar.MachAr
        return DType.__name__
        sys.executable,
        sys.version_info[0],
        sys.version_info[1],
        warnings.warn(
    "abs",
    "acos",
    "acosh",
    "asin",
    "asinh",
    "atan",
    "atan2",
    "atanh",
    "bitwise_invert",
    "bitwise_left_shift",
    "bitwise_right_shift",
    "concat",
    "memmap",
    "permute_dims",
    "pow",
    "recarray",
    "record",
    "sctypeDict",
    # `numpy.dtypes` as module and do not have a public class at all.
    # and it should eventually be replaced with a better solution, e.g. when
    # As types/classes, most DTypes can simply be pickled by their name:
    # Deprecated 2022-11-22, NumPy 1.25.
    # DTypes become HeapTypes.
    # explicitly (Numba has ufuncs as attributes).
    # For these, we pickle them by reconstructing them from the scalar type:
    # However, user defined legacy dtypes (like rational) do not end up in
    # make sense to add a `__qualname__` to ufuncs, to allow this more
    # pickle supports for this `__name__` to be a `__qualname__`. It may
    # Report the `__name__`. pickle will try to find the module. Note that
    # See also: https://github.com/dask/distributed/issues/3450
    # This is a work-around to pickle type(np.dtype(np.float64)), etc.
    )
    for envkey in env_added:
    from . import multiarray
    hasattr(multiarray, "_multiarray_umath") and hasattr(umath, "_multiarray_umath")
    https://numpy.org/devdocs/user/troubleshooting-importerror.html
    if envkey not in os.environ:
    if name == "MachAr":
    if not DType._legacy or DType.__module__ == "numpy.dtypes":
    import sys
    msg = """
    msg = (
    path = sys.modules["numpy"].__path__
    raise AttributeError(f"Module {__name__!r} has no attribute {name!r}")
    raise ImportError(msg)
    raise ImportError(msg.format(path))
    return _DType_reconstruct, (scalar_type,)
    return func.__name__
    return type(dtype(scalar_type))
    scalar_type = DType.type
  * The NumPy version is: "%s"
  * The Python version is: Python%d.%d from "%s"
"""
""" % (
# _multiarray_umath and not either of the old c-extension modules
# add these for module-freeze analysis (like PyInstaller)
# appearing in an import-time traceback
# Check that multiarray,umath are pure python modules wrapping
# disables OpenBLAS affinity setting of the main thread that limits
# do this after everything else, to minimize the chance of this misleadingly
# Note: module name memmap is overwritten by a class with same name
# python threads or processes to one core
# Unclutter namespace (must keep _*_reconstruct for unpickling)
):
]
__all__ += einsumfunc.__all__
__all__ += function_base.__all__
__all__ += getlimits.__all__
__all__ += numeric.__all__
__all__ += shape_base.__all__
__all__ = [
acos = numeric.arccos
acosh = numeric.arccosh
and make sure that they are the versions you expect.
are available in the main ``numpy`` namespace - use that instead.
asin = numeric.arcsin
asinh = numeric.arcsinh
atan = numeric.arctan
atan2 = numeric.arctan2
atanh = numeric.arctanh
bitwise_invert = numeric.invert
bitwise_left_shift = numeric.left_shift
bitwise_right_shift = numeric.right_shift
concat = numeric.concatenate
Contains the core of NumPy: ndarray, ufuncs, dtypes, etc.
copyreg.pickle(type(dtype), _DType_reduce, _DType_reconstruct)
copyreg.pickle(ufunc, _ufunc_reduce)
def __getattr__(name):
def _DType_reconstruct(scalar_type):
def _DType_reduce(DType):
def _ufunc_reduce(func):
del copyreg, _ufunc_reduce, _DType_reduce
del env_added
del envkey
del nt
del os
del PytestTester
env_added = []
except ImportError as exc:
finally:
for envkey in ["OPENBLAS_MAIN_FREE", "GOTOBLAS_MAIN_FREE"]:
from . import _machar
from . import einsumfunc
from . import function_base
from . import getlimits
from . import numeric
from . import numerictypes as nt
from . import shape_base
from . import umath
from .einsumfunc import *
from .fromnumeric import *
from .function_base import *
from .getlimits import *
from .memmap import *
from .numeric import *
from .numeric import absolute as abs
from .numerictypes import sctypeDict
from .records import record, recarray
from .shape_base import *
from numpy._pytesttester import PytestTester
from numpy.version import version as __version__
if not (
import copyreg
import os
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!
Importing the numpy C-extensions failed. This error can happen for
installed.
many reasons, often due to issues with your setup or how NumPy was
multiarray.set_typeDict(nt.sctypeDict)
Original error was: %s
permute_dims = numeric.transpose
Please carefully study the documentation linked above for further help.
Please note and check the following:
Please note that this module is private.  All functions and objects
pow = numeric.power
test = PytestTester(__name__)
try:
We have compiled some common reasons and troubleshooting tips at:
