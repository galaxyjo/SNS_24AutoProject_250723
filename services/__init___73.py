
                        nonwhitespace_re.findall(original_value)
                    # _AttributeValue.
                    # already a list. This can also happen when a
                    # AttributeValueList so it can be an
                    # Eliminate any candidates that don't have this feature.
                    # html5lib calls setAttributes twice for the
                    # it again.
                    # needs to be split and converted to a
                    # same tag when rearranging the parse tree. On
                    # Tag object is cloned. If this happens, leave
                    # the second call the attribute value here is
                    # the value alone rather than trying to split
                    # This is a _RawAttributeValue (a string) that
                    )
                    candidate_set = candidate_set.intersection(set(we_have_the_feature))
                    candidate_set = set(candidates)
                    candidates = we_have_the_feature
                    modified_value = original_value
                    modified_value = self.attribute_value_list_class(
                # value is a whitespace-separated list of
                # values. Split it into a list.
                # We have a "class"-type attribute whose string
                cls.XML_PREFIX
                cls.XML_PREFIX_B
                else:
                if candidates is None:
                if isinstance(original_value, _RawAttributeValue):
                modified_attrs[attr] = modified_value
                original_value: _AttributeValue = modified_attrs[attr]
                return candidate
            "The SAXTreeBuilder class was deprecated in 4.13.0 and will be removed soon thereafter. It is completely untested and probably doesn't work; do not use it.",
            # <meta charset="utf8">
            # <meta http-equiv="content-type" content="text/html; charset=utf8">
            # anymore.
            # HTML 4 style:
            # HTML 5 style:
            # non-XHTML document is being parsed as XML.
            # Nothing to do.
            # nothing.
            # recently registered builder.
            # Register the builder while we're at it.
            # than 'html'. This is a reliable indicator that a
            # The document has already started. Don't bother checking
            # There are no builders at all.
            # They didn't ask for any features. Give them the most
            # This method was incorrectly called multiple times. Do
            # We encountered an XML declaration and then a tag other
            ) and not cls.LOOKS_LIKE_HTML.search(markup)
            ) and not cls.LOOKS_LIKE_HTML_B.search(markup)
            and self._first_processing_instruction is not None
            and self._first_processing_instruction.lower().startswith("xml ")
            calling code and can probably be removed.
            cls._warn(stacklevel=stacklevel + 2)
            DeprecationWarning,
            Each 4-tuple represents a strategy that the parser can try
            feature = feature_list.pop()
            has undergone character replacement)
            if attr in universal or (tag_specific and attr in tag_specific):
            if candidate in candidate_set:
            if len(we_have_the_feature) > 0:
            in this encoding. NOTE: This argument is not used by the
            looks_like_xml = markup_b.startswith(
            looks_like_xml = markup_s.startswith(
            markup_b: bytes = markup
            markup_s: str = markup
            modified_value: _AttributeValue
            multi_valued_attributes = self.DEFAULT_CDATA_LIST_ATTRIBUTES
            name != "html"
            or self._root_tag_name is not None
            preserve_whitespace_tags = self.DEFAULT_PRESERVE_WHITESPACE_TAGS
            provided, the most recently registered TreeBuilder subclass
            registered subclass with all the requested features.
            return
            return False
            return modified_attrs
            return None
            return self.builders[0]
            return True
            self._first_processing_instruction is not None
            self._warn(stacklevel=10)
            self.builders_for_feature[feature].insert(0, treebuilder_class)
            self.empty_element_tags = empty_element_tags
            self.empty_element_tags = self.DEFAULT_EMPTY_ELEMENT_TAGS
            setattr(this_module, name, obj)
            stacklevel=2,
            stacklevel=stacklevel,
            store_line_numbers = self.TRACKS_LINE_NUMBERS
            strategy will be tried in turn.
            string_containers = self.DEFAULT_STRING_CONTAINERS
            substituted = True
            tag["charset"] = CharsetMetaAttributeValue(charset)
            tag["content"] = ContentMetaAttributeValue(content)
            these encodings.
            this_module.__all__.append(name)
            this_module.builder_registry.register(obj)
            to convert the document to Unicode and parse it. Each
            we_have_the_feature = self.builders_for_feature.get(feature, [])
            will be used.
            x.lower() == "content-type" for x in http_equiv
            XMLParsedAsHTMLWarning,
            XMLParsedAsHTMLWarning.MESSAGE,
           `TreeBuilder.features` attribute should list its features.
           Any appropriate attribute values will be modified in place.
           to convert the markup into a Unicode string.
         `HTMLParserTreeBuilder` for implementations that take into
         account the quirks of particular parsers.
         as-is. See `LXMLTreeBuilderForXML` and
         By default, the only strategy is to parse the markup
         function.
         otherwise.
        """
        """Call this method before parsing a document."""
        """Call this method when encountering an XML declaration, or a
        """Call this when you encounter the document's root tag.
        """Do any work necessary to reset the underlying parser
        """Issue a warning about XML being parsed as HTML."""
        """Look up a TreeBuilder subclass with the desired features.
        """Might a tag with this name be an empty-element tag?
        """Perform a check on some markup to see if it looks like XML
        """Register a treebuilder based on its advertised features.
        """Replace the declared encoding in a <meta> tag with a placeholder,
        """Run any preliminary steps necessary to make incoming markup
        """Run incoming markup through some parsing process."""
        """Set up any substitutions that will need to be performed on
        """The BeautifulSoup object has been initialized and is now
        """When an attribute value is associated with a tag that can
        """Wrap an HTML fragment to make it look like a document.
        "*": {"class", "accesskey", "dropzone"},
        "<foo></foo>" will become "<foo/>", and "<foo>bar</foo>" will
        "a": {"rel", "rev"},
        "address",
        "area",
        "area": {"rel"},
        "article",
        "aside",
        "base",
        "basefont",
        "bgsound",
        "blockquote",
        "br",
        "canvas",
        "col",
        "command",
        "dd",
        "div",
        "dl",
        "dt",
        "embed",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "form": {"accept-charset"},
        "frame",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "icon": {"sizes"},
        "iframe": {"sandbox"},
        "image",
        "img",
        "input",
        "isindex",
        "keygen",
        "li",
        "link",
        "link": {"rel", "rev"},
        "main",
        "menuitem",
        "meta",
        "nav",
        "nextid",
        "noscript",
        "object": {"archive"},
        "ol",
        "output",
        "output": {"for"},
        "p",
        "param",
        "pre",
        "processing instruction" that might be an XML declaration.
        "rp": RubyParenthesisString,
        "rt": RubyTextString,
        "script": Script,
        "section",
        "source",
        "spacer",
        "style": Stylesheet,
        "table",
        "td": {"headers"},
        "template": TemplateString,
        "tfoot",
        "th": {"headers"},
        "track",
        "ul",
        "video",
        "wbr",
        #
        # attribute and have "http-equiv" set to "content-type".
        # attribute with a standin object that can take on any
        # But we can accommodate meta['http-equiv'] being made a
        # cdata_list_attribute (again, very unlikely) without much
        # cdata_list_attributes.
        # document was originally in. This means HTML 5-style <meta>
        # encoding.
        # everywhere.
        # First, cast the attrs dict to _AttributeValues. This might
        # Go down the list of features in order, and eliminate any builders
        # Go through the original list of candidates and pick the first one
        # handler.endElementNS((ns, node.nodeName), node.nodeName)
        # handler.endPrefixMapping(prefix)
        # HTML 4-style <meta> tags that provide the "content"
        # Ignore the prefix for now.
        # In both cases we will replace the value of the appropriate
        # not be accurate yet, but it will be by the time this method
        # not this is actually a problem.
        # print("End %s" % name)
        # print("Start %s, %r" % (name, attrs))
        # returns.
        # specifies meta['content'] or meta['charset'] as
        # tags that provide the "charset" attribute. It also means
        # that don't match every feature.
        # that the programmer who instantiates the TreeBuilder
        # that's in candidate_set.
        # the attribute values.
        # the behavior of sourceline and sourcepos has been made consistent
        # The only valid candidates are the ones in candidate_set.
        # There is at least a possibility that we need to modify one of
        # These are from earlier versions of HTML and are removed in HTML5.
        # These are from HTML5.
        # These are HTML5 specific, as are *.accesskey and *.dropzone above.
        # Throw away (ns, nodeName) for now.
        # TODO: store_line_numbers is probably irrelevant now that
        # TODO: This cast will fail in the (very unlikely) scenario
        # trouble.
        # We are interested in <meta> tags that say what encoding the
        # We are only interested in <meta> tags
        # We won't know until we encounter the first tag whether or
        )
        ):
        :meta private:
        :param attrs: A dictionary containing the tag's attributes.
        :param document_declared_encoding: The markup itself claims to be
        :param exclude_encodings: The user asked *not* to try any of
        :param features: A list of features to look for. If none are
        :param fragment: A fragment of HTML.
        :param markup: The markup that's about to be parsed.
        :param soup: A BeautifulSoup object.
        :param stacklevel: The stacklevel of the code calling this\
        :param tag_name: The name of a markup tag.
        :param tag_name: The name of a tag.
        :param treebuilder_class: A subclass of `TreeBuilder`. its
        :param user_specified_encoding: The user asked to try this encoding
        :return: A full HTML document.
        :return: A TreeBuilder subclass, or None if there's no
        :return: The modified dictionary that was originally passed in.
        :return: True if the markup looks like non-XHTML XML, False
        :return: Whether or not a substitution was performed.
        :yield: A series of 4-tuples: (markup, encoding, declared encoding,
        _AttributeValue,
        _Encoding,
        _Encodings,
        _RawMarkup,
        _RawOrProcessedAttributeValues,
        a `Tag` when it's output as a string.
        acceptable to the parser.
        an empty-element tag (it's not in
        An HTML document may come in to Beautiful Soup as one
        assert self.soup is not None
        attribute_dict_class: type[AttributeDict] = AttributeDict,
        attribute_value_list_class: type[AttributeValueList] = AttributeValueList,
        attrs = AttributeDict((key[1], value) for key, value in list(attrs.items()))
        Basically, replaces class="foo bar" with class=["foo", "bar"]
        be left alone.
        being associated with the TreeBuilder.
        being incorrectly parsed as HTML, and issue the warning.
        being parsed as XML.
        but some of the tree builders can't do that.
        By default, this does nothing.
        By default, this does nothing. See `HTMLTreeBuilder` for a
        candidate_set = None
        candidates = None
        case where this is used.
        charset: str | None = cast(Optional[str], tag.get("charset"))
        cls, markup: _RawMarkup | None, stacklevel: int = 3
        content: str | None = cast(Optional[str], tag.get("content"))
        Different parsers do this differently. For instance, lxml
        document_declared_encoding: _Encoding | None = None,
        doesn't. Abstracting this away lets us write simple tests
        elif content is not None and any(
        else:
        empty_element_tags: set[str] = USE_DEFAULT,
        empty-element tag if and only if it has no children.
        empty-element tags, so a tag will be presented as an
        encoding, but exit in a different encoding, and the <meta> tag
        exclude_encodings: _Encodings | None = None,
        feature_list = list(features)
        feature_list.reverse()
        for a new document.
        for attr in list(modified_attrs.keys()):
        for candidate in candidates:
        for feature in treebuilder_class.features:
        For instance: an HTMLBuilder does not consider a <p> tag to be
        have multiple values for that attribute, convert the string
        HTMLBuilder.empty_element_tags). This means an empty <p> tag
        http_equiv: list[str] = tag.get_attribute_list("http-equiv")
        if (
        if candidate_set is None or candidates is None:
        if charset is not None:
        if empty_element_tags is self.USE_DEFAULT:
        if isinstance(markup, bytes):
        if issubclass(obj, TreeBuilder):
        if len(features) == 0:
        if len(self.builders) == 0:
        if looks_like_xml:
        if markup is None:
        if multi_valued_attributes is self.USE_DEFAULT:
        if not modified_attrs or not self.cdata_list_attributes:
        if preserve_whitespace_tags is self.USE_DEFAULT:
        if self._root_tag_name is not None:
        if self.empty_element_tags is None:
        if store_line_numbers == self.USE_DEFAULT:
        if string_containers == self.USE_DEFAULT:
        if tag.name != "meta":
        introduces an empty <head> tag, and html5lib
        markup = markup[:500]
        markup: _RawMarkup,
        modified_attrs = cast(_AttributeValues, attrs)
        multi_valued_attributes: dict[str, set[str]] = USE_DEFAULT,
        NavigableString,
        needs to be changed to reflect this.
        NOTE: This method modifies its input in place.
        obj = getattr(module, name)
        pass
        preserve_whitespace_tags: set[str] = USE_DEFAULT,
        raise NotImplementedError()
        results against other HTML fragments.
        return False
        return fragment
        return modified_attrs
        return None
        return substituted
        return tag_name in self.empty_element_tags
        self,
        self, nsTuple: tuple[str, str], nodeName: str, attrs: dict[str, str]
        self, tag_name: str, attrs: _RawOrProcessedAttributeValues
        self._first_processing_instruction = None
        self._first_processing_instruction = processing_instruction
        self._root_tag_name = name
        self._root_tag_name = None
        self.attribute_dict_class = attribute_dict_class
        self.attribute_value_list_class = attribute_value_list_class
        self.builders = []
        self.builders.insert(0, treebuilder_class)
        self.builders_for_feature = defaultdict(list)
        self.cdata_list_attributes = multi_valued_attributes
        self.endElement(nodeName)
        self.preserve_whitespace_tags = preserve_whitespace_tags
        self.soup = None
        self.soup = soup
        self.soup.handle_data(content)
        self.soup.handle_endtag(name)
        self.soup.handle_starttag(name, None, None, attrs)
        self.startElement(nodeName, attrs)
        self.store_line_numbers = store_line_numbers
        self.string_containers = string_containers
        self-closing.
        store_line_numbers: bool = USE_DEFAULT,
        string_containers: dict[str, type[NavigableString]] = USE_DEFAULT,
        substituted = False
        super().__init__(*args, **kwargs)
        Tag,
        tag_specific = self.cdata_list_attributes.get(tag_name.lower(), None)
        that's not XHTML. If so, issue a warning.
        The default implementation has no opinion about which tags are
        The final markup may or may not actually present this tag as
        the XML document turns out to be a non-XHTML document that's
        This helps Beautiful Soup detect potential issues later, if
        This is much less reliable than doing the check while parsing,
        This is where we actually check whether an XML document is
        This method should not be used outside of unit tests.
        to be substituted when the tag is output to a string.
        universal: set[str] = self.cdata_list_attributes.get("*", set())
        user_specified_encoding: _Encoding | None = None,
        value to a list of strings.
        warnings.warn(
        which run HTML fragments through the parser and compare the
        while len(feature_list) > 0:
        will be presented as "<p></p>", not "<p/>" or "<p>".
        yield markup, None, None, False
      (such as HTML's 'class') willl be stored in an instance of this
      `AttributeValueList`, which is a normal Python list, and you
      class.  The default is Beautiful Soup's built-in
      will probably never need to change it.
     :py:class:`bs4.element.Tag` object. You can turn this off by
     are immune from pretty-printing; their contents will always be
     'class' into lists. Setting this to a dictionary will
     contents of those tags. The default is to use NavigableString
     customize this behavior; look at :py:attr:`bs4.builder.HTMLTreeBuilder.DEFAULT_CDATA_LIST_ATTRIBUTES`
     default by changing :py:attr:`DEFAULT_STRING_CONTAINERS`.
     doesn't keep track of this information, then store_line_numbers
     for an example.
     for every tag, no matter what the name. You can override the
     Internally, these are called "CDATA list attributes", but that
     is ``multi_valued_attributes``.
     is irrelevant.
     numbers and positions of the original markup, that information
     output as-is.
     passing store_line_numbers=False; then Tag.sourcepos and
     probably doesn't make sense to an end-user, so the argument name
     Tag.sourceline will always be None. If the parser you're using
     the classes that should be instantiated to contain the textual
     the way <pre> tags are treated in HTML. Tags in this set
     TreeBuilder will not turn any values for attributes like
     will, by default, be stored in each corresponding
    """
    """A Beautiful Soup treebuilder that listens for SAX events.
    """A mixin class for any class (a TreeBuilder, or some class used by a
    """A way of looking up TreeBuilder subclasses by their name or by desired
    """Copy TreeBuilders from the given module into this module."""
    """This TreeBuilder knows facts about HTML, such as which tags are treated
    """Turn a textual document into a Beautiful Soup object tree.
    "DetectsXMLParsedAsHTML",
    "HTMLTreeBuilder",
    "ParserRejectedMarkup",  # backwards compatibility only as of 4.13.0
    "SAXTreeBuilder",
    "TreeBuilder",
    "TreeBuilderRegistry",
    # check may be run before any Beautiful Soup objects are created.
    # They don't have html5lib installed.
    # They don't have lxml installed.
    # This is typed as str, not `ProcessingInstruction`, because this
    #:
    #: "metadata content" elements that can contain strings.
    #: "phrasing content" tags, because the content they contain is
    #: (https://html.spec.whatwg.org/#metadata-content) and looking for
    #: a list of values if possible. Upon output, the list will be
    #: A tag will be considered an empty-element
    #: A value for these tag/attribute combinations is a space- or
    #: an unusual content model for them. I made this list by going
    #: but it may do so eventually, and this information is available if
    #: By default, tags are treated as empty-element tags if they have
    #: By default, whitespace inside these HTML tags will be
    #: can be useful to be able to distinguish it.
    #: class="foo bar" means that the 'class' attribute has two values,
    #: comma-separated list of CDATA, rather than a single CDATA.
    #: converted back into a string.
    #: defines a different set of DEFAULT_EMPTY_ELEMENT_TAGS based on the
    #: encounter one of these attributes, we will parse its value into
    #: 'foo' and 'bar', not the single value 'foo bar'.  When we
    #: For some of these tags, it's because the HTML standard defines
    #: HTML 4 and HTML5 standards.
    #: instantiated with some class other than `bs4.element.NavigableString`.
    #: Most parsers don't keep track of line numbers.
    #: no contents--that is, using XML rules. HTMLTreeBuilder
    #: preserved rather than being collapsed.
    #: qualitatively different from other text in the document, and it
    #: qualitatively different from the other tags.
    #: Regular expression for seeing if byte markup has an <html> tag.
    #: Regular expression for seeing if string markup has an <html> tag.
    #: represented by a string class other than `bs4.element.NavigableString`.
    #: Some HTML tags are defined as having no contents. Beautiful Soup
    #: Soup does not treat these elements differently from other elements,
    #: space-separated list of values, not a single value. That is,
    #: tag when and only when it has no contents.
    #: The HTML standard defines these attributes as containing a
    #: The HTML standard defines these tags as block-level elements. Beautiful
    #: The Ruby tags (<rt> and <rp>) are here despite being normal
    #: The start of an XML document bytestring.
    #: The start of an XML document string.
    #: The textual contents of tags with these names should be
    #: These HTML tags need special treatment so they can be
    #: through the HTML spec
    #: TODO: Arguably <noscript> could go here but it seems
    #: treats these specially.
    #: Whitespace should be preserved inside these tags.
    #: you need to use it.
    )
    ) -> _AttributeValues:
    ) -> bool:
    ) -> Iterable[tuple[_RawMarkup, _Encoding | None, _Encoding | None, bool]]:
    ) -> None:
    ):
    :param attribute_dict_class: The value of a multi-valued attribute
    :param multi_valued_attributes: If this is set to None, the
    :param preserve_whitespace_tags: A set of tags to treat
    :param store_line_numbers: If the parser keeps track of the line
    :param string_containers: A dictionary mapping tag names to
    @classmethod
    _AttributeValues,
    _first_processing_instruction: str | None  #: :meta private:
    _RawAttributeValue,
    _root_tag_name: str | None  #: :meta private:
    `TreeBuilder`, there's a less reliable implementation based on
    }
    ALTERNATE_NAMES: Iterable[str] = []
    Any,
    appropriate warning.
    AttributeDict,
    AttributeValueList,
    builders: list[type[TreeBuilder]]
    builders_for_feature: dict[str, list[type[TreeBuilder]]]
    cast,
    cdata_list_attributes: dict[str, set[str]]  #: :meta private:
    CharsetMetaAttributeValue,
    ContentMetaAttributeValue,
    def __init__(
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __init__(self, *args: Any, **kwargs: Any) -> None:
    def _document_might_be_xml(self, processing_instruction: str) -> None:
    def _initialize_xml_detector(self) -> None:
    def _replace_cdata_list_attribute_values(
    def _root_tag_encountered(self, name: str) -> None:
    def _warn(cls, stacklevel: int = 5) -> None:
    def can_be_empty_element(self, tag_name: str) -> bool:
    def characters(self, content: str) -> None:
    def close(self) -> None:
    def endDocument(self) -> None:
    def endElement(self, name: str) -> None:
    def endElementNS(self, nsTuple: tuple[str, str], nodeName: str) -> None:
    def endPrefixMapping(self, prefix: str) -> None:
    def feed(self, markup: _RawMarkup) -> None:
    def initialize_soup(self, soup: BeautifulSoup) -> None:
    def lookup(self, *features: str) -> type[TreeBuilder] | None:
    def prepare_markup(
    def register(self, treebuilder_class: type[TreeBuilder]) -> None:
    def reset(self) -> None:
    def set_up_substitutions(self, tag: Tag) -> bool:
    def startDocument(self) -> None:
    def startElement(self, name: str, attrs: dict[str, str]) -> None:
    def startElementNS(
    def startPrefixMapping(self, prefix: str, nodeValue: str) -> None:
    def test_fragment_to_document(self, fragment: str) -> str:
    def warn_if_markup_looks_like_xml(
    DEFAULT_BLOCK_ELEMENTS: set[str] = {
    DEFAULT_CDATA_LIST_ATTRIBUTES: dict[str, set[str]] = {
    DEFAULT_CDATA_LIST_ATTRIBUTES: dict[str, set[str]] = defaultdict(set)
    DEFAULT_EMPTY_ELEMENT_TAGS: set[str] | None = None
    DEFAULT_EMPTY_ELEMENT_TAGS: set[str] = {
    DEFAULT_PRESERVE_WHITESPACE_TAGS: set[str] = {"pre", "textarea"}
    DEFAULT_PRESERVE_WHITESPACE_TAGS: set[str] = set()
    DEFAULT_STRING_CONTAINERS: dict[str, type[bs4.element.NavigableString]] = {
    DEFAULT_STRING_CONTAINERS: dict[str, type[bs4.element.NavigableString]] = {}
    different parser libraries into a single, unified interface.
    document is being incorrectly parsed as HTML, and issue an
    empty_element_tags: set[str] | None = None  #: :meta private:
    examining the raw markup.
    features.
    features: Iterable[str] = []
    for name in module.__all__:
    from . import _html5lib
    from . import _lxml
    from bs4 import BeautifulSoup
    from bs4._typing import (
    from bs4.element import (
    hasn't worked properly.
    instruction that might be an XML declaration, and also able to
    is_xml: bool = False
    Iterable,
    LOOKS_LIKE_HTML: Pattern[str] = re.compile("<[^ +]html", re.I)
    LOOKS_LIKE_HTML_B: Pattern[bytes] = re.compile(b"<[^ +]html", re.I)
    NAME: str = "[Unknown tree builder]"
    nonwhitespace_re,
    observe tags as they're opened. If you can't do that for a given
    Optional,
    pass
    Pattern,
    picklable: bool = False
    preserve_whitespace_tags: set[str]  #: :meta private:
    register_treebuilders_from(_html5lib)
    register_treebuilders_from(_lxml)
    rest of Beautiful Soup, so there have been long stretches where it
    RubyParenthesisString,
    RubyTextString,
    Script,
    soon. It was a good idea, but it wasn't properly integrated into the
    soup: BeautifulSoup | None  #: :meta private:
    specially by the HTML standard.
    string_containers: dict[str, type[NavigableString]]  #: :meta private:
    Stylesheet,
    TemplateString,
    This is an abstract superclass which smooths out the behavior of
    This is not currently used for anything, and it will be removed
    This requires being able to observe an incoming processing
    this_module = sys.modules[__name__]
    tracks_line_numbers: bool  #: :meta private:
    TRACKS_LINE_NUMBERS: bool = False
    TreeBuilder) that's in a position to detect whether an XML
    TYPE_CHECKING,
    USE_DEFAULT: Any = object()  #: :meta private:
    XML_PREFIX: str = "<?xml"
    XML_PREFIX_B: bytes = b"<?xml"
# backwards compatibility.
# builder registrations will take precedence. In general, we want lxml
# Builders are registered in reverse order of priority, so that custom
# Exceptions were moved to their own module in 4.13. Import here for
# Some useful features for a TreeBuilder to have.
# to take precedence over html5lib, because it's faster. And we only
# Use of this source code is governed by the MIT license.
# want to use HTMLParser as a last resort.
#: and use it to look up `TreeBuilder` classes in this registry.
#: The `BeautifulSoup` constructor will take a list of features
)
]
__all__ = [
__license__ = "MIT"
builder_registry: TreeBuilderRegistry = TreeBuilderRegistry()
class DetectsXMLParsedAsHTML:
class HTMLTreeBuilder:
class SAXTreeBuilder:
class TreeBuilder:
class TreeBuilderRegistry:
def register_treebuilders_from(module: ModuleType) -> None:
except ImportError:
FAST = "fast"
from . import _htmlparser  # noqa: E402
from __future__ import annotations
from bs4._typing import (
from bs4._warnings import XMLParsedAsHTMLWarning
from bs4.element import (
from bs4.exceptions import ParserRejectedMarkup
from collections import defaultdict
from types import ModuleType
from typing import (
HTML = "html"
HTML_5 = "html5"
if TYPE_CHECKING:
import bs4
import re
import sys
import warnings
PERMISSIVE = "permissive"
register_treebuilders_from(_htmlparser)
STRICT = "strict"
try:
XML = "xml"
