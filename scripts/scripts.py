
                              callable) or a filename (to make a script by
                              copying from a source location).
                              entry specification (to make a script from a
                        "Failed to write executable - trying to " "use .deleteme logic"
                        os.remove(dfname)
                        os.remove(dfname)  # Not allowed to fail here
                        pass  # still in use - ignore error
                        sysconfig.get_config_var("EXE"),
                        sysconfig.get_config_var("VERSION"),
                    "from the script encoding (%r)" % (shebang, encoding)
                    "python%s" % (sysconfig.get_config_var("EXE")),
                    "python%s%s"
                    "The shebang (%r) is not decodable "
                    # Failed writing an executable - it might be in use.
                    % (
                    )
                    ),
                    continue
                    date_time = time.gmtime(int(source_date_epoch))[:6]
                    dfname = "%s.deleteme" % outname
                    distlib_package,
                    except Exception:
                    ext = "py"
                    ext = "pyw"
                    if os.path.exists(dfname):
                    logger.debug("Able to replace executable using " ".deleteme logic")
                    logger.warning(
                    logger.warning("Skipping existing file %s", outname)
                    name,
                    os.rename(outname, dfname)  # nor here
                    outname = "{}.{}".format(outname, ext)
                    outname = n
                    return executable
                    return fp.read(2) == "#!"
                    self._fileop.set_executable_mode([outname])
                    self._fileop.write_binary_file(outname, script_bytes)
                    self.variant_separator,
                    self.version_info[0],
                    self.version_info[1],
                    sysconfig.get_config_var("BINDIR"),
                    try:
                    zf.writestr("__main__.py", script_bytes)
                    zf.writestr(zinfo, script_bytes)
                    zinfo = ZipInfo(filename="__main__.py", date_time=date_time)
                  https://hg.mozilla.org/mozilla-central/file/tip/mach
                "%s%s%s.%s"
                "python%s" % sysconfig.get_config_var("EXE"),
                # a version suffix are created, so we use python.exe
                # for Python builds from source on Windows, no Python executables with
                # Use wrapper exe for Jython on Windows
                # Workaround for Jython is not needed on Linux systems.
                % (
                )
                adjust = True
                args = " %s" % " ".join(args)
                bits = "32"
                bits = "64"
                else:
                encoding, lines = detect_encoding(f.readline)
                except Exception:
                executable = '"%s"' % executable
                executable = '{} "{}"'.format(env, _executable)
                executable = os.path.join(
                f.close()
                f.seek(0)
                if b"pythonw" in first_line:  # pragma: no cover
                if e.startswith(".py"):
                if java.lang.System.getProperty("os.name") == "Linux":
                if os.path.exists(outname) and not self.clobber:
                if self._is_nt and not outname.endswith("." + ext):  # pragma: no cover
                if self.set_mode:
                if source_date_epoch:
                import java
                launcher = self._get_launcher("t")
                launcher = self._get_launcher("w")
                logger.warning("%s is an empty file (skipping)", script)
                logger.warning("Failed to open %s", executable)
                max_shebang_length = 127
                max_shebang_length = 512
                msg = "Unable to find resource {} in package {}".format(
                n = os.path.basename(outname)
                n, e = os.path.splitext(outname)
                outname = "%s.exe" % outname
                post_interp = args.encode("utf-8")
                post_interp = match.group(1) or b""
                raise
                raise ValueError(
                raise ValueError(msg)
                return
                return executable
                return False
                self._fileop.set_executable_mode([outname])
                self._fileop.write_binary_file(outname, script_bytes)
                self._write_script([n], shebang, f.read(), filenames, ext)
                shebang = self._get_shebang(encoding, post_interp)
                shebang.decode(encoding)
                shebang_length <= max_shebang_length
                source_date_epoch = os.environ.get("SOURCE_DATE_EPOCH")
                sysconfig.get_path("scripts"),
                try:
                with open(executable) as fp:
            """
            # Add 3 for '#!' prefix and newline suffix.
            # determine it relative to the current package
            # Issue 31: don't hardcode an absolute package name, but
            (contains a #! line)
            )
            and "-X:Frames" not in post_interp
            and "-X:FullFrames" not in post_interp
            args = options.get("interpreter_args", [])
            Determine if the specified executable is a script
            distlib_package = __name__.rsplit(".", 1)[0]
            dn, fn = os.path.split(executable)
            elif executable.lower().endswith("jython.exe"):
            else:
            enquote = False  # assume this will be taken care of
            env, _executable = executable.split(" ", 1)
            except OSError:
            except UnicodeDecodeError:  # pragma: no cover
            executable = enquote_executable(executable)
            executable = get_executable()
            executable = os.path.join(
            executable = os.path.join(dn, fn)
            executable = self._fix_jython_executable(executable)
            executable = self._get_alternate_executable(executable, options)
            executable = self.executable
            ext = "py"
            ext = "pyw"
            f = None
            f = open(script, "rb")
            filenames.append(outname)
            filenames.extend(self.make(specification, options))
            first_line = f.readline()
            fn = fn.replace("python", "pythonw")
            func=entry.suffix,
            if " " in _executable and not _executable.startswith('"'):
            if args:
            if ext == "py":
            if f:
            if match:
            if not executable.startswith('"'):
            if not first_line:  # pragma: no cover
            if not resource:
            if not self._fileop.dry_run:
            if not self.dry_run:
            if os.name == "nt":
            if self._is_shell(executable):
            if self.set_mode:
            if struct.calcsize("P") == 8:  # 64-bit
            if sys.platform == "darwin":
            if use_launcher:  # pragma: no cover
            import_name=entry.suffix.split(".")[0],
            logger.debug("not copying %s (up-to-date)", script)
            logger.info("copying and adjusting %s -> %s", script, self.target_dir)
            match = FIRST_LINE_RE.match(first_line.replace(b"\r\n", b"\n"))
            module=entry.prefix,
            name = "{}{}{}.exe".format(kind, bits, platform_suffix)
            os.name == "java" and os._name == "posix"
            outname = os.path.join(self.target_dir, name)
            platform_suffix = "-arm" if get_platform() == "win-arm64" else ""
            post_interp += b" -X:Frames"
            raise ValueError("The shebang (%r) is not decodable from utf-8" % shebang)
            resource = finder(distlib_package).find(name)
            result += b"' '''"
            result += b"'''exec' " + executable + post_interp + b' "$0" "$@"\n'
            result = b"#!" + executable + post_interp + b"\n"
            result = b"#!/bin/sh\n"
            result.add(
            result.add("{}{}".format(name, self.version_info[0]))
            result.add(name)
            return
            return "/usr/bin/env %s" % executable
            return resource.bytes
            script_bytes = launcher + shebang + zip_data
            script_bytes = shebang + script_bytes
            self._copy_script(specification, filenames)
            self._fileop.copy_file(script, outname)
            self._make_script(entry, filenames, options=options)
            shebang += linesep
            shebang.decode("utf-8")
            shebang_length = len(executable) + len(post_interp) + 3
            simple_shebang = (b" " not in executable) and (
            simple_shebang = True
            stream = BytesIO()
            sys.platform == "cli"
            try:
            with ZipFile(stream, "w") as zf:
            zip_data = stream.getvalue()
        """
        # #coding:xxx cookie), the shebang has to be decodable from
        # Always open the file, but ignore failures in dry-run mode --
        # cater for executable paths with spaces (not uncommon on Windows)
        # check that the shebang is decodable using utf-8.
        # executable = os.path.normcase(executable)
        # Executable launcher support.
        # first line of a file, the #coding:xxx cookie cannot be
        # for example /usr/bin/env "/dir with spaces/bin/jython"
        # If the script is encoded to a custom encoding (use a
        # If the user didn't specify an executable, it may be necessary to
        # in case of IronPython, play safe and enable frames support
        # instead of "/usr/bin/env /dir with spaces/bin/jython"
        # issue #124. Although paths in Windows are generally case-insensitive,
        # Issue #51: don't use fsencode, since we later try to
        # it gets a #coding:xxx cookie. The shebang has to be the
        # It only makes sense to set mode bits on POSIX.
        # LATIN CAPITAL LETTER SHARP S - U+1E9E) is normcased to ß (which is a
        # LATIN SMALL LETTER SHARP S' - U+00DF). The two are not considered by
        # Launchers are from https://bitbucket.org/vinay.sajip/simple_launcher/
        # make sure we quote only the executable in case of env
        # N.B. The normalising operation above has been commented out: See
        # Normalise case for Windows - COMMENTED OUT
        # otherwise whole
        # Python parser starts to read a script using UTF-8 until
        # script.
        # that way, we'll get accurate feedback if we can read the
        # the script encoding too.
        # they aren't always. For example, a path containing a ẞ (which is a
        # UTF-8.
        # Windows as equivalent in path names.
        # written before. So the shebang has to be decodable from
        )
        ):  # pragma: no cover
        :param options: A dictionary of options controlling script generation.
        :param specification: The specification, which is either a valid export
        :param specifications: A list of specifications.
        :return: A list of all absolute pathnames written to,
        :return: A list of all absolute pathnames written to.
        adjust = False
        base = os.path.basename(exename)
        Build a shebang line. In the simple case (on Windows, or a shebang line
        def _fix_jython_executable(self, executable):
        def _get_launcher(self, kind):
        def _is_shell(self, executable):
        elif in_venv():  # pragma: no cover
        elif not sysconfig.is_python_build():
        else:
        else:  # pragma: no cover
        enquote = True
        entry = get_export_entry(specification)
        except OSError:  # pragma: no cover
        except UnicodeDecodeError:  # pragma: no cover
        executable = executable.encode("utf-8")
        filenames = []
        for name in names:
        for specification in specifications:
        if "" in self.variants:
        if "X" in self.variants:
        if "X.Y" in self.variants:
        if (
        if encoding != "utf-8":
        if enquote:
        if entry is None:
        if executable.startswith("/usr/bin/env "):
        if not adjust:
        if not self.force and not self._fileop.newer(script, outname):
        if not shebang.endswith(linesep):
        if not use_launcher:
        if options and options.get("gui", False):
        if options.get("gui", False) and self._is_nt:  # pragma: no cover
        if options:
        if os.name != "posix":
        if self.executable:
        if simple_shebang:
        if sys.platform.startswith("java"):  # pragma: no cover
        linesep = os.linesep.encode("utf-8")
        Make a script.
        outname = os.path.join(self.target_dir, os.path.basename(script))
        post_interp = b""
        result = set()
        return executable
        return filenames
        return result
        return self._fileop.dry_run
        return self.manifest % base
        return self.script_template % dict(
        return shebang
        script = os.path.join(self.source_dir, convert_path(script))
        script = self._get_script_text(entry).encode("utf-8")
        scriptnames = self.get_script_filenames(entry.name)
        See also: http://www.in-ulm.de/~mascheck/various/shebang/#length
        self, source_dir, target_dir, add_launchers=True, dry_run=False, fileop=None
        self._fileop = fileop or FileOperator(dry_run)
        self._fileop.dry_run = value
        self._is_nt = os.name == "nt" or (os.name == "java" and os._name == "nt")
        self._write_script(scriptnames, shebang, script, filenames, ext)
        self.add_launchers = add_launchers
        self.clobber = False
        self.force = False
        self.set_mode = (os.name == "posix") or (
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.variants = {"", "X.Y"}
        self.version_info = sys.version_info
        shebang = self._build_shebang(executable, post_interp)
        shebang = self._get_shebang("utf-8", post_interp, options=options)
        shebang which allows the script to run either under Python or sh, using
        suitable quoting. Thanks to Harald Nordgren for his input.
        Take a list of specifications and make scripts from them,
        the shebang. Otherwise, use /bin/sh as the executable, with a contrived
        try:
        use_launcher = self.add_launchers and self._is_nt
        which is not too long or contains spaces) use a simple formulation for
    """
    # Public API follows
    ):
    @dry_run.setter
    @property
    A class to copy or create scripts from source scripts or callable
    convert_path,
    def __init__(
    def _build_shebang(self, executable, post_interp):
    def _copy_script(self, script, filenames):
    def _get_alternate_executable(self, executable, options):
    def _get_script_text(self, entry):
    def _get_shebang(self, encoding, post_interp=b"", options=None):
    def _make_script(self, entry, filenames, options=None):
    def _write_script(self, names, shebang, script_bytes, filenames, ext):
    def dry_run(self):
    def dry_run(self, value):
    def get_manifest(self, exename):
    def get_script_filenames(self, name):
    def make(self, specification, options=None):
    def make_multiple(self, specifications, options=None):
    executable = None  # for shebangs
    FileOperator,
    get_executable,
    get_export_entry,
    get_platform,
    if " " in executable:
    if os.name == "nt" or (os.name == "java" and os._name == "nt"):  # pragma: no cover
    if sys.platform.startswith("java"):  # pragma: no cover
    in_venv,
    manifest = _DEFAULT_MANIFEST
    return executable
    script_template = SCRIPT_TEMPLATE
    specifications.
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(%(func)s())
    variant_separator = "-"
 <!-- Identify the application security requirements. -->
 </requestedPrivileges>
 </security>
 </trustInfo>
 <assemblyIdentity version="1.0.0.0"
 <requestedExecutionLevel level="asInvoker" uiAccess="false"/>
 <requestedPrivileges>
 <security>
 <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
 name="%s"
 processorArchitecture="X86"
 type="win32"/>
"""
#
# check if Python is called on the first line with this expression
# Copyright (C) 2013-2023 Vinay Sajip.
# Keep the old name around (for now), as there is at least one project using it!
# Licensed to the Python Software Foundation under a contributor agreement.
# See LICENSE.txt and CONTRIBUTORS.txt.
)
_DEFAULT_MANIFEST = """
_enquote_executable = enquote_executable
</assembly>""".strip()
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
class ScriptMaker:
def enquote_executable(executable):
FIRST_LINE_RE = re.compile(b"^#!.*pythonw?[0-9.]*([ \t].*)?$")
from %(module)s import %(import_name)s
from .compat import sysconfig, detect_encoding, ZipFile
from .resources import finder
from .util import (
from io import BytesIO
from zipfile import ZipInfo
if __name__ == '__main__':
import logging
import os
import re
import struct
import sys
import time
logger = logging.getLogger(__name__)
SCRIPT_TEMPLATE = r"""# -*- coding: utf-8 -*-
