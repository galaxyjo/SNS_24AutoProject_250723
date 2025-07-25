
    ----------
        " iio.v3.imread. To keep the current behavior (and make this warning disappear)"
        " use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.",
        "Starting with ImageIO v3 the behavior of this function will switch to that of"
        DeprecationWarning,
        Further keyword arguments are passed to the reader. See :func:`.help`
        http address or file object, see the docs for more info.
        stacklevel=2,
        the appropriate for you based on the filename and its contents.
        The format to use to read the file. By default imageio selects
        The resource to load the image from, e.g. a filename, pathlib.Path,
        to see what arguments are available for a particular format.
    """
    """imread(uri, format=None, **kwargs)
    "config",
    "formats",
    "get_reader",
    "get_writer",
    "help",
    "imiter",
    "imopen",
    "imread",
    "imsave",
    "imwrite",
    "mimread",
    "mimsave",
    "mimwrite",
    "mvolread",
    "mvolsave",
    "mvolwrite",
    "plugins",
    "read",
    "save",
    "show_formats",
    "v2",
    "v3",
    "volread",
    "volsave",
    "volwrite",
    # aliases
    # functions to deprecate
    # imread,  # Will take over once v3 is released
    # imwrite, # Will take over once v3 is released
    # misc
    # v2 aliases
    # v2 API
    # v3 API
    )
    a dtype of uint8 (and thus may differ from what e.g. PIL returns).
    comes with a dict of meta data at its 'meta' attribute.
    format : str
    get_reader as read,
    get_reader,
    get_writer as save,
    get_writer,
    help,
    imiter,
    imopen,
    imread as imread_v2,
    imwrite as imsave,
    imwrite,
    kwargs : ...
    mimread,
    mimwrite as mimsave,
    mimwrite,
    mvolread,
    mvolwrite as mvolsave,
    mvolwrite,
    Note that the image data is returned as-is, and may not always have
    Parameters
    Reads an image from the specified file. Returns a numpy array, which
    return imread_v2(uri, format=format, **kwargs)
    uri : {str, pathlib.Path, bytes, file}
    volread,
    volwrite as volsave,
    volwrite,
    warnings.warn(
"""
# Copyright (c) 2014-2020, imageio contributors
# flake8: noqa
# gets inserted into a slightly larger description (in setup.py) for
# imageio is distributed under the terms of the (new) BSD License.
# import all APIs into the top level (meta API)
# import config after core to avoid circular import
# Instantiate the old format manager
# Load some bits from core
# the page on Pypi:
# This docstring is used at the index of the documentation pages, and
)
]
__all__ = [
__version__ = "2.37.0"
and is easy to install.
data, and scientific formats. It is cross-platform, runs on Python 3.9+,
def imread(uri, format=None, **kwargs):
formats = FormatManager()
from . import config
from . import plugins
from . import v2
from . import v3
from .core import FormatManager
from .v2 import (
from .v3 import (
Imageio is a Python library that provides an easy interface to read and
import warnings
Main website: https://imageio.readthedocs.io/
show_formats = formats.show
write a wide range of image data, including animated images, volumetric
