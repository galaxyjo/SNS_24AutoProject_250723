
                "ignore",
                FutureWarning,
                r".*In the future `np\.long` will be defined as.*",
            )
            np_long = np.long  # type: ignore[attr-defined]
            np_ulong = np.ulong  # type: ignore[attr-defined]
            warnings.filterwarnings(
        f"Please upgrade numpy to >= {_min_numpy_ver} to use this pandas version"
        f"this version of pandas is incompatible with numpy < {_min_numpy_ver}\n"
        f"your numpy version is {_np_version}.\n"
        np_long = np.int_
        np_ulong = np.uint
        with warnings.catch_warnings():
    "_np_version",
    "is_numpy_dev",
    "np",
    )
    except AttributeError:
    np_long = np.int_
    np_ulong = np.uint
    raise ImportError(
    try:
"""support numpy compatibility across versions"""
# numpy versioning
]
__all__ = [
_min_numpy_ver = "1.22.4"
_nlv = Version(_np_version)
_np_version = np.__version__
else:
from pandas.util.version import Version
if _nlv < Version(_min_numpy_ver):
if np_version_gt2:
import numpy as np
import warnings
is_numpy_dev = _nlv.dev is not None
np_long: type
np_ulong: type
np_version_gt2 = _nlv >= Version("2.0.0")
np_version_gte1p24 = _nlv >= Version("1.24")
np_version_gte1p24p3 = _nlv >= Version("1.24.3")
np_version_gte1p25 = _nlv >= Version("1.25")
np_version_lt1p23 = _nlv < Version("1.23")
