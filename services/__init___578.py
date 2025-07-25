
            # for stdin, we want the write end (our end) to use overlapped I/O
            # for stdout/err, it's the read end that's overlapped
            return PipeReceiveStream(rh), msvcrt.open_osfhandle(wh, 0)
            return PipeSendStream(wh), msvcrt.open_osfhandle(rh, os.O_RDONLY)
            return trio.lowlevel.FdStream(rfd), wfd
            return trio.lowlevel.FdStream(wfd), rfd
            rfd, wfd = os.pipe()
            rh, wh = windows_pipe(overlapped=(False, True))
            rh, wh = windows_pipe(overlapped=(True, False))
        # as it's an exported symbol, noqa'd
        # for 3.5 included an example that imported socketpair from
        # Not worth type checking these definitions
        # removal was mentioned in the release notes.
        # This isn't exported or documented, but it's also not
        # underscore-prefixed, and seems kosher to use. The asyncio docs
        # when asyncio.windows_utils.socketpair was removed in 3.7, the
        # windows_utils (before socket.socketpair existed on Windows), and
        def create_pipe_from_child_output() -> tuple[PipeReceiveStream, int]:
        def create_pipe_from_child_output() -> tuple[trio.lowlevel.FdStream, int]:
        def create_pipe_to_child_stdin() -> tuple[PipeSendStream, int]:
        def create_pipe_to_child_stdin() -> tuple[trio.lowlevel.FdStream, int]:
        from .._windows_pipes import PipeReceiveStream, PipeSendStream
        from .kqueue import wait_child_exiting
        from .waitid import wait_child_exiting  # noqa: F401
        from .windows import wait_child_exiting
        from asyncio.windows_utils import pipe as windows_pipe
        import msvcrt
        pass
        raise ImportError("pipes not implemented on this platform")
      :class:`~trio.abc.ReceiveStream` and ``subprocess_end`` is
      :class:`~trio.abc.SendStream` and ``subprocess_end`` is
      :class:`subprocess.Popen`.
      A pair ``(trio_end, subprocess_end)`` where ``trio_end`` is a
      something suitable for passing as the ``stdin`` argument of
    """
    """Block until the child process managed by ``process`` is exiting.
    """Create a new pipe suitable for receiving data into this
    """Create a new pipe suitable for sending data from this
    # internal types for the pipe representations used in type checking only
    :meth:`subprocess.Popen.wait` will immediately be able to
    _create_child_pipe_error = ex
    _wait_child_exiting_error = ex
    been waited on; that is, ``process.returncode`` must be None.
    class ClosableReceiveStream:
    class ClosableSendStream:
    consumed by this call, since :class:`~subprocess.Popen` wants
    def __init__(self, *args, **kwargs): pass
    def close(self) -> None: ...
    elif os.name == "nt":
    elif os.name == "posix":
    elif sys.platform != "linux" and (TYPE_CHECKING or hasattr(_core, "wait_kevent")):
    else:
    else:  # pragma: no cover
    if sys.platform == "win32":
    if TYPE_CHECKING:
    It is invalid to call this function if the process has already
    process from the standard output or error stream of a child
    process to the standard input of a child we're about to spawn.
    raise NotImplementedError from _create_child_pipe_error  # pragma: no cover
    raise NotImplementedError from _wait_child_exiting_error  # pragma: no cover
    return the process's exit status. The actual exit status is not
    Returns:
    to be able to do that itself.
    we're about to spawn.
    When this function returns, it indicates that a call to
# Fallback versions of the functions provided -- implementations
# per OS are imported atop these at the bottom of the module.
# Platform-specific subprocess bits'n'pieces.
_create_child_pipe_error: ImportError | None = None
_wait_child_exiting_error: ImportError | None = None
async def wait_child_exiting(process: _subprocess.Process) -> None:
def create_pipe_from_child_output() -> tuple[ClosableReceiveStream, int]:
def create_pipe_to_child_stdin() -> tuple[ClosableSendStream, int]:
except ImportError as ex:  # pragma: no cover
from .. import _core, _subprocess
from .._abc import ReceiveStream, SendStream  # noqa: TC001
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import os
import sys
import trio
try:
