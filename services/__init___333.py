
                              via PEP 658.
        canonical_name,
        filename,
        from . import importlib
        metadata_contents,
        return bool(strtobool(os.environ["_PIP_USE_IMPORTLIB_METADATA"]))
        return cast(Backend, importlib)
        return False
      dictates whether ``importlib.metadata`` is used, regardless of Python
      environment variable to *True*).
      makes pip use ``pkg_resources`` (unless the user set the aforementioned
      to add a global constant ``_PIP_USE_IMPORTLIB_METADATA = False``. This
      version.
    """
    """Get a representation of the environment specified by ``paths``.
    """Get the default representation for the current environment.
    """Get the dist representation of the specified METADATA file contents.
    """Get the distribution metadata representation in the specified directory.
    """Get the representation of the specified wheel's distribution metadata.
    """Whether to use the ``importlib.metadata`` or ``pkg_resources`` backend.
    "BaseDistribution",
    "BaseEnvironment",
    "FilesystemWheel",
    "get_default_environment",
    "get_environment",
    "get_wheel_distribution",
    "MemoryWheel",
    "select_backend",
    "Wheel",
    )
    * If environment variable ``_PIP_USE_IMPORTLIB_METADATA`` is set, it
    * On Python 3.11+, Python distributors can patch ``importlib.metadata``
    :param canonical_name: Normalized project name of the given dist.
    :param canonical_name: Normalized project name of the given wheel.
    :param filename: Filename for the dist this metadata represents.
    :param metadata_contents: Contents of a METADATA file within a dist, or one served
    ``pkg_resourcess`` otherwise. This can be overridden by a couple of ways:
    By default, pip uses ``importlib.metadata`` on Python 3.11+, and
    canonical_name: str,
    def __init__(self, *args, **kwargs): pass
    Distribution: Type[BaseDistribution]
    Environment instance should be built from ``sys.path`` and may use caching
    Environment: Type[BaseEnvironment]
    filename: str,
    from . import pkg_resources
    from typing import Literal, Protocol
    given import paths. The backend must build a fresh instance representing
    if _should_use_importlib_metadata():
    if sys.version_info < (3, 11):
    import importlib.metadata
    in `metadata_contents`.
    metadata_contents: bytes,
    NAME: 'Literal["importlib", "pkg_resources"]'
    Protocol = object
    return bool(getattr(importlib.metadata, "_PIP_USE_IMPORTLIB_METADATA", True))
    return cast(Backend, pkg_resources)
    return select_backend().Distribution.from_directory(directory)
    return select_backend().Distribution.from_metadata_file_contents(
    return select_backend().Distribution.from_wheel(wheel, canonical_name)
    return select_backend().Environment.default()
    return select_backend().Environment.from_paths(paths)
    the given on-disk ``.dist-info`` directory.
    the given wheel's ``.dist-info`` directory.
    the state of installed distributions when this function is called.
    This returns a Distribution instance from the chosen backend based on
    This returns a Distribution instance from the chosen backend sourced from the data
    This returns an Environment instance from the chosen backend based on the
    This returns an Environment instance from the chosen backend. The default
    to share instance state accorss calls.
    with contextlib.suppress(KeyError, ValueError):
) -> BaseDistribution:
@functools.lru_cache(maxsize=None)
]
__all__ = [
class Backend:
def _should_use_importlib_metadata() -> bool:
def get_default_environment() -> BaseEnvironment:
def get_directory_distribution(directory: str) -> BaseDistribution:
def get_environment(paths: Optional[List[str]]) -> BaseEnvironment:
def get_metadata_distribution(
def get_wheel_distribution(wheel: Wheel, canonical_name: str) -> BaseDistribution:
def select_backend() -> Backend:
else:
from .base import BaseDistribution, BaseEnvironment, FilesystemWheel, MemoryWheel, Wheel
from pip._internal.utils.misc import strtobool
from typing import TYPE_CHECKING, List, Optional, Type, cast
if TYPE_CHECKING:
import contextlib
import functools
import os
import sys
