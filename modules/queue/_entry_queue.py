
                            "Internal error: `parent_nursery` should never be `None`",
                        ) from exc  # pragma: no cover
                        raise AssertionError(
                    # be fixed soon when we address #1607.
                    # system nursery is already closed.
                    # TODO(2020-06): this is a gross hack and should
                    # We're quite late in the shutdown process and the
                    _core.spawn_system_task(kill_everything, exc)
                    await _core.checkpoint()
                    await self.wakeup.wait_woken()
                    exc: BaseException,
                    if parent_nursery is None:
                    parent_nursery = _core.current_task().parent_nursery
                    parent_nursery.start_soon(kill_everything, exc)
                    raise exc
                ) -> NoReturn:
                async def kill_everything(  # noqa: RUF029  # await not used
                del self.idempotent_queue[job]
                else:
                except RuntimeError:
                if not self.queue and not self.idempotent_queue:
                raise _core.RunFinishedError("run() has exited")
                run_all_bounded()
                run_cb(job)
                run_cb(self.queue.popleft())
                self.done = True
                self.idempotent_queue[sync_fn, args] = None
                self.queue.append((sync_fn, args))
                sync_fn(*args)
                try:
              exits.)
              has already exited. (Any call that *doesn't* raise this error
              if the associated call to :func:`trio.run`
              is guaranteed to be fully processed before :func:`trio.run`
            #       pass
            #   self.done = True
            #   with self.lock:
            # (see the comment above). Notice that this code would still be
            # against signal handlers.
            # already been shut down.
            # because all we want is to force run_sync_soon
            # because it doesn't protect us against concurrent signal delivery
            # calls, and then our queue item might not be processed, or the
            # correct if written like:
            # done. That's why we don't need the lock to protect
            # job to disable it if it wants it disabled. Exceptions are
            # Keep the work done with this lock held as minimal as possible,
            # No more jobs will be submitted, so just clear out any residual
            # ones:
            # otherwise the main thread might exit *while* we're doing these
            # to either be completely before or completely after the write to
            # treated like system task exceptions (i.e., converted into
            # TrioInternalError and cause everything to shut down).
            # wakeup call might trigger an OSError b/c the IO manager has
            # We have to hold the lock all the way through here, because
            # We run this with KI protection enabled; it's the callback's
            assert not self.idempotent_queue
            assert not self.queue
            else:
            except BaseException as exc:
            for _ in range(len(self.queue)):
            for job in list(self.idempotent_queue):
            if idempotent:
            if self.done:
            run_all_bounded()
            self.wakeup.wakeup_thread_and_signal_safe()
            sync_fn, args = job
            try:
            while True:
            with self.lock:
          :exc:`~trio.TrioInternalError` and *all* tasks are cancelled. You
          explicitly.
          need to use :func:`~trio.lowlevel.disable_ki_protection`
          should be careful that ``sync_fn`` doesn't crash.
          you want ``sync_fn`` to be interruptible by control-C, then you
        """
        """Schedule a call to ``sync_fn(*args)`` to occur in the context of a
        #     https://bugs.python.org/issue13697#msg237140
        # and signal-UNsafe version in threading. We need the signal safe
        # being queued while we iterate, and to do a bounded amount of work on
        # deadlocks", then let's make a little check.
        # each pass:
        # RLock has two implementations: a signal-safe version in _thread, and
        # See:
        # since the symptoms if this goes wrong are just "weird rare
        # This has to be carefully written to be safe in the face of new items
        # version. Python 3.2 and later should always use this anyway, but,
        * :exc:`KeyboardInterrupt` protection is *enabled* by default; if
        * If ``sync_fn`` raises an exception, then it's converted into a
        *args: Unpack[PosArgsT],
        :func:`~trio.lowlevel.spawn_system_task`). In particular this means
        :raises trio.RunFinishedError:
        All calls with ``idempotent=False`` are processed in strict
        and ``idempotent=True`` calls; there's no rule for how calls in the
        Any ordering guarantees apply separately to ``idempotent=False``
        assert _core.currently_ki_protected()
        assert self.lock.__class__.__module__ == "_thread"
        call submission which is equal to an already-pending call. Trio
        def run_all_bounded() -> None:
        def run_cb(job: Job) -> None:
        different categories are ordered with respect to each other.
        except _core.Cancelled:
        first-in first-out order.
        from signal handlers. This is the fundamental primitive used to
        hashable, and Trio will make a best-effort attempt to discard any
        idempotent: bool = False,
        If ``idempotent=True``, then ``sync_fn`` and ``args`` must be
        If you need this, you'll have to build your own.
        re-enter the Trio run loop from outside of it.
        return len(self.queue) + len(self.idempotent_queue)
        self,
        self._reentry_queue.run_sync_soon(sync_fn, *args, idempotent=idempotent)
        self.wakeup.close()
        sync_fn: Callable[[Unpack[PosArgsT]], object],
        that:
        The call is effectively run as part of a system task (see
        The call will happen "soon", but there's no guarantee about exactly
        This is safe to call from the main thread, from other threads, and
        Trio task.
        try:
        when, and no mechanism provided for finding out when it's happened.
        will process these in first-in first-out order.
        with self.lock:
       :class:`TrioToken` object, so you can use it to identify a particular
       `trio.open_signal_receiver` uses to receive notifications about
       and `trio.from_thread` use to communicate with worker threads, that
       call.
       handlers. This is the low-level primitive that :func:`trio.to_thread`
       signals, and so forth.
    """
    """An opaque object representing a single call to :func:`trio.run`.
    # atomic WRT signal delivery (signal handlers can run on either side, but
    # implemented in Python, and not reentrant -- so it was thread-safe, but
    # it's even ordered!
    # just to make 1 assignment, so that's atomic WRT a signal anyway.
    # lock is effectively *disabled* when we enter from signal context. The
    # main thread -- it just might happen at some inconvenient place. But if
    # Must be a reentrant lock, because it's acquired from signal handlers.
    # not *during* a deque operation). dict makes similar guarantees - and
    # not signal-safe. deque is implemented in C, so each operation is atomic
    # RLock is signal-safe as of cpython 3.2. NB that this does mean that the
    # run_sync_soon is called from a signal it's atomic WRT the
    # This used to use a queue.Queue. but that was broken, because Queues are
    # way we use the lock this is OK though, because when
    # WRT threads (and this is guaranteed in the docs), AND each operation is
    # you look at the one place where the main thread holds the lock, it's
    ) -> None:
    _reentry_queue: EntryQueue
    1. It lets you re-enter the Trio run loop from external threads or signal
    2. Each call to :func:`trio.run` has exactly one associated
    async def task(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def close(self) -> None:
    def run_sync_soon(
    def size(self) -> int:
    done: bool = False
    from typing_extensions import TypeVarTuple, Unpack
    idempotent_queue: dict[Job, None] = attrs.Factory(dict)
    It has no public constructor; instead, see :func:`current_trio_token`.
    lock: threading.RLock = attrs.Factory(threading.RLock)
    PosArgsT = TypeVarTuple("PosArgsT")
    queue: deque[Job] = attrs.Factory(deque)
    This object has two uses:
    wakeup: WakeupSocketpair = attrs.Factory(WakeupSocketpair)
# -*- coding: utf-8 -*-
@attrs.define
@attrs.define(eq=False)
@final
class EntryQueue:
class TrioToken:
from .. import _core
from .._util import final
from ._wakeup_socketpair import WakeupSocketpair
from __future__ import annotations
from collections import deque
from collections.abc import Callable
from typing import TYPE_CHECKING, NoReturn
Function = Callable[..., object]  # type: ignore[explicit-any]
if TYPE_CHECKING:
import attrs
import threading
Job = tuple[Function, tuple[object, ...]]
