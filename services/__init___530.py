
                return style
            + "."
            + (builtin and ", though it should be builtin")
            f"Could not find style module {mod!r}"
            if name == found_name:
        # perhaps it got dropped into our styles package
        )
        builtin = ""
        builtin = "yes"
        cls = name.title() + "Style"
        for found_name, style in find_plugin_styles():
        mod = "pygments.styles." + name
        mod = __import__(mod, None, None, [cls])
        mod, cls = _STYLE_NAME_TO_MODULE_MAP[name]
        raise ClassNotFound(
        raise ClassNotFound(f"Could not find style class {cls!r} in style module.")
        return getattr(mod, cls)
        yield name
        yield v[1]
    """
    """Return a generator for all styles by name, both builtin and plugin."""
    are listed in :data:`pygments.styles.STYLE_MAP`.
    else:
    except AttributeError:
    except ImportError:
    for name, _ in find_plugin_styles():
    for v in STYLES.values():
    found.
    if name in _STYLE_NAME_TO_MODULE_MAP:
    Return a style class by its short name. The names of the builtin styles
    try:
    Will raise :exc:`pygments.util.ClassNotFound` if no style of that name is
"""
#: ``'submodule::classname'`` strings.
#: A dictionary of built-in styles, mapping style names to
#: Internal reverse mapping to make `get_style_by_name` more efficient
#: This list is deprecated. Use `pygments.styles.STYLES` instead
:copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
_STYLE_NAME_TO_MODULE_MAP = {v[1]: (v[0], k) for k, v in STYLES.items()}
~~~~~~~~~~~~~~~
Contains built-in styles.
def get_all_styles():
def get_style_by_name(name):
from pip._vendor.pygments.plugin import find_plugin_styles
from pip._vendor.pygments.styles._mapping import STYLES
from pip._vendor.pygments.util import ClassNotFound
pygments.styles
STYLE_MAP = {v[1]: v[0].split(".")[-1] + "::" + k for k, v in STYLES.items()}
