
            msg = f"module {mod_name} has no attribute {name}"
            raise AttributeError(msg)
            return VersionInfo._from_version_string(meta["version"])
        from importlib.metadata import metadata
        if name == "__version_info__":
        if name not in ("__version__", "__version_info__"):
        meta = metadata("attrs")
        return meta["version"]
    """
    "asdict",
    "assoc",
    "astuple",
    "attr",
    "attrib",
    "Attribute",
    "attributes",
    "attrs",
    "AttrsInstance",
    "cmp_using",
    "Converter",
    "converters",
    "define",
    "evolve",
    "exceptions",
    "Factory",
    "field",
    "fields",
    "fields_dict",
    "filters",
    "frozen",
    "get_run_validators",
    "has",
    "ib",
    "make_class",
    "mutable",
    "NOTHING",
    "NothingType",
    "resolve_types",
    "s",
    "set_run_validators",
    "setters",
    "validate",
    "validators",
    _Nothing,
    attrib,
    Attribute,
    attrs,
    Converter,
    Create a metadata proxy for packaging information that uses *mod_name* in
    def __getattr__(name: str) -> str:
    def __init__(self, *args, **kwargs): pass
    evolve,
    Factory,
    fields,
    fields_dict,
    its warnings and errors.
    make_class,
    NOTHING,
    return __getattr__
    validate,
"""
# SPDX-License-Identifier: MIT
)
]
__all__ = [
__getattr__ = _make_getattr(__name__)
class AttrsInstance:
Classes Without Boilerplate
dataclass = partial(attrs, auto_attribs=True)  # happy Easter ;)
def _make_getattr(mod_name: str) -> Callable:
from . import converters, exceptions, filters, setters, validators
from ._cmp import cmp_using
from ._config import get_run_validators, set_run_validators
from ._funcs import asdict, assoc, astuple, has, resolve_types
from ._make import (
from ._next_gen import define, field, frozen, mutable
from ._version_info import VersionInfo
from functools import partial
from typing import Callable, Literal
ib = attr = attrib
NothingType = Literal[_Nothing.NOTHING]
s = attributes = attrs
