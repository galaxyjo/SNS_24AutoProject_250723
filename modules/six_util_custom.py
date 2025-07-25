
                                 assigned = assigned, updated = updated)
                             "to %s because it doesn't define __str__()." %
                             klass.__name__)
                        assigned = functools.WRAPPER_ASSIGNMENTS,
                        updated = functools.WRAPPER_UPDATES):
                      "moves.urllib")
                      "moves.urllib_error", "moves.urllib.error")
                      "moves.urllib_parse", "moves.urllib.parse")
                      "moves.urllib_request", "moves.urllib.request")
                      "moves.urllib_response", "moves.urllib.response")
                      "moves.urllib_robotparser", "moves.urllib.robotparser")
                    break
                    d['__orig_bases__'] = bases
                    errors = "strict"
                    fp.encoding is not None):
                    isinstance(data, unicode) and
                    new_attr = name
                    new_attr = old_attr
                    want_unicode = True
                "tkinter.colorchooser"),
                "tkinter.commondialog"),
                "tkinter.simpledialog"),
                # of extra care (we mimic what is done by __build_class__).
                # This version introduced PEP 560 that requires a bit
                _locs_ = frame.f_locals
                continue
                data = data.encode(fp.encoding, errors)
                data = str(data)
                else:
                errors = getattr(fp, "errors", None)
                if errors is None:
                if isinstance(arg, unicode):
                if old_attr is None:
                if resolved_bases is not bases:
                importer.name == __name__):
                new = name
                new_mod = name
                old_attr = name
                orig_vars.pop(slots_var)
                raise TypeError("end must be None or a string")
                raise TypeError("sep must be None or a string")
                raise value.with_traceback(tb)
                resolved_bases = bases
                resolved_bases = types.resolve_bases(bases)
                return 1 << 31
                setattr(wrapper, attr, value)
                slots = [slots]
                value = getattr(wrapped, attr)
                value = tp()
                want_unicode = True
                write(sep)
              updated = functools.WRAPPER_UPDATES):
            # 32-bit
            # 64-bit
            # If the file has an encoding, encode unicode with it.
            # in case of a reload
            # removing this descriptor.
            # This is a bit ugly, but it avoids running this again by
            _globs_ = frame.f_globals
            _locs_ = _globs_
            break
            def __len__(self):
            del frame
            del moves.__dict__[name]
            del sys.meta_path[i]
            delattr(obj.__class__, self.name)
            elif not isinstance(end, str):
            elif not isinstance(sep, str):
            else:
            end = newline
            except AttributeError:
            for arg in args:
            for slots_var in slots:
            fp.flush()
            fp.write(data)
            frame = sys._getframe(1)
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
            if (isinstance(fp, file) and
            if _locs_ is None:
            if i:
            if isinstance(end, unicode):
            if isinstance(sep, unicode):
            if isinstance(slots, str):
            if new is None:
            if new_attr is None:
            if new_mod is None:
            if not isinstance(data, basestring):
            if old_attr is None:
            if sys.version_info[:2] >= (3, 7):
            if value is None:
            if value.__traceback__ is not tb:
            len(X())
            MAXSIZE=int((1 << 31) - 1)
            MAXSIZE=int((1 << 63) - 1)
            mod=mod._resolve()
            mod.__loader__=self
            newline="\n"
            newline=unicode("\n")
            orig_vars['__qualname__']=cls.__qualname__
            pass
            raise AttributeError("no such move, %r" % (name,))
            raise ImportError("This loader does not know module " + fullname)
            raise TypeError("invalid keyword arguments to print()")
            raise value
            raise ValueError("@python_2_unicode_compatible cannot be applied "
            return
            return meta(name, resolved_bases, d)
            return meta.__prepare__(name, bases)
            return self
            return self.known_modules[fullname]
            return spec_from_loader(fullname, self)
            return sys.modules[fullname]
            return type(self).__next__(self)
            self.attr=new_attr
            self.attr=old_attr
            self.known_modules[self.name + "." + fullname]=mod
            self.mod=new
            self.mod=new_mod
            self.mod=old
            self.mod=old_mod
            sep=space
            space=" "
            space=unicode(" ")
            tb=None
            try:
            value=None
            write(arg)
         """Get the function out of a possibly unbound function""")
         "Return an iterator over the (key, [values]) pairs of a dictionary.")
         "Return an iterator over the (key, value) pairs of a dictionary.")
        """
        """Execute code in a namespace."""
        """Return None
        """The new-style print function for Python 2.4 and 2.5."""
        # be floating around. Therefore, we can't use isinstance() to check for
        # Here's some real nastiness: Another "instance" of the six module might
        # inserted an importer with different class.
        # It's possible to have sizeof(long) != sizeof(Py_ssize_t).
        # Jython always uses 32 bits.
        # the six meta path importer, since the other six instance will have
        @ classmethod
        _assertNotRegex = "assertNotRegex"
        _assertNotRegex = "assertNotRegexpMatches"
        _assertRaisesRegex = "assertRaisesRegex"
        _assertRaisesRegex = "assertRaisesRegexp"
        _assertRegex = "assertRegex"
        _assertRegex = "assertRegexpMatches"
        _importer._add_module(attr, "moves." + attr.name)
        _module = self._resolve()
        _print(*args, **kwargs)
        attrs += [attr.name for attr in self._moved_attributes]
        attrs = ["__doc__", "__name__"]
        class X:
        def __new__(cls, name, this_bases, d):
        def __prepare__(cls, name, this_bases):
        def next(self):
        def write(data):
        del X
        delattr(_MovedItems, name)
        elif _locs_ is None:
        else:
        end = kwargs.pop("end", None)
        except AttributeError:
        except KeyError:
        except OverflowError:
        exec("""exec _code_ in _globs_, _locs_""")
        finally:
        flush = kwargs.pop("flush", False)
        for attr in assigned:
        for attr in updated:
        for fullname in fullnames:
        for i, arg in enumerate(args):
        fp = kwargs.get("file", sys.stdout)
        fp = kwargs.pop("file", sys.stdout)
        if (type(importer).__name__ == "_SixMetaPathImporter" and
        if '__str__' not in klass.__dict__:
        if _globs_ is None:
        if end is None:
        if end is not None:
        if flush and fp is not None:
        if fp is None:
        if fullname in self.known_modules:
        if hasattr(cls, '__qualname__'):
        if isinstance(mod, MovedModule):
        if kwargs:
        if not want_unicode:
        if PY3:
        if sep is None:
        if sep is not None:
        if slots is not None:
        if want_unicode:
        klass.__str__=lambda self: self.__unicode__().encode('utf-8')
        klass.__unicode__=klass.__str__
        MAXSIZE=int((1 << 31) - 1)
        mod=self.__get_module(fullname)
        module=_import_module(self.mod)
        MovedModule("winreg", "_winreg"),
        orig_vars=cls.__dict__.copy()
        orig_vars.pop('__dict__', None)
        orig_vars.pop('__weakref__', None)
        pass
        Python 3.4 (see PEP451)
        raise tp, value, tb
        raise TypeError("not expecting type '%s'" % type(s))
        raise value
        raise value from from_value
        Required, if is_package is implemented"""
        result = self._resolve()
        return ['parse', 'error', 'request', 'response', 'robotparser']
        return _import_module(self.mod)
        return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)
        return attrs
        return d.iteritems(**kw)
        return d.iterkeys(**kw)
        return d.iterlists(**kw)
        return d.itervalues(**kw)
        return func
        return functools.partial(_update_wrapper, wrapped=wrapped,
        return getattr(module, self.attr)
        return hasattr(self.__get_module(fullname), "__path__")
        return it.next()
        return iter(d.items(**kw))
        return iter(d.keys(**kw))
        return iter(d.lists(**kw))
        return iter(d.values(**kw))
        return metaclass(cls.__name__, cls.__bases__, orig_vars)
        return mod
        return None
        return ord(bs[0])
        return ord(buf[i])
        return result
        return s
        return s.decode(encoding, errors)
        return s.encode("latin-1")
        return s.encode(encoding, errors)
        return self.known_modules[self.name + "." + fullname]
        return self.load_module(spec.name)
        Return true, if the named module is a package.
        return types.MethodType(func, None, cls)
        return types.MethodType(func, obj, obj.__class__)
        return unbound
        return unbound.im_func
        return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")
        return value
        return wrapper
        self.__doc__ = self.__class__.__doc__
        self.__get_module(fullname)  # eventually raises ImportError
        self.known_modules = {}
        self.name = name
        self.name = six_module_name
        sep = kwargs.pop("sep", None)
        setattr(obj, self.name, result)  # Invokes __set__.
        setattr(self, attr, value)
        slots = orig_vars.get('__slots__')
        super(_LazyModule, self).__init__(name)
        super(MovedAttribute, self).__init__(name)
        super(MovedModule, self).__init__(name)
        sys.modules[fullname] = mod
        tb = None
        try:
        value = getattr(_module, attr)
        value = None
        want_unicode = False
        We need this method to get correct spec objects with
        wrapper.__wrapped__ = wrapped
        write(end)
      - `bytes` -> `bytes`
      - `bytes` -> decoded to `str`
      - `str` -> `str`
      - `str` -> `unicode`
      - `str` -> encoded to `bytes`
      - `unicode` -> `unicode`
      - `unicode` -> encoded to `str`
    """
    """Add an item to six.moves."""
    """Add documentation to a function."""
    """Class decorator for creating a class with a metaclass."""
    """Coerce **s** to six.binary_type.
    """Coerce * s * to `str`.
    """Coerce *s* to six.text_type.
    """Create a base class with a metaclass."""
    """Create a six.moves.urllib namespace that resembles the Python 3 namespace"""
    """Import module, returning the module after the last dot."""
    """Lazy loading of moved objects in six.moves.urllib_error"""
    """Lazy loading of moved objects in six.moves.urllib_parse"""
    """Lazy loading of moved objects in six.moves.urllib_request"""
    """Lazy loading of moved objects in six.moves.urllib_response"""
    """Lazy loading of moved objects in six.moves.urllib_robotparser"""
    """Lazy loading of moved objects"""
    """Remove item from six.moves."""
    # ``wrapped`` object.
    # attribute on ``wrapper`` object and it doesn't raise an error if any of
    # function does on Python versions after 3.2. It sets the ``__wrapped__``
    # metaclass for one level of class instantiation that replaces itself with
    # Optimization: Fast return for the common case.
    # Subclasses should override this
    # the actual metaclass.
    # the attributes mentioned in ``assigned`` and ``updated`` are missing on
    # This does exactly the same what the :func:`py3:functools.update_wrapper`
    # This requires a bit of explanation: the basic idea is to make a dummy
    # Workaround for standalone backslash
    ]
    __import__(name)
    __path__ = []  # mark as package
    __spec__.submodule_search_locations = []  # PEP 451 @UndefinedVariable
    _assertCountEqual = "assertCountEqual"
    _assertCountEqual = "assertItemsEqual"
    _assertNotRegex = "assertNotRegexpMatches"
    _assertRaisesRegex = "assertRaisesRegexp"
    _assertRegex = "assertRegexpMatches"
    _func_closure = "__closure__"
    _func_closure = "func_closure"
    _func_code = "__code__"
    _func_code = "func_code"
    _func_defaults = "__defaults__"
    _func_defaults = "func_defaults"
    _func_globals = "__globals__"
    _func_globals = "func_globals"
    _meth_func = "__func__"
    _meth_func = "im_func"
    _meth_self = "__self__"
    _meth_self = "im_self"
    _moved_attributes += [
    _moved_attributes = []
    _print = print_
    _update_wrapper.__doc__ = functools.update_wrapper.__doc__
    A class decorator that defines __unicode__ and __str__ methods under Python 2.
    A meta path importer to import six_util_custom.moves and its submodules.
    advance_iterator = next
    binary_type = bytes
    binary_type = str
    byte2int = operator.itemgetter(0)
    BytesIO = io.BytesIO
    callable = callable
    class Iterator:
    class metaclass:
    class_types = (type, types.ClassType)
    class_types = type,
    create_bound_method = types.MethodType
    def __dir__(self):
    def __get__(self, obj, tp):
    def __get_module(self, fullname):
    def __getattr__(self, attr):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, name):
    def __init__(self, name, old, new=None):
    def __init__(self, name, old_mod, new_mod, old_attr=None, new_attr=None):
    def __init__(self, six_module_name):
    def _add_module(self, mod, *fullnames):
    def _get_module(self, fullname):
    def _resolve(self):
    def _update_wrapper(wrapper, wrapped,
    def advance_iterator(it):
    def b(s):
    def byte2int(bs):
    def callable(obj):
    def create_bound_method(func, obj):
    def create_module(self, spec):
    def create_unbound_method(func, cls):
    def exec_(_code_, _globs_=None, _locs_=None):
    def exec_module(self, module):
    def find_module(self, fullname, path=None):
    def find_spec(self, fullname, path, target=None):
    def get_code(self, fullname):
    def get_unbound_function(unbound):
    def indexbytes(buf, i):
    def is_package(self, fullname):
    def iteritems(d, **kw):
    def iterkeys(d, **kw):
    def iterlists(d, **kw):
    def itervalues(d, **kw):
    def load_module(self, fullname):
    def print_(*args, **kwargs):
    def raise_from(value, from_value):
    def reraise(tp, value, tb=None):
    def u(s):
    def wrapper(cls):
    def wraps(wrapped, assigned=functools.WRAPPER_ASSIGNMENTS,
    del i, importer
    del io
    del struct
    elif isinstance(s, text_type):
    elif not isinstance(s, (text_type, binary_type)):
    elif PY3 and isinstance(s, binary_type):
    else:
    error = _importer._get_module("moves.urllib_error")
    except AttributeError:
    exec_ = getattr(moves.builtins, "exec")
    exec_("""def raise_from(value, from_value):
    exec_("""def reraise(tp, value, tb=None):
    finally:
    for i, importer in enumerate(sys.meta_path):
    For Python 2:
    For Python 3:
    from importlib.util import spec_from_loader
    func.__doc__ = doc
    get_source = get_code  # same as get_code
    if isinstance(attr, MovedModule):
    if isinstance(s, binary_type):
    if isinstance(s, text_type):
    if PY2 and isinstance(s, text_type):
    if PY2:
    if sys.platform.startswith("java"):
    if sys.version_info[1] <= 1:
    if type(s) is str:
    import io
    import StringIO
    import struct
    indexbytes = operator.getitem
    int2byte = chr
    int2byte = struct.Struct(">B").pack
    integer_types = (int, long)
    integer_types = int,
    Iterator = object
    iterbytes = functools.partial(itertools.imap, ord)
    iterbytes = iter
    MAXSIZE = sys.maxsize
    MovedAttribute("AbstractBasicAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("AbstractDigestAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("addbase", "urllib", "urllib.response"),
    MovedAttribute("addclosehook", "urllib", "urllib.response"),
    MovedAttribute("addinfo", "urllib", "urllib.response"),
    MovedAttribute("addinfourl", "urllib", "urllib.response"),
    MovedAttribute("BaseHandler", "urllib2", "urllib.request"),
    MovedAttribute("build_opener", "urllib2", "urllib.request"),
    MovedAttribute("CacheFTPHandler", "urllib2", "urllib.request"),
    MovedAttribute("ContentTooShortError", "urllib", "urllib.error"),
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO"),
    MovedAttribute("FancyURLopener", "urllib", "urllib.request"),
    MovedAttribute("FileHandler", "urllib2", "urllib.request"),
    MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter"),
    MovedAttribute("filterfalse", "itertools", "itertools",
                   "ifilterfalse", "filterfalse"),
    MovedAttribute("FTPHandler", "urllib2", "urllib.request"),
    MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd"),
    MovedAttribute("getcwdb", "os", "os", "getcwd", "getcwdb"),
    MovedAttribute("getoutput", "commands", "subprocess"),
    MovedAttribute("getproxies", "urllib", "urllib.request"),
    MovedAttribute("HTTPBasicAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("HTTPCookieProcessor", "urllib2", "urllib.request"),
    MovedAttribute("HTTPDefaultErrorHandler", "urllib2", "urllib.request"),
    MovedAttribute("HTTPDigestAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("HTTPError", "urllib2", "urllib.error"),
    MovedAttribute("HTTPErrorProcessor", "urllib2", "urllib.request"),
    MovedAttribute("HTTPHandler", "urllib2", "urllib.request"),
    MovedAttribute("HTTPPasswordMgr", "urllib2", "urllib.request"),
    MovedAttribute("HTTPPasswordMgrWithDefaultRealm", "urllib2", "urllib.request"),
    MovedAttribute("HTTPRedirectHandler", "urllib2", "urllib.request"),
    MovedAttribute("HTTPSHandler", "urllib2", "urllib.request"),
    MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input"),
    MovedAttribute("install_opener", "urllib2", "urllib.request"),
    MovedAttribute("intern", "__builtin__", "sys"),
    MovedAttribute("map", "itertools", "builtins", "imap", "map"),
    MovedAttribute("OpenerDirector", "urllib2", "urllib.request"),
    MovedAttribute("parse_http_list", "urllib2", "urllib.request"),
    MovedAttribute("parse_keqv_list", "urllib2", "urllib.request"),
    MovedAttribute("parse_qs", "urlparse", "urllib.parse"),
    MovedAttribute("parse_qsl", "urlparse", "urllib.parse"),
    MovedAttribute("ParseResult", "urlparse", "urllib.parse"),
    MovedAttribute("pathname2url", "urllib", "urllib.request"),
    MovedAttribute("proxy_bypass", "urllib", "urllib.request"),
    MovedAttribute("ProxyBasicAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("ProxyDigestAuthHandler", "urllib2", "urllib.request"),
    MovedAttribute("ProxyHandler", "urllib2", "urllib.request"),
    MovedAttribute("quote", "urllib", "urllib.parse"),
    MovedAttribute("quote_plus", "urllib", "urllib.parse"),
    MovedAttribute("range", "__builtin__", "builtins", "xrange", "range"),
    MovedAttribute("reduce", "__builtin__", "functools"),
    MovedAttribute("reload_module", "__builtin__",
                   "importlib" if PY34 else "imp", "reload"),
    MovedAttribute("Request", "urllib2", "urllib.request"),
    MovedAttribute("RobotFileParser", "robotparser", "urllib.robotparser"),
    MovedAttribute("shlex_quote", "pipes", "shlex", "quote"),
    MovedAttribute("splitquery", "urllib", "urllib.parse"),
    MovedAttribute("SplitResult", "urlparse", "urllib.parse"),
    MovedAttribute("splittag", "urllib", "urllib.parse"),
    MovedAttribute("splituser", "urllib", "urllib.parse"),
    MovedAttribute("splitvalue", "urllib", "urllib.parse"),
    MovedAttribute("StringIO", "StringIO", "io"),
    MovedAttribute("UnknownHandler", "urllib2", "urllib.request"),
    MovedAttribute("unquote", "urllib", "urllib.parse"),
    MovedAttribute("unquote_plus", "urllib", "urllib.parse"),
    MovedAttribute("unquote_to_bytes", "urllib", "urllib.parse",
                   "unquote", "unquote_to_bytes"),
    MovedAttribute("url2pathname", "urllib", "urllib.request"),
    MovedAttribute("urlcleanup", "urllib", "urllib.request"),
    MovedAttribute("urldefrag", "urlparse", "urllib.parse"),
    MovedAttribute("urlencode", "urllib", "urllib.parse"),
    MovedAttribute("URLError", "urllib2", "urllib.error"),
    MovedAttribute("urljoin", "urlparse", "urllib.parse"),
    MovedAttribute("urlopen", "urllib2", "urllib.request"),
    MovedAttribute("URLopener", "urllib", "urllib.request"),
    MovedAttribute("urlparse", "urlparse", "urllib.parse"),
    MovedAttribute("urlretrieve", "urllib", "urllib.request"),
    MovedAttribute("urlsplit", "urlparse", "urllib.parse"),
    MovedAttribute("urlunparse", "urlparse", "urllib.parse"),
    MovedAttribute("urlunsplit", "urlparse", "urllib.parse"),
    MovedAttribute("UserDict", "UserDict", "collections"),
    MovedAttribute("UserList", "UserList", "collections"),
    MovedAttribute("UserString", "UserString", "collections"),
    MovedAttribute("uses_fragment", "urlparse", "urllib.parse"),
    MovedAttribute("uses_netloc", "urlparse", "urllib.parse"),
    MovedAttribute("uses_params", "urlparse", "urllib.parse"),
    MovedAttribute("uses_query", "urlparse", "urllib.parse"),
    MovedAttribute("uses_relative", "urlparse", "urllib.parse"),
    MovedAttribute("xrange", "__builtin__", "builtins", "xrange", "range"),
    MovedAttribute("zip", "itertools", "builtins", "izip", "zip"),
    MovedAttribute("zip_longest", "itertools", "itertools",
                   "izip_longest", "zip_longest"),
    MovedModule("_dummy_thread", "dummy_thread",
                "_dummy_thread" if sys.version_info < (3, 9) else "_thread"),
    MovedModule("_thread", "thread", "_thread"),
    MovedModule("BaseHTTPServer", "BaseHTTPServer", "http.server"),
    MovedModule("builtins", "__builtin__"),
    MovedModule("CGIHTTPServer", "CGIHTTPServer", "http.server"),
    MovedModule("collections_abc", "collections",
                "collections.abc" if sys.version_info >= (3, 3) else "collections"),
    MovedModule("configparser", "ConfigParser"),
    MovedModule("copyreg", "copy_reg"),
    MovedModule("cPickle", "cPickle", "pickle"),
    MovedModule("dbm_gnu", "gdbm", "dbm.gnu"),
    MovedModule("dbm_ndbm", "dbm", "dbm.ndbm"),
    MovedModule("email_mime_base", "email.MIMEBase", "email.mime.base"),
    MovedModule("email_mime_image", "email.MIMEImage", "email.mime.image"),
    MovedModule("email_mime_multipart", "email.MIMEMultipart", "email.mime.multipart"),
    MovedModule("email_mime_nonmultipart", "email.MIMENonMultipart",
                "email.mime.nonmultipart"),
    MovedModule("email_mime_text", "email.MIMEText", "email.mime.text"),
    MovedModule("html_entities", "htmlentitydefs", "html.entities"),
    MovedModule("html_parser", "HTMLParser", "html.parser"),
    MovedModule("http_client", "httplib", "http.client"),
    MovedModule("http_cookiejar", "cookielib", "http.cookiejar"),
    MovedModule("http_cookies", "Cookie", "http.cookies"),
    MovedModule("queue", "Queue"),
    MovedModule("reprlib", "repr"),
    MovedModule("SimpleHTTPServer", "SimpleHTTPServer", "http.server"),
    MovedModule("socketserver", "SocketServer"),
    MovedModule("tkinter", "Tkinter"),
    MovedModule("tkinter_colorchooser", "tkColorChooser",
    MovedModule("tkinter_commondialog", "tkCommonDialog",
    MovedModule("tkinter_constants", "Tkconstants", "tkinter.constants"),
    MovedModule("tkinter_dialog", "Dialog", "tkinter.dialog"),
    MovedModule("tkinter_dnd", "Tkdnd", "tkinter.dnd"),
    MovedModule("tkinter_filedialog", "FileDialog", "tkinter.filedialog"),
    MovedModule("tkinter_font", "tkFont", "tkinter.font"),
    MovedModule("tkinter_messagebox", "tkMessageBox", "tkinter.messagebox"),
    MovedModule("tkinter_scrolledtext", "ScrolledText", "tkinter.scrolledtext"),
    MovedModule("tkinter_simpledialog", "SimpleDialog", "tkinter.simpledialog"),
    MovedModule("tkinter_tix", "Tix", "tkinter.tix"),
    MovedModule("tkinter_tkfiledialog", "tkFileDialog", "tkinter.filedialog"),
    MovedModule("tkinter_tksimpledialog", "tkSimpleDialog",
    MovedModule("tkinter_ttk", "ttk", "tkinter.ttk"),
    MovedModule("urllib", __name__ + ".moves.urllib", __name__ + ".moves.urllib"),
    MovedModule("urllib_error", __name__ + ".moves.urllib_error", "urllib.error"),
    MovedModule("urllib_parse", __name__ + ".moves.urllib_parse", "urllib.parse"),
    MovedModule("urllib_robotparser", "robotparser", "urllib.robotparser"),
    MovedModule("xmlrpc_client", "xmlrpclib", "xmlrpc.client"),
    MovedModule("xmlrpc_server", "SimpleXMLRPCServer", "xmlrpc.server"),
    parse = _importer._get_module("moves.urllib_parse")
    raise TypeError("not expecting type '%s'" % type(s))
    request = _importer._get_module("moves.urllib_request")
    response = _importer._get_module("moves.urllib_response")
    return getattr(self, _assertCountEqual)(*args, **kwargs)
    return getattr(self, _assertNotRegex)(*args, **kwargs)
    return getattr(self, _assertRaisesRegex)(*args, **kwargs)
    return getattr(self, _assertRegex)(*args, **kwargs)
    return klass
    return s
    return sys.modules[name]
    return type.__new__(metaclass, 'temporary_class', (), {})
    return wrapper
    returning text and apply this decorator to the class.
    robotparser = _importer._get_module("moves.urllib_robotparser")
    setattr(_MovedItems, attr.name, attr)
    setattr(_MovedItems, move.name, move)
    setattr(Module_six_moves_urllib_error, attr.name, attr)
    setattr(Module_six_moves_urllib_parse, attr.name, attr)
    setattr(Module_six_moves_urllib_request, attr.name, attr)
    setattr(Module_six_moves_urllib_response, attr.name, attr)
    setattr(Module_six_moves_urllib_robotparser, attr.name, attr)
    spec_from_loader = None
    string_types = basestring,
    string_types = str,
    StringIO = BytesIO = StringIO.StringIO
    StringIO = io.StringIO
    text_type = str
    text_type = unicode
    This class implements a PEP302 finder and loader. It should be compatible
    To support Python 2 and 3 with a single code base, define a __str__ method
    try:
    Under Python 3 it does nothing.
    unichr = chr
    unichr = unichr
    viewitems = operator.methodcaller("items")
    viewitems = operator.methodcaller("viewitems")
    viewkeys = operator.methodcaller("keys")
    viewkeys = operator.methodcaller("viewkeys")
    viewvalues = operator.methodcaller("values")
    viewvalues = operator.methodcaller("viewvalues")
    with Python 2.5 and all existing versions of Python3
    wraps = functools.wraps
    wraps.__doc__ = functools.wraps.__doc__
""")
"""Utilities for writing code that runs on Python 2 and 3"""
#
# Add windows specific modules.
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# Complete the moves implementation.
# copies of the Software, and to permit persons to whom the Software is
# copies or substantial portions of the Software.
# Copyright (c) 2010-2020 Benjamin Peterson
# Finally, add the importer to the meta path import hook.
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# furnished to do so, subject to the following conditions:
# happen if six is removed from sys.modules and then reloaded. (Setuptools does
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# in the Software without restriction, including without limitation the rights
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# of this software and associated documentation files (the "Software"), to deal
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# Permission is hereby granted, free of charge, to any person obtaining a copy
# Remove other six meta path importers, since they cause problems. This can
# SOFTWARE.
# The above copyright notice and this permission notice shall be included in all
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# This code is at the end of this module to speed up module loading.
# this for some reason.)
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# Turn this module into a package.
# Useful for very coarse version differentiation.
]
__author__ = "Benjamin Peterson <benjamin@python.org>"
__package__ = __name__  # see PEP 366 @ReservedAssignment
__path__ = []  # required for PEP 302 and PEP 451
__version__ = "1.16.0"
_add_doc(b, """Byte literal""")
_add_doc(get_unbound_function,
_add_doc(iteritems,
_add_doc(iterkeys, "Return an iterator over the keys of a dictionary.")
_add_doc(iterlists,
_add_doc(itervalues, "Return an iterator over the values of a dictionary.")
_add_doc(reraise, """Reraise an exception.""")
_add_doc(u, """Text literal""")
_importer=_SixMetaPathImporter(__name__)
_importer._add_module(Module_six_moves_urllib(__name__ + ".moves.urllib"),
_importer._add_module(Module_six_moves_urllib_error(__name__ + ".moves.urllib.error"),
_importer._add_module(Module_six_moves_urllib_parse(__name__ + ".moves.urllib_parse"),
_importer._add_module(Module_six_moves_urllib_request(__name__ + ".moves.urllib.request"),
_importer._add_module(Module_six_moves_urllib_response(__name__ + ".moves.urllib.response"),
_importer._add_module(Module_six_moves_urllib_robotparser(__name__ + ".moves.urllib.robotparser"),
_importer._add_module(moves, "moves")
_moved_attributes=[
_MovedItems._moved_attributes = _moved_attributes
_urllib_error_moved_attributes = [
_urllib_parse_moved_attributes = [
_urllib_request_moved_attributes = [
_urllib_response_moved_attributes = [
_urllib_robotparser_moved_attributes = [
class _LazyDescr:
class _LazyModule:
class _MovedItems:
class _SixMetaPathImporter:
class Module_six_moves_urllib:
class Module_six_moves_urllib_error:
class Module_six_moves_urllib_parse:
class Module_six_moves_urllib_request:
class Module_six_moves_urllib_response:
class Module_six_moves_urllib_robotparser:
class MovedAttribute:
class MovedModule:
def _add_doc(func, doc):
def _import_module(name):
def add_metaclass(metaclass):
def add_move(move):
def assertCountEqual(self, *args, **kwargs):
def assertNotRegex(self, *args, **kwargs):
def assertRaisesRegex(self, *args, **kwargs):
def assertRegex(self, *args, **kwargs):
def ensure_binary(s, encoding='utf-8', errors='strict'):
def ensure_str(s, encoding='utf-8', errors='strict'):
def ensure_text(s, encoding='utf-8', errors='strict'):
def python_2_unicode_compatible(klass):
def remove_move(name):
def with_metaclass(meta, *bases):
del attr
else:
except NameError:
for attr in _moved_attributes:
for attr in _urllib_error_moved_attributes:
for attr in _urllib_parse_moved_attributes:
for attr in _urllib_request_moved_attributes:
for attr in _urllib_response_moved_attributes:
for attr in _urllib_robotparser_moved_attributes:
from __future__ import absolute_import
get_function_closure = operator.attrgetter(_func_closure)
get_function_code = operator.attrgetter(_func_code)
get_function_defaults = operator.attrgetter(_func_defaults)
get_function_globals = operator.attrgetter(_func_globals)
get_method_function = operator.attrgetter(_meth_func)
get_method_self = operator.attrgetter(_meth_self)
if globals().get("__spec__") is not None:
if print_ is None:
if PY3:
if PY34:
if sys.meta_path:
if sys.platform == "win32":
if sys.version_info[:2] < (3, 3):
if sys.version_info[:2] > (3,):
if sys.version_info[0:2] < (3, 4):
import functools
import itertools
import operator
import sys
import type_util
Module_six_moves_urllib_error._moved_attributes = _urllib_error_moved_attributes
Module_six_moves_urllib_parse._moved_attributes = _urllib_parse_moved_attributes
Module_six_moves_urllib_request._moved_attributes = _urllib_request_moved_attributes
Module_six_moves_urllib_response._moved_attributes = _urllib_response_moved_attributes
Module_six_moves_urllib_robotparser._moved_attributes = _urllib_robotparser_moved_attributes
moves = _MovedItems(__name__ + ".moves")
next = advance_iterator
print_ = getattr(moves.builtins, "print", None)
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0:2] >= (3, 4)
sys.meta_path.append(_importer)
try:
