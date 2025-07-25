
                        c_wchar_p(locked_handle),
                        c_wchar_p(text),
                        count * sizeof(c_wchar),
                    # function with the GMEM_MOVEABLE flag.
                    # http://msdn.com/ms649051
                    # If the hMem parameter identifies a memory object,
                    # the object must have been allocated using the
                    )
                    count = wcslen(text) + 1
                    ctypes.memmove(
                    handle = safeGlobalAlloc(GMEM_MOVEABLE, count * sizeof(c_wchar))
                    import PyQt4  # check if PyQt4 is installed
                    locked_handle = safeGlobalLock(handle)
                    pass  # We want to fail fast for all non-ImportError exceptions.
                    return init_qt_clipboard()
                    safeGlobalUnlock(handle)
                    safeSetClipboardData(CF_UNICODETEXT, handle)
                "/klipper",
                "org.kde.klipper",
                "Pyperclip cannot copy a blank string to the clipboard on Cygwin. "
                "Pyperclip cannot handle \\r characters on Cygwin.",
                "Pyperclip's support for Cygwin is not perfect, "
                "qdbus",
                "see https://github.com/asweigart/pyperclip/issues/55",
                "setClipboardContents",
                "This is effectively a no-op.",
                "waitForNewPaste() timed out after " + str(timeout) + " seconds."
                "waitForPaste() timed out after " + str(timeout) + " seconds."
                # (Also, it may return a handle to an empty buffer,
                # but technically that's not empty)
                # GetClipboardData may return NULL with errno == NO_ERROR
                # if the clipboard is empty.
                break
                else:
                except ImportError:
                if text:
                import PyQt5  # check if PyQt5 is installed
                return ""
                return init_qt_clipboard()
                safeEmptyClipboard()
                stacklevel=find_stack_level(),
                text.encode(ENCODING),
                try:
            # => We need a valid hwnd to copy something.
            # EmptyClipboard sets the clipboard owner to NULL;
            # http://msdn.com/ms649048
            # https://pypi.python.org/project/QtPy
            # If an application calls OpenClipboard with hwnd set to NULL,
            # If qtpy isn't installed, fall back on importing PyQt4.
            # qtpy is a small abstraction layer that lets you write applications
            # this causes SetClipboardData to fail.
            # using a single api call to either PyQt or PySide.
            )
            [
            ["pbcopy", "w"], stdin=subprocess.PIPE, close_fds=True
            ["pbpaste", "r"], stdout=subprocess.PIPE, close_fds=True
            ["powershell.exe", "-command", "Get-Clipboard"],
            ["qdbus", "org.kde.klipper", "/klipper", "getClipboardContents"],
            ["xclip", "-selection", selection, "-o"],
            ["xclip", "-selection", selection], stdin=subprocess.PIPE, close_fds=True
            ["xsel", selection_flag, "-i"], stdin=subprocess.PIPE, close_fds=True
            ["xsel", selection_flag, "-o"], stdout=subprocess.PIPE, close_fds=True
            ],
            0, b"STATIC", None, 0, 0, 0, 0, 0, None, None, None, None
            args.append("--clear")
            args.append(PRIMARY_SELECTION)
            clipboardContents = clipboardContents[:-1]
            close_fds=True,
            content = fd.read()
            else:
            except ImportError:
            f"Argument must be one of {', '.join(allowed_clipboard_types)}"
            f"can be copied to the clipboard, not {type(text).__name__}"
            f"only str, int, float, and bool values "
            fd.write(text)
            from PyQt4.QtGui import QApplication
            from PyQt5.QtWidgets import QApplication
            handle = safeGetClipboardData(CF_UNICODETEXT)
            if not handle:
            if success:
            import AppKit
            import Foundation  # check if pyobjc is installed
            import qtpy  # check if qtpy is installed
            p = subprocess.Popen(args, stdin=subprocess.PIPE, close_fds=True)
            p.communicate(input=None)
            p.communicate(input=text.encode(ENCODING))
            raise PyperclipException(EXCEPT_MSG)
            raise PyperclipTimeoutException(
            raise PyperclipWindowsException("Error calling " + self.f.__name__)
            raise PyperclipWindowsException("Error calling OpenClipboard")
            return c_wchar_p(handle).value
            return clipboardText
            return currentText
            return False
            return init_dev_clipboard_clipboard()
            return init_klipper_clipboard()
            return init_osx_pbcopy_clipboard()
            return init_osx_pyobjc_clipboard()
            return init_qt_clipboard()
            return init_wl_clipboard()
            return init_wsl_clipboard()
            return init_xclip_clipboard()
            return init_xsel_clipboard()
            safeCloseClipboard()
            safeDestroyWindow(hwnd)
            selection = PRIMARY_SELECTION
            selection_flag = PRIMARY_SELECTION
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stdout = p.communicate()[0]
            stdout=subprocess.PIPE,
            subprocess.check_call(args, close_fds=True)
            success = OpenClipboard(hwnd)
            time.sleep(0.01)
            try:
            warnings.warn(
            with clipboard(hwnd):
            yield
            yield hwnd
        - klipper
        - no (this is what is set when no clipboard mechanism can be found)
        - pbcopy
        - pyobjc (default on macOS)
        - qt
        - windows (default on Windows)
        - xclip
        - xsel
        """
        """Copy string argument to clipboard"""
        """Returns contents of clipboard"""
        "cygwin" in platform.system().lower()
        "klipper": init_klipper_clipboard,
        "no": init_no_clipboard,
        "pbcopy": init_osx_pbcopy_clipboard,
        "pyobjc": init_osx_pyobjc_clipboard,
        "qt": init_qt_clipboard,  # TODO - split this into 'qtpy', 'pyqt4', and 'pyqt5'
        "windows": init_windows_clipboard,
        "wl-clipboard": init_wl_clipboard,
        "xclip": init_xclip_clipboard,
        "xsel": init_xsel_clipboard,
        # as predefined lpClass is just fine.
        # even if blank, Klipper will append a newline at the end
        # FIXME(pyperclip#55): pyperclip currently does not support Cygwin,
        # http://msdn.com/ms649016#_win32_Copying_Information_to_the_Clipboard
        # Intentionally ignore extraneous output on stderr when clipboard is empty
        # make sure that newline is there
        # see https://github.com/asweigart/pyperclip/issues/55
        # some other application is accessing it (?)
        # such as 'CYGWIN_NT-6.1'
        # This function is heavily based on
        # TODO: https://github.com/asweigart/pyperclip/issues/43
        # We may not get the clipboard handle immediately because
        # we really just need the hwnd, so setting "STATIC"
        # We try for at least 500ms to get the clipboard.
        # Workaround for https://bugs.kde.org/show_bug.cgi?id=342874
        # WSL appends "\r\n" to the contents.
        )
        ) as p:
        allowed_clipboard_types = [repr(_) for _ in clipboard_types]
        app = QApplication([])
        args = ["wl-copy"]
        args = ["wl-paste", "-n"]
        assert clipboardContents.endswith("\n")
        assert len(clipboardContents) > 0
        board = AppKit.NSPasteboard.generalPasteboard()
        board.declareTypes_owner_([AppKit.NSStringPboardType], None)
        board.setData_forType_(newData, AppKit.NSStringPboardType)
        BOOL,
        cb = app.clipboard()
        cb.setText(text)
        clipboardContents = stdout.decode(ENCODING)
        clipboardText = paste()
        content = board.stringForType_(AppKit.NSStringPboardType)
        Context manager that opens the clipboard and prevents
        Context that provides a valid Windows hwnd.
        currentText = paste()
        def __bool__(self) -> bool:
        def __call__(self, *args, **kwargs):
        DWORD,
        else:
        except ImportError:
        finally:
        from qtpy.QtWidgets import QApplication
        HANDLE,
        HGLOBAL,
        HINSTANCE,
        HMENU,
        hwnd = safeCreateWindowExA(
        HWND,
        if "\r" in text:
        if _executable_exists("klipper") and _executable_exists("qdbus"):
        if _executable_exists("wslconfig.exe"):
        if _executable_exists("xclip"):
        if _executable_exists("xsel"):
        if clipboardContents.endswith("\n"):
        if clipboardText != "":
        if currentText != originalText:
        if not ret and get_errno():
        if not success:
        if not text:
        if os.environ.get("WAYLAND_DISPLAY") and _executable_exists("wl-copy"):
        if os.path.exists("/dev/clipboard"):
        if primary:
        if text == "":
        if timeout is not None and time.time() > startTime + timeout:
        INT,
        LPCSTR,
        LPVOID,
        newData = newStr.dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
        newStr = Foundation.NSString.stringWithString_(text).nsstring()
        other applications from modifying the clipboard content.
        p = subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True)
        raise PyperclipException(
        raise ValueError(
        ret = self.f(*args)
        return clipboardContents
        return content
        return init_windows_clipboard()
        return ret
        return stdout.decode(ENCODING)
        return stdout[:-2].decode(ENCODING)
        return str(cb.text())
        selection = DEFAULT_SELECTION
        selection_flag = DEFAULT_SELECTION
        setattr(self.f, key, value)
        stdout, _stderr = p.communicate()
        success = False
        super().__setattr__("f", f)
        t = time.time() + 0.5
        text = _stringifyText(text)  # Converts non-str values to str.
        time.sleep(0.01)
        try:
        UINT,
        while time.time() < t:
        with clipboard(None):
        with open("/dev/clipboard", "w", encoding="utf-8") as fd:
        with open("/dev/clipboard", encoding="utf-8") as fd:
        with subprocess.Popen(
        with subprocess.Popen(["clip.exe"], stdin=subprocess.PIPE, close_fds=True) as p:
        with window() as hwnd:
    - klipper
    - pbcopy
    - pbpaste
    - qdbus
    - wl-copy/wl-paste
    - xclip
    - xsel
    """
    """This function call blocks until a new text string exists on the
    """This function call blocks until a non-empty text string exists on the
    "copy",
    "determine_clipboard",
    "paste",
    "set_clipboard",
    "waitForNewPaste",
    "waitForPaste",
    # $DISPLAY should exist
    # Sets pyperclip's copy() and paste() functions:
    # Setup for the CYGWIN platform:
    # Setup for the LINUX platform:
    # Setup for the macOS platform:
    # Setup for the WINDOWS platform:
    # Try to import from qtpy, but if that fails try PyQt5 then PyQt4
    )
    ):  # Cygwin has a variety of values returned by platform.system(),
    @contextlib.contextmanager
    ]
    }
    a number of seconds that has elapsed without non-empty text being put on
    A stub function for copy(), which will load the real copy() function when
    A stub function for paste(), which will load the real paste() function when
    acceptedTypes = (str, int, float, bool)
    accordingly.
    app = QApplication.instance()
    automatically chooses.
    automatically run, which will automatically select a clipboard mechanism.
    but the user was just going to immediately call set_clipboard() to use a
    c_size_t,
    c_wchar,
    c_wchar_p,
    call set_clipboard() to pick another clipboard mechanism. Or, if the user
    called so that the real copy() function is used for later calls.
    called so that the real paste() function is used for later calls.
    CF_UNICODETEXT = 13
    class ClipboardUnavailable:
    clipboard that is different from the text that was there when the function
    clipboard. It returns this text.
    clipboard_types = {
    commands. (These commands should come with OS X.).
    copy, paste = clipboard_types[clipboard]()
    copy, paste = determine_clipboard()
    def __call__(self, *args):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, f) -> None:
    def __setattr__(self, key, value):
    def clipboard(hwnd):
    def copy_dev_clipboard(text):
    def copy_klipper(text):
    def copy_osx_pbcopy(text):
    def copy_osx_pyobjc(text):
    def copy_qt(text):
    def copy_windows(text):
    def copy_wl(text, primary=False):
    def copy_wsl(text):
    def copy_xclip(text, primary=False):
    def copy_xsel(text, primary=False):
    def paste_dev_clipboard() -> str:
    def paste_klipper():
    def paste_osx_pbcopy():
    def paste_osx_pyobjc():
    def paste_qt() -> str:
    def paste_windows():
    def paste_wl(primary=False):
    def paste_wsl():
    def paste_xclip(primary=False):
    def paste_xsel(primary=False):
    def window():
    DEFAULT_SELECTION = "-b"
    DEFAULT_SELECTION = "c"
    Determine the OS/platform and set the copy() and paste() functions
    different clipboard mechanism.
    elif os.name == "nt" or platform.system() == "Windows":
    except ImportError:
    Explicitly sets the clipboard mechanism. The "clipboard mechanism" is how
    For more information, please visit
    from ctypes.wintypes import (
    get_errno,
    global copy, paste
    global Foundation, AppKit, qtpy, PyQt4, PyQt5
    global HGLOBAL, LPVOID, DWORD, LPCSTR, INT
    global HWND, HINSTANCE, HMENU, BOOL, UINT, HANDLE
    global QApplication
    GMEM_MOVEABLE = 0x0002
    https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
    if (
    if app is None:
    if clipboard not in clipboard_types:
    if HAS_DISPLAY:
    if not isinstance(text, acceptedTypes):
    if os.name == "mac" or platform.system() == "Darwin":
    if platform.system() == "Linux":
    implement the copy/paste feature. The clipboard parameter must be one of:
    msvcrt = ctypes.CDLL("msvcrt")
    OpenClipboard = windll.user32.OpenClipboard
    OpenClipboard.argtypes = [HWND]
    OpenClipboard.restype = BOOL
    originalText = paste()
    PRIMARY_SELECTION = "p"
    PRIMARY_SELECTION = "-p"
    print("Copy functionality unavailable!")
    Pyperclip could not find a copy/paste mechanism for your system.
    PyperclipException,
    PyperclipWindowsException,
    return ClipboardUnavailable(), ClipboardUnavailable()
    return copy != lazy_load_stub_copy and paste != lazy_load_stub_paste
    return copy(text)
    return copy_dev_clipboard, paste_dev_clipboard
    return copy_klipper, paste_klipper
    return copy_osx_pbcopy, paste_osx_pbcopy
    return copy_osx_pyobjc, paste_osx_pyobjc
    return copy_qt, paste_qt
    return copy_windows, paste_windows
    return copy_wl, paste_wl
    return copy_wsl, paste_wsl
    return copy_xclip, paste_xclip
    return copy_xsel, paste_xsel
    return init_no_clipboard()
    return paste()
    return str(text)
    safeCloseClipboard = CheckedCall(windll.user32.CloseClipboard)
    safeCloseClipboard.argtypes = []
    safeCloseClipboard.restype = BOOL
    safeCreateWindowExA = CheckedCall(windll.user32.CreateWindowExA)
    safeCreateWindowExA.argtypes = [
    safeCreateWindowExA.restype = HWND
    safeDestroyWindow = CheckedCall(windll.user32.DestroyWindow)
    safeDestroyWindow.argtypes = [HWND]
    safeDestroyWindow.restype = BOOL
    safeEmptyClipboard = CheckedCall(windll.user32.EmptyClipboard)
    safeEmptyClipboard.argtypes = []
    safeEmptyClipboard.restype = BOOL
    safeGetClipboardData = CheckedCall(windll.user32.GetClipboardData)
    safeGetClipboardData.argtypes = [UINT]
    safeGetClipboardData.restype = HANDLE
    safeGlobalAlloc = CheckedCall(windll.kernel32.GlobalAlloc)
    safeGlobalAlloc.argtypes = [UINT, c_size_t]
    safeGlobalAlloc.restype = HGLOBAL
    safeGlobalLock = CheckedCall(windll.kernel32.GlobalLock)
    safeGlobalLock.argtypes = [HGLOBAL]
    safeGlobalLock.restype = LPVOID
    safeGlobalUnlock = CheckedCall(windll.kernel32.GlobalUnlock)
    safeGlobalUnlock.argtypes = [HGLOBAL]
    safeGlobalUnlock.restype = BOOL
    safeSetClipboardData = CheckedCall(windll.user32.SetClipboardData)
    safeSetClipboardData.argtypes = [UINT, HANDLE]
    safeSetClipboardData.restype = HANDLE
    simply calls copy() or paste() without calling set_clipboard() first,
    sizeof,
    startTime = time.time()
    sudo apt-get install wl-clipboard
    sudo apt-get install xclip
    sudo apt-get install xsel
    the clipboard."""
    the copy() and paste() functions interact with the operating system to
    The lazy loading this stub function implements gives the user a chance to
    This allows users to import pyperclip without having determine_clipboard()
    This could be a problem if it selects, say, the memory-heavy PyQt4 module
    This function raises PyperclipTimeoutException if timeout was set to
    try:
    was first called. It returns this text.
    wcslen = CheckedCall(msvcrt.wcslen)
    wcslen.argtypes = [c_wchar_p]
    wcslen.restype = UINT
    while True:
    will fall back on whatever clipboard mechanism that determine_clipboard()
    windll = ctypes.windll
  if not pyperclip.is_available():
  import pyperclip
  pyperclip.copy('The text to be copied to the clipboard.')
  spam = pyperclip.paste()
"""
# `import PyQt4` sys.exit()s if DISPLAY is not in the environment.
# and importing is done in determine_clipboard():
# and not load PyQt4 if it is absent.
# Automatic detection of clipboard mechanisms
# Initially, copy() and paste() are set to lazy loading wrappers which will
# pandas aliases
# set `copy` and `paste` to real functions the first time they're used, unless
# set_clipboard() or determine_clipboard() is called first.
# Thus, we need to detect the presence of $DISPLAY manually
# Windows-related clipboard functions:
)
]
__all__ = [
__version__ = "1.8.2"
A cross-platform clipboard module for Python,
A malicious user could rename or add programs with these names, tricking
By Al Sweigart al@inventwithpython.com
class CheckedCall:
class PyperclipTimeoutException:
clipboard_get = paste
clipboard_set = copy
copy, paste = lazy_load_stub_copy, lazy_load_stub_paste
Cygwin is currently not supported.
def _stringifyText(text) -> str:
def determine_clipboard():
def init_dev_clipboard_clipboard():
def init_klipper_clipboard():
def init_no_clipboard():
def init_osx_pbcopy_clipboard():
def init_osx_pyobjc_clipboard():
def init_qt_clipboard():
def init_windows_clipboard():
def init_wl_clipboard():
def init_wsl_clipboard():
def init_xclip_clipboard():
def init_xsel_clipboard():
def is_available() -> bool:
def lazy_load_stub_copy(text):
def lazy_load_stub_paste():
def set_clipboard(clipboard):
def waitForNewPaste(timeout=None):
def waitForPaste(timeout=None):
ENCODING = "utf-8"
EXCEPT_MSG = """
For example, in Debian:
from ctypes import (
from pandas.errors import (
from pandas.util._exceptions import find_stack_level
from shutil import which as _executable_exists
HAS_DISPLAY = os.getenv("DISPLAY")
import contextlib
import ctypes
import os
import platform
import subprocess
import time
import warnings
Licence at LICENSES/PYPERCLIP_LICENSE
On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via
On Mac, the pyobjc module is used, falling back to the pbcopy and pbpaste cli
On Windows, no additional modules are needed.
Otherwise on Linux, you will need the PyQt5 modules installed.
package manager.
Pyperclip
Pyperclip into running them with whatever permissions the Python process has.
Security Note: This module runs programs with these names:
This module does not work with PyGObject yet.
Usage:
with copy & paste functions for plain text.
