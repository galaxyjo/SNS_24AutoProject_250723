
    ----------
                " Set `chunksize=1` or more." % longest_iterable_len,
                " This may seriously degrade multiprocess performance."
                "Iterable length %d > 1000 but `chunksize` is not set."
                stacklevel=2,
                tqdm_class(ex.map(fn, *iterables, chunksize=chunksize), **kwargs)
                TqdmWarning,
            )
            from warnings import warn
            max_workers=max_workers, initializer=tqdm_class.set_lock, initargs=(lk,)
            return list(
            warn(
        # (most time spent dispatching items to workers).
        # default `chunksize=1` has poor performance for large iterables
        # share lock in case workers are already using `tqdm`
        ) as ex:
        [default: max(32, cpu_count() + 4)].
        [default: min(32, cpu_count() + 4)].
        `concurrent.futures.ProcessPoolExecutor.__init__`.
        `concurrent.futures.ProcessPoolExecutor.map`. [default: 1].
        `concurrent.futures.ThreadPoolExecutor.__init__`.
        `tqdm` class to use for bars [default: tqdm.auto.tqdm].
        del tqdm_class._lock
        if longest_iterable_len > 1000:
        kwargs["total"] = length_hint(iterables[0])
        longest_iterable_len = max(map(length_hint, iterables))
        Maximum number of workers to spawn; passed to
        Member of `tqdm_class.get_lock()` to use [default: mp_lock].
        Size of chunks sent to worker processes; passed to
        tqdm_class.set_lock(old_lock)
        tqdm_kwargs = tqdm_kwargs.copy()
        tqdm_kwargs["lock_name"] = "mp_lock"
        with PoolExecutor(
    """
    """get (create if necessary) and then restore `tqdm_class`'s lock"""
    chunksize  : [default: 1].
    chunksize  : int, optional
    chunksize = kwargs.pop("chunksize", 1)
    driven by `concurrent.futures.ProcessPoolExecutor`.
    driven by `concurrent.futures.ThreadPoolExecutor`.
    else:
    Equivalent of `list(map(fn, *iterables))`
    from concurrent.futures import ProcessPoolExecutor
    from concurrent.futures import ThreadPoolExecutor
    if "lock_name" not in tqdm_kwargs:
    if "total" not in kwargs:
    if iterables and "chunksize" not in tqdm_kwargs:
    if old_lock is None:
    Implementation of `thread_map` and `process_map`.
    kwargs = tqdm_kwargs.copy()
    lock = getattr(lock, lock_name, lock)  # maybe subtype
    lock = old_lock or tqdm_class.get_lock()  # maybe create a new lock
    lock_name  : [default: "":str].
    lock_name  : str, optional
    lock_name = kwargs.pop("lock_name", "")
    max_workers  : [default: min(32, cpu_count() + 4)].
    max_workers  : int, optional
    max_workers = kwargs.pop("max_workers", min(32, cpu_count() + 4))
    old_lock = getattr(tqdm_class, "_lock", None)  # don't create a new lock
    Parameters
    return _executor_map(ProcessPoolExecutor, fn, *iterables, **tqdm_kwargs)
    return _executor_map(ThreadPoolExecutor, fn, *iterables, **tqdm_kwargs)
    tqdm_class  : [default: tqdm.auto.tqdm].
    tqdm_class  : optional
    tqdm_class = kwargs.pop("tqdm_class", tqdm_auto)
    tqdm_class.set_lock(lock)
    with ensure_lock(tqdm_class, lock_name=lock_name) as lk:
    yield lock
"""
# -*- coding: utf-8 -*-
@contextmanager
__all__ = ["thread_map", "process_map"]
__author__ = {"github.com/": ["casperdcl"]}
def _executor_map(PoolExecutor, fn, *iterables, **tqdm_kwargs):
def ensure_lock(tqdm_class, lock_name=""):
def process_map(fn, *iterables, **tqdm_kwargs):
def thread_map(fn, *iterables, **tqdm_kwargs):
from ..auto import tqdm as tqdm_auto
from ..std import TqdmWarning
from contextlib import contextmanager
from operator import length_hint
from os import cpu_count
Thin wrappers around `concurrent.futures`.
