
                    res = res.replace("%", "%%")
                if item.config.getvalue("assertmode") == "rewrite":
                new_expl = [line.replace("\n", "\\n") for line in new_expl]
                new_expl = truncate.truncate_if_required(new_expl, item)
                res = "\n~".join(new_expl)
                return res
            " on import to provide assert expression information."
            "Control assertion debugging tools.\n"
            "Higher levels will provide more detailed explanation when an assertion fails."
            "'plain' performs no assertion debugging.\n"
            "'rewrite' (the default) rewrites assert statements in test modules"
            "Specify a verbosity level for assertions, overriding the main level. "
            # type: ignore[unreachable]
            assertstate.hook.set_session(None)
            assertstate.hook.set_session(session)
            break
            config=item.config, op=op, left=left, right=right
            if new_expl:
            ihook.pytest_assertion_pass(item=item, lineno=lineno, orig=orig, expl=expl)
            importhook = hook
            msg = "expected module names as *args, got {0} instead"
            raise TypeError(msg.format(repr(names)))
            sys.meta_path.remove(hook)
          (eg. if running in verbose mode).
          later.
          to protect later % formatting.
        """
        """Call the pytest_assertrepr_compare hook and prepare the result.
        "--assert",
        "enable_assertion_pass_hook",
        "Make sure to delete any previously generated pyc cache files.",
        # for importhook and for PytestPluginManager.rewrite_hook.
        # TODO(typing): Add a protocol for mark_rewrite() and use it
        )
        ),
        * Embedded newlines are escaped to help util.format_explanation()
        * If the rewrite mode is used embedded %-characters are replaced
        * Overly verbose explanations are truncated unless configured otherwise
        action="store",
        choices=("rewrite", "plain"),
        Config.VERBOSITY_ASSERTIONS,
        def call_assertion_pass_hook(lineno: int, orig: str, expl: str) -> None:
        default="rewrite",
        default=False,
        dest="assertmode",
        following:
        for new_expl in hook_result:
        help="Enables the pytest_assertion_pass hook. "
        help=(
        hook = config.stash[assertstate_key].hook
        hook_result = ihook.pytest_assertrepr_compare(
        if assertstate.hook is not None:
        if hook is not None and hook in sys.meta_path:
        if isinstance(hook, rewrite.AssertionRewritingHook):
        if not isinstance(name, str):
        importhook = DummyRewriteHook()  # type: ignore
        metavar="MODE",
        parser,
        pass
        pretty printing.
        return (yield)
        return None
        self.hook: rewrite.AssertionRewritingHook | None = None
        self.mode = mode
        self.trace = config.trace.root.get("assertion")
        The result can be formatted by util.format_explanation() for
        This uses the first result from the hook and then ensures the
        type="bool",
        util._assertion_pass = call_assertion_pass_hook
        util._config = None
        util._reprcompare, util._assertion_pass = saved_assert_hooks
    """
    """A no-op import hook for when rewriting is disabled."""
    """Register one or more module names to be rewritten on import.
    """Setup the pytest_assertrepr_compare and pytest_assertion_pass hooks.
    """State for the assertion plugin."""
    """Try to install the rewrite hook, raise SystemError if it fails."""
    # (which does not collect test modules).
    # so for example not in the managing process of pytest-xdist
    # This hook is only called when test modules are collected
    )
    :param names: The module names to register.
    actually imported, usually in your __init__.py if you are a plugin
    assertstate = session.config.stash.get(assertstate_key, None)
    comparison for the test.
    Config._add_verbosity_ini(
    config.add_cleanup(undo)
    config.stash[assertstate_key] = AssertionState(config, "rewrite")
    config.stash[assertstate_key].hook = hook = rewrite.AssertionRewritingHook(config)
    config.stash[assertstate_key].trace("installed rewrite import hook")
    config: Config, op: str, left: Any, right: Any
    def __init__(self, config: Config, mode) -> None:
    def callbinrepr(op, left: object, right: object) -> str | None:
    def mark_rewrite(self, *names: str) -> None:
    def undo() -> None:
    else:
    finally:
    for hook in sys.meta_path:
    for name in names:
    from _pytest.main import Session
    group = parser.getgroup("debugconfig")
    group.addoption(
    if assertstate:
    if ihook.pytest_assertion_pass.get_hookimpls():
    ihook = item.ihook
    importhook.mark_rewrite(*names)
    parser.addini(
    reporting via the pytest_assertrepr_compare hook.  This sets up this custom
    return hook
    return util.assertrepr_compare(config=config, op=op, left=left, right=right)
    saved_assert_hooks = util._reprcompare, util._assertion_pass
    sys.meta_path.insert(0, hook)
    the package will get their assert statements rewritten.
    The rewrite module will use util._reprcompare if it exists to use custom
    This function will make sure that this module or all modules inside
    Thus you should make sure to call this before the module is
    try:
    using a package.
    util._config = item.config
    util._reprcompare = callbinrepr
"""Support for presenting detailed information in failing assertions."""
# mypy: allow-untyped-defs
) -> list[str] | None:
@hookimpl(wrapper=True, tryfirst=True)
class AssertionState:
class DummyRewriteHook:
def install_importhook(config: Config) -> rewrite.AssertionRewritingHook:
def pytest_addoption(parser: Parser) -> None:
def pytest_assertrepr_compare(
def pytest_collection(session: Session) -> None:
def pytest_runtest_protocol(item: Item) -> Generator[None, object, object]:
def pytest_sessionfinish(session: Session) -> None:
def register_assert_rewrite(*names: str) -> None:
from __future__ import annotations
from _pytest.assertion import rewrite
from _pytest.assertion import truncate
from _pytest.assertion import util
from _pytest.assertion.rewrite import assertstate_key
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
from typing import Any
from typing import Generator
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import sys
