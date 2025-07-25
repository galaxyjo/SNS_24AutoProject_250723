
        " `from yaml import CLoader as Loader, CDumper as Dumper`.",
        " and its location is subject to change.  To use the"
        " LibYAML-based parser and emitter, import from `yaml`:"
        "The _yaml extension module is now located at yaml._yaml"
        DeprecationWarning,
    # Don't `del yaml` here because yaml is actually an existing
    # namespace member of _yaml.
    )
    del warnings
    exc = ModuleNotFoundError if version_info >= (3, 6) else ImportError
    from sys import version_info
    import warnings
    raise exc("No module named '_yaml'")
    warnings.warn(
# and has been moved into the `yaml` package namespace.
# close enough for anyone who's relying on it even when they shouldn't.
# extension module, which previously existed as a standalone module
# https://docs.python.org/3.8/library/types.html
# If the module is top-level (i.e. not a part of any specific package)
# in some circumstances, the yaml module we imoprted may be from a different version, so we need
# It does not perfectly mimic its old counterpart, but should get
# then the attribute should be set to ''.
# This is a stub package designed to roughly emulate the _yaml
# to tread carefully when poking at it here (it may not have the attributes we expect)
__name__ = "_yaml"
__package__ = ""
else:
if not getattr(yaml, "__with_libyaml__", False):
import yaml
