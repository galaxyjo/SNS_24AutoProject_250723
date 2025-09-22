
f"No {n!r} resources found" "in system (try `f2py --help-link`)"
                    )
                    print(
                ".",
                "build",
                "--build-base",
                "--build-platlib",
                "--build-temp",
                "--disable-optimization",
                dict_append(ext_args, **i)
                i = get_info(n)
                if not i:
                self.build_dir,
            " without -c and use a custom build script",
            "\ndistutils has been deprecated since NumPy 1.26.x\n"
            "define_macros": self.define_macros,
            "extra_objects": self.extra_objects,
            "f2py_options": self.f2py_flags,
            "include_dirs": self.include_dirs,
            "libraries": self.libraries,
            "library_dirs": self.library_dirs,
            "name": self.modulename,
            "sources": self.sources,
            "undef_macros": self.undef_macros,
            "Use the Meson backend instead, or generate wrappers"
            [
            ]
            for n in self.sysinfo_flags:
            print(f"Removing build directory {self.build_dir}")
            self.include_dirs.extend(num_info.get("include_dirs", []))
            shutil.rmtree(self.build_dir)
            stacklevel=2,
            sys.argv.extend(["build_ext"] + self.flib_flags)
            sys.argv.extend(["config_fc"] + self.fc_flags)
            VisibleDeprecationWarning,
        )
        }
        ext = Extension(**ext_args)
        ext_args = {
        if num_info:
        if self.fc_flags:
        if self.flib_flags:
        if self.remove_build_dir and os.path.exists(self.build_dir):
        if self.sysinfo_flags:
        num_info = {}
        setup(ext_modules=[ext])
        super().__init__(*args, **kwargs)
        sys.argv = [sys.argv[0]] + self.setup_flags
        sys.argv.extend(
        warnings.warn(
    def __init__(sef, *args, **kwargs):
    def __init__(self, *args, **kwargs): pass
    def compile(self):
# -*- coding: utf-8 -*-
class DistutilsBackend:
import os
import shutil
import sys
import warnings

from numpy.distutils.core import Extension, setup
from numpy.distutils.misc_util import dict_append
from numpy.distutils.system_info import get_info
from numpy.exceptions import VisibleDeprecationWarning

pass
