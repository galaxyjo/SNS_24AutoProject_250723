
            complevel=complevel,
            complib=complib,
            fletcher32=fletcher32,
            mode=mode,
            store.close()
            tmp_path,
            yield store
        ) as store:
        if store is not None:
        pass
        store.remove(key)
        tmp_path = pathlib.Path(tmpdirname, path)
        with HDFStore(
    """
    except (ValueError, KeyError):
    except OSError:
    For tests using tables, try removing the table to be sure there is
    no content from previous tests using the same table name.
    path, mode="a", complevel=None, complib=None, fletcher32=False
    try:
    with tempfile.TemporaryDirectory() as tmpdirname:
# contextmanager to ensure the file cleanup
# set these parameters so we don't have file sharing
) -> Generator[HDFStore, None, None]:
@contextmanager
def _maybe_remove(store, key):
def ensure_clean_store(
def safe_close(store):
from collections.abc import Generator
from contextlib import contextmanager
from pandas.io.pytables import HDFStore
import pathlib
import pytest
import tempfile
tables = pytest.importorskip("tables")
tables.parameters.MAX_BLOSC_THREADS = 1
tables.parameters.MAX_NUMEXPR_THREADS = 1
tables.parameters.MAX_THREADS = 1
