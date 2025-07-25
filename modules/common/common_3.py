
    ----------
                "dtype is `object`."
                "For example they cannot be stored in a single array unless the "
                # GH#36706 npdev 1.20.0 2020-09-28
                r"<class 'numpy.dtype\[int64\]'> do not have a common DType. "
                r"The DTypes <class 'numpy.dtype\[datetime64\]'> and "
            "Cannot compare type",
            "Invalid comparison between",
            "invalid type promotion",
            "not supported between",
            # Index does not defer for comparisons
            # NB: we are assuming no pd.NAs for now
            (
            ),
            return np.array
            return x._ndarray
            return x.astype(bool)
        #  just exclude NumpyExtensionArray[bool]
        # Eventually we'd like this to be tighter, but for now we'll
        [
        ]
        if is_cmp and isinstance(left, Index):
        if is_cmp:
        if isinstance(x, BooleanArray):
        if isinstance(x, NumpyExtensionArray):
        left - right
        left + right
        left < right
        left <= right
        left > right
        left >= right
        return DataFrame
        return Index
        return Series
        return x
        rev_box = np.array
        right - left
        right + left
        right < left
        right <= left
        right > left
        right >= left
        Whether the operation is a comparison method.
    """
    # Not for tznaive-tzaware comparison
    # Note: not quite the same as how we do this for tm.box_expected
    # rev_box: box to use for reversed comparisons
    )
    array,
    Assert that comparison operations with mismatched types behave correctly.
    BooleanArray,
    box : {pd.DataFrame, pd.Series, pd.Index, pd.array, tm.to_array}
    DataFrame,
    def xbox2(x):
    expected = xbox(np.zeros(result.shape, dtype=np.bool_))
    Get the box to use for 'expected' in an arithmetic or comparison operation.
    Helper to assert that left and right can be neither added nor subtracted.
    Helper to assert that left and right cannot be added.
    if isinstance(left, DataFrame) or isinstance(right, DataFrame):
    if isinstance(left, Index) or isinstance(right, Index):
    if isinstance(left, Series) or isinstance(right, Series):
    if isinstance(right, Index) and isinstance(left, Series):
    Index,
    is_cmp : bool, default False
    left : Any
    left : np.ndarray, ExtensionArray, Index, or Series
    left : object
    msg : str or None, default None
    msg : str, default "cannot add"
    msg = "|".join(
    NumpyExtensionArray,
    Parameters
    result = xbox2(left != right)
    result = xbox2(left == right)
    result = xbox2(right != left)
    result = xbox2(right == left)
    return tm.to_array
    rev_box = xbox
    right : Any
    right : object
    Series,
    tm.assert_equal(result, ~expected)
    tm.assert_equal(result, expected)
    tm.assert_equal(result, rev_box(~expected))
    tm.assert_equal(result, rev_box(expected))
    with pytest.raises(TypeError, match=msg):
    xbox = box if box not in [Index, array] else np.array
"""
)
Assertion helpers for arithmetic tests.
def assert_cannot_add(left, right, msg="cannot add"):
def assert_invalid_addsub_type(left, right, msg=None):
def assert_invalid_comparison(left, right, box):
def get_upcast_box(left, right, is_cmp: bool = False):
from pandas import (
from pandas.core.arrays import (
import numpy as np
import pandas._testing as tm
import pytest
