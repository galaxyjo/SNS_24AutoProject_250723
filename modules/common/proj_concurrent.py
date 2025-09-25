# modules/common/proj_concurrent.py
from contextlib import contextmanager
from operator import length_hint
from os import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tqdm import tqdm as tqdm_auto  # ✅ fixed: direct import from tqdm
from tqdm.std import TqdmWarning
import warnings

__all__ = ["thread_map", "process_map"]
__author__ = {"github.com/": ["casperdcl"]}


@contextmanager
def ensure_lock(tqdm_class, lock_name=""):
    old_lock = getattr(tqdm_class, "_lock", None)
    lock = getattr(old_lock, lock_name, old_lock) if old_lock else None
    if lock is None:
        lock = tqdm_class.get_lock()
    tqdm_class.set_lock(lock)
    yield lock
    del tqdm_class._lock


def _executor_map(PoolExecutor, fn, *iterables, **tqdm_kwargs):
    chunksize = tqdm_kwargs.pop("chunksize", 1)
    lock_name = tqdm_kwargs.pop("lock_name", "")
    max_workers = tqdm_kwargs.pop("max_workers", min(32, cpu_count() + 4))
    tqdm_class = tqdm_kwargs.pop("tqdm_class", tqdm_auto)

    if iterables and length_hint(iterables[0]) > 1000 and "chunksize" not in tqdm_kwargs:
        warnings.warn(
            "Iterable length > 1000 but `chunksize` is not set. "
            "Set `chunksize=1` or more. This may seriously degrade multiprocess performance.",
            TqdmWarning,
            stacklevel=2,
        )

    with ensure_lock(tqdm_class, lock_name=lock_name) as lk:
        if PoolExecutor is ThreadPoolExecutor:
            with PoolExecutor(
                max_workers=max_workers,
                initializer=tqdm_class.set_lock,
                initargs=(lk,),
            ) as ex:
                return list(ex.map(fn, *iterables, chunksize=chunksize, **tqdm_kwargs))
        else:
            # ProcessPoolExecutor: cannot pickle RLock, so skip initializer
            with PoolExecutor(max_workers=max_workers) as ex:
                return list(ex.map(fn, *iterables, chunksize=chunksize, **tqdm_kwargs))


def thread_map(fn, *iterables, **tqdm_kwargs):
    return _executor_map(ThreadPoolExecutor, fn, *iterables, **tqdm_kwargs)


def process_map(fn, *iterables, **tqdm_kwargs):
    return _executor_map(ProcessPoolExecutor, fn, *iterables, **tqdm_kwargs)
