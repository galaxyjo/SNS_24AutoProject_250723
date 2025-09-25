# scripts/install_package.py
# =============================
# 출처: install_package.py
import setuptools.command.install_scripts as orig
from distutils import log
from distutils.errors import DistutilsModuleError
import os, sys
from pkg_resources import Distribution, PathMetadata, ensure_directory

class install_scripts(orig.install_scripts):
    """Custom install script handler"""
    def run(self):
        try:
            orig.install_scripts.run(self)
            log.info("✅ install_package 실행 완료")
        except (ImportError, DistutilsModuleError) as e:
            log.error(f"⚠️ install_package 실패: {e}")
