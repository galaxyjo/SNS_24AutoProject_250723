
                "are using a Homebrew or Linuxbrew Python, please see discussion "
                "at https://github.com/Homebrew/homebrew-core/issues/76621"
                "Configuring installation scheme with distutils config files "
                "is deprecated and will no longer work in the near future. If you "
            ),
            and (_looks_like_red_hat_scheme() or _looks_like_debian_scheme())
            and (len(new_v.parts) < 3 or new_v.parts[2] != "local")
            and _looks_like_bpo_44860()
            and _looks_like_slackware_scheme()
            and _PLATLIBDIR != "lib"
            and home is not None
            and is_osx_framework()
            and k == "headers"
            and k == "platlib"
            and k in ("headers", "include", "platinclude")
            and k in ("platlib", "purelib")
            and len(new_v.parts) > 1
            and new_v.name.startswith("pypy")
            and new_v.parts[1] == "usr"
            and not WINDOWS
            and old_v.name.startswith("python")
            and old_v.parent == new_v.parent
            and old_v.parent.name.startswith("python")
            and old_v.parent.parent == new_v.parent
            and old_v.parts[1:3] == ("usr", "local")
            and sys.version_info >= (3, 9)
            continue
            gone_in=None,
            not (user or home or prefix or running_under_virtualenv())
            part = part[: (0 - len(abiflags))]
            reason=(
            replacement=None,
            sys.implementation.name == "pypy"
            sysconfig.is_python_build(check_home=True)
            user
            WINDOWS and k in ("platlib", "purelib") and _looks_like_msys2_mingw_scheme()
        "\ndistutils: %s"
        "\nsysconfig: %s"
        "Additional context:",
        "home = %r",
        "Lib" not in p and "lib" in p and not p.endswith("site-packages")
        "prefix = %r",
        "root = %r",
        "user = %r",
        "Value for %s does not match. Please report this to <%s>"
        # /usr/local instead of /usr. Debian also places lib in dist-packages
        # and not warn about it. See bpo-43307 and python/cpython#24628.
        # Both Debian and Red Hat patch Python to place the system site under
        # but not usersite to match the location.
        # CPython decide whether this is a bug or feature. See bpo-43948.
        # CPython's POSIX install script invokes pip (via ensurepip) against the
        # directory name to be ``pypy`` instead. So we treat this as a bug fix
        # distutils incorrectly put PyPy packages under ``site-packages/python``
        # https://github.com/python/cpython/blob/8c21941ddaf/Lib/sysconfig.py#L178-L194
        # in the ``posix_home`` scheme, but PyPy devs said they expect the
        # instead of site-packages, but the /usr/local check should cover it.
        # interpreter located in the source tree, not the install site. This
        # mismatch when sys.platlibdir is not "lib".
        # MSYS2 MINGW's sysconfig patch does not include the "site-packages"
        # On Python 3.9+, sysconfig's posix_user scheme sets platlib against
        # On Red Hat and derived Linux distributions, distutils is patched to
        # part of the path. This is incorrect and will be fixed in MSYS.
        # Slackware incorrectly patches posix_user to use lib64 instead of lib,
        # sys.platlibdir, but distutils's unix_user incorrectly coninutes
        # sysconfig's ``osx_framework_user`` does not include ``pythonX.Y`` in
        # the ``include`` value, but distutils's ``headers`` does. We'll let
        # triggers special logic in sysconfig that's not present in distutils.
        # use "lib64" instead of "lib" for platlib.
        # using the same $usersite for both platlib and purelib. This creates a
        )
        _log_context()
        _warn_mismatched(old_v, new_v, key=key)
        and _looks_like_red_hat_patched_platlib_purelib(INSTALL_SCHEMES[k])
        and cmd.prefix == f"{os.path.normpath(sys.prefix)}/local"
        cmd.exec_prefix == f"{os.path.normpath(sys.exec_prefix)}/local"
        deprecated(
        dist_name,
        for k in ("unix_prefix", "unix_home")
        for p in (paths[key] for key in ("platlib", "purelib"))
        home,
        home=home,
        if k == "platlib" and _looks_like_red_hat_lib():
        if old_v == new_v:
        if part.endswith(ldversion):
        if skip_bpo_44860:
        if skip_cpython_build:
        if skip_linux_system_special_case:
        if skip_msys2_mingw_bug:
        if skip_osx_framework_user_special_case:
        if skip_pypy_special_case:
        if skip_slackware_user_scheme:
        ignore_config_files=True,
        isolated,
        isolated=isolated,
        k in INSTALL_SCHEMES
        new_v = pathlib.Path(getattr(new, k))
        old_v = pathlib.Path(getattr(old, k))
        paths = sysconfig.get_paths(scheme="posix_user", expand=False)
        platlib = platlib.replace("/$platlibdir/", f"/{_PLATLIBDIR}/")
        prefix,
        prefix=prefix,
        return
        return False
        return new
        return old
        return True
        root,
        root=root,
        skip_bpo_44860 = (
        skip_cpython_build = (
        skip_linux_system_special_case = (
        skip_msys2_mingw_bug = (
        skip_osx_framework_user_special_case = (
        skip_pypy_special_case = (
        skip_slackware_user_scheme = (
        sysconfig._PIP_USE_SYSCONFIG = True / False
        unix_user_platlib = INSTALL_SCHEMES["unix_user"]["platlib"]
        user,
        user=user,
        warning_contexts.append((old_v, new_v, f"scheme.{k}"))
        yield from parts
        yield part
    """
    """Check if the value is Debian's APT-controlled dist-packages.
    """Debian adds two additional schemes."""
    """MSYS2 patches distutils and sysconfig to use a UNIX-like scheme.
    """Red Hat patches ``sys.prefix`` and ``sys.exec_prefix``.
    """Red Hat patches platlib in unix_prefix and unix_home, but not purelib.
    """Return the default platform-shared lib location."""
    """Return the default pure-Python lib location."""
    """Slackware patches sysconfig but fails to patch distutils and site.
    """The resolution to bpo-44860 will change this incorrect platlib.
    """This function determines the value of _USE_SYSCONFIG.
    "get_bin_prefix",
    "get_bin_user",
    "get_major_minor_version",
    "get_platlib",
    "get_purelib",
    "get_scheme",
    "get_src_prefix",
    "site_packages",
    "USER_CACHE_DIR",
    "user_site",
    # a pip reinstall.
    # but import it soon enough that it is in memory and available during
    # Check if this path mismatch is caused by distutils config files. Those
    # deprecation message for them.
    # files will no longer work once we switch to sysconfig, so this raises a
    # Import distutils lazily to avoid deprecation warnings,
    # LDVERSION does not end with sys.abiflags. Just return the path unchanged.
    # Post warnings about this mismatch so user can report them back.
    # Strip sys.abiflags from LDVERSION-based path components.
    (fortunately?) done quite unconditionally, so we create a default command
    )
    *,
    ]
    _log_context(user=user, home=home, root=root, prefix=prefix)
    _MISMATCH_LEVEL = logging.DEBUG
    _MISMATCH_LEVEL = logging.WARNING
    _warn_mismatched(old, new, key=key)
    abiflags = getattr(sys, "abiflags", None)
    and is missing the final ``"site-packages"``.
    but here the default is ``deb_system`` instead of ``unix_local``. Ultimately
    But Python distributors can override this decision by setting:
    By default, pip uses sysconfig on Python 3.10+.
    cmd.finalize_options()
    cmd: Any = install(Distribution())
    command's ``prefix`` and ``exec_prefix`` to append ``"/local"``. This is
    Debian's ``distutils.sysconfig.get_python_lib()`` implementation returns the
    default package path controlled by APT, but does not patch ``sysconfig`` to
    default_old = _distutils.distutils_scheme(
    dist_name: str,
    do the same. This is similar to the bug worked around in ``get_scheme()``,
    except KeyError:
    except KeyError:  # User-site not available.
    for k in SCHEME_KEYS:
    for old_v, new_v, key in warning_contexts:
    for part in parts:
    from . import _distutils
    from distutils.command.install import install
    from distutils.command.install import INSTALL_SCHEMES
    from distutils.dist import Distribution
    get_major_minor_version,
    get_src_prefix,
    home: Optional[str] = None,
    However, MSYS2 incorrectly patches sysconfig ``nt`` scheme. The fix is
    if "/$platlibdir/" in platlib:
    if "/lib64/" not in platlib:
    if _looks_like_deb_system_dist_packages(old):
    if _USE_SYSCONFIG:
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="bin_prefix"):
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="platlib"):
    if _warn_if_mismatch(pathlib.Path(old), pathlib.Path(new), key="purelib"):
    if any(default_old[k] != getattr(old, k) for k in SCHEME_KEYS):
    if not _looks_like_debian_scheme():
    if not ldversion or not abiflags or not ldversion.endswith(abiflags):
    if not warning_contexts:
    if old == new:
    if user_site is None:  # User-site not available.
    if value == "/usr/lib/python3/dist-packages":
    is_osx_framework,
    isolated: bool = False,
    issue_url = "https://github.com/pypa/pip/issues/10151"
    ldversion = sysconfig.get_config_var("LDVERSION")
    likely going to be included in their 3.10 release, so we ignore the warning.
    logger.log(_MISMATCH_LEVEL, "\n".join(parts), user, home, root, prefix)
    logger.log(_MISMATCH_LEVEL, message, key, issue_url, old, new)
    message = (
    MSYS2 MINGW's patch uses lowercase ``"lib"`` instead of the usual uppercase,
    new = _sysconfig.get_bin_prefix()
    new = _sysconfig.get_platlib()
    new = _sysconfig.get_purelib()
    new = _sysconfig.get_scheme(
    object without any configuration to detect this.
    old = _distutils.get_bin_prefix()
    old = _distutils.get_platlib()
    old = _distutils.get_purelib()
    old = _distutils.get_scheme(
    parts = [
    path, but does not do the same to the site module.
    paths = sysconfig.get_paths("nt", expand=False)
    platlib = scheme["platlib"]
    prefix: Optional[str] = None,
    Rationale in https://github.com/pypa/pip/issues/10647
    Red Hat's ``00251-change-user-install-location.patch`` changes the install
    return "/lib64/" in paths["purelib"] and "/lib64/" not in user_site
    return "deb_system" in INSTALL_SCHEMES and "unix_local" in INSTALL_SCHEMES
    return (
    return _sysconfig.get_scheme("", user=True).scripts
    return all(
    return bool(getattr(sysconfig, "_PIP_USE_SYSCONFIG", _USE_SYSCONFIG_DEFAULT))
    return False
    return old
    return True
    return unix_user_platlib == "$usersite"
    return unpatched.replace("$platbase/", "$base/") == scheme["purelib"]
    root: Optional[str] = None,
    run.
    See <https://bugs.python.org/issue44860>.
    See msys2/MINGW-packages#9319.
    site_packages,
    skip the warning when needed.
    Slackware changes sysconfig's user scheme to use ``"lib64"`` for the lib
    This is a function for testability, but should be constant during any one
    This is the only way I can see to tell a Red Hat-patched Python.
    try:
    unpatched = platlib.replace("/lib64/", "/lib/")
    user: bool = False,
    USER_CACHE_DIR,
    user_site,
    warning_contexts = []
    we can't do anything about this Debian bug, and this detection allows us to
# Be noisy about incompatibilities if this platforms "should" be using
# sysconfig, but is explicitly opting out and using distutils instead.
)
) -> None:
) -> Scheme:
@functools.lru_cache(maxsize=None)
]
__all__ = [
_PLATLIBDIR: str = getattr(sys, "platlibdir", "lib")
_USE_SYSCONFIG = _should_use_sysconfig()
_USE_SYSCONFIG_DEFAULT = sys.version_info >= (3, 10)
def _fix_abiflags(parts: Tuple[str]) -> Generator[str, None, None]:
def _log_context(
def _looks_like_bpo_44860() -> bool:
def _looks_like_deb_system_dist_packages(value: str) -> bool:
def _looks_like_debian_scheme() -> bool:
def _looks_like_msys2_mingw_scheme() -> bool:
def _looks_like_red_hat_lib() -> bool:
def _looks_like_red_hat_patched_platlib_purelib(scheme: Dict[str, str]) -> bool:
def _looks_like_red_hat_scheme() -> bool:
def _looks_like_slackware_scheme() -> bool:
def _should_use_sysconfig() -> bool:
def _warn_if_mismatch(old: pathlib.Path, new: pathlib.Path, *, key: str) -> bool:
def _warn_mismatched(old: pathlib.Path, new: pathlib.Path, *, key: str) -> None:
def get_bin_prefix() -> str:
def get_bin_user() -> str:
def get_platlib() -> str:
def get_purelib() -> str:
def get_scheme(
else:
from . import _sysconfig
from .base import (
from pip._internal.models.scheme import SCHEME_KEYS, Scheme
from pip._internal.utils.compat import WINDOWS
from pip._internal.utils.deprecation import deprecated
from pip._internal.utils.virtualenv import running_under_virtualenv
from typing import Any, Dict, Generator, Optional, Tuple
if _USE_SYSCONFIG_DEFAULT and not _USE_SYSCONFIG:
if not _USE_SYSCONFIG:
import functools
import logging
import os
import pathlib
import sys
import sysconfig
logger = logging.getLogger(__name__)
