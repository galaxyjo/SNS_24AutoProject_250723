
-------------------------
        " active use-case for it, please reach out to us on GitHub.",
        " deprecated and will be removed in ImageIO v3. There is no"
        " replacement planned for this feature. If you have an"
        "Setting plugin priority through an environment variable is"
        DeprecationWarning,
        is None, it should return the 'global' meta-data.
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
        return importlib.import_module(f"imageio.plugins.{name}")
        the user expects. Can be ``inf`` for streaming data.
        user-provided keyword arguments here.
    """
    """Lazy-Import Plugins
    )
    * Implement ``_append_data(im, meta)`` to add data (and meta-data).
    * Implement ``_close()`` to clean up.
    * Implement ``_get_data(index)`` to return an array and a meta-data dict.
    * Implement ``_get_length()`` to provide a suitable length based on what
    * Implement ``_get_meta_data(index)`` to return a meta-data dict. If index
    * Implement ``_open(**kwargs)`` to initialize the reader. Deal with the
    * Implement ``_open(**kwargs)`` to initialize the writer. Deal with the
    * Implement ``_set_meta_data(meta)`` to set the global meta-data.
    :template: better_class.rst
    :toctree: ../_autosummary
    >>> imageio.plugins.freeimage.download()
    >>> import imageio
    delay importing freeimage until the second line:
    except ImportError:
    formats.sort(*os.getenv("IMAGEIO_FORMAT_ORDER", "").split(","))
    imageio.core.Format
    imageio.core.Format.__init__
    imageio.core.Format._can_read
    imageio.core.Format._can_write
    imageio.core.Request
    namespace upon first access. For example, the following snippet will
    This function dynamically loads plugins into the imageio.plugin
    try:
    warnings.warn(
    You can always check existing plugins if you want to see examples.
"""
# flake8: noqa
# imageio is distributed under the terms of the (new) BSD License.
# see https://stackoverflow.com/questions/2447353/getattr-on-a-module
# this class replaces plugin module. For details
# this is done here.
# v2 allows formatting plugins by environment variable
# v2 imports remove in v3
.. autosummary::
.. currentmodule:: imageio
.. note::
:class:`imageio.core.Format`. and implement the following functions:
``imageio.core.Format.Reader`` and that implements the following functions:
``imageio.core.Format.Writer`` and implement the following functions:
def __getattr__(name):
env_plugin_order = os.getenv("IMAGEIO_FORMAT_ORDER", None)
For reading, create a nested class that inherits from
For writing, create a nested class that inherits from
from .. import formats
Further, each format contains up to two nested classes; one for reading and
Here you can find documentation on how to write your own plugin to allow
if env_plugin_order is not None:  # pragma: no cover
ImageIO to access a new backend. Plugins are quite object oriented, and
import importlib
import os
import warnings
need to be defined.
one for writing. To support reading and/or writing, the respective classes
the relevant classes and their interaction are documented here:
To implement a new plugin, create a new class that inherits from
What methods to implement
