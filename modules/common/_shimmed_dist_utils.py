
            "This CFFI feature requires setuptools on Python >= 3.12. Please install the setuptools package."
            "This CFFI feature requires setuptools on Python >= 3.12. The setuptools module is missing or non-functional."
            # FUTURE: msvc9compiler module was removed in setuptools 74; consider removing, as it's only used by an ancient patch in `recompiler`
            from distutils.msvc9compiler import MSVCCompiler
            MSVCCompiler = None
        "This CFFI feature requires distutils. Please install the distutils or setuptools package."
        # Python 3.12 has no built-in distutils to fall back on, so any import problem is fatal
        ) from ex
        except ImportError:
        raise Exception(
        try:
    # (the .pth shim should usually work, but this is even more robust)
    # anything older, just let the underlying distutils import error fly
    # bring in just the bits of distutils we need, whether they really came from setuptools or stdlib-embedded distutils
    # import setuptools first; this is the most robust way to ensure its embedded distutils is available
    # silently ignore on older Pythons (support fallback to stdlib distutils where available)
    ) from ex
    del setuptools
    if sys.platform == "win32":
    if sys.version_info >= (3, 12):
    import setuptools
    pass
    raise Exception(
"""
del sys
else:
error messages beyond `No module named 'distutils' on Python >= 3.12, or when setuptools' vendored distutils is broken.
except Exception as ex:
import sys
Temporary shim module to indirect the bits of distutils we need from setuptools/distutils while providing useful
This is a compromise to avoid a hard-dep on setuptools for Python >= 3.12, since many users don't need runtime compilation support from CFFI.
try:
