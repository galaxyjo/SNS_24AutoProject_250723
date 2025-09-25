# modules/common/common_35.py (디버깅 후 전체 스크립트)

from __future__ import annotations
import builtins
import contextlib
import inspect
import numpy as np
import warnings
from collections import defaultdict
from collections.abc import Iterable, Collection
from functools import partial
from typing import Any, Callable, Generator, Hashable, Sequence, overload, TYPE_CHECKING

from pandas import Index
from pandas.compat.numpy import np_version_gte1p24
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike
from pandas.core.dtypes.common import is_bool_dtype, is_integer
from pandas.core.dtypes.generic import ABCSeries, ABCIndex, ABCExtensionArray, ABCMultiIndex
from pandas.core.dtypes.inference import iterable_not_string
from pandas._libs import lib

def all_none(*args) -> bool:
    return all(x is None for x in args)

def all_not_none(*args) -> bool:
    return all(x is not None for x in args)

def any_none(*args) -> bool:
    return any(x is None for x in args)

def any_not_none(*args) -> bool:
    return any(x is not None for x in args)

def apply_if_callable(maybe_callable, obj, **kwargs):
    if callable(maybe_callable):
        return maybe_callable(obj, **kwargs)
    return obj

def cast_scalar_indexer(val):
    if isinstance(val, (int, np.integer)):
        return int(val)
    return val

def convert_to_list_like(obj):
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    if isinstance(obj, (tuple, set, np.ndarray, Index)):
        return list(obj)
    return [obj]

def flatten(line):
    for el in line:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def is_bool_indexer(key: Any) -> bool:
    if isinstance(key, np.ndarray):
        return key.dtype == bool
    if isinstance(key, (list, tuple)):
        return all(isinstance(k, bool) for k in key)
    return False

def pipe(obj, func: Callable[..., Any], *args, **kwargs):
    return func(obj, *args, **kwargs)

def random_state(state: np.random.Generator | int | None) -> np.random.Generator:
    if isinstance(state, np.random.Generator):
        return state
    if state is None:
        return np.random.default_rng()
    return np.random.default_rng(state)

@contextlib.contextmanager
def temp_setattr(obj, attr: str, value, condition: bool = True) -> Generator[None]:
    if condition:
        old = getattr(obj, attr)
        setattr(obj, attr, value)
        try:
            yield
        finally:
            setattr(obj, attr, old)
    else:
        yield
