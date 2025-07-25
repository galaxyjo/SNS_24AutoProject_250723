
        return s.translate(_escape_map_full)
    """
    assert not isinstance(s, bytes), "Pass a unicode string"
    characters, both double quote (") and single quote (') characters are also
    if quote:
    If the optional flag quote is true (the default), the quotation mark
    ord("'"): "&#x27;",
    ord("&"): "&amp;",
    ord('"'): "&quot;",
    ord("<"): "&lt;",
    ord(">"): "&gt;",
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    return s.translate(_escape_map)
    translated.
"""
# NB: this is a candidate for a bytes/string polymorphic interface
_escape_map = {ord("&"): "&amp;", ord("<"): "&lt;", ord(">"): "&gt;"}
_escape_map_full = {
}
def escape(s, quote=True):
General functions for HTML manipulation, backported from Py3.
module names and locations.
Note that this uses Python 2.7 code with the corresponding Python 3
