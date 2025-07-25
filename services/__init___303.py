
    " is deprecated since 1.26.0, and will be removed",
    "`np.compat`, which was used during the Python 2 to 3 transition,"
    DeprecationWarning,
    stacklevel=2,
  * compatibility
  * we may only need a small subset of the copied library/module
"""
)
__all__ = []
__all__.extend(_inspect.__all__)
__all__.extend(py3k.__all__)
Compatibility module.
extensions, which may be included for the following reasons:
from . import py3k
from .._utils import _inspect
import warnings
This module contains duplicated code from Python itself or 3rd party
This module is deprecated since 1.26.0 and will be removed in future versions.
warnings.warn(
