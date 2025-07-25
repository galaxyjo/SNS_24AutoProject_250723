
            "instead. This alias will be removed in a future version.",
            "PandasArray has been renamed NumpyExtensionArray. Use that "
            FutureWarning,
            stacklevel=find_stack_level(),
        # GH#53694
        )
        from pandas.util._exceptions import find_stack_level
        import warnings
        return NumpyExtensionArray
        warnings.warn(
    "ArrowExtensionArray",
    "ArrowStringArray",
    "BooleanArray",
    "Categorical",
    "DatetimeArray",
    "FloatingArray",
    "IntegerArray",
    "IntervalArray",
    "NumpyExtensionArray",
    "PeriodArray",
    "SparseArray",
    "StringArray",
    "TimedeltaArray",
    ArrowExtensionArray,
    ArrowStringArray,
    BooleanArray,
    Categorical,
    DatetimeArray,
    FloatingArray,
    if name == "PandasArray":
    IntegerArray,
    IntervalArray,
    NumpyExtensionArray,
    PeriodArray,
    raise AttributeError(f"module 'pandas.arrays' has no attribute '{name}'")
    SparseArray,
    StringArray,
    TimedeltaArray,
"""
)
]
__all__ = [
All of pandas' ExtensionArrays.
def __getattr__(name: str) -> type[NumpyExtensionArray]:
from pandas.core.arrays import (
See :ref:`extending.extension-types` for more.
