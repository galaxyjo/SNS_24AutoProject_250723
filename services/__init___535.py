
            in to something that can be JSON encoded. Defaults to None.
        **kwargs (Any): Keyword arguments for the replacement :class:`~rich.console.Console`.
        *args (Any): Positional arguments for the replacement :class:`~rich.console.Console`.
        _console = Console()
        all (bool, optional): Show all attributes. Defaults to False.
        all=all,
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        allow_nan=allow_nan,
        check_circular (bool, optional): Check for circular references. Defaults to True.
        check_circular=check_circular,
        Console: A console instance.
        data (Any): If json is not supplied, then encode this data.
        data=data,
        default (Callable, optional): A callable that converts values that can not be encoded
        default=default,
        docs (bool, optional): Also render doc strings. Defaults to True.
        docs=is_inspect or docs,
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        dunder=dunder,
        end (str, optional): Character to write at end of output. Defaults to "\\n".
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        ensure_ascii=ensure_ascii,
        file (IO[str], optional): File to write to, or None for stdout. Defaults to None.
        flush (bool, optional): Has no effect as Rich always flushes output. Defaults to False.
        from .console import Console
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        help=is_inspect or help,
        highlight (bool, optional): Enable highlighting of output: Defaults to True.
        highlight=highlight,
        indent (int, optional): Number of spaces to indent. Defaults to 2.
        indent=indent,
        json (str): A string containing JSON.
        json,
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        methods=is_inspect or methods,
        obj (Any): An object to inspect.
        obj,
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        private=private,
        sep (str, optional): Separator between printed objects. Defaults to " ".
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        skip_keys=skip_keys,
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
        sort_keys=sort_keys,
        sort=sort,
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        title=title,
        value (bool, optional): Pretty print value. Defaults to True.
        value=value,
    """
    """Get a global :class:`~rich.console.Console` instance. This function is used when Rich requires a Console,
    """Inspect any Python object.
    """Pretty prints JSON. Output will be valid JSON.
    """Reconfigures the global console by replacing it with another.
    # Can happen if the cwd has been deleted
    # Special case for inspect(inspect)
    )
    * inspect(<OBJECT>) to see summarized info.
    * inspect(<OBJECT>, all=True) to see all attributes.
    * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.
    * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.
    * inspect(<OBJECT>, methods=True) to see methods.
    * inspect(<OBJECT>, private=True) to see private attributes (single underscore).
    *,
    *objects: Any,
    _console = console or get_console()
    _console = get_console()
    _console.__dict__ = new_console.__dict__
    _console.print(_inspect)
    _IMPORT_CWD = ""
    _IMPORT_CWD = os.path.abspath(os.getcwd())
    _inspect = Inspect(
    all: bool = False,
    allow_nan: bool = True,
    and hasn't been explicitly given one.
    Args:
    check_circular: bool = True,
    console: Optional["Console"] = None,
    data: Any = None,
    default: Optional[Callable[[Any], Any]] = None,
    docs: bool = True,
    dunder: bool = False,
    end: str = "\n",
    ensure_ascii: bool = False,
    file: Optional[IO[str]] = None,
    flush: bool = False,
    For more advanced features, see the :class:`~rich.console.Console` class.
    from .console import Console
    from pip._vendor.rich._inspect import Inspect
    from pip._vendor.rich.console import Console
    get_console().print_json(
    global _console
    help: bool = False,
    highlight: bool = True,
    if _console is None:
    indent: Union[None, int, str] = 2,
    is_inspect = obj is inspect
    json: Optional[str] = None,
    methods: bool = False,
    new_console = Console(*args, **kwargs)
    obj: Any,
    print("Hello, **World**")
    private: bool = False,
    r"""Print object(s) supplied via positional arguments.
    return _console
    return write_console.print(*objects, sep=sep, end=end)
    Returns:
    sep: str = " ",
    skip_keys: bool = False,
    sort: bool = True,
    sort_keys: bool = False,
    This function has an identical signature to the built-in print.
    title: Optional[str] = None,
    value: bool = True,
    write_console = get_console() if file is None else Console(file=file)
"""Rich text and beautiful formatting in the terminal."""
# Global console used by alternative print
) -> None:
__all__ = ["get_console", "reconfigure", "print", "inspect", "print_json"]
_console: Optional["Console"] = None
def get_console() -> "Console":
def inspect(
def print(
def print_json(
def reconfigure(*args: Any, **kwargs: Any) -> None:
except FileNotFoundError:
from ._extension import load_ipython_extension  # noqa: F401
from typing import IO, TYPE_CHECKING, Any, Callable, Optional, Union
if __name__ == "__main__":  # pragma: no cover
if TYPE_CHECKING:
import os
try:
