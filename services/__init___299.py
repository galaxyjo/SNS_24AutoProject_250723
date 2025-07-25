
        "Editable install doesn't support tests with a compile step",
        allow_module_level=True,
    )
    pytest.skip(
    pytest.skip("WASM/Pyodide does not use or support Fortran", allow_module_level=True)
from numpy.testing import IS_WASM, IS_EDITABLE
if IS_EDITABLE:
if IS_WASM:
import pytest
