
    pass
"""
# Has to come after _run to resolve a circular import
# Imports that always exist
# Kqueue imports
# Windows imports
and deal with private internal data structures. Things in this namespace
are publicly available in either trio, trio.lowlevel, or trio.testing.
del sys  # It would be better to import sys as _sys, but mypy does not understand it
elif sys.platform != "linux" and sys.platform != "win32":
if sys.platform == "win32":
import sys
This namespace represents the core functionality that has to be built-in
