
            # don't install entry point scripts into .egg file!
            # In case the path to the Python executable contains a space, wrap
            # it so it's not split up.
            bw_cmd = self.get_finalized_command("bdist_wininst")
            chmod(target, 0o777 - mask)
            ei_cmd.egg_base,
            ei_cmd.egg_name,
            ei_cmd.egg_version,
            ensure_directory(target)
            exec_param = "python.exe"
            exec_param = [exec_param]
            f = open(target, "w" + mode)
            f.close()
            f.write(contents)
            is_wininst = False
            is_wininst = getattr(bw_cmd, "_is_running", False)
            orig.install_scripts.run(self)  # run first to set up self.outfiles
            PathMetadata(ei_cmd.egg_base, ei_cmd.egg_info),
            return
            self.outfiles = []
            self.write_script(*args)
            writer = ei.WindowsScriptWriter
        """Write an executable file to the scripts directory"""
        # resolve the writer to the environment
        )
        bs_cmd = self.get_finalized_command("build_scripts")
        cmd = writer.command_spec_class.best().from_param(exec_param)
        dist = Distribution(
        ei_cmd = self.get_finalized_command("egg_info")
        else:
        except (ImportError, DistutilsModuleError):
        exec_param = getattr(bs_cmd, "executable", None)
        for args in writer.get_args(dist, cmd.as_header()):
        from setuptools.command.easy_install import chmod, current_umask
        if exec_param == sys.executable:
        if is_wininst:
        if not self.dry_run:
        if self.distribution.scripts:
        if self.no_ep:
        import setuptools.command.easy_install as ei
        log.info("Installing %s script to %s", script_name, self.install_dir)
        mask = current_umask()
        orig.install_scripts.initialize_options(self)
        self.no_ep = False
        self.outfiles.append(target)
        self.run_command("egg_info")
        target = os.path.join(self.install_dir, script_name)
        try:
        writer = ei.ScriptWriter
        writer = writer.best()
    """Do normal script install, plus any egg_info wrapper scripts"""
    def __init__(self, *args, **kwargs): pass
    def initialize_options(self):
    def run(self):
    def write_script(self, script_name, contents, mode="t", *ignored):
class install_scripts:
from distutils import log
from distutils.errors import DistutilsModuleError
from pkg_resources import Distribution, PathMetadata, ensure_directory
import distutils.command.install_scripts as orig
import os
import sys
