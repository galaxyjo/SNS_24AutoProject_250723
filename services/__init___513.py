    is_url,
    make_vcs_requirement_url,
    RemoteNotFoundError,
    RemoteNotValidError,
    vcs,
# (The test directory may still need to import from a vcs sub-package.)
# Expose a limited set of classes and functions so callers outside of
# Import all vcs modules to register each VCS in the VcsSupport object.
# the vcs package don't need to import deeper than `pip._internal.vcs`.
)
from pip._internal.vcs.versioncontrol import (  # noqa: F401
import pip._internal.vcs.bazaar
import pip._internal.vcs.git
import pip._internal.vcs.mercurial
import pip._internal.vcs.subversion  # noqa: F401
