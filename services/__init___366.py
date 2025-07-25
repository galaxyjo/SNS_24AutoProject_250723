
                     change between major releases as new statistics are
                     gathered or removed so before accessing keys ensure that
                     stable (not changing), but there existence **may**
                     they actually exist and handle when they do not.
                    f"Got retry_base instance ({f.__class__.__name__}) as callable argument, "
                    f"this will probably hang indefinitely (did you mean retry={f.__class__.__name__}(...)?)"
                    result = fn(*args, **kwargs)
                    retry_state.set_exception(sys.exc_info())  # type: ignore[arg-type]
                    retry_state.set_result(result)
                  future we may provide a way to aggregate the various
                  object - either directly or indirectly) they will each have
                  running call (so if multiple threads share the same retrying
                  statistics from each thread).
                  there own view of statistics they have collected (in the
                )
                and hasattr(tornado.gen, "is_coroutine_function")
                and tornado.gen.is_coroutine_function(f)
                break
                else:
                except BaseException:  # noqa: B902
                r = AsyncRetrying(*dargs, **dkw)
                r = Retrying(*dargs, **dkw)
                r = TornadoRetrying(*dargs, **dkw)
                raise retry_exc.reraise()
                retry_error_callback, self.retry_error_callback
                retry_state.prepare_for_next_attempt()
                return do  # type: ignore[no-any-return]
                return self.retry_error_callback(retry_state)
                self.before(retry_state)
                self.sleep(do)
                tornado
                try:
                warnings.warn(
                yield AttemptManager(retry_state=retry_state)
            # We don't have the result, actually.
            ),
            ):
            after=_first_set(after, self.after),
            before_sleep=_first_set(before_sleep, self.before_sleep),
            before=_first_set(before, self.before),
            do = self.iter(retry_state=retry_state)
            elif (
            elif isinstance(do, DoSleep):
            else:
            exception = self.outcome.exception()
            f"{field}={getattr(self, field)!r}" for field in self.REPR_FIELDS
            f"<{self.__class__.__name__} object at 0x{id(self):x} ("
            f"after={self.after})>"
            f"before={self.before}, "
            f"retry={self.retry}, "
            f"sleep={self.sleep}, "
            f"stop={self.stop}, "
            f"wait={self.wait}, "
            fut.set_exception(value)
            fut.set_result(value)
            if iscoroutinefunction(f):
            if isinstance(do, DoAttempt):
            if isinstance(f, retry_base):
            if self.before is not None:
            if self.reraise:
            if self.retry_error_callback:
            r: "BaseRetrying"
            raise retry_exc from fut.exception()
            raise self.last_attempt.result()
            reraise=_first_set(reraise, self.reraise),
            result = "none yet"
            result = f"failed ({exception.__class__.__name__} {exception})"
            result = f"returned {self.outcome.result()}"
            retry_error_callback=_first_set(
            retry_error_cls=_first_set(retry_error_cls, self.retry_error_cls),
            retry_exc = self.retry_error_cls(fut)
            retry=_first_set(retry, self.retry),
            return DoAttempt()
            return fut.result()
            return None
            return r.wraps(f)
            return self(f, *args, **kw)
            return self._local.statistics
            return self._local.statistics  # type: ignore[no-any-return]
            return self.copy(*args, **kwargs).wraps(f)
            return True  # Swallow exception.
            self._local.statistics = t.cast(t.Dict[str, t.Any], {})
            self.after(retry_state)
            self.before_sleep(retry_state)
            self.retry_state.set_exception((exc_type, exc_value, traceback))
            self.retry_state.set_result(None)
            sleep = 0.0
            sleep = self.wait(retry_state)
            sleep=_first_set(sleep, self.sleep),
            stop=_first_set(stop, self.stop),
            t.Optional[t.Callable[["RetryCallState"], None]], object
            t.Optional[t.Callable[["RetryCallState"], t.Any]], object
            t.Type[BaseException], BaseException, "types.TracebackType| None"
            wait=_first_set(wait, self.wait),
        """
        """Construct a new Future object."""
        """Copy this object with some parameters changed if needed."""
        """Return a dictionary of runtime statistics.
        """Return whether a exception is being held in this future."""
        """Wrap a function for retrying.
        #: Arguments of the function wrapped by this retry call
        #: Function wrapped by this retry call
        #: Keyword arguments of the function wrapped by this retry call
        #: Last outcome (result or exception) produced by the function
        #: Next action as decided by the retry manager
        #: Retry call start timestamp
        #: Retry manager object
        #: The number of the current attempt
        #: Time spent sleeping in retries
        #: Timestamp of the last outcome
        )
        **kwargs: t.Any,
        *args: t.Any,
        .. note:: The values in this dictionary are local to the thread
        .. warning:: The keys in this dictionary **should** be some what
        :param f: A function to wraps for retrying.
        @functools.wraps(f)
        ] = _unset,
        ],
        after: t.Callable[["RetryCallState"], None] = after_nothing,
        after: t.Union[t.Callable[["RetryCallState"], None], object] = _unset,
        args: t.Any,
        before: t.Callable[["RetryCallState"], None] = before_nothing,
        before: t.Union[t.Callable[["RetryCallState"], None], object] = _unset,
        before_sleep: t.Optional[t.Callable[["RetryCallState"], None]] = None,
        before_sleep: t.Union[
        cls, attempt_number: int, value: t.Any, has_exception: bool
        clsname = self.__class__.__name__
        def retry_with(*args: t.Any, **kwargs: t.Any) -> WrappedFn:
        def wrap(f: WrappedFn) -> WrappedFn:
        def wrapped_f(*args: t.Any, **kw: t.Any) -> t.Any:
        elif self.outcome.failed:
        else:
        exc_info: t.Tuple[
        exc_type: t.Optional[t.Type[BaseException]],
        exc_value: t.Optional[BaseException],
        except AttributeError:
        fn: t.Callable[..., WrappedFnReturnT],
        fn: t.Optional[WrappedFn],
        fut = cls(attempt_number)
        fut = Future(self.attempt_number)
        fut = retry_state.outcome
        fut.set_exception(exc_info[1])
        fut.set_result(val)
        if exc_type is not None and exc_value is not None:
        if fut is None:
        if has_exception:
        if not (is_explicit_retry or self.retry(retry_state)):
        if self.after is not None:
        if self.before_sleep is not None:
        if self.last_attempt.failed:
        if self.outcome is None:
        if self.outcome_timestamp is None:
        if self.stop(retry_state):
        if self.wait:
        is_explicit_retry = fut.failed and isinstance(fut.exception(), TryAgain)
        kwargs: t.Any,
        may not) have useful and/or informational keys and values when
        pass
        raise self
        ran. When it is running or has ran previously it should have (but
        reraise: bool = False,
        reraise: t.Union[bool, object] = _unset,
        retry: "RetryBaseT" = retry_if_exception_type(),
        retry: t.Union[retry_base, object] = _unset,
        retry_error_callback: t.Optional[t.Callable[["RetryCallState"], t.Any]] = None,
        retry_error_callback: t.Union[
        retry_error_cls: t.Type[RetryError] = RetryError,
        retry_error_cls: t.Union[t.Type[RetryError], object] = _unset,
        retry_object: BaseRetrying,
        retry_state = RetryCallState(retry_object=self, fn=fn, args=args, kwargs=kwargs)
        retry_state = RetryCallState(self, fn=None, args=(), kwargs={})
        retry_state.idle_for += sleep
        retry_state.next_action = RetryAction(sleep)
        return (
        return DoSleep(sleep)
        return f"{self.__class__.__name__}({state_str})"
        return f"{self.__class__.__name__}[{self.last_attempt}]"
        return f"<{clsname} {id(self)}: attempt #{self.attempt_number}; slept for {slept}; last result: {result}>"
        return fut
        return repr(self)
        return retry()(dargs[0])
        return self.__class__(
        return self.exception() is not None
        return self.outcome_timestamp - self.start_time
        return wrap
        return wrapped_f  # type: ignore[return-value]
        running is underway and/or completed.
        self,
        self, retry_state: "RetryCallState"
        self._local = threading.local()
        self.after = after
        self.args = args
        self.attempt_number += 1
        self.attempt_number = attempt_number
        self.attempt_number: int = 1
        self.before = before
        self.before_sleep = before_sleep
        self.begin()
        self.fn = fn
        self.idle_for: float = 0.0
        self.kwargs = kwargs
        self.last_attempt = last_attempt
        self.next_action = None
        self.next_action: t.Optional[RetryAction] = None
        self.outcome = None
        self.outcome, self.outcome_timestamp = fut, ts
        self.outcome: t.Optional[Future] = None
        self.outcome_timestamp = None
        self.outcome_timestamp: t.Optional[float] = None
        self.reraise = reraise
        self.retry = retry
        self.retry_error_callback = retry_error_callback
        self.retry_error_cls = retry_error_cls
        self.retry_object = retry_object
        self.retry_state = retry_state
        self.sleep = float(sleep)
        self.sleep = sleep
        self.start_time = time.monotonic()
        self.statistics.clear()
        self.statistics["attempt_number"] += 1
        self.statistics["attempt_number"] = 1
        self.statistics["delay_since_first_attempt"] = retry_state.seconds_since_start
        self.statistics["idle_for"] += sleep
        self.statistics["idle_for"] = 0
        self.statistics["start_time"] = time.monotonic()
        self.stop = stop
        self.wait = wait
        sleep: t.Callable[[t.Union[int, float]], None] = sleep,
        sleep: t.Union[t.Callable[[t.Union[int, float]], None], object] = _unset,
        slept = float(round(self.idle_for, 2))
        state_str = ", ".join(
        stop: "StopBaseT" = stop_never,
        stop: t.Union["StopBaseT", object] = _unset,
        super().__init__()
        super().__init__(last_attempt)
        This dictionary will be empty when the controller has never been
        traceback: t.Optional["types.TracebackType"],
        try:
        ts = time.monotonic()
        wait: "WaitBaseT" = wait_none(),
        wait: t.Union["WaitBaseT", object] = _unset,
        while True:
        wrapped_f.retry = self  # type: ignore[attr-defined]
        wrapped_f.retry_with = retry_with  # type: ignore[attr-defined]
    - __init__: to initialize all necessary fields
    - NAME: for identification in retry object methods and callbacks
    - REPR_FIELDS: class variable specifying attributes to include in repr(self)
    """
    """Always retry the executed function when raised."""
    """Base class for representing actions to take by retry object.
    """Encapsulates a (future or past) attempted call to a target function."""
    """Encapsulates the last attempt instance right before giving up."""
    """Manage attempt context."""
    """Retrying controller."""
    """State related to a single call wrapped with Retrying."""
    """Wrap a function with a new `Retrying` object.
    "after_log",
    "after_nothing",
    "AsyncRetrying",
    "AttemptManager",
    "BaseAction",
    "BaseRetrying",
    "before_log",
    "before_nothing",
    "before_sleep_log",
    "before_sleep_nothing",
    "DoAttempt",
    "DoSleep",
    "Future",
    "NO_RESULT",
    "retry",
    "retry_all",
    "retry_always",
    "retry_any",
    "retry_base",
    "retry_if_exception",
    "retry_if_exception_cause_type",
    "retry_if_exception_message",
    "retry_if_exception_type",
    "retry_if_not_exception_message",
    "retry_if_not_exception_type",
    "retry_if_not_result",
    "retry_if_result",
    "retry_never",
    "retry_unless_exception_type",
    "RetryAction",
    "RetryCallState",
    "RetryError",
    "Retrying",
    "sleep",
    "sleep_using_event",
    "stop_after_attempt",
    "stop_after_delay",
    "stop_all",
    "stop_any",
    "stop_never",
    "stop_when_event_set",
    "TryAgain",
    "wait_chain",
    "wait_combine",
    "wait_exponential",
    "wait_exponential_jitter",
    "wait_fixed",
    "wait_full_jitter",
    "wait_incrementing",
    "wait_none",
    "wait_random",
    "wait_random_exponential",
    "WrappedFn",
    # support both @retry and @retry() as valid syntax
    ) -> "BaseRetrying":
    ) -> "Future":
    ) -> None:
    ) -> t.Optional[bool]:
    ) -> t.Union[DoAttempt, DoSleep, t.Any]:  # noqa
    ) -> WrappedFnReturnT:
    ):
    :param dargs: positional arguments passed to Retrying object
    :param dkw: keyword arguments passed to the Retrying object
    @abstractmethod
    @classmethod
    @property
    after: t.Callable[["RetryCallState"], None] = after_nothing,
    before: t.Callable[["RetryCallState"], None] = before_nothing,
    before_sleep: t.Optional[t.Callable[["RetryCallState"], None]] = None,
    Concrete implementations must define:
    def __call__(
    def __enter__(self) -> None:
    def __exit__(
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, attempt_number: int) -> None:
    def __init__(self, last_attempt: "Future") -> None:
    def __init__(self, retry_state: "RetryCallState"):
    def __init__(self, sleep: t.SupportsFloat) -> None:
    def __iter__(self) -> t.Generator[AttemptManager, None, None]:
    def __repr__(self) -> str:
    def __str__(self) -> str:
    def begin(self) -> None:
    def construct(
    def copy(
    def failed(self) -> bool:
    def iter(
    def prepare_for_next_attempt(self) -> None:
    def reraise(self) -> "t.NoReturn":
    def seconds_since_start(self) -> t.Optional[float]:
    def set_exception(
    def set_result(self, val: t.Any) -> None:
    def statistics(self) -> t.Dict[str, t.Any]:
    def wraps(self, f: WrappedFn) -> WrappedFn:
    else:
    from .retry import RetryBaseT
    from .stop import StopBaseT
    from .wait import WaitBaseT
    from pip._vendor.tenacity.tornadoweb import TornadoRetrying
    FutureGenericT = futures.Future
    FutureGenericT = futures.Future[t.Any]
    if len(dargs) == 1 and callable(dargs[0]):
    import types
    NAME = "retry"
    NAME: t.Optional[str] = None
    pass
    REPR_FIELDS = ("sleep",)
    REPR_FIELDS: t.Sequence[str] = ()
    reraise: bool = False,
    retry: "RetryBaseT" = retry_if_exception_type(),
    retry_error_callback: t.Optional[t.Callable[["RetryCallState"], t.Any]] = None,
    retry_error_cls: t.Type["RetryError"] = RetryError,
    return second if first is _unset else first
    sleep: t.Callable[[t.Union[int, float]], None] = sleep,
    stop: "StopBaseT" = stop_never,
    wait: "WaitBaseT" = wait_none(),
#
# Copyright 2013-2014 Ray Holder
# Copyright 2016 Étienne Bersac
# Copyright 2016 Joshua Harlow
# Copyright 2016-2018 Julien Danjou
# Copyright 2017 Elisey Zanko
# distributed under the License is distributed on an "AS IS" BASIS,
# http://www.apache.org/licenses/LICENSE-2.0
# if an old version is found.
# If tornado is non-None, tenacity will attempt to execute some code
# Import all built-in after strategies for easier usage.
# Import all built-in before strategies for easier usage.
# Import all built-in retry strategies for easier usage.
# Import all built-in stop strategies for easier usage.
# Import all built-in wait strategies for easier usage.
# Import all nap strategies for easier usage.
# Licensed under the Apache License, Version 2.0 (the "License");
# limitations under the License.
# not attempt to use tornado even if it is present in the environment.
# Replace a conditional import with a hard-coded None so that pip does
# See the License for the specific language governing permissions and
# that is sensitive to the version of tornado, which could break pip
# Unless required by applicable law or agreed to in writing, software
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
) -> t.Callable[[WrappedFn], WrappedFn]: ...
@t.overload
]
__all__ = [
_unset = object()
class AttemptManager:
class BaseAction:
class BaseRetrying:
class DoAttempt:
class DoSleep:
class Future:
class RetryAction:
class RetryCallState:
class RetryError:
class Retrying:
class TryAgain:
def _first_set(first: t.Union[t.Any, object], second: t.Any) -> t.Any:
def retry(
def retry(*dargs: t.Any, **dkw: t.Any) -> t.Any:
def retry(func: WrappedFn) -> WrappedFn: ...
else:
from .after import after_log  # noqa
from .after import after_nothing  # noqa
from .before import before_log  # noqa
from .before import before_nothing  # noqa
from .before_sleep import before_sleep_log  # noqa
from .before_sleep import before_sleep_nothing  # noqa
from .nap import sleep  # noqa
from .nap import sleep_using_event  # noqa
from .retry import retry_all  # noqa
from .retry import retry_always  # noqa
from .retry import retry_any  # noqa
from .retry import retry_base  # noqa
from .retry import retry_if_exception  # noqa
from .retry import retry_if_exception_cause_type  # noqa
from .retry import retry_if_exception_message  # noqa
from .retry import retry_if_exception_type  # noqa
from .retry import retry_if_not_exception_message  # noqa
from .retry import retry_if_not_exception_type  # noqa
from .retry import retry_if_not_result  # noqa
from .retry import retry_if_result  # noqa
from .retry import retry_never  # noqa
from .retry import retry_unless_exception_type  # noqa
from .stop import stop_after_attempt  # noqa
from .stop import stop_after_delay  # noqa
from .stop import stop_all  # noqa
from .stop import stop_any  # noqa
from .stop import stop_never  # noqa
from .stop import stop_when_event_set  # noqa
from .wait import wait_chain  # noqa
from .wait import wait_combine  # noqa
from .wait import wait_exponential  # noqa
from .wait import wait_exponential_jitter  # noqa
from .wait import wait_fixed  # noqa
from .wait import wait_incrementing  # noqa
from .wait import wait_none  # noqa
from .wait import wait_random  # noqa
from .wait import wait_random_exponential  # noqa
from .wait import wait_random_exponential as wait_full_jitter  # noqa
from abc import abstractmethod
from concurrent import futures
from inspect import iscoroutinefunction
from pip._vendor.tenacity._asyncio import AsyncRetrying  # noqa:E402,I100
if sys.version_info[1] >= 9:
if t.TYPE_CHECKING:
if tornado:
import functools
import sys
import threading
import time
import typing as t
import warnings
NO_RESULT = object()
tornado = None  # type: ignore
WrappedFn = t.TypeVar("WrappedFn", bound=t.Callable[..., t.Any])
WrappedFnReturnT = t.TypeVar("WrappedFnReturnT")
