
            s = s.replace("'", "&#x27;")
            s = s.replace('"', "&quot;")
        """
        characters, both double quote (") and single quote (') characters are also
        if quote:
        If the optional flag quote is true (the default), the quotation mark
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        return s
        s = s.replace("&", "&amp;")  # Must be done first!
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        translated.
    """
    # cgi.escape isn't good enough for the single Py3.3 html test to pass.
    # Define it inline here instead. From the Py3.4 stdlib. Note that the
    # html.escape() function from the Py3.3 stdlib is not suitable for use on
    # Py2.x.
    __all__ = ["escape"]
    def escape(s, quote=True):
    General functions for HTML manipulation.
    pass
__future_module__ = True
else:
from future.utils import PY3
if PY3:
