
        _mode_options["copy_on_write"] == "warn"
        _mode_options["copy_on_write"] is True
        and _mode_options["data_manager"] == "block"
    "config",
    "describe_option",
    "detect_console_encoding",
    "get_option",
    "option_context",
    "options",
    "reset_option",
    "set_option",
    "using_copy_on_write",
    "warn_copy_on_write",
    )
    _global_config,
    _mode_options = _global_config["future"]
    _mode_options = _global_config["mode"]
    describe_option,
    get_option,
    option_context,
    options,
    reset_option,
    return (
    return _mode_options["infer_string"]
    return _mode_options["nullable_dtypes"]
    set_option,
"""
)
]
__all__ = [
are initialized.
def using_copy_on_write() -> bool:
def using_nullable_dtypes() -> bool:
def using_pyarrow_string_dtype() -> bool:
def warn_copy_on_write() -> bool:
from pandas._config import config
from pandas._config import dates  # pyright: ignore[reportUnusedImport]  # noqa: F401
from pandas._config.config import (
from pandas._config.display import detect_console_encoding
importing `dates` and `display` ensures that keys needed by _libs
pandas._config is considered explicitly upstream of everything else in pandas,
should have no intra-pandas dependencies.
