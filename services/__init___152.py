
    -------
    ----------
        Name of the method.
        pandas object that is being grouped.
        return (0,)
        return (0.5,)
        return (obj,)
    """
    A tuple of required arguments for the method.
    Get required arguments for a groupby method.
    if name == "corrwith":
    if name == "quantile":
    if name in ("nth", "fillna", "take"):
    it is often the case that arguments are required for certain methods.
    name: str
    obj: Series or DataFrame
    Parameters
    return ()
    Returns
    When parametrizing a test over groupby methods (e.g. "sum", "mean", "fillna"),
def get_groupby_method_args(name, obj):
