# modules/common/print_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import pprint
from typing import Any


__all__ = ["pprint_block", "pformat_block"]


def pformat_block(obj: Any) -> str:
    """
    Pretty-format an object inside a clean visual block.
    """
    pretty = pprint.pformat(obj, indent=2, width=80, compact=True)
    lines = pretty.splitlines()
    boxed = ["┌────────────────────────────────────────────────────┐"]
    for line in lines:
        boxed.append(f"│ {line}")
    boxed.append("└────────────────────────────────────────────────────┘")
    return "\n".join(boxed)


def pprint_block(obj: Any) -> None:
    """
    Print a pretty-formatted object inside a block.
    """
    print(pformat_block(obj))
