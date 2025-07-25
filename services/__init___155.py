
            # GH#18463
            expected = expected.fillna(np.nan)
            expected = expected.fillna(pd.NA)
        else:
        if ser.dtype.storage == "pyarrow_numpy":
    if ser.dtype != object:
    return expected
def _convert_na_value(ser, expected):
import numpy as np
import pandas as pd
object_pyarrow_numpy = ("object", "string[pyarrow_numpy]")
