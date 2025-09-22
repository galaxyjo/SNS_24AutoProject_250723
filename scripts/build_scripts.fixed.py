
sysconfig.get_config_var("EXE"),
                                sysconfig.get_config_var("VERSION"),
                            "changing mode of %s from %o to %o", file, oldmode, newmode
                            "from the script encoding ({})".format(shebang, encoding)
                            "from utf-8".format(shebang)
                            "python%s%s"
                            "The shebang ({!r}) is not decodable "
                            % (
                            ),
                            sysconfig.get_config_var("BINDIR"),
                        )
                        executable = os.path.join(
                        executable = self.executable
                        log.info(
                        os.chmod(file, newmode)
                        outf.write(shebang)
                        outf.writelines(f.readlines())
                        raise ValueError(
                        shebang.decode("utf-8")
                        shebang.decode(encoding)
                    # #coding:xxx cookie), the shebang has to be decodable from
                    # first line of a file, the #coding:xxx cookie cannot be
                    # If the script is encoded to a custom encoding (use a
                    # it gets a #coding:xxx cookie. The shebang has to be the
                    # Python parser starts to read a script using UTF-8 until
                    # the script encoding too.
                    # UTF-8.
                    # written before. So the shebang has to be decodable from
                    adjust = True
                    continue
                    else:
                    except UnicodeDecodeError:
                    executable = os.fsencode(executable)
                    f.close()
                    if newmode != oldmode:
                    if not sysconfig.python_build:
                    log.info("changing mode of %s", file)
                    newmode = (oldmode | 0o555) & 0o7777
                    oldmode = os.stat(file)[ST_MODE] & 0o7777
                    post_interp = match.group(1) or b""
                    raise
                    self.warn("%s is an empty file (skipping)" % script)
                    shebang = b"#!" + executable + post_interp + b"\n"
                    try:
                    with open(outfile, "wb") as outf:
                continue
                else:
                encoding, lines = tokenize.detect_encoding(f.readline)
                f = None
                f = open(script, "rb")
                f.seek(0)
                first_line = f.readline()
                if f:
                if match:
                if not first_line:
                if not self.dry_run:
                if self.dry_run:
                log.debug("not copying %s (up-to-date)", script)
                log.info("copying and adjusting %s -> %s", script, self.build_dir)
                match = first_line_re.match(first_line)
                self.copy_file(script, outfile)
                updated_files.append(outfile)
            "build",
            # Always open the file, but ignore failures in dry-run mode --
            # script.
            # that way, we'll get accurate feedback if we can read the
            ("build_scripts", "build_dir"),
            ("executable", "executable"),
            ("force", "force"),
            adjust = False
            else:
            except OSError:
            for file in outfiles:
            if adjust:
            if not self.force and not newer(script, outfile):
            outfile = os.path.join(self.build_dir, os.path.basename(script))
            outfiles.append(outfile)
            return
            script = convert_path(script)
            try:
        """
        # XXX should we modify self.outfiles?
        ("build-dir=", "d", 'directory to "build" (copy) to'),
        ("executable=", "e", "specify final destination interpreter path"),
        ("force", "f", "forcibly build everything (ignore file timestamps"),
        )
        for script in self.scripts:
        ie. starts with "\#!" and contains "python"), then adjust the first
        if not self.scripts:
        if os.name == "posix":
        line to refer to the current Python interpreter as we copy.
        outfiles = []
        Python script in the Unix way (first line matches 'first_line_re',
        r"""Copy each script listed in 'self.scripts'; if it's marked as a
        return outfiles, updated_files
        return self.scripts
        self.build_dir = None
        self.copy_scripts()
        self.executable = None
        self.force = None
        self.mkpath(self.build_dir)
        self.outfiles = None
        self.scripts = None
        self.scripts = self.distribution.scripts
        self.set_undefined_options(
        updated_files = []
    ]
    boolean_options = ["force"]
    def __init__(self, *args, **kwargs): pass
    def copy_scripts(self):
    def finalize_options(self):
    def get_source_files(self):
    def initialize_options(self):
    def run(self):
    description = '"build" scripts (copy and fixup #! line)'
    user_options = [
"""distutils.command.build_scripts
# check if Python is called on the first line with this expression
class build_scripts:
first_line_re = re.compile(b"^#!.*python[0-9.]*([ \t].*)?$")
from distutils import log
from distutils import sysconfig
from distutils.dep_util import newer
from distutils.util import convert_path
from stat import ST_MODE
Implements the Distutils 'build_scripts' command."""
import os
import re
import tokenize

pass
