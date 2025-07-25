
    """
    """This is preserved for old console scripts that may still be referencing
    For additional details, see https://github.com/pypa/pip/issues/7498.
    from pip._internal.utils.entrypoints import _wrapper
    it.
    return _wrapper(args)
# init_logging() must be called before any call to logging.getLogger()
# which happens at import of most modules.
_log.init_logging()
def main(args: Optional[List[str]] = None) -> int:
from pip._internal.utils import _log
from typing import List, Optional
