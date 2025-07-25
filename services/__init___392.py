
        "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`",
        "Please use `tqdm.notebook.trange` instead of `tqdm.tnrange`",
        "This function will be removed in tqdm==5.0.0\n"
        stacklevel=2,
        TqdmDeprecationWarning,
    """See tqdm.notebook.tqdm for full documentation"""
    """Shortcut for `tqdm.notebook.tqdm(range(*args), **kwargs)`."""
    "__version__",
    "main",
    "tgrange",
    "TMonitor",
    "tnrange",
    "tqdm",
    "tqdm_gui",
    "tqdm_notebook",
    "tqdm_pandas",
    "TqdmDeprecationWarning",
    "TqdmExperimentalWarning",
    "TqdmKeyError",
    "TqdmMonitorWarning",
    "TqdmSynchronisationWarning",
    "TqdmTypeError",
    "TqdmWarning",
    "trange",
    )
    from .notebook import tqdm as _tqdm_notebook
    from .notebook import trange as _tnrange
    from warnings import warn
    return _tnrange(*args, **kwargs)
    return _tqdm_notebook(*args, **kwargs)
    tqdm,
    TqdmDeprecationWarning,
    TqdmExperimentalWarning,
    TqdmKeyError,
    TqdmMonitorWarning,
    TqdmTypeError,
    TqdmWarning,
    trange,
    warn(
)
]
__all__ = [
def tnrange(*args, **kwargs):  # pragma: no cover
def tqdm_notebook(*args, **kwargs):  # pragma: no cover
from ._monitor import TMonitor, TqdmSynchronisationWarning
from ._tqdm_pandas import tqdm_pandas
from .cli import main  # TODO: remove in v5.0.0
from .gui import tqdm as tqdm_gui  # TODO: remove in v5.0.0
from .gui import trange as tgrange  # TODO: remove in v5.0.0
from .std import (
from .version import __version__
