
    -------
    ----------
            #  not a single-column, in order to operate against non-DataFrame
            #  single-row special cases in datetime arithmetic
            #  vectors of the same length. But convert to two rows to avoid
            # for vector operations, we need a DataFrame to be a single-row,
            # pd.array would return an IntegerArray
            # type: ignore[attr-defined]
            (ndframe, func, expected)
            and is_string_dtype(right.dtype)
            and right.dtype.storage in ("pyarrow", "pyarrow_numpy")
            expected = expected.T
            expected = Index(expected)
            expected = NumpyExtensionArray(np.asarray(expected._values))
            expected = pd.array(expected, copy=False)
            expected = pd.concat([expected] * 2, ignore_index=True)
            expected = Series(expected)
            expected = Series(expected).to_frame()
            for func, name in cython_table
            if name == func_name
            isinstance(right, ExtensionArray)
            left._mask, right._mask
            left_buf1 = left_pa_data.chunk(0).buffers()[1]
            left_pa_data = left._pa_array
            return left_buf1 == right_buf1
            right = cast("ArrowExtensionArray", right)
            right_buf1 = right_pa_data.chunk(0).buffers()[1]
            right_pa_data = right._pa_array
            warnings.filterwarnings("ignore", "Dtype inference", category=FutureWarning)
        "as",
        "D",
        "fs",
        "h",
        "M",
        "m",
        "ms",
        "ns",
        "ps",
        "s",
        "us",
        "W",
        "Y",
        #  the _data or the _mask
        # Assume it is the reverse operator
        # By convention, we'll say these share memory if they share *either*
        # Call with reversed args to get to unpacking logic below.
        # ensure we don't rely on the property returning a class
        # For testing, those properties return a generic callable, and not
        # https://github.com/pandas-dev/pandas/issues/32638 and linked issues
        # https://github.com/pandas-dev/pandas/pull/43930#discussion_r736862669
        # See https://github.com/pandas-dev/pandas/pull/46018 and
        # the actual class. In this case that is equivalent, but it is to
        # type: ignore[attr-defined]
        )
        ):
        ]
        + BINARY_PYARROW_DTYPES
        + BOOL_PYARROW_DTYPES
        + DATE_PYARROW_DTYPES
        + DATETIME_PYARROW_DTYPES
        + DECIMAL_PYARROW_DTYPES
        + FLOAT_PYARROW_DTYPES
        + STRING_PYARROW_DTYPES
        + TIME_PYARROW_DTYPES
        + TIMEDELTA_PYARROW_DTYPES
        A function performing the operation.
        ALL_INT_PYARROW_DTYPES
        ALL_INT_PYARROW_DTYPES_STR_REPR + FLOAT_PYARROW_DTYPES_STR_REPR
        and is_string_dtype(left.dtype)
        and left.dtype.storage in ("pyarrow", "pyarrow_numpy")
        arr = left._mgr.arrays[0]
        def op(x, y): return rop(y, x)
        Dtype,
        Each element represents the row of csv.
        else:
        expected = np.array(expected)
        expected = to_array(expected)
        Expected error to raise.
        Expected output of to_csv() in current OS.
        for tz in [None, "UTC", "US/Pacific", "US/Eastern"]
        for unit in ["s", "ms", "us", "ns"]
        if (
        if isinstance(expected, RangeIndex):
        if transpose:
        isinstance(left, ExtensionArray)
        left = cast("ArrowExtensionArray", left)
        List of three items (DataFrame, function, expected result)
        NpDtype,
        op = getattr(operator, short_opname)
        pa.time32("ms"),
        pa.time32("s"),
        pa.time64("ns"),
        pa.time64("us"),
        pa.timestamp(unit=unit, tz=tz)
        raise NotImplementedError(box_cls)
        Regular `pytest.raises` function with `match` equal to `None`.
        results += [
        results.append((ndframe, func_name, expected))
        return False
        return lambda *args, **kwargs: SubclassedDataFrame(*args, **kwargs)
        return lambda *args, **kwargs: SubclassedSeries(*args, **kwargs)
        return left
        return np.asarray(obj)
        return np.shares_memory(left, right)
        return np.shares_memory(left._data, right._data) or np.shares_memory(
        return shares_memory(arr, right)
        return shares_memory(left._codes, right)
        return shares_memory(left._left, right) or shares_memory(left._right, right)
        return shares_memory(left._ndarray, right)
        return shares_memory(left._values, right)
        return shares_memory(left.sp_values, right)
        return shares_memory(right, left)
        rop = getattr(operator, short_opname[1:])
        str(ArrowDtype(typ)) for typ in ALL_INT_PYARROW_DTYPES
        str(ArrowDtype(typ)) for typ in FLOAT_PYARROW_DTYPES
        The first item is a name of a NDFrame method ('sum', 'prod') etc.
        The op name, in form of "add" or "__add__".
        The second item is the expected return value.
        with warnings.catch_warnings():
    """
    "__add__",
    "__floordiv__",
    "__mod__",
    "__mul__",
    "__pow__",
    "__radd__",
    "__rfloordiv__",
    "__rmod__",
    "__rmul__",
    "__rpow__",
    "__rsub__",
    "__rtruediv__",
    "__sub__",
    "__truediv__",
    "ALL_INT_EA_DTYPES",
    "ALL_INT_NUMPY_DTYPES",
    "ALL_NUMPY_DTYPES",
    "ALL_REAL_NUMPY_DTYPES",
    "assert_almost_equal",
    "assert_attr_equal",
    "assert_categorical_equal",
    "assert_class_equal",
    "assert_contains_all",
    "assert_copy",
    "assert_cow_warning",
    "assert_datetime_array_equal",
    "assert_dict_equal",
    "assert_equal",
    "assert_extension_array_equal",
    "assert_frame_equal",
    "assert_index_equal",
    "assert_indexing_slices_equivalent",
    "assert_interval_array_equal",
    "assert_is_sorted",
    "assert_is_valid_plot_return_object",
    "assert_metadata_equivalent",
    "assert_numpy_array_equal",
    "assert_period_array_equal",
    "assert_produces_warning",
    "assert_series_equal",
    "assert_sp_array_equal",
    "assert_timedelta_array_equal",
    "at",
    "BOOL_DTYPES",
    "box_expected",
    "BYTES_DTYPES",
    "can_set_locale",
    "COMPLEX_DTYPES",
    "convert_rows_list_to_csv_str",
    "DATETIME64_DTYPES",
    "decompress_file",
    "ENDIAN",
    "ensure_clean",
    "external_error_raised",
    "FLOAT_EA_DTYPES",
    "FLOAT_NUMPY_DTYPES",
    "get_cython_table_params",
    "get_dtype",
    "get_finest_unit",
    "get_locales",
    "get_obj",
    "get_op_from_name",
    "getitem",
    "iat",
    "iloc",
    "loc",
    "maybe_produces_warning",
    "NARROW_NP_DTYPES",
    "NP_NAT_OBJECTS",
    "NULL_OBJECTS",
    "OBJECT_DTYPES",
    "raise_assert_detail",
    "raises_chained_assignment_error",
    "round_trip_localpath",
    "round_trip_pathlib",
    "round_trip_pickle",
    "set_locale",
    "set_timezone",
    "setitem",
    "shares_memory",
    "SIGNED_INT_EA_DTYPES",
    "SIGNED_INT_NUMPY_DTYPES",
    "STRING_DTYPES",
    "SubclassedDataFrame",
    "SubclassedSeries",
    "TIMEDELTA64_DTYPES",
    "to_array",
    "UNSIGNED_INT_EA_DTYPES",
    "UNSIGNED_INT_NUMPY_DTYPES",
    "use_numexpr",
    "with_csv_dialect",
    "write_to_compressed",
    #  https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions
    # https://github.com/apache/arrow/blob/master/python/pyarrow/src/arrow/python/helpers.cc#L86
    # pa.float16 doesn't seem supported
    # temporary implementation until we get pd.array in place
    # TODO: Add container like pyarrow types:
    )
    ):
    @property
    ]
    _metadata = ["testattr", "name"]
    _metadata = ["testattr"]
    + BOOL_DTYPES
    + BYTES_DTYPES
    + COMPLEX_DTYPES
    + DATETIME64_DTYPES
    + OBJECT_DTYPES
    + STRING_DTYPES
    + TIMEDELTA64_DTYPES
    ALL_INT_PYARROW_DTYPES = UNSIGNED_INT_PYARROW_DTYPES + SIGNED_INT_PYARROW_DTYPES
    ALL_INT_PYARROW_DTYPES_STR_REPR = [
    ALL_INT_PYARROW_DTYPES_STR_REPR = []
    ALL_PYARROW_DTYPES = (
    ALL_PYARROW_DTYPES = []
    ALL_REAL_NUMPY_DTYPES
    ALL_REAL_PYARROW_DTYPES_STR_REPR = (
    ALL_REAL_PYARROW_DTYPES_STR_REPR = []
    ArrowDtype,
    assert_almost_equal,
    assert_attr_equal,
    assert_categorical_equal,
    assert_class_equal,
    assert_contains_all,
    assert_copy,
    assert_cow_warning,
    assert_datetime_array_equal,
    assert_dict_equal,
    assert_equal,
    assert_extension_array_equal,
    assert_frame_equal,
    assert_index_equal,
    assert_indexing_slices_equivalent,
    assert_interval_array_equal,
    assert_is_sorted,
    assert_is_valid_plot_return_object,
    assert_metadata_equivalent,
    assert_numpy_array_equal,
    assert_period_array_equal,
    assert_produces_warning,
    assert_series_equal,
    assert_sp_array_equal,
    assert_timedelta_array_equal,
    BaseMaskedArray,
    BINARY_PYARROW_DTYPES = [pa.binary()]
    bool,
    BOOL_PYARROW_DTYPES = [pa.bool_()]
    box_cls : {Index, Series, DataFrame}
    bytearray,
    bytes,
    Callable
    Callable,
    can_set_locale,
    cast,
    cls("NaT", unit)
    Combine frame, functions from com._cython_table
    complex,
    ContextManager,
    Convert list of CSV rows to single CSV-formatted string for current OS.
    DataFrame,
    DATE_PYARROW_DTYPES = [pa.date32(), pa.date64()]
    DATETIME_PYARROW_DTYPES = [
    DECIMAL_PYARROW_DTYPES = [pa.decimal128(7, 3)]
    decompress_file,
    def __init__(self, *args, **kwargs): pass
    def _constructor(self):
    def _constructor_expanddim(self):
    def _constructor_sliced(self):
    dict,
    dtype = getattr(obj, "dtype", None)
    elif box_cls is DataFrame:
    elif box_cls is Index:
    elif box_cls is np.ndarray or box_cls is np.array:
    elif box_cls is Series:
    elif box_cls is to_array:
    elif isinstance(left, np.ndarray):
    else:
    ensure_clean,
    except AttributeError:
    expected : np.ndarray, Index, Series
    expected_exception : Exception
    ExtensionArray,
    Find the higher of two datetime64 units.
    float,
    FLOAT_NUMPY_DTYPES + ALL_REAL_EXTENSION_DTYPES + ALL_REAL_PYARROW_DTYPES_STR_REPR
    FLOAT_PYARROW_DTYPES = [pa.float32(), pa.float64()]
    FLOAT_PYARROW_DTYPES_STR_REPR = [
    FLOAT_PYARROW_DTYPES_STR_REPR = []
    for cls in [np.datetime64, np.timedelta64]
    for func_name, expected in func_names_and_expected:
    for unit in [
    from pandas._typing import (
    from pandas.core.arrays import ArrowExtensionArray
    frozenset,
    func_names_and_expected : Sequence of two items
    function
    get_dtype,
    get_locales,
    get_obj,
    Helper function to mark pytest.raises that have an external error message.
    Helper function to wrap the expected output of a test in a given box_class.
    if (
    if _UNITS.index(left) >= _UNITS.index(right):
    if box_cls is pd.array:
    if dtype is None:
    if isinstance(left, (Index, Series)):
    if isinstance(left, BaseMaskedArray) and isinstance(right, BaseMaskedArray):
    if isinstance(left, DataFrame) and len(left._mgr.arrays) == 1:
    if isinstance(left, MultiIndex):
    if isinstance(left, NDArrayBackedExtensionArray):
    if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
    if isinstance(left, pd.core.arrays.IntervalArray):
    if isinstance(left, pd.core.arrays.SparseArray):
    if isinstance(left, RangeIndex):
    import pyarrow as pa
    import pytest
    Index,
    int,
    keys and expected result.
    list
    list,
    maybe_produces_warning,
    memoryview,
    MultiIndex,
    ndframe : DataFrame or Series
    np.float16,
    np.float32,
    np.int16,
    np.int32,
    np.int8,
    np.uint16,
    np.uint32,
    np.uint8,
    NumpyExtensionArray,
    op_name : str
    Pandas-compat for np.shares_memory.
    Parameters
    raise NotImplementedError(type(left), type(right))
    raise_assert_detail,
    raises_chained_assignment_error,
    range,
    RangeIndex,
    results = []
    return expected
    return extract_array(obj, extract_numpy=True)
    return op
    return pytest.raises(expected_exception, match=None)
    return results
    return right
    return sep.join(rows_list) + sep
    return x
    return x.at
    return x.iat
    return x.iloc
    return x.loc
    Returns
    round_trip_localpath,
    round_trip_pathlib,
    round_trip_pickle,
    rows_list : List[str]
    sep = os.linesep
    Series,
    set,
    set_locale,
    set_timezone,
    short_opname = op_name.strip("_")
    SIGNED_INT_PYARROW_DTYPES = [pa.int8(), pa.int16(), pa.int32(), pa.int64()]
    Similar to pd.array, but does not cast numpy dtypes to nullable dtypes.
    str
    str,
    STRING_PYARROW_DTYPES = [pa.string()]
    subclass of box_cls
    The operator function for a given op name.
    This method is used for creating expected value of to_csv() method.
    TIME_PYARROW_DTYPES = [
    TIMEDELTA_PYARROW_DTYPES = [pa.duration(unit) for unit in ["s", "ms", "us", "ns"]]
    try:
    tuple,
    TYPE_CHECKING,
    UNSIGNED_INT_PYARROW_DTYPES = [pa.uint8(), pa.uint16(), pa.uint32(), pa.uint64()]
    use_numexpr,
    with_csv_dialect,
    write_to_compressed,
# -----------------------------------------------------------------------------
# Comparators
# Indexing test helpers
)
]
__all__ = [
_UNITS = ["s", "ms", "us", "ns"]
ALL_FLOAT_DTYPES: list[Dtype] = [*FLOAT_NUMPY_DTYPES, *FLOAT_EA_DTYPES]
ALL_INT_DTYPES: list[Dtype] = [*ALL_INT_NUMPY_DTYPES, *ALL_INT_EA_DTYPES]
ALL_INT_EA_DTYPES = UNSIGNED_INT_EA_DTYPES + SIGNED_INT_EA_DTYPES
ALL_INT_NUMPY_DTYPES = UNSIGNED_INT_NUMPY_DTYPES + SIGNED_INT_NUMPY_DTYPES
ALL_NUMERIC_DTYPES: list[Dtype] = [*ALL_REAL_DTYPES, *COMPLEX_DTYPES]
ALL_NUMPY_DTYPES = (
ALL_REAL_DTYPES: list[Dtype] = [*ALL_REAL_NUMPY_DTYPES, *ALL_REAL_EXTENSION_DTYPES]
ALL_REAL_EXTENSION_DTYPES = FLOAT_EA_DTYPES + ALL_INT_EA_DTYPES
ALL_REAL_NULLABLE_DTYPES = (
ALL_REAL_NUMPY_DTYPES = FLOAT_NUMPY_DTYPES + ALL_INT_NUMPY_DTYPES
arithmetic_dunder_methods = [
BOOL_DTYPES: list[Dtype] = [bool, "bool"]
BYTES_DTYPES: list[Dtype] = [bytes, "bytes"]
class SubclassedDataFrame:
class SubclassedSeries:
comparison_dunder_methods = ["__eq__", "__ne__", "__le__", "__lt__", "__ge__", "__gt__"]
COMPLEX_DTYPES: list[Dtype] = [complex, "complex64", "complex128"]
COMPLEX_FLOAT_DTYPES: list[Dtype] = [*COMPLEX_DTYPES, *FLOAT_NUMPY_DTYPES]
cython_table = pd.core.common._cython_table.items()
DATETIME64_DTYPES: list[Dtype] = ["datetime64[ns]", "M8[ns]"]
def at(x):
def box_expected(expected, box_cls, transpose: bool = True):
def convert_rows_list_to_csv_str(rows_list: list[str]) -> str:
def external_error_raised(expected_exception: type[Exception]) -> ContextManager:
def get_cython_table_params(ndframe, func_names_and_expected):
def get_finest_unit(left: str, right: str):
def get_op_from_name(op_name: str) -> Callable:
def getitem(x):
def iat(x):
def iloc(x):
def loc(x):
def setitem(x):
def shares_memory(left, right) -> bool:
def to_array(obj):
else:
ENDIAN = {"little": "<", "big": ">"}[byteorder]
FLOAT_EA_DTYPES: list[Dtype] = ["Float32", "Float64"]
FLOAT_NUMPY_DTYPES: list[NpDtype] = [float, "float32", "float64"]
from __future__ import annotations
from decimal import Decimal
from pandas import (
from pandas._config.localization import (
from pandas._testing._io import (
from pandas._testing._warnings import (
from pandas._testing.asserters import (
from pandas._testing.compat import (
from pandas._testing.contexts import (
from pandas.compat import pa_version_under10p1
from pandas.core.arrays import (
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.construction import extract_array
from pandas.core.dtypes.common import is_string_dtype
from sys import byteorder
from typing import (
if not pa_version_under10p1:
if TYPE_CHECKING:
import numpy as np
import operator
import os
import pandas as pd
import warnings
NARROW_NP_DTYPES = [
NP_NAT_OBJECTS = [
NULL_OBJECTS = [None, np.nan, pd.NaT, float("nan"), pd.NA, Decimal("NaN")]
OBJECT_DTYPES: list[Dtype] = [object, "object"]
PYTHON_DATA_TYPES = [
SIGNED_INT_EA_DTYPES: list[Dtype] = ["Int8", "Int16", "Int32", "Int64"]
SIGNED_INT_NUMPY_DTYPES: list[NpDtype] = [int, "int8", "int16", "int32", "int64"]
STRING_DTYPES: list[Dtype] = [str, "str", "U"]
TIMEDELTA64_DTYPES: list[Dtype] = ["timedelta64[ns]", "m8[ns]"]
UNSIGNED_INT_EA_DTYPES: list[Dtype] = ["UInt8", "UInt16", "UInt32", "UInt64"]
UNSIGNED_INT_NUMPY_DTYPES: list[NpDtype] = ["uint8", "uint16", "uint32", "uint64"]
