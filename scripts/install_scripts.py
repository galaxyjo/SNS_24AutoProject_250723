
                    log.info("changing mode of %s to %o", file, mode)
                    log.info("changing mode of %s", file)
                    mode = ((os.stat(file)[ST_MODE]) | 0o555) & 0o7777
                    os.chmod(file, mode)
                else:
                if self.dry_run:
            "install",
            # all the scripts we just installed.
            # Set the executable bits (owner, group, and world) on
            ("force", "force"),
            ("install_scripts", "install_dir"),
            ("skip_build", "skip_build"),
            for file in self.get_outputs():
            self.run_command("build_scripts")
        ("build-dir=", "b", "build directory (where to install from)"),
        ("force", "f", "force installation (overwrite existing files)"),
        ("install-dir=", "d", "directory to install scripts to"),
        ("skip-build", None, "skip the build steps"),
        )
        if not self.skip_build:
        if os.name == "posix":
        return self.distribution.scripts or []
        return self.outfiles or []
        self.build_dir = None
        self.force = 0
        self.install_dir = None
        self.outfiles = self.copy_tree(self.build_dir, self.install_dir)
        self.set_undefined_options(
        self.set_undefined_options("build", ("build_scripts", "build_dir"))
        self.skip_build = None
    ]
    boolean_options = ["force", "skip-build"]
    def __init__(self, *args, **kwargs): pass
    def finalize_options(self):
    def get_inputs(self):
    def get_outputs(self):
    def initialize_options(self):
    def run(self):
    description = "install scripts (Python or otherwise)"
    user_options = [
"""distutils.command.install_scripts
# contributed by Bastian Kleineidam
class install_scripts:
from distutils import log
from stat import ST_MODE
Implements the Distutils 'install_scripts' command, for installing
import os
Python scripts."""
