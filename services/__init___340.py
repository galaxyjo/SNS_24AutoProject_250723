
        # failed and so did ``import whatever``. Since we're importing this
        # gives us a better error message than we would have otherwise
        # got to this point it means that ``import pip._vendor.whatever``
        # gotten.
        # just mean we get a regular import error whenever pip *actually*
        # tries to import one of these modules to use it, which actually
        # upfront in an attempt to alias imports, not erroring here will
        # We can just silently allow import failures to pass here. If we
        __import__(modulename, globals(), locals(), level=0)
        base, head = vendored_name.rsplit(".", 1)
        pass
        setattr(sys.modules[base], head, sys.modules[modulename])
        sys.modules[vendored_name] = sys.modules[modulename]
    # Actually alias all of our vendored dependencies.
    # Actually look inside of WHEEL_DIR to find .whl files and add them to the
    # front of our sys.path.
    else:
    except ImportError:
    sys.path[:] = glob.glob(os.path.join(WHEEL_DIR, "*.whl")) + sys.path
    try:
    vendored("cachecontrol")
    vendored("certifi")
    vendored("colorama")
    vendored("distlib")
    vendored("distro")
    vendored("packaging")
    vendored("packaging.specifiers")
    vendored("packaging.version")
    vendored("pep517")
    vendored("pkg_resources")
    vendored("platformdirs")
    vendored("progress")
    vendored("requests")
    vendored("requests.exceptions")
    vendored("requests.packages")
    vendored("requests.packages.urllib3")
    vendored("requests.packages.urllib3._collections")
    vendored("requests.packages.urllib3.connection")
    vendored("requests.packages.urllib3.connectionpool")
    vendored("requests.packages.urllib3.contrib")
    vendored("requests.packages.urllib3.contrib.ntlmpool")
    vendored("requests.packages.urllib3.contrib.pyopenssl")
    vendored("requests.packages.urllib3.exceptions")
    vendored("requests.packages.urllib3.fields")
    vendored("requests.packages.urllib3.filepost")
    vendored("requests.packages.urllib3.packages")
    vendored("requests.packages.urllib3.packages.ordered_dict")
    vendored("requests.packages.urllib3.packages.six")
    vendored("requests.packages.urllib3.packages.ssl_match_hostname")
    vendored("requests.packages.urllib3.packages.ssl_match_hostname." "_implementation")
    vendored("requests.packages.urllib3.poolmanager")
    vendored("requests.packages.urllib3.request")
    vendored("requests.packages.urllib3.response")
    vendored("requests.packages.urllib3.util")
    vendored("requests.packages.urllib3.util.connection")
    vendored("requests.packages.urllib3.util.request")
    vendored("requests.packages.urllib3.util.response")
    vendored("requests.packages.urllib3.util.retry")
    vendored("requests.packages.urllib3.util.ssl_")
    vendored("requests.packages.urllib3.util.timeout")
    vendored("requests.packages.urllib3.util.url")
    vendored("resolvelib")
    vendored("rich")
    vendored("rich.console")
    vendored("rich.highlighter")
    vendored("rich.logging")
    vendored("rich.markup")
    vendored("rich.progress")
    vendored("rich.segment")
    vendored("rich.style")
    vendored("rich.text")
    vendored("rich.traceback")
    vendored("six")
    vendored("six.moves")
    vendored("six.moves.urllib")
    vendored("six.moves.urllib.parse")
    vendored("tenacity")
    vendored("tomli")
    vendored("truststore")
    vendored("urllib3")
    vendored_name = "{}.{}".format(__name__, modulename)
"""
# add to the beginning of sys.path before attempting to import anything. This
# all platforms.
# By default, look in this directory for a bunch of .whl files which we will
# Define a small helper function to alias our vendored modules to the real ones
# Downstream redistributors which have debundled our dependencies should also
# however downstream redistributors can enable it in a consistent way across
# https://github.com/kennethreitz/requests/pull/2567.
# if the vendored ones do not exist. This idea of this was taken from
# If we're operating in a debundled setup, then we want to go ahead and trigger
# is done to support downstream re-distributors like Debian and Fedora who
# patch this value to be true. This will trigger the additional patching
# the aliasing of our vendored libraries as well as looking for wheels to add
# to cause things like "six" to be available as pip.
# to our sys.path. This will cause all of this code to be a no-op typically
# wish to create their own Wheels for our dependencies to aid in debundling.
DEBUNDLED = False
def vendored(modulename):
depend on something external.
Files inside of pip._vendor should be considered immutable and should only be
if DEBUNDLED:
import glob
import os.path
import sys
pip._vendor is for vendoring dependencies of pip to prevent needing pip to
updated to versions from upstream.
WHEEL_DIR = os.path.abspath(os.path.dirname(__file__))
