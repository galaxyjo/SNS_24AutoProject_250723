# C:\SNS_24AutoProject_250723\modules\pprint_util_custom.py

from pprint import PrettyPrinter as _PrettyPrinter


class PrettyPrinter(_PrettyPrinter):
    def __init__(self, *args, sort_dicts=False, **kwargs):
        self._sort_dicts = sort_dicts
        super().__init__(*args, sort_dicts=sort_dicts, **kwargs)

    def format(self, obj, context, maxlevels, level):
        try:
            return super().format(obj, context, maxlevels, level)
        except Exception:
            return ("<bad value>", True, False)

    def _safe_key(self, key):
        try:
            return str(key)
        except Exception:
            return "<bad key>"

    def _safe_value(self, value):
        try:
            return str(value)
        except Exception:
            return "<bad value>"

    def _format_dict(self, d):
        return {self._safe_key(k): self._safe_value(v) for k, v in d.items()}

    def _format_list(self, l):
        return [self._safe_value(v) for v in l]
