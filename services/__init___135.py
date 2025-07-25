
    -----
    --------
                # Check if we are actually the item from item_cache, iloc creates a
                # new object
                f"methodtype must be one of {methodtype}, got {types} instead."
                lives
                return obj is parent._item_cache[obj._cacher[0]]
              jolie
            )
            if obj._cacher[0] in parent._item_cache:
            msg = f"local variable {base_msg}"
            msg = f"name {base_msg}"
            name = self.class_instance.__name__
            name = type(self.class_instance).__name__
            raise ValueError(
            return False
          positions
         black    7
         white    4
         x    2
         y    4
        # attr only exists on Windows, so typing fails on other platforms
        # parent could be dead
        0   1   0   1
        base_msg = f"{repr(name)} is not defined"
        else:
        if hasattr(parent, "_item_cache"):
        if is_local:
        if methodtype not in types:
        if parent is None:
        if self.methodtype == "classmethod":
        message += f" ({ctypes.WinError()})"  # type: ignore[attr-defined]
        parent = obj._cacher[1]()
        return f"This {self.methodtype} must be defined in the concrete class {name}"
        self.class_instance = class_instance
        self.methodtype = methodtype
        super().__init__(message)
        super().__init__(msg)
        types = {"method", "classmethod", "staticmethod", "property"}
        x       y
       ...
    """
    "A typical example is when you are setting values in a column of a "
    "A value is trying to be set on a copy of a DataFrame or Series "
    "AbstractMethodError",
    "assignment in a single step and ensure this keeps updating the original `df`.\n\n"
    "AttributeConflictWarning",
    "CategoricalConversionWarning",
    "ChainedAssignmentError: behaviour will change in pandas 3.0!\n"
    "ClosedFileError",
    "CSSWarning",
    "DatabaseError",
    "DataError",
    "DataFrame, like:\n\n"
    "default behaviour in pandas 3.0) this will never work to update the "
    "df[col] = df[col].method(value) instead, to perform "
    "DtypeWarning",
    "DuplicateLabelError",
    "EmptyDataError",
    "For example, when doing 'df[col].method(value, inplace=True)', try "
    "https://pandas.pydata.org/pandas-docs/stable/user_guide/"
    "in certain cases, but when using Copy-on-Write (which will become the "
    "IncompatibilityWarning",
    "indexing.html#returning-a-view-versus-a-copy"
    "indexing.html#returning-a-view-versus-a-copy\n"
    "IndexingError",
    "IntCastingNaNError",
    "InvalidColumnName",
    "InvalidComparison",
    "InvalidIndexError",
    "InvalidVersion",
    "LossySetitemError",
    "MergeError",
    "never work because the intermediate object on which we are setting "
    "NoBufferPresent",
    "NullFrequencyError",
    "NumbaUtilError",
    "NumExprClobberingError",
    "object on which we are setting values always behaves as a copy.\n\n"
    "OptionError",
    "original DataFrame or Series, because the intermediate object on which "
    "OutOfBoundsDatetime",
    "OutOfBoundsTimedelta",
    "ParserError",
    "ParserWarning",
    "PerformanceWarning",
    "PossibleDataLossError",
    "PossiblePrecisionLoss",
    "PyperclipException",
    "PyperclipWindowsException",
    "See the caveats in the documentation: "
    "SettingWithCopyError",
    "SettingWithCopyWarning",
    "SpecificationError",
    "the assignment in a single step.\n\n"
    "The behavior will change in pandas 3.0. This inplace method will "
    "the operation inplace on the original object.\n\n"
    "through chained assignment using an inplace method.\n"
    "through chained assignment.\n"
    "to update the original DataFrame or Series, because the intermediate "
    "Try using '.loc[row_indexer, col_indexer] = value' instead, to perform "
    "UndefinedVariableError",
    "UnsortedIndexError",
    "UnsupportedFunctionCall",
    "using 'df.method({col: value}, inplace=True)' instead, to perform "
    "using 'df.method({col: value}, inplace=True)' or "
    "ValueLabelTypeMismatch",
    "values always behaves as a copy.\n\n"
    "we are setting values will behave as a copy.\n"
    "When using the Copy-on-Write mode, such chained assignment never works "
    "When using the Copy-on-Write mode, such inplace method never works "
    "You are setting values through chained assignment. Currently this works "
    # in the item cache
    # on the Series; most of them also set _item_cache which adds 1 to our relevant
    # PerformanceWarning: indexing past lexsort depth may impact performance.
    # reference count, but iloc does not, so we have to check if we are actually
    # This is a mess, selection paths that return a view set the _cacher attribute
    ...                          ['1'] * 100000),
    ...                      "c": ["meow", "bark", "chirp", "nay"]},
    ...                      index=range(4)).set_index("a")
    ...                     "b": ["cat", "dog", "weasel", "horse"]},
    ...                     index=range(4))
    ...                    "B": ["x", "x", "z", "y"],
    ...                    "C": [1, 2, 3, 4]}
    ...                    "color": ["white", "white", "brown", "black"],
    ...                    "joe": ["x", "x", "z", "y"],
    ...                    "jolie": [1, 2, 3, 4]})
    ...                    "lives": [4, 4, 3, 7]},
    ...                    'b': ['b'] * 300000})  # doctest: +SKIP
    ...                    'B': range(5),
    ...                    'C': range(5)})
    ...                   )
    ...                   [3, 3, 4, 4]], columns=idx)
    ...                   columns=["key", "data"])
    ...               index = pd.MultiIndex.from_product([["a", "b"], ["c"]]))
    ...           1;1,8
    ...           1;2,1'''
    ...         raise pd.errors.AbstractMethodError(cls, methodtype="classmethod")
    ...         raise pd.errors.AbstractMethodError(self)
    ...      print(i, block)
    ...     @classmethod
    ...     allows_duplicate_labels=False
    ...     def classmethod(cls):
    ...     def method(self):
    ...     lambda x: 'background-color: blueGreenRed;'
    ...     lambda x: 'border: 1px solid red red;'
    ...     return sum(x) * 2.7
    ...   for i, block in enumerate(reader):
    ... # CategoricalConversionWarning: One or more series with value labels...
    ... # ChainedAssignmentError: ...
    ... # ClosedFileError: my-store file is not open!
    ... # DatabaseError: Execution failed on sql 'test': near "test": syntax error
    ... # DtypeWarning: Columns (0) have mixed types
    ... # IndexingError: indexer may only contain one '...' entry
    ... # IndexingError: Too many indexers
    ... # IndexingError: Unalignable boolean Series provided as indexer...
    ... # InvalidColumnName: Not all pandas column names were valid Stata variable...
    ... # NumExprClobberingError: Variables in expression "(abs) > (2)" overlap...
    ... # NumExprClobberingError: Variables in expression "(sin) + (a)" overlap...
    ... # ParserWarning: Falling back to the 'python' engine...
    ... # PossibleDataLossError: Re-opening the file [my-store] with mode [a]...
    ... # PossiblePrecisionLoss: Column converted from int64 to float64...
    ... # SettingWithCopyError: A value is trying to be set on a copy of a...
    ... # SettingWithCopyWarning: A value is trying to be set on a copy of a...
    ... # SpecificationError: nested renamer is not supported
    ... # UndefinedVariableError: local variable 'y' is not defined
    ... # UndefinedVariableError: name 'x' is not defined
    ... # ValueLabelTypeMismatch: Stata value labels (pandas categories) must be str...
    ... )
    ... ).to_excel('styled.xlsx')  # doctest: +SKIP
    ... cat,foo,bar
    ... dog,foo,"baz'''
    [name1] which conflicts with the new [name2]...
    ``eval`` or ``query`` will throw the error if the engine is set
    ``PeriodIndex.shift``.
    `int` and `str`.
    `pd.read_csv` and `pd.read_table` methods.
    `read_csv` and `read_table` functions to explicit the conversion:
    `read_csv` or `read_html` are parsing contents of a file.
    <class 'int'>
    <class 'str'>
    >>> class Foo:
    >>> conn = connect(':memory:')
    >>> csv = '''a;b;c
    >>> data = '''a,b,c
    >>> def incorrect_function(x):
    >>> df
    >>> df = df.set_index(["cat", "color"])
    >>> df = df.set_index(["jim", "joe"])
    >>> df = pd.DataFrame([[1, 1, 2, 2],
    >>> df = pd.DataFrame({"0categories": pd.Series([2, 2])})
    >>> df = pd.DataFrame({"A": [0, 0, 1, 1],
    >>> df = pd.DataFrame({"cat": [0, 0, 1, 1],
    >>> df = pd.DataFrame({"categories": pd.Series(["a", 2], dtype="category")})
    >>> df = pd.DataFrame({"jim": [0, 0, 1, 1],
    >>> df = pd.DataFrame({"key": ["a", "a", "b", "b"], "data": [1, 2, 3, 4]},
    >>> df = pd.DataFrame({"s": pd.Series([1, 2**53], dtype=np.int64)})
    >>> df = pd.DataFrame({'a': (['1'] * 100000 + ['X'] * 100000 +
    >>> df = pd.DataFrame({'A': [1, 1, 1, 2, 2],
    >>> df = pd.DataFrame({'A': [1, 1, 1, 2, 2]}, columns=['A'])
    >>> df = pd.DataFrame({'A': [1, 1, 1]})
    >>> df = pd.DataFrame({'abs': [1, 1, 1]})
    >>> df = pd.DatetimeIndex(["2011-01-01 10:00", "2011-01-01"], freq=None)
    >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]')  # doctest: +SKIP
    >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]', engine='python')
    >>> df.groupby("key").agg(incorrect_function, engine="numba")
    >>> df.groupby('A').agg(['min', 'min']) # doctest: +SKIP
    >>> df.groupby('A').agg({'B': {'foo': ['sum', 'max']}}) # doctest: +SKIP
    >>> df.groupby('A').B.agg({'foo': 'count'}) # doctest: +SKIP
    >>> df.loc[(0, "black"):(1, "white")]
    >>> df.loc[(1, 'z')]  # doctest: +SKIP
    >>> df.loc[..., ..., 'A'] # doctest: +SKIP
    >>> df.loc[0:3]['A'] = 'a' # doctest: +SKIP
    >>> df.loc[1, ..., ...] # doctest: +SKIP
    >>> df.query("A > @y") # doctest: +SKIP
    >>> df.query("A > x") # doctest: +SKIP
    >>> df.query("abs > 2") # doctest: +SKIP
    >>> df.shift(2)
    >>> df.style.applymap(
    >>> df.to_csv('test.csv', index=False)  # doctest: +SKIP
    >>> df.to_stata('test') # doctest: +SKIP
    >>> df["A"][0:3] = 10 # doctest: +SKIP
    >>> df[:, 0]
    >>> df[pd.Series([True], dtype=bool)] # doctest: +SKIP
    >>> df1 = pd.DataFrame([[1, 2], [3, 4]], index=idx1)
    >>> df1.to_hdf('file', 'data', 'w', append=True)  # doctest: +SKIP
    >>> df2 = pd.DataFrame([[5, 6], [7, 8]], index=idx2)
    >>> df2 = pd.read_csv('test.csv')  # doctest: +SKIP
    >>> df2 = pd.read_csv('test.csv', sep=',', dtype={'a': str})  # doctest: +SKIP
    >>> df2.iloc[262140, 0]  # doctest: +SKIP
    >>> df2.iloc[262150, 0]  # doctest: +SKIP
    >>> df2.to_hdf('file', 'data', 'a', append=True)  # doctest: +SKIP
    >>> empty = StringIO()
    >>> from io import StringIO
    >>> from pandas.io.stata import StataReader
    >>> from sqlite3 import connect
    >>> idx = pd.MultiIndex.from_product([["x", "y"], [0, 1]])
    >>> idx1 = pd.Index(['a', 'b'], name='name1')
    >>> idx2 = pd.Index(['c', 'd'], name='name2')
    >>> import io
    >>> left = pd.DataFrame({"a": ["a", "b", "b", "d"],
    >>> left.join(right, on="a", validate="one_to_one",)
    >>> np.cumsum(df.groupby(["A"]))
    >>> pd.DataFrame(np.array([[1, np.nan], [2, 3]]), dtype="i8")
    >>> pd.eval("sin + a", engine='numexpr') # doctest: +SKIP
    >>> pd.eval('x + 1') # doctest: +SKIP
    >>> pd.options.mode.chained_assignment = 'raise'
    >>> pd.options.mode.copy_on_write = False
    >>> pd.options.mode.copy_on_write = True
    >>> pd.read_csv(empty)
    >>> pd.read_csv(StringIO(data), skipfooter=1, engine='python')
    >>> pd.read_sql('select * test', conn) # doctest: +SKIP
    >>> right = pd.DataFrame({"a": ["a", "b", "c", "d"],
    >>> s = pd.Series([0, 1, 2], index=['a', 'b', 'c']).set_flags(
    >>> s = pd.Series(range(2),
    >>> s.loc["a", "c", "d"] # doctest: +SKIP
    >>> s.reindex(['a', 'a', 'b'])
    >>> ser = pd.Series(['a', 'b', 'c'])
    >>> ser.rolling(2).sum()
    >>> sin, a = 1, 2
    >>> store = pd.HDFStore('my-store', 'a') # doctest: +SKIP
    >>> store.close() # doctest: +SKIP
    >>> store.keys() # doctest: +SKIP
    >>> store.open("w") # doctest: +SKIP
    >>> test = Foo.classmethod()
    >>> test2 = Foo().method()
    >>> type(df2.iloc[262140, 0])  # doctest: +SKIP
    >>> type(df2.iloc[262150, 0])  # doctest: +SKIP
    >>> with StataReader('dta_file', chunksize=2) as reader: # doctest: +SKIP
    0    white    4
    0    x    1
    0   1   1   2   2
    1
    '1'
    1    brown    3
    1    z        3
    1    z    3
    1   3   3   4   4
    1. `sep` other than a single character (e.g. regex separators)
    2. `skipfooter` higher than 0
    3. `sep=None` with `delim_whitespace=False`
    a        [0, 1]
    AbstractMethodError: This classmethod must be defined in the concrete class Foo
    Access to the clipboard handle would be denied due to some other
    Adding `engine='python'` to `pd.read_csv` removes the Warning:
    AttributeConflictWarning: the [index_name] attribute of the existing index is
    Because the column name is an invalid Stata variable, the name needs to be
    can never update the original Series or DataFrame.
    cat  color
    chained indexing.
    checking happens per chunk read.
    column which will be an object type. See the examples below to better
    converted to a float64 dtype.
    converted.
    Copy-on-Write always behaves as a copy. Thus, assigning through a chain
    CSSWarning: Unhandled color format: 'blueGreenRed'
    CSV file.
    Currently, 'c' unsupported options include the following parameters:
    DataError: No numeric types to aggregate
    Dataframe or Series using a nested renamer (dict-of-dict).
    def __init__(self, *args, **kwargs): pass
    def __init__(self, class_instance, methodtype: str = "method") -> None:
    def __init__(self, message: str) -> None:
    def __init__(self, name: str, is_local: bool | None = None) -> None:
    def __str__(self) -> str:
    Despite the warning, the CSV file is read with mixed types in a single
    df.loc[(1, 'z')]
    'df["col"][row_indexer] = value\n\n'
    different frequency than the existing index on an HDFStore.
    DuplicateLabelError: Index has duplicates.
    EmptyDataError: No columns to parse from file
    Error is raised when executing sql with bad syntax or sql that throws an error.
    Error raised for unsupported Numba engine routines.
    Error raised when an operation would introduce duplicate labels.
    Error raised when slicing a MultiIndex which has not been lexsorted.
    Examples
    Exception is raised by _validate_comparison_value to indicate an invalid comparison.
    Exception is raised in _get_data_buffer to signal that there is no requested buffer.
    Exception is raised when trying to index and there is a mismatch in dimensions.
    Exception is raised when trying to perform an operation on a closed HDFStore file.
    Exception raised by ``agg`` when the functions are ill-specified.
    Exception raised by ``query`` or ``eval`` when using an undefined variable name.
    Exception raised in ``pd.read_csv`` when empty data or header is encountered.
    Exception raised when a ``freq`` cannot be null.
    Exception raised when attempting to call a unsupported numpy function.
    Exception raised when attempting to use an invalid index key.
    Exception raised when clipboard functionality is unsupported by Windows.
    Exception raised when clipboard functionality is unsupported.
    Exception raised when converting (``astype``) an array with NaN to an integer type.
    Exception raised when merging data.
    Exception raised when trying to open a HDFStore file when already opened.
    Exception raised when trying to set on a copied slice from a ``DataFrame``.
    Exception raised when trying to use a built-in numexpr name as a variable name.
    Exception that is raised by an error encountered in parsing file contents.
    Exceptionn raised when performing an operation on non-numerical data.
    For example, ``np.cumsum(groupby_object)``.
    For example, calling ``ohlc`` on a non-numerical column or a function
    For more information on evaluation order,
    For more information on view vs. copy,
    happen unintentionally when chained indexing.
    if hasattr(obj, "_cacher"):
    Important to notice that ``df2`` will contain both `str` and `int` for the
    IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer
    InvalidIndexError: (slice(None, None, None), 0)
    It happens due to a lack of support or functionality for parsing a
    It will also specify whether the undefined variable is local or not.
    jim  joe
    label
    MergeError: Merge keys are not unique in left dataset; not a one-to-one merge
    must be ['values', 'index']
    name than the existing index on an HDFStore or attempting to append an index with a
    names without assigning column name.
    never work. In such a situation, we are always setting into a temporary
    No warning was issued.
    Notes
    NullFrequencyError: Cannot shift with no freq
    NumbaUtilError: The first 2 arguments to incorrect_function
    numexpr package is installed.
    object that is the result of an indexing operation (getitem), which under
    Occurs when attempting to append an index with a different
    on a rolling window.
    One way to solve this issue is using the `dtype` parameter in the
    or `read_table` encounter non-uniform dtypes in a column(s) of a given
    OutOfBoundsDatetime,
    OutOfBoundsTimedelta,
    ParserError: ',' expected after '"'. Error could possibly be due
    parsers, generally from the default 'c' parser to 'python'.
    particular attribute of a CSV file with the requested engine.
    Particularly ``DatetimeIndex.shift``, ``TimedeltaIndex.shift``,
    pd.read_csv : Read CSV (comma-separated) file into DataFrame.
    pd.read_table : Read general delimited file into DataFrame.
    Raise this error instead of NotImplementedError for abstract methods.
    Raised by ``to_clipboard()`` and ``read_clipboard()``.
    Raised by `pd.read_csv` and `pd.read_table` when it is necessary to change
    Raised for a dtype incompatibility. This can happen whenever `read_csv`
    Raised when trying to do a __setitem__ on an np.ndarray that is not lossless.
    read_csv : Read CSV (comma-separated) file into a DataFrame.
    read_html : Read HTML table into a DataFrame.
    read_table : Read general delimited file into a DataFrame.
    return False
    same input, '1'.
    see :ref:`the user guide<indexing.evaluation_order>`.
    see :ref:`the user guide<indexing.view_versus_copy>`.
    See Also
    styling isn't properly formatted.
    Subclass of ``ValueError``.
    Subclass of `KeyError`.
    than MultiIndex lexsort depth (1)'
    The ``mode.chained_assignment`` needs to be set to set to 'raise.' This can
    The ``mode.chained_assignment`` needs to be set to set to 'warn.'
    The exception raised in two scenarios.
    The first way is calling ``agg`` on a
    The second way is calling ``agg`` on a Dataframe with duplicated functions
    The warning can be avoided by adding `engine='python'` as a parameter in
    This can be due to the styling not having an equivalent value or because the
    This example creates and reads a large CSV file with a column that contains
    This is a generic error raised for errors encountered when functions like
    This is an internal error.
    This warning is issued when dealing with larger files because the dtype
    to 'numexpr'. 'numexpr' is the default engine value for these methods if the
    to parsing errors in the skipped footer rows
    Traceback (most recent call last):
    understand this issue.
    UnsortedIndexError: 'Key length (2) was greater
    UnsupportedFunctionCall: numpy operations are not valid with groupby.
    Use .groupby(...).cumsum() instead
    'Use `df.loc[row_indexer, "col"] = values` instead, to perform the '
    Using a `sep` in `pd.read_csv` other than a single character:
    'Warn' is the default option. This can happen unintentionally when
    Warning is raised when converting css styling fails.
    Warning is raised when reading a partial labeled Stata file using a iterator.
    Warning raised by to_stata on a category column that contains non-string values.
    Warning raised by to_stata on a column with a value outside or equal to int64.
    Warning raised by to_stata the column contains a non-valid stata name.
    Warning raised when index attributes conflict when using HDFStore.
    Warning raised when reading a file that doesn't use the default 'c' parser.
    Warning raised when reading different dtypes in a column from a file.
    Warning raised when there is a possible performance impact.
    Warning raised when trying to set on a copied slice from a ``DataFrame``.
    Warning raised when trying to set using chained assignment.
    Warning raised when trying to use where criteria on an incompatible HDF5 file.
    When the ``mode.copy_on_write`` option is enabled, chained assignment can
    When the column value is outside or equal to the int64 value the column is
    window process is accessing it.
"""
)
]
__all__ = [
_chained_assignment_method_msg = (
_chained_assignment_msg = (
_chained_assignment_warning_method_msg = (
_chained_assignment_warning_msg = (
class AbstractMethodError:
class AttributeConflictWarning:
class CategoricalConversionWarning:
class ChainedAssignmentError:
class ClosedFileError:
class CSSWarning:
class DatabaseError:
class DataError:
class DtypeWarning:
class DuplicateLabelError:
class EmptyDataError:
class IncompatibilityWarning:
class IndexingError:
class IntCastingNaNError:
class InvalidColumnName:
class InvalidComparison:
class InvalidIndexError:
class LossySetitemError:
class MergeError:
class NoBufferPresent:
class NullFrequencyError:
class NumbaUtilError:
class NumExprClobberingError:
class ParserError:
class ParserWarning:
class PerformanceWarning:
class PossibleDataLossError:
class PossiblePrecisionLoss:
class PyperclipException:
class PyperclipWindowsException:
class SettingWithCopyError:
class SettingWithCopyWarning:
class SpecificationError:
class UndefinedVariableError:
class UnsortedIndexError:
class UnsupportedFunctionCall:
class ValueLabelTypeMismatch:
def _check_cacher(obj):
Expose public exceptions & warnings
from __future__ import annotations
from pandas._config.config import OptionError
from pandas._libs.tslibs import (
from pandas.util.version import InvalidVersion
import ctypes
