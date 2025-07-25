
            from pip._vendor.platformdirs.android import Android
            return Android  # return to avoid redefinition of result
            return Result
        appauthor=appauthor,
        appname=appname,
        ensure_exists=ensure_exists,
        from pip._vendor.platformdirs.android import _android_folder
        from pip._vendor.platformdirs.macos import MacOS as Result
        from pip._vendor.platformdirs.unix import Unix as Result
        from pip._vendor.platformdirs.windows import Windows as Result
        from pip._vendor.typing_extensions import Literal
        from typing import Literal
        if _android_folder() is not None:
        if os.getenv("SHELL") or os.getenv("PREFIX"):
        multipath=multipath,
        opinion=opinion,
        roaming=roaming,
        version=version,
    """
    """:returns: documents directory tied to the user"""
    """:returns: documents path tied to the user"""
    """:returns: downloads directory tied to the user"""
    """:returns: downloads path tied to the user"""
    """:returns: music directory tied to the user"""
    """:returns: music path tied to the user"""
    """:returns: pictures directory tied to the user"""
    """:returns: pictures path tied to the user"""
    """:returns: videos directory tied to the user"""
    """:returns: videos path tied to the user"""
    "__version__",
    "__version_info__",
    "AppDirs",
    "PlatformDirs",
    "PlatformDirsABC",
    "site_cache_dir",
    "site_cache_path",
    "site_config_dir",
    "site_config_path",
    "site_data_dir",
    "site_data_path",
    "user_cache_dir",
    "user_cache_path",
    "user_config_dir",
    "user_config_path",
    "user_data_dir",
    "user_data_path",
    "user_documents_dir",
    "user_documents_path",
    "user_downloads_dir",
    "user_downloads_path",
    "user_log_dir",
    "user_log_path",
    "user_music_dir",
    "user_music_path",
    "user_pictures_dir",
    "user_pictures_path",
    "user_runtime_dir",
    "user_runtime_path",
    "user_state_dir",
    "user_state_path",
    "user_videos_dir",
    "user_videos_path",
    ).site_cache_dir
    ).site_cache_path
    ).site_config_dir
    ).site_config_path
    ).site_data_dir
    ).site_data_path
    ).user_cache_dir
    ).user_cache_path
    ).user_config_dir
    ).user_config_path
    ).user_data_dir
    ).user_data_path
    ).user_log_dir
    ).user_log_path
    ).user_runtime_dir
    ).user_runtime_path
    ).user_state_dir
    ).user_state_path
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :param multipath: See `multipath <platformdirs.api.PlatformDirsABC.multipath>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :returns: cache directory tied to the user
    :returns: cache path tied to the user
    :returns: config directory shared by the users
    :returns: config directory tied to the user
    :returns: config path shared by the users
    :returns: config path tied to the user
    :returns: data directory shared by users
    :returns: data directory tied to the user
    :returns: data path shared by users
    :returns: data path tied to the user
    :returns: log directory tied to the user
    :returns: log path tied to the user
    :returns: runtime directory tied to the user
    :returns: runtime path tied to the user
    :returns: state directory tied to the user
    :returns: state path tied to the user
    appauthor: str | None | Literal[False] = None,
    appname: str | None = None,
    elif sys.platform == "darwin":
    else:
    else:  # pragma: no cover (py38+)
    ensure_exists: bool = False,  # noqa: FBT001, FBT002
    from pathlib import Path
    if os.getenv("ANDROID_DATA") == "/data" and os.getenv("ANDROID_ROOT") == "/system":
    if sys.platform == "win32":
    if sys.version_info >= (3, 8):  # pragma: no cover (py38+)
    multipath: bool = False,  # noqa: FBT001, FBT002
    opinion: bool = True,  # noqa: FBT001, FBT002
    return PlatformDirs(
    return PlatformDirs().user_documents_dir
    return PlatformDirs().user_documents_path
    return PlatformDirs().user_downloads_dir
    return PlatformDirs().user_downloads_path
    return PlatformDirs().user_music_dir
    return PlatformDirs().user_music_path
    return PlatformDirs().user_pictures_dir
    return PlatformDirs().user_pictures_path
    return PlatformDirs().user_videos_dir
    return PlatformDirs().user_videos_path
    return Result
    roaming: bool = False,  # noqa: FBT001, FBT002
    version: str | None = None,
"""
) -> Path:
) -> str:
]
__all__ = [
AppDirs = PlatformDirs  #: Backwards compatibility with appdirs
def _set_platform_dir_class() -> type[PlatformDirsABC]:
def site_cache_dir(
def site_cache_path(
def site_config_dir(
def site_config_path(
def site_data_dir(
def site_data_path(
def user_cache_dir(
def user_cache_path(
def user_config_dir(
def user_config_path(
def user_data_dir(
def user_data_path(
def user_documents_dir() -> str:
def user_documents_path() -> Path:
def user_downloads_dir() -> str:
def user_downloads_path() -> Path:
def user_log_dir(
def user_log_path(
def user_music_dir() -> str:
def user_music_path() -> Path:
def user_pictures_dir() -> str:
def user_pictures_path() -> Path:
def user_runtime_dir(
def user_runtime_path(
def user_state_dir(
def user_state_path(
def user_videos_dir() -> str:
def user_videos_path() -> Path:
from .api import PlatformDirsABC
from .version import __version__
from .version import __version_tuple__ as __version_info__
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import os
import sys
PlatformDirs = _set_platform_dir_class()  #: Currently active platform
usage.
Utilities for determining application-specific dirs. See <https://github.com/platformdirs/platformdirs> for details and
