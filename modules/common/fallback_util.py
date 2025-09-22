def fallback(primary, secondary):
    return primary if primary is not None else secondary


def fallback_dict(d: dict, key: str, default=None):
    return d.get(key) if d and key in d else default
