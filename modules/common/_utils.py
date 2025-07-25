
                cmd, stdout=null, stderr=subprocess.STDOUT, **_popen_kwargs()
            )
            creationflags = 0x00000200
            preexec_fn = os.setpgrp  # the _pre_exec does not seem to work
            subprocess.check_call(
        "creationflags": creationflags,
        "No ffmpeg exe could be found. Install ffmpeg on your system, "
        "or set the IMAGEIO_FFMPEG_EXE environment variable."
        "preexec_fn": preexec_fn,
        "startupinfo": startupinfo,
        # https://stackoverflow.com/questions/5045771
        # Prevent propagation of sigint (see #4)
        # Stops executable from flashing on Windows (see #22)
        # Unset preexec_fn to work around a strange hang on fork() (see #58)
        b"\n", 1
        context = importlib.resources.as_file(ref)
        context = importlib.resources.path("imageio_ffmpeg.binaries", "__init__.py")
        else:
        exe = os.path.join(sys.prefix, "bin", "ffmpeg")
        exe = os.path.join(sys.prefix, "Library", "bin", "ffmpeg.exe")
        if sys.platform.startswith("win"):
        pass
        preexec_fn = None
        ref = importlib.resources.files("imageio_ffmpeg.binaries") / "__init__.py"
        return exe
        return False
        return True
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        with open(os.devnull, "w") as null:
    """
    # (installed e.g. via `conda install ffmpeg -c conda-forge`)
    # 1. Try environment variable. - Dont test it: the user is explicit here!
    # 2. Try from here
    # 3. Try binary from conda package
    # 4. Try system ffmpeg command
    # Auto-detect
    # Nothing was found
    # Return the dir. We assume that the data files are on a normal dir on the fs.
    )
    )[0]
    }
    cmd = [exe, "-version"]
    creationflags = 0
    else:
    except (OSError, ValueError, subprocess.CalledProcessError):
    exe = "ffmpeg"
    exe = _get_ffmpeg_exe()
    exe = get_ffmpeg_exe()
    exe = os.getenv("IMAGEIO_FFMPEG_EXE", None)
    exe = os.path.join(_get_bin_dir(), FNAME_PER_PLATFORM.get(plat, ""))
    falsy = ("", "0", "false", "no")
    ffmpeg could be found.
    Get the ffmpeg executable file. This can be the binary defined by
    Get the version of the used ffmpeg executable (as a string).
    if _is_valid_exe(exe):
    if exe and os.path.isfile(exe) and _is_valid_exe(exe):
    if exe:
    if os.getenv("IMAGEIO_FFMPEG_NO_PREVENT_SIGINT", "").lower() not in falsy:
    if plat.startswith("win"):
    if prevent_sigint:
    if sys.platform.startswith("win"):
    if sys.version_info < (3, 9):
    line = line.decode(errors="ignore").strip()
    line = subprocess.check_output([exe, "-version"], **_popen_kwargs()).split(
    plat = get_platform()
    preexec_fn = None
    raise RuntimeError(
    return {
    return None
    return str(path.parent)
    return version
    startupinfo = None
    system ffmpeg (in that order). A RuntimeError is raised if no valid
    the IMAGEIO_FFMPEG_EXE environment variable, the binary distributed
    try:
    version = line.split("version", 1)[-1].lstrip().split(" ", 1)[0].strip()
    with context as path:
    with imageio-ffmpeg, an ffmpeg binary installed with conda, or the
@lru_cache()
def _get_bin_dir():
def _get_ffmpeg_exe():
def _is_valid_exe(exe):
def _popen_kwargs(prevent_sigint=False):
def get_ffmpeg_exe():
def get_ffmpeg_version():
from ._definitions import FNAME_PER_PLATFORM, get_platform
from functools import lru_cache
import importlib.resources
import logging
import os
import subprocess
import sys
logger = logging.getLogger("imageio_ffmpeg")
