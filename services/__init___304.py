
    -----
    -------
    --------
            "module {!r} has no attribute " "{!r}".format(__name__, attr)
        )
        ``fortranobject.h``.
        `numpy.distutils` directly from ``.f`` and/or ``.pyf`` files
        Absolute path to the directory containing ``fortranobject.c`` and
        from numpy._pytesttester import PytestTester
        in one go.
        raise AttributeError(
        return test
        test = PytestTester(__name__)
        This function is not needed when building an extension with
      * ``fortranobject.c``
      * ``mymod-f2pywrappers.f`` (if it was generated in Step 1)
      * ``mymodmodule.c``
      ``mymod-f2pywrappers.f`` files next to ``mymod.pyf``.
      following source files:
      generates ``mymodmodule.c`` and (if needed)
    """
    # Avoid importing things that aren't needed for building
    # which might import the main numpy module
    * Step 1: run ``python -m numpy.f2py mymod.pyf --quiet``. This
    * Step 2: build your Python extension module. This requires the
    .. note::
    .. versionadded:: 1.21.1
    ``fortranobject.c`` as a source file, and include the ``fortranobject.h``
    both of these files.
    building a Python extension using a ``.pyf`` signature file is a two-step
    else:
    header. This function can be used to obtain the directory containing
    if attr == "test":
    include_path : str
    Notes
    numpy.get_include : function that returns the numpy include directory
    process. For a module ``mymod``:
    Python extension modules built with f2py-generated code need to use
    return list(globals().keys() | {"test"})
    return os.path.join(os.path.dirname(__file__), "src")
    Return the directory that contains the ``fortranobject.c`` and ``.h`` files.
    Returns
    See Also
    Unless the build system you are using has specific support for f2py,
"""
"""Fortran to Python Interface Generator.
__all__ = ["run_main", "get_include"]
Copyright 1999 -- 2011 Pearu Peterson all rights reserved.
Copyright 2011 -- present NumPy Developers.
def __dir__():
def __getattr__(attr):
def get_include():
from . import f2py2e
import os
main = f2py2e.main
NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
of the NumPy License.
Permission to use, modify, and distribute this software is given under the terms
run_main = f2py2e.run_main
