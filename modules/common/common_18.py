
    -----
    ------
    -------
    --------
    ----------
                    #  test_loc_getitem_list_of_labels_categoricalindex_with_na
                    # Don't raise on e.g. ["A", "B", np.nan], see
                    raise ValueError(na_msg)
                # GH#42461 cython will raise TypeError if we pass a subclass
                if lib.is_bool_array(key_array, skipna=True):
                key = list(key)
                na_msg = "Cannot mask with non-boolean array containing NA / NaN values"
                name = None
                return False
                warnings.simplefilter("ignore", np.VisibleDeprecationWarning)
            "a numpy RandomState, or None"
            "does not match length of index "
            "Indexing with a float is no longer supported. Manually convert "
            "Length of values "
            "random_state must be an integer, array-like, a BitGenerator, Generator, "
            "to an integer key instead."
            # Can remove warning filter once NumPy 1.24 is min version
            # GH#34193
            f"({len(data)}) "
            f"({len(index)})"
            if not lib.is_bool_array(key_array):
            if not np_version_gte1p24:
            if obj.name != name:
            if type(key) is not list:  # noqa: E721
            key_array = np.asarray(key)
            labels = [labels]
            labels = list(labels)
            msg = f"{target} is both the pipe target and a keyword argument"
            name = None
            raise ValueError(msg)
            result = np.asarray(values, dtype=dtype)
            return lib.is_bool_list(key)
            return mapper[x]
            return partial(defaultdict, into.default_factory)
            return True
            return x
            setattr(obj, attr, old_value)
            yield element
            yield from flatten(element)
        # Avoid building an array of arrays:
        # check if np.array(key).dtype would be bool
        # error: Argument 1 to "construct_1d_object_array_from_listlike"
        # has incompatible type "Iterable[Any]"; expected "Sized"
        # over each element
        # Using try/except since it's more performant than checking is_list_like
        )
        ``(callable, data_keyword)`` tuple where ``data_keyword`` is a
        a callable object that can accept an iterator to create
        A dictionary of keyword arguments passed into ``func``.
        All other types are not considered a boolean indexer.
        and contains missing values.
        and convert to an ndarray.
        and obj.start == 0
        and obj.start == obj.stop
        and obj.start is None
        and obj.start is not None
        and obj.step is None
        and obj.stop == line
        and obj.stop is None
        and obj.stop is not None
        AnyArrayLike,
        ArrayLike,
        Attribute to modify.
        conditionally use this context manager.
        Default None.
        elif is_bool_dtype(key.dtype):
        else:
        except TypeError:  # non-iterable
        except ValueError:
        For array-like input, boolean ndarrays or ExtensionArrays
        func, target = func
        Function to apply to this object or, alternatively, a
        if condition:
        if isinstance(into, defaultdict):
        if iterable_not_string(element):
        if key.dtype == np.object_:
        if len(key) > 0:
        If receives `None`, returns np.random.
        If receives an int, array-like, or BitGenerator, passes to
        If receives an np.random RandomState or Generator, just returns that unchanged.
        If receives anything else, raises an informative ValueError.
        If specified, use as dtype of the resulting array, otherwise infer.
        if target in kwargs:
        if x in mapper:
        into = type(into)
        isinstance(obj, slice)
        key, (ABCSeries, np.ndarray, ABCIndex, ABCExtensionArray)
        kwargs[target] = obj
        labels = [labels]
        list of column names or None values.
        list of column names with the None values replaced.
        Must be a class, an initialized collections.defaultdict,
        np.random.RandomState() as seed.
        NpDtype,
        Object whose attribute will be modified.
        object.
        old_value = getattr(obj, attr)
        Only list-likes may be considered boolean indexers.
        or an instance of a collections.abc.Mapping subclass.
        Positional arguments passed into ``func``.
        raise IndexError(
        raise TypeError("to_dict() only accepts initialized defaultdicts")
        raise TypeError(f"unsupported type: {into}")
        raise ValueError(
        RandomState,
        result = construct_1d_object_array_from_listlike(values)
        result = np.asarray(values, dtype=object)
        return [obj]
        return construct_1d_object_array_from_listlike(values)
        return construct_1d_object_array_from_listlike(values)  # type: ignore[arg-type]
        return func(*args, **kwargs)
        return func(obj, *args, **kwargs)
        return get_callable_name(obj.func)
        return getattr(obj, "__name__")
        return list(obj)
        return list(values)
        return maybe_callable(obj, **kwargs)
        return np.random
        return np.random.RandomState(state)
        return state
        return type(obj).__name__
        return values
        return values._values
        setattr(obj, attr, value)
        string indicating the keyword of ``callable`` that expects the
        T,
        the desired Mapping.
        The non string sequence to flatten
        try:
        Value to temporarily set attribute to.
        values = [tuple(x) for x in values]
        values = list(values)
        When the array is an object-dtype ndarray or ExtensionArray
        Whether `key` is a valid boolean indexer.
        Whether to set the attribute. Provided in order to not have to
        with ``_is_boolean`` set are considered boolean indexers.
        with warnings.catch_warnings():
        yield obj
    """
    # assumes lib.is_scalar(val)
    # distinguishing between no name and a name of ''
    # everything failed (probably because the argument
    # ExtensionArray can only be returned when values is an Index, all other iterables
    # fall back to class name
    # instead of the empty string in this case to allow
    # signature, so instead we special-case some common types.
    # some objects don't; could recurse
    # typical case has name
    # wasn't actually callable); we return None
    # will return np.ndarray. Unfortunately "all other" cannot be encoded in a type
    )
    ) and not isinstance(key, ABCMultiIndex):
    **kwargs
    **kwargs : dict, optional
    *args : iterable, optional
    .. versionadded:: 1.4.0
    ...
    abc,
    ABCExtensionArray,
    ABCIndex,
    ABCMultiIndex,
    ABCSeries,
    Any,
    Apply a function ``func`` to object ``obj`` either by passing obj as the
    array
    attr : str
    bool
    builtins.max: "max",
    builtins.max: "np.maximum.reduce",
    builtins.max: np.maximum.reduce,
    builtins.min: "min",
    builtins.min: "np.minimum.reduce",
    builtins.min: np.minimum.reduce,
    builtins.sum: "np.sum",
    builtins.sum: "sum",
    builtins.sum: np.sum,
    Callable,
    cast,
    Check the length of data matches the length of the index.
    Check whether `key` is a valid boolean indexer.
    check_array_indexer : Check that `key` is a valid array to index,
    Collection,
    condition : bool, default True
    Convert list-like or scalar input to list-like. List, numpy and pandas array-like
    DataFrame.to_dict
    def f(x):
    defaultdict,
    Disallow indexing with a float key, even if that key is a round number.
    dtype : dtype
    element of the tuple.
    elif isinstance(key, list):
    elif isinstance(state, np.random.Generator):
    elif isinstance(state, np.random.RandomState):
    elif isinstance(values, abc.Iterable) and not isinstance(values, str):
    elif isinstance(values, ABCIndex):
    elif isinstance(values, ABCSeries):
    elif state is None:
    else:
    Evaluate possibly callable input using obj and kwargs if it is callable,
    except ValueError:
    finally:
    Find non-trivial slices in "line": return a list of booleans with same length.
    first argument to the function or, in the case that the func is a tuple,
    Flatten an arbitrarily nested sequence.
    flattened : generator
    for element in line:
    for obj in objs[1:]:
    from pandas import Index
    from pandas._typing import (
    func : callable or tuple of (callable, str)
    Generator,
    Hashable,
    Helper function for processing random_state arguments.
    Helper function to standardize a supplied mapping.
    If a name is missing then replace it by level_n, where n is the count
    if callable(maybe_callable):
    if callable(obj):
    if condition:
    if hasattr(obj, "__name__"):
    if into == defaultdict:
    if is_integer(state) or isinstance(state, (np.ndarray, np.random.BitGenerator)):
    if isinstance(
    if isinstance(func, tuple):
    if isinstance(labels, (str, tuple)):
    if isinstance(obj, abc.Iterable) and not isinstance(obj, abc.Sized):
    if isinstance(obj, partial):
    if isinstance(values, (list, np.ndarray, ABCIndex, ABCSeries, ABCExtensionArray)):
    if isinstance(values, list) and dtype in [np.object_, object]:
    if issubclass(result.dtype.type, str):
    if len(data) != len(index):
    if lib.is_float(val) and val.is_integer():
    if not (isinstance(values, (list, tuple)) or hasattr(values, "__array__")):
    if not inspect.isclass(into):
    if not isinstance(labels, (list, np.ndarray)):
    if not issubclass(into, abc.Mapping):
    If obj is Iterable but not list-like, consume into list.
    if obj is not None and not isinstance(obj, (tuple, list)):
    if result.ndim == 2:
    if we define a builtin function for this argument, return it,
    if we define an internal function for this argument, return it
    inputs are returned unmodified whereas others are converted to list.
    interpret the first element of the tuple as a function and pass the obj to
    into : instance or subclass of collections.abc.Mapping
    is a dict, Series or just a function.
    is_bool_dtype,
    is_integer,
    Iterable,
    key : Any
    labels = asarray_tuplesafe(labels, dtype=dtype)
    labels: np.ndarray | Iterable, dtype: NpDtype | None = None
    line : sequence
    list
    mapping : a collections.abc.Mapping subclass or other constructor
    maybe_callable : possibly a callable
    name = objs[0].name
    names : list-like
    Notes
    np.all: "all",
    np.any: "any",
    np.cumprod: "cumprod",
    np.cumsum: "cumsum",
    np.max: "max",
    np.mean: "mean",
    np.median: "median",
    np.min: "min",
    np.nancumprod: "cumprod",
    np.nancumsum: "cumsum",
    np.nanmax: "max",
    np.nanmean: "mean",
    np.nanmedian: "median",
    np.nanmin: "min",
    np.nanprod: "prod",
    np.nanstd: "std",
    np.nansum: "sum",
    np.nanvar: "var",
    np.prod: "prod",
    np.random.RandomState or np.random.Generator. If state is None, returns np.random
    np.std: "std",
    np.sum: "sum",
    np.var: "var",
    obj : NDFrame
    obj : object
    obj = cast(Collection, obj)
    obj, func: Callable[..., T] | tuple[Callable[..., T], str], *args, **kwargs
    object : obj with modified attribute.
    object : the return type of ``func``.
    otherwise return as it is.
    otherwise return the arg
    outval : scalar
    overload,
    Parameters
    Raises
    return (
    return (arg for arg in args if arg is not None)
    return [f"level_{i}" if name is None else name for i, name in enumerate(names)]
    return [isinstance(k, slice) and not is_null_slice(k) for k in line]
    return [values]
    return _builtin_table.get(arg, arg)
    return _cython_table.get(arg)
    return all(arg is None for arg in args)
    return all(arg is not None for arg in args)
    return any(arg is None for arg in args)
    return any(arg is not None for arg in args)
    return f if isinstance(mapper, (abc.Mapping, ABCSeries)) else mapper
    return False
    return into
    return labels
    return maybe_callable
    return name
    return None
    return obj
    return result
    return sum(x is not None for x in args)
    return val
    Returns
    Returns a boolean indicating if all arguments are None.
    Returns a boolean indicating if all arguments are not None.
    Returns a boolean indicating if any argument is None.
    Returns a boolean indicating if any argument is not None.
    Returns a function that will map names/labels, dependent if mapper
    Returns a generator consisting of the arguments that are not None.
    Returns the count of arguments that are not None.
    See Also
    Sequence,
    Series.to_dict
    state : int, array-like, BitGenerator, Generator, np.random.RandomState, None.
    state: int | np.ndarray | np.random.BitGenerator | np.random.RandomState | None,
    Temporarily set attribute on an object.
    that function as a keyword argument whose key is the value of the second
    This doesn't consider strings sequences.
    Transform label or iterable of labels to array, for use in Index.
    try:
    TYPE_CHECKING,
    val : scalar
    value : Any
    ValueError
    values: ArrayLike | list | tuple | zip, dtype: NpDtype | None = ...
    values: Hashable | Iterable | AnyArrayLike,
    We have a full length slice.
    We have a null slice.
    We have an empty slice, e.g. no values are selected.
    Yields
"""
#  default to axis=None.
#  whereas np.min and np.max (which directly call obj.min and obj.max)
# -*- coding: utf-8 -*-
# GH#53425: Only for deprecation
# the ufuncs np.maximum.reduce and np.minimum.reduce default to axis=0,
# TODO: used only once in indexing; belongs elsewhere?
)
) -> list | AnyArrayLike:
) -> np.ndarray:
) -> np.random.RandomState: ...
) -> T:
@contextlib.contextmanager
@overload
_builtin_table = {
_builtin_table_alias = {
_cython_table = {
}
def all_none(*args) -> bool:
def all_not_none(*args) -> bool:
def any_none(*args) -> bool:
def any_not_none(*args) -> bool:
def apply_if_callable(maybe_callable, obj, **kwargs):
def asarray_tuplesafe(
def asarray_tuplesafe(values: Iterable, dtype: NpDtype | None = ...) -> ArrayLike: ...
def asarray_tuplesafe(values: Iterable, dtype: NpDtype | None = None) -> ArrayLike:
def cast_scalar_indexer(val):
def consensus_name_attr(objs):
def convert_to_list_like(
def count_not_none(*args) -> int:
def fill_missing_names(names: Sequence[Hashable | None]) -> list[Hashable]:
def flatten(line):
def get_callable_name(obj):
def get_cython_func(arg: Callable) -> str | None:
def get_rename_function(mapper):
def index_labels_to_array(
def is_bool_indexer(key: Any) -> bool:
def is_builtin_func(arg):
def is_empty_slice(obj) -> bool:
def is_full_slice(obj, line: int) -> bool:
def is_null_slice(obj) -> bool:
def is_true_slices(line) -> list[bool]:
def maybe_iterable_to_list(obj: Iterable[T] | T) -> Collection[T] | T:
def maybe_make_list(obj):
def not_none(*args):
def pipe(
def random_state(
def random_state(state: np.random.Generator) -> np.random.Generator: ...
def random_state(state: RandomState | None = None):
def require_length_match(data, index: Index) -> None:
def standardize_mapping(into):
def temp_setattr(obj, attr: str, value, condition: bool = True) -> Generator[None]:
from __future__ import annotations
from collections import (
from collections.abc import (
from functools import partial
from pandas._libs import lib
from pandas.compat.numpy import np_version_gte1p24
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike
from pandas.core.dtypes.common import (
from pandas.core.dtypes.generic import (
from pandas.core.dtypes.inference import iterable_not_string
from typing import (
if TYPE_CHECKING:
import builtins
import contextlib
import inspect
import numpy as np
import warnings
Misc tools for implementing data structures
Note: pandas.core.common is *not* part of the public API.
