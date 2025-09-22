import json


def dumps(obj, **kw):
    if "ensure_ascii" not in kw:
        kw["ensure_ascii"] = False
    return json.dumps(obj, **kw)


def loads(s, **kw):
    return json.loads(s, **kw)


def pretty(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)


__all__ = ["dumps", "loads", "pretty"]
