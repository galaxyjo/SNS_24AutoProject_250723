
                "distribution.".format(**locals())
                "normally this is bundled with this package so if you get "
                "The '{target}' package is required; "
                "this warning, consult the packager of your "
                __import__(extant)
                extant = prefix + target
                mod = sys.modules[extant]
                pass
                return mod
                sys.modules[fullname] = mod
            )
            else None
            except ImportError:
            if self._module_matches_namespace(fullname)
            importlib.util.spec_from_loader(fullname, self)
            raise ImportError(
            sys.meta_path.append(self)
            try:
        """
        """Figure out if the target module is vendored."""
        """Return a module spec for vendored names."""
        )
        else:
        for prefix in self.search_path:
        if self not in sys.meta_path:
        Install this importer into sys.meta_path if not already present.
        Iterate over the search path to locate and load fullname.
        pass
        return (
        return not root and any(map(target.startswith, self.vendored_names))
        return self.load_module(spec.name)
        root, base, target = fullname.partition(self.root_name + ".")
        Search first the vendor package then as a natural package.
        self.root_name = root_name
        self.vendor_pkg = vendor_pkg or root_name.replace("extern", "_vendor")
        self.vendored_names = set(vendored_names)
        yield ""
        yield self.vendor_pkg + "."
    """
    @property
    A PEP 302 meta path importer for finding optionally-vendored
    def __init__(self, root_name, vendored_names=(), vendor_pkg=None):
    def _module_matches_namespace(self, fullname):
    def create_module(self, spec):
    def exec_module(self, module):
    def find_spec(self, fullname, path=None, target=None):
    def install(self):
    def load_module(self, fullname):
    def search_path(self):
    or otherwise naturally-installed packages from root_name.
class VendorImporter:
import importlib.util
import sys
names = "packaging", "pyparsing", "appdirs"
VendorImporter(__name__, names).install()
