
            resources.files(__package__).joinpath("_in_process.py")
        )
        return resources.as_file(
        return resources.path(__package__, "_in_process.py")
    # Python 3.8 compatibility
    def _in_proc_script_path():
    resources.files
"""
"""This is a subpackage because the directory is on sys.path for _in_process.py
else:
except AttributeError:
import importlib.resources as resources
the backend might import.
The subpackage should stay as empty as possible to avoid shadowing modules that
try:
