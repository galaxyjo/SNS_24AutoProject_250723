# modules/common/import_util.py

import importlib
import sys
from types import ModuleType
from typing import Optional


def dynamic_import(module_name: str) -> Optional[ModuleType]:
    """Dynamically imports a module by name."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def import_from(module_name: str, obj_name: str):
    """Imports an object from a module by name."""
    module = dynamic_import(module_name)
    if module is None:
        return None
    return getattr(module, obj_name, None)


def is_module_available(module_name: str) -> bool:
    """Checks if a module is available without importing it."""
    return (
        module_name in sys.modules or importlib.util.find_spec(module_name) is not None
    )
