
                pass
                return importlib.import_module("setuptools._distutils")
            def create_module(self, spec):
            def exec_module(self, module):
            for frame, line in traceback.walk_stack(None)
            frame.f_globals["__file__"].endswith("setup.py")
            return
        """
        "also replaces the `distutils` module in `sys.modules`. This may lead "
        "Distutils was imported before Setuptools, but importing Setuptools "
        "that setuptools is always imported before distutils."
        "to undesirable behaviors or errors. To avoid these issues, avoid "
        "traditional way (e.g. not an editable install), and/or make sure "
        "using distutils directly, ensure that setuptools is installed in the "
        # https://foss.heptapod.net/pypy/pypy/-/blob/be829135bc0d758997b3566062999ee8b23872b4/lib-python/3/site.py#L250
        # PyPy for 3.6 unconditionally imports distutils, so bypass the warning
        )
        class DistutilsLoader:
        clear_distutils()
        del sys.modules[name]
        Detect if pip is being imported in a build script. Ref #2355.
        Ensure stdlib distutils when running under pip.
        ensure_local_distutils()
        if path is not None:
        if self.pip_imported_during_build():
        import importlib.abc
        import importlib.util
        import traceback
        method = getattr(self, method_name, lambda: None)
        method_name = "spec_for_{fullname}".format(**locals())
        pass
        return
        return any(
        return importlib.util.spec_from_loader("distutils", DistutilsLoader())
        return method()
        See pypa/pip#8761 for rationale.
        self.spec_for_distutils = lambda: None
        sys.meta_path.remove(DISTUTILS_FINDER)
        warn_distutils_present()
    """
    # sanity check that submodules load as expected
    )
    @staticmethod
    Allow selection of distutils by environment variable.
    assert "_distutils" in core.__file__, core.__file__
    clear_distutils()
    core = importlib.import_module("distutils.core")
    def __init__(self, *args, **kwargs): pass
    def find_spec(self, fullname, path, target=None):
    def pip_imported_during_build():
    def spec_for_distutils(self):
    def spec_for_pip(self):
    distutils = importlib.import_module("setuptools._distutils")
    distutils.__name__ = "distutils"
    Ensure that the local copy of distutils is preferred over stdlib.
    except ValueError:
    for more motivation.
    for name in mods:
    if "distutils" not in sys.modules:
    if enabled():
    if is_pypy and sys.version_info < (3, 7):
    mods = [name for name in sys.modules if re.match(r"distutils\b", name)]
    return which == "local"
    See https://github.com/pypa/setuptools/issues/417#issuecomment-392298401
    sys.meta_path.insert(0, DISTUTILS_FINDER)
    sys.modules["distutils"] = distutils
    try:
    warnings.warn(
    warnings.warn("Setuptools is replacing distutils.")
    which = os.environ.get("SETUPTOOLS_USE_DISTUTILS", "stdlib")
class DistutilsMetaFinder:
def add_shim():
def clear_distutils():
def do_override():
def enabled():
def ensure_local_distutils():
def remove_shim():
def warn_distutils_present():
DISTUTILS_FINDER = DistutilsMetaFinder()
import importlib
import os
import re
import sys
import warnings
is_pypy = "__pypy__" in sys.builtin_module_names
warnings.filterwarnings("ignore", r".+ distutils\b.+ deprecated", DeprecationWarning)
