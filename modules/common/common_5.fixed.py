
-------
        assert df.dtypes["A"] == dtypes["A"]
        assert df.dtypes["B"] == dtypes["B"]
        assert df.dtypes["C"] == dtypes["C"]
        assert df.dtypes["D"] == dtypes["D"]
        columns = frames[0].columns
        dtypes = {k: dtype for k, v in dtypes.items()}
        dtypes.update(dtype)
        index = frames[0].index
        return concat(zipped, axis=1)
        return DataFrame(zipped)
        zipped = [f.loc[:, c] for c in columns for f in frames]
        zipped = [f.loc[i, :] for i in index for f in frames]
    """
    # float16 are most likely to be upcasted to float32
    assumption that these all have the first frames' index/columns.
    concat,
    DataFrame,
    dtypes = {"A": "float32", "B": "float32", "C": "float16", "D": "float64"}
    dtypes = {"A": "int32", "B": "uint64", "C": "uint8", "D": "int64"}
    elif isinstance(dtype, dict):
    else:
    from pandas._typing import AxisInt
    if axis == 1:
    if dtypes.get("A"):
    if dtypes.get("B"):
    if dtypes.get("C"):
    if dtypes.get("D"):
    if isinstance(dtype, str):
    new_frame : DataFrame
    Returns
    take a list of frames, zip them together under the
)
def _check_mixed_float(df, dtype=None):
def _check_mixed_int(df, dtype=None):
def zip_frames(frames: list[DataFrame], axis: AxisInt = 1) -> DataFrame:
from __future__ import annotations
from pandas import (
from typing import TYPE_CHECKING
if TYPE_CHECKING:
