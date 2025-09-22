# tests/test_print_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import re
from modules.common.print_util import pformat_block, pprint_block


def test_pformat_block_output_structure():
    obj = {"a": 1, "b": [1, 2, 3]}
    result = pformat_block(obj)
    lines = result.splitlines()
    assert lines[0].startswith("┌")
    assert lines[-1].startswith("└")
    assert all(
        line.startswith("│") or line.startswith("└") or line.startswith("┌")
        for line in lines
    )


def test_pformat_block_content():
    obj = {"x": 10}
    result = pformat_block(obj)
    assert "x" in result
    assert "10" in result


def test_pprint_block_does_not_crash(capsys):
    obj = {"nested": {"a": 1, "b": 2}}
    pprint_block(obj)
    out = capsys.readouterr().out
    assert "nested" in out
    assert "a" in out
    assert "b" in out
    assert re.search(r"┌.*┐", out)
