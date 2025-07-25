
            "Unable to invoke 'cpp'.  "
            + "Make sure its path was passed correctly\n"
            + ("Original error: %s" % e)
            text = f.read()
        # as \n for Python's purpose
        # Note the use of universal_newlines to treat all newlines
        (r'') here. For example:
        )
        arguments.
        Encoding to use for the file to parse
        execute 'cpp', so it must be in your PATH.
        If several arguments are required, pass a list of strings.
        If use_cpp is True, set this to the command line arguments strings
        If use_cpp is True, this is the path to 'cpp' on your
        Name of the file you want to parse.
        Name of the file you want to preprocess.
        on the file prior to parsing it.
        Optional parser object to be used instead of the default CParser
        parser = CParser()
        path_list += [cpp_args]
        path_list += cpp_args
        raise RuntimeError(
        Refer to the documentation of parse_file for the meaning of these
        r'-I../utils/fake_libc_include'
        Set to True if you want to execute the C pre-processor
        system. If no path is provided, it attempts to just
        text = check_output(path_list, universal_newlines=True)
        text = preprocess_file(filename, cpp_path, cpp_args)
        to cpp. Be careful with quotes - it's best to pass a raw string
        with open(filename, encoding=encoding) as f:
    """
    """Parse a C file using pycparser.
    """Preprocess a file using cpp.
    cpp_args:
    cpp_path:
    elif cpp_args != "":
    else:
    encoding:
    Errors from cpp will be printed out.
    except OSError as e:
    filename, use_cpp=False, cpp_path="cpp", cpp_args="", parser=None, encoding=None
    filename:
    if isinstance(cpp_args, list):
    if parser is None:
    if use_cpp:
    parser:
    path_list += [filename]
    path_list = [cpp_path]
    return parser.parse(text, filename)
    return text
    thrown if the file doesn't parse successfully.
    try:
    use_cpp:
    When successful, an AST is returned. ParseError can be
    When successful, returns the preprocessed file's contents.
#
# -----------------------------------------------------------------
# Eli Bendersky [https://eli.thegreenplace.net/]
# interacting with pycparser
# License: BSD
# pycparser: __init__.py
# This package file exports some convenience functions for
):
__all__ = ["c_lexer", "c_parser", "c_ast"]
__version__ = "2.22"
def parse_file(
def preprocess_file(filename, cpp_path="cpp", cpp_args=""):
from .c_parser import CParser
from subprocess import check_output
