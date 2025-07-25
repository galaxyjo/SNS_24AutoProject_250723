
            cryptography_version
            urllib3.__version__, chardet_version, charset_normalizer_version
        "urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
        "version!".format(
        # chardet_version >= 3.0.2, < 6.0.0
        # charset_normalizer >= 2.0.0 < 4.0.0
        # Check cryptography version
        # pip does not need or use character detection
        )
        ),
        _check_cryptography(cryptography_version)
        assert (2, 0, 0) <= (major, minor, patch) < (4, 0, 0)
        assert (3, 0, 2) <= (major, minor, patch) < (6, 0, 0)
        assert minor >= 21
        cryptography_version = list(map(int, cryptography_version.split(".")))
        from cryptography import __version__ as cryptography_version
        from pip._vendor.urllib3.contrib import pyopenssl
        import ssl
        major, minor, patch = chardet_version.split(".")[:3]
        major, minor, patch = charset_normalizer_version.split(".")[:3]
        major, minor, patch = int(major), int(minor), int(patch)
        pass
        pyopenssl.inject_into_urllib3()
        raise ImportError("pip internals: don't import cryptography on Windows")
        RequestsDependencyWarning,
        return
        ssl = None
        urllib3.__version__, chardet_version, charset_normalizer_version
        urllib3_version.append("0")
        warning = "Old version of cryptography ({}) may cause slowdown.".format(
        warnings.warn(warning, RequestsDependencyWarning)
       "key1": "value1",
       "key2": "value2"
     "form": {
     ...
     },
    #       as part of pip.
    # Check charset_normalizer for compatibility.
    # Check urllib3 for compatibility.
    # cryptography < 1.3.4
    # Note: This logic prevents upgrading cryptography on Windows, if imported
    # Sometimes, urllib3 only reports its version as 16.1.
    # urllib3 >= 1.21.1
    )
    assert major >= 1
    assert urllib3_version != ["dev"]  # Verify urllib3 isn't installed from git.
    check_compatibility(
    elif charset_normalizer_version:
    else:
    except ImportError:
    except ValueError:
    FileModeWarning,
    from pip._internal.utils.compat import WINDOWS
    if chardet_version:
    if cryptography_version < [1, 3, 4]:
    if len(urllib3_version) == 2:
    if major == 1:
    if not getattr(ssl, "HAS_SNI", False):
    if not WINDOWS:
    major, minor, patch = int(major), int(minor), int(patch)
    major, minor, patch = urllib3_version  # noqa: F811
    pass
    try:
    urllib3_version = urllib3_version.split(".")
    warnings.warn(
   {
   }
   >>> b'Python is a programming language' in r.content
   >>> import requests
   >>> payload = dict(key1='value1', key2='value2')
   >>> print(r.text)
   >>> r = requests.get('https://www.python.org')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> r.status_code
   200
   True
"""
#          /
#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
# Attempt to enable urllib3's fallback for SNI support
# Check imported dependencies for compatibility.
# FileModeWarnings go off per the default.
# if the standard library doesn't support SNI or the
# Set default logging handler to avoid "No handler found" warnings.
# 'ssl' library isn't available.
# urllib3's DependencyWarnings should be silenced.
)
... or POST:
:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
~~~~~~~~~~~~~~~~~~~~~
Basic GET usage:
chardet_version = None
charset_normalizer_version = None
def _check_cryptography(cryptography_version):
def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version):
except (AssertionError, ValueError):
except ImportError:
from .exceptions import (
from .exceptions import RequestsDependencyWarning
from logging import NullHandler
from pip._vendor import urllib3
from pip._vendor.urllib3.exceptions import DependencyWarning
import logging
import warnings
is at <https://requests.readthedocs.io>.
logging.getLogger(__name__).addHandler(NullHandler())
Requests HTTP Library
Requests is an HTTP library, written in Python, for human beings.
The other HTTP methods are supported - see `requests.api`. Full documentation
try:
warnings.simplefilter("default", FileModeWarning, append=True)
warnings.simplefilter("ignore", DependencyWarning)
