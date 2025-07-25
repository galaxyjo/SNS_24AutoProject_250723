
                    loader.add_constructor(cls.yaml_tag, cls.from_yaml)
                cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
                for loader in cls.yaml_loader:
            cls.yaml_dumper.add_representer(cls, cls.to_yaml)
            cls.yaml_tag, data, cls, flow_style=cls.yaml_flow_style
            dumper.emit(event)
            dumper.represent(data)
            dumper.serialize(node)
            else:
            if isinstance(cls.yaml_loader, list):
            stream = io.BytesIO()
            stream = io.StringIO()
            yield loader.get_data()
            yield loader.get_event()
            yield loader.get_node()
            yield loader.get_token()
        """
        )
        allow_unicode=allow_unicode,
        canonical=canonical,
        Convert a Python object to a representation node.
        Convert a representation node to a Python object.
        default_flow_style=default_flow_style,
        default_style=default_style,
        dumper.close()
        dumper.dispose()
        dumper.open()
        else:
        encoding=encoding,
        explicit_end=explicit_end,
        explicit_start=explicit_start,
        for data in documents:
        for event in events:
        for node in nodes:
        getvalue = stream.getvalue
        if "yaml_tag" in kwds and kwds["yaml_tag"] is not None:
        if encoding is None:
        indent=indent,
        line_break=line_break,
        Loader.add_constructor(tag, constructor)
        Loader.add_implicit_resolver(tag, regexp, first)
        Loader.add_multi_constructor(tag_prefix, multi_constructor)
        Loader.add_path_resolver(tag, path, kind)
        loader.dispose()
        loader.FullLoader.add_constructor(tag, constructor)
        loader.FullLoader.add_implicit_resolver(tag, regexp, first)
        loader.FullLoader.add_multi_constructor(tag_prefix, multi_constructor)
        loader.FullLoader.add_path_resolver(tag, path, kind)
        loader.Loader.add_constructor(tag, constructor)
        loader.Loader.add_implicit_resolver(tag, regexp, first)
        loader.Loader.add_multi_constructor(tag_prefix, multi_constructor)
        loader.Loader.add_path_resolver(tag, path, kind)
        loader.UnsafeLoader.add_constructor(tag, constructor)
        loader.UnsafeLoader.add_implicit_resolver(tag, regexp, first)
        loader.UnsafeLoader.add_multi_constructor(tag_prefix, multi_constructor)
        loader.UnsafeLoader.add_path_resolver(tag, path, kind)
        return {}
        return dumper.represent_yaml_object(
        return getvalue()
        return loader.construct_yaml_object(node, cls)
        return loader.get_single_data()
        return loader.get_single_node()
        sort_keys=sort_keys,
        stream = io.StringIO()
        stream,
        super().__init__(name, bases, kwds)
        tags=tags,
        version=version,
        while loader.check_data():
        while loader.check_event():
        while loader.check_node():
        while loader.check_token():
        width=width,
    """
    )
    @classmethod
    __slots__ = ()  # no direct instantiation, so allow immutable subclasses
    __with_libyaml__ = False
    __with_libyaml__ = True
    A path is a list of keys that forms a path
    Add a constructor for the given tag.
    Add a multi-constructor for the given tag prefix.
    Add a path based resolver for the given tag.
    Add a representer for the given type.
    Add an implicit scalar detector.
    allow_unicode=None,
    An object that can dump itself to a YAML stream
    and a node object and produces the corresponding Python object.
    and an instance of the given data type
    and an instance of the given data type or subtype
    and load itself from a YAML stream.
    and produce corresponding Python objects.
    and produce corresponding representation trees.
    and produce the corresponding Python object.
    and produce the corresponding representation tree.
    and producing the corresponding representation node.
    canonical=None,
    Constructor is a function that accepts a Loader instance
    def __init__(cls, name, bases, kwds):
    def __init__(self, *args, **kwargs): pass
    def from_yaml(cls, loader, node):
    def to_yaml(cls, dumper, data):
    default_flow_style=False,
    default_style=None,
    documents,
    dumper = Dumper(
    Dumper.add_implicit_resolver(tag, regexp, first)
    Dumper.add_multi_representer(data_type, multi_representer)
    Dumper.add_path_resolver(tag, path, kind)
    Dumper.add_representer(data_type, representer)
    Dumper=Dumper,
    else:
    Emit YAML parsing events into a stream.
    encoding=None,
    events,
    explicit_end=None,
    explicit_start=None,
    finally:
    first is a sequence of possible initial characters or None.
    from .cyaml import *
    getvalue = None
    If an implicit scalar value matches the given regexp,
    if getvalue:
    if Loader is None:
    if settings is None:
    If stream is None, return the produced string instead.
    if stream is None:
    indent=None,
    Keys can be string values, integers, or None.
    line_break=None,
    loader = Loader(stream)
    Multi-constructor accepts a Loader instance, a tag suffix,
    Multi-constructor is called for a node if its tag starts with tag_prefix.
    Multi-representer is a function accepting a Dumper instance
    nodes,
    Parse a YAML stream and produce parsing events.
    Parse all YAML documents in a stream
    Parse the first YAML document in a stream
    Produce only basic YAML tags.
    Representer is a function accepting a Dumper instance
    Resolve all tags except those known to be
    Resolve all tags, even those known to be
    Resolve only basic YAML tags. This is known
    return dump_all([data], stream, Dumper=Dumper, **kwds)
    return dump_all([data], stream, Dumper=SafeDumper, **kwds)
    return dump_all(documents, stream, Dumper=SafeDumper, **kwds)
    return load(stream, FullLoader)
    return load(stream, SafeLoader)
    return load(stream, UnsafeLoader)
    return load_all(stream, FullLoader)
    return load_all(stream, SafeLoader)
    return load_all(stream, UnsafeLoader)
    return serialize_all([node], stream, Dumper=Dumper, **kwds)
    Scan a YAML stream and produce scanning tokens.
    Serialize a Python object into a YAML stream.
    Serialize a representation tree into a YAML stream.
    Serialize a sequence of Python objects into a YAML stream.
    Serialize a sequence of representation trees into a YAML stream.
    sort_keys=True,
    stream=None,
    tags=None,
    the corresponding tag is assigned to the scalar.
    The metaclass for YAMLObject.
    to a node in the representation tree.
    to be safe for untrusted input.
    try:
    unsafe on untrusted input.
    version=None,
    width=None,
    yaml_dumper = Dumper
    yaml_flow_style = None
    yaml_loader = [Loader, FullLoader, UnsafeLoader]
    yaml_tag = None
# ------------------------------------------------------------------------------
# break code that uses it.
# XXX "Warnings control" is now deprecated. Leaving in the API function to not
):
__version__ = "6.0.2"
class YAMLObject:
class YAMLObjectMetaclass:
def add_constructor(tag, constructor, Loader=None):
def add_implicit_resolver(tag, regexp, first=None, Loader=None, Dumper=Dumper):
def add_multi_constructor(tag_prefix, multi_constructor, Loader=None):
def add_multi_representer(data_type, multi_representer, Dumper=Dumper):
def add_path_resolver(tag, path, kind=None, Loader=None, Dumper=Dumper):
def add_representer(data_type, representer, Dumper=Dumper):
def compose(stream, Loader=Loader):
def compose_all(stream, Loader=Loader):
def dump(data, stream=None, Dumper=Dumper, **kwds):
def dump_all(
def emit(
def full_load(stream):
def full_load_all(stream):
def load(stream, Loader):
def load_all(stream, Loader):
def parse(stream, Loader=Loader):
def safe_dump(data, stream=None, **kwds):
def safe_dump_all(documents, stream=None, **kwds):
def safe_load(stream):
def safe_load_all(stream):
def scan(stream, Loader=Loader):
def serialize(node, stream=None, Dumper=Dumper, **kwds):
def serialize_all(
def unsafe_load(stream):
def unsafe_load_all(stream):
def warnings(settings=None):
except ImportError:
from .dumper import *
from .error import *
from .events import *
from .loader import *
from .nodes import *
from .tokens import *
import io
try:
