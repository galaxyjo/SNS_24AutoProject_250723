
        from future.moves.dbm import ndbm
        ndbm = None
    __future_module__ = True
    except ImportError:
    from dbm import ndbm
    pass
    try:
# In case some (badly written) code depends on dbm.ndbm after import dbm,
# Py3.3's dbm/__init__.py imports ndbm but doesn't expose it via __all__.
# we simulate this:
else:
from future.utils import PY3
if PY3:
