
        from pandas.core.util.hashing import hash_array
        from pandas.core.util.hashing import hash_pandas_object
        from pandas.util._decorators import Appender
        from pandas.util._decorators import cache_readonly
        from pandas.util._decorators import Substitution
        return Appender
        return cache_readonly
        return hash_array
        return hash_pandas_object
        return Substitution
    # These imports need to be lazy to avoid circular import errors
    if key == "Appender":
    if key == "cache_readonly":
    if key == "hash_array":
    if key == "hash_pandas_object":
    if key == "Substitution":
    raise AttributeError(f"module 'pandas.util' has no attribute '{key}'")
    return s[:1].upper() + s[1:]
def __getattr__(key: str):
def capitalize_first_letter(s):
