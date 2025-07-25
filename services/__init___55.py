
-------------
        "deprecated and will be removed in a future version. Only the BlockManager "
        "pandas from the source directory, you may need to run "
        "'python setup.py build_ext' to build the C extensions first."
        "The env variable PANDAS_DATA_MANAGER is set. The data_manager option is "
        "Unable to import required dependencies:\n" + "\n".join(_missing_dependencies)
        "will be available. Unset this environment variable to silence this warning.",
        __git_version__,
        __import__(_dependency)
        __version__,
        _missing_dependencies.append(f"{_dependency}: {_e}")
        f"C extension: {_module} not built. If you want to import "
        FutureWarning,
        is_numpy_dev as _is_numpy_dev,  # pyright: ignore[reportUnusedImport] # noqa: F401
        stacklevel=2,
    "api",
    "array",
    "arrays",
    "ArrowDtype",
    "bdate_range",
    "BooleanDtype",
    "Categorical",
    "CategoricalDtype",
    "CategoricalIndex",
    "concat",
    "crosstab",
    "cut",
    "DataFrame",
    "date_range",
    "DateOffset",
    "DatetimeIndex",
    "DatetimeTZDtype",
    "describe_option",
    "errors",
    "eval",
    "ExcelFile",
    "ExcelWriter",
    "factorize",
    "Flags",
    "Float32Dtype",
    "Float64Dtype",
    "from_dummies",
    "get_dummies",
    "get_option",
    "Grouper",
    "HDFStore",
    "Index",
    "IndexSlice",
    "infer_freq",
    "Int16Dtype",
    "Int32Dtype",
    "Int64Dtype",
    "Int8Dtype",
    "Interval",
    "interval_range",
    "IntervalDtype",
    "IntervalIndex",
    "io",
    "isna",
    "isnull",
    "json_normalize",
    "lreshape",
    "melt",
    "merge",
    "merge_asof",
    "merge_ordered",
    "MultiIndex",
    "NA",
    "NamedAgg",
    "NaT",
    "notna",
    "notnull",
    "offsets",
    "option_context",
    "options",
    "Period",
    "period_range",
    "PeriodDtype",
    "PeriodIndex",
    "pivot",
    "pivot_table",
    "plotting",
    "qcut",
    "RangeIndex",
    "read_clipboard",
    "read_csv",
    "read_excel",
    "read_feather",
    "read_fwf",
    "read_gbq",
    "read_hdf",
    "read_html",
    "read_json",
    "read_orc",
    "read_parquet",
    "read_pickle",
    "read_sas",
    "read_spss",
    "read_sql",
    "read_sql_query",
    "read_sql_table",
    "read_stata",
    "read_table",
    "read_xml",
    "reset_option",
    "Series",
    "set_eng_float_format",
    "set_option",
    "show_versions",
    "SparseDtype",
    "StringDtype",
    "test",
    "testing",
    "Timedelta",
    "timedelta_range",
    "TimedeltaIndex",
    "Timestamp",
    "to_datetime",
    "to_numeric",
    "to_pickle",
    "to_timedelta",
    "tseries",
    "UInt16Dtype",
    "UInt32Dtype",
    "UInt64Dtype",
    "UInt8Dtype",
    "unique",
    "value_counts",
    "wide_to_long",
    # conversion
    # dtype
    # excel
    # indexes
    # misc
    # missing
    # numpy compat
    # parsers
    # pickle
    # pytables
    # sql
    # tseries
    )
    ) from _err
    __git_version__ = v.get("full-revisionid")
    __version__ = v.get("closest-tag", v["version"])
    _built_with_meson = True
    _module = _err.name
    `Series`, `DataFrame`, etc. automatically align the data for you in
    and NumPy data structures into DataFrame objects.
    array,
    ArrowDtype,
    bdate_range,
    BooleanDtype,
    Categorical,
    CategoricalDtype,
    CategoricalIndex,
    computations.
    concat,
    conversion, moving window statistics, date shifting and lagging.
    crosstab,
    cut,
    data sets.
    DataFrame,
    date_range,
    DateOffset,
    DatetimeIndex,
    DatetimeTZDtype,
    del get_versions, v
    describe_option,
    Excel files, databases, and saving/loading data from the ultrafast HDF5
    ExcelFile,
    ExcelWriter,
    except ImportError as _e:  # pragma: no cover
    factorize,
    Flags,
    Float32Dtype,
    Float64Dtype,
    format.
    from pandas._version import get_versions
    from pandas._version_meson import (  # pyright: ignore [reportMissingImports]
    from pandas.compat import (
    from_dummies,
    get_dummies,
    get_option,
    Grouper,
    HDFStore,
    higher dimensional objects
    Index,
    IndexSlice,
    Int16Dtype,
    Int32Dtype,
    Int64Dtype,
    Int8Dtype,
    Interval,
    interval_range,
    IntervalDtype,
    IntervalIndex,
    isna,
    isnull,
    lreshape,
    melt,
    merge,
    merge_asof,
    merge_ordered,
    MultiIndex,
    NA,
    NamedAgg,
    NaT,
    notna,
    notnull,
    operations on data sets, for both aggregating and transforming data.
    option_context,
    options,
    Period,
    period_range,
    PeriodDtype,
    PeriodIndex,
    pivot,
    pivot_table,
    point data.
    qcut,
    raise ImportError(
    RangeIndex,
    read_clipboard,
    read_csv,
    read_excel,
    read_feather,
    read_fwf,
    read_gbq,
    read_hdf,
    read_html,
    read_json,
    read_orc,
    read_parquet,
    read_pickle,
    read_sas,
    read_spss,
    read_sql,
    read_sql_query,
    read_sql_table,
    read_stata,
    read_table,
    read_xml,
    reset_option,
    Series,
    set_eng_float_format,
    set_option,
    StringDtype,
    Timedelta,
    timedelta_range,
    TimedeltaIndex,
    Timestamp,
    to a set of labels, or the user can simply ignore the labels and let
    to_datetime,
    to_numeric,
    to_pickle,
    to_timedelta,
    try:
    UInt16Dtype,
    UInt32Dtype,
    UInt64Dtype,
    UInt8Dtype,
    unique,
    v = get_versions()
    value_counts,
    warnings.warn(
    wide_to_long,
  - Automatic and explicit data alignment: objects can be explicitly aligned
  - Easy handling of missing data in floating point as well as non-floating
  - Flexible reshaping and pivoting of data sets.
  - Hierarchical labeling of axes (possible to have multiple labels per tick).
  - Intelligent label-based slicing, fancy indexing, and subsetting of large
  - Intuitive merging and joining data sets.
  - Make it easy to convert ragged, differently-indexed data in other Python
  - Powerful, flexible group by functionality to perform split-apply-combine
  - Robust IO tools for loading data from flat files (CSV and delimited),
  - Size mutability: columns can be inserted and deleted from DataFrame and
  - Time series-specific functionality: date range generation and frequency
"""
# based on the documentation.
# GH#55043 - deprecation of the data_manager option
# let init-time option registration happen
# Let users know if they're missing any of our hard dependencies
# module level doc-string
# Pandas is not (yet) a py.typed library: the public API is determined
# Use __all__ to let type checkers know what is part of the public API.
# use the closest tagged version if possible
)
**pandas** is a Python package providing fast, flexible, and expressive data
]
__all__ = [
__doc__ = """
__docformat__ = "restructuredtext"
_built_with_meson = False
_hard_dependencies = ("numpy", "pytz", "dateutil")
_missing_dependencies = []
=====================================================================
analysis / manipulation tool available in any language**. It is already well on
del _hard_dependencies, _dependency, _missing_dependencies
del warnings, os
doing practical, **real world** data analysis in Python. Additionally, it has
easy and intuitive. It aims to be the fundamental high-level building block for
except ImportError as _err:  # pragma: no cover
except ImportError:
for _dependency in _hard_dependencies:
from __future__ import annotations
from pandas import api, arrays, errors, io, plotting, tseries
from pandas import testing
from pandas._config import (
from pandas.core.api import (
from pandas.core.computation.api import eval
from pandas.core.dtypes.dtypes import SparseDtype
from pandas.core.reshape.api import (
from pandas.io.api import (
from pandas.io.json._normalize import json_normalize
from pandas.tseries import offsets
from pandas.tseries.api import infer_freq
from pandas.util._print_versions import show_versions
from pandas.util._tester import test
Here are just a few of the things that pandas does well:
if "PANDAS_DATA_MANAGER" in os.environ:
if _missing_dependencies:  # pragma: no cover
import os
import pandas.core.config_init  # pyright: ignore[reportUnusedImport] # noqa: F401
import warnings
its way toward this goal.
Main Features
pandas - a powerful data analysis and manipulation library for Python
structures designed to make working with "relational" or "labeled" data both
the broader goal of becoming **the most powerful and flexible open source data
try:
