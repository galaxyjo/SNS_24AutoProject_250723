# modules/common/_shimmed_dist_utils.py
# ✅ manualfixed: Python 3.12 distutils 제거 대응 / 셋업툴 임시 shim 구조 정리

import sys

def get_msvc_compiler():
    """
    Safely attempt to load MSVCCompiler from distutils or fallback.
    Returns:
        MSVCCompiler class or None if not available
    Raises:
        Exception with clear message if required modules are missing in Python >= 3.12
    """
    try:
        if sys.version_info >= (3, 12):
            try:
                import setuptools
                from distutils.msvc9compiler import MSVCCompiler  # vendored via setuptools
                return MSVCCompiler
            except ImportError as ex:
                raise Exception(
                    "⚠️ This CFFI feature requires setuptools on Python >= 3.12. "
                    "The setuptools module is missing or distutils not vendored. "
                    "Please install/upgrade setuptools."
                ) from ex
        else:
            try:
                from distutils.msvc9compiler import MSVCCompiler
                return MSVCCompiler
            except ImportError:
                return None
    except Exception as ex:
        raise Exception(
            "❌ Failed to load MSVCCompiler. distutils may be unavailable. "
            "Check your Python environment."
        ) from ex


if __name__ == "__main__":
    compiler_cls = get_msvc_compiler()
    if compiler_cls is not None:
        print("✅ MSVCCompiler is available:", compiler_cls)
    else:
        print("⚠️ MSVCCompiler is not available in this environment.")
