
    "__version__",
    "HookCaller",
    "HookCallError",
    "HookImpl",
    "HookimplMarker",
    "HookimplOpts",
    "HookRelay",
    "HookspecMarker",
    "HookspecOpts",
    "PluggyTeardownRaisedWarning",
    "PluggyWarning",
    "PluginManager",
    "PluginValidationError",
    "Result",
    # broken installation, we don't even try
    # unknown only works because we do poor mans version compare
    __version__ = "unknown"
    from ._version import version as __version__
]
__all__ = [
except ImportError:
from ._hooks import HookCaller
from ._hooks import HookImpl
from ._hooks import HookimplMarker
from ._hooks import HookimplOpts
from ._hooks import HookRelay
from ._hooks import HookspecMarker
from ._hooks import HookspecOpts
from ._manager import PluginManager
from ._manager import PluginValidationError
from ._result import HookCallError
from ._result import Result
from ._warnings import PluggyTeardownRaisedWarning
from ._warnings import PluggyWarning
try:
