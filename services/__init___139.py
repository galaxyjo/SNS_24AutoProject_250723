
    # and mark only those modules as public
    # import modules that have public classes/functions
    __all__ = ["style"]
    from pandas.io.formats import style
# ruff: noqa: TCH004
from typing import TYPE_CHECKING
if TYPE_CHECKING:
