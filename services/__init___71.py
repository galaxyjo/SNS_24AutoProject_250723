
                ("3+5", 8),
                continue
                node.parent, pytest.Session
                pytest.param("6*9", 42, marks=pytest.mark.xfail),
                return True
            "test_input,expected",
            ):
            [
            ],
            assert eval(test_input) == expected
            deselected.append(colitem)
            deselected.append(item)
            f" but it is {empty_parameterset!r}"
            f"{EMPTY_PARAMETERSET_OPTION!s} must be one of skip, xfail or fail_at_collect"
            if all(mark.kwargs.get(k, NOT_SET) == v for k, v in kwargs.items()):
            if isinstance(node, pytest.Directory) and isinstance(
            if isinstance(node, pytest.Session):
            if subname in name:
            mapped_names.add(node.name)
            mapped_names.update(function_obj.__dict__)
            mark_name_mapping[mark.name].append(mark)
            name = parts[0]
            parts = line.split(":", 1)
            raise UsageError("Keyword expressions do not support call parameters.")
            remaining.append(colitem)
            remaining.append(item)
            rest = parts[1] if len(parts) == 2 else ""
            return False
            tw.line()
            tw.line(rest)
            tw.write(f"@pytest.mark.{name}:", bold=True)
        "Additionally keywords are matched to classes and functions "
        "An expression is a Python evaluable expression "
        "and their parent classes. Example: -k 'test_method or test_"
        "as well as functions which have names assigned directly to them. "
        "containing extra names in their 'extra_keyword_matches' set, "
        "contains 'test_method' or 'test_other', while -k 'not test_method' "
        "For example: -m 'mark1 and not mark2'.",
        "-k 'not test_method and not test_other' will eliminate the matches. "
        "-k",
        "-m",
        "--markers",
        "matches those that don't contain 'test_method' in their names. "
        "other' matches all test functions and classes whose name "
        "The matching is case-insensitive.",
        "where all names are substring-matched against test names "
        # Add the markers to the keywords as we no longer handle them correctly.
        # Add the names added as extra keywords to current or parent items.
        # Add the names attached to the current function through direct assignment.
        # Add the names of the current item and any parent items,
        # except the Session and root Directory's which are not
        # interesting for matching.
        )
        @pytest.mark.parametrize(
        action="store",
        action="store_true",
        config._do_configure()
        config._ensure_unconfigure()
        config.hook.pytest_deselected(items=deselected)
        def test_eval(test_input, expected):
        default="",
        dest="keyword",
        dest="markexpr",
        else:
        for line in config.getini("markers"):
        for mark in markers:
        for mark in matches:
        for name in names:
        for node in item.listchain():
        function_obj = getattr(item, "function", None)
        help="Only run tests matching given mark expression. "
        help="Only run tests which match the given substring expression. "
        help="show markers (builtin, plugin and per-project ones).",
        if expr.evaluate(MarkMatcher.from_markers(item.iter_markers())):
        if function_obj:
        if kwargs:
        if not (matches := self.own_mark_name_mapping.get(name, [])):
        if not expr.evaluate(KeywordMatcher.from_item(colitem)):
        import pytest
        items[:] = remaining
        mapped_names = set()
        mapped_names.update(item.listextrakeywords())
        mapped_names.update(mark.name for mark in item.iter_markers())
        mark_name_mapping = collections.defaultdict(list)
        metavar="EXPRESSION",
        metavar="MARKEXPR",
        names = (name.lower() for name in self._names)
        raise UsageError(
        raise UsageError(f"{exc_message}: {expr}: {e}") from None
        return
        return 0
        return cls(mapped_names)
        return cls(mark_name_mapping)
        return Expression.compile(expr)
        return False
        subname = subname.lower()
        tw = _pytest.config.create_terminal_writer(config)
    """
    """A matcher for keywords.
    """A matcher for markers which are present.
    """Specify a parameter in `pytest.mark.parametrize`_ calls or
    "get_empty_parameterset_mark",
    "Mark",
    "MARK_GEN",
    "MarkDecorator",
    "MarkGenerator",
    "ParameterSet",
    )
    *values: object,
    .. code-block:: python
    :class:`Function`.
    :param id: The id to attribute to this parameter set.
    :param marks: A single mark or a list of marks to be applied to this parameter set.
    :param values: Variable args of the values of the parameter set, in order.
    :ref:`parametrized fixtures <fixture-parametrize-marks>`.
    @classmethod
    __slots__ = ("_names",)
    __slots__ = ("own_mark_name_mapping",)
    _names: AbstractSet[str]
    Additionally, matches on names in the 'extra_keyword_matches' set of
    any item, as well as names directly assigned to test functions.
    config.stash[old_mark_config_key] = MARK_GEN._config
    def __call__(self, name: str, /, **kwargs: str | int | bool | None) -> bool:
    def __call__(self, subname: str, /, **kwargs: str | int | bool | None) -> bool:
    def from_item(cls, item: Item) -> KeywordMatcher:
    def from_markers(cls, markers: Iterable[Mark]) -> MarkMatcher:
    deselect_by_keyword(items, config)
    deselect_by_mark(items, config)
    deselected = []
    deselected: list[Item] = []
    empty_parameterset = config.getini(EMPTY_PARAMETERSET_OPTION)
    except ParseError as e:
    expr = _parse_expression(keywordexpr, "Wrong expression passed to '-k'")
    expr = _parse_expression(matchexpr, "Wrong expression passed to '-m'")
    for colitem in items:
    for item in items:
    from _pytest.nodes import Item
    Given a list of names, matches any substring of one of these names. The
    group = parser.getgroup("general")
    group._addoption(
    group.addoption(
    id: str | None = None,
    if config.option.markers:
    if deselected:
    if empty_parameterset not in ("skip", "xfail", "fail_at_collect", None, ""):
    if not keywordexpr:
    if not matchexpr:
    import _pytest.config
    keywordexpr = config.option.keyword.lstrip()
    MARK_GEN._config = config
    MARK_GEN._config = config.stash.get(old_mark_config_key, None)
    marks: MarkDecorator | Collection[MarkDecorator | Mark] = (),
    matchexpr = config.option.markexpr
    Only matches names of items which are either a :class:`Class` or a
    own_mark_name_mapping: dict[str, list[Mark]]
    parser.addini("markers", "Register new markers for test functions", "linelist")
    parser.addini(EMPTY_PARAMETERSET_OPTION, "Default marker for empty parametersets")
    remaining = []
    remaining: list[Item] = []
    return None
    return ParameterSet.param(*values, marks=marks, id=id)
    string inclusion check is case-insensitive.
    Tries to match on any marker names, attached to the given colitem.
    try:
    Will match on the name of colitem, including the names of its parents.
"""Generic mechanism for marking and selecting python functions."""
) -> ParameterSet:
@dataclasses.dataclass
@hookimpl(tryfirst=True)
]
__all__ = [
class KeywordMatcher:
class MarkMatcher:
def _parse_expression(expr: str, exc_message: str) -> Expression:
def deselect_by_keyword(items: list[Item], config: Config) -> None:
def deselect_by_mark(items: list[Item], config: Config) -> None:
def param(
def pytest_addoption(parser: Parser) -> None:
def pytest_cmdline_main(config: Config) -> int | ExitCode | None:
def pytest_collection_modifyitems(items: list[Item], config: Config) -> None:
def pytest_configure(config: Config) -> None:
def pytest_unconfigure(config: Config) -> None:
from .expression import Expression
from .expression import ParseError
from .structures import EMPTY_PARAMETERSET_OPTION
from .structures import get_empty_parameterset_mark
from .structures import Mark
from .structures import MARK_GEN
from .structures import MarkDecorator
from .structures import MarkGenerator
from .structures import ParameterSet
from __future__ import annotations
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config import UsageError
from _pytest.config.argparsing import NOT_SET
from _pytest.config.argparsing import Parser
from _pytest.stash import StashKey
from typing import AbstractSet
from typing import Collection
from typing import Iterable
from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import collections
import dataclasses
old_mark_config_key = StashKey[Optional[Config]]()
