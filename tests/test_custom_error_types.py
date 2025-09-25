import pytest
from modules.common.custom_error_types import FFIError

def test_ffierror_str():
    err = FFIError("Something went wrong")
    assert str(err) == "FFIError: Something went wrong"

def test_ffierror_is_instance_of_exception():
    err = FFIError("Error")
    assert isinstance(err, Exception)
