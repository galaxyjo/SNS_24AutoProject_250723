
                        child, child.next_element, None
                        child, child.next_element, target.next_sibling
                        child, child.previous_element, el
                        child, child.previous_element, last_child, child.parent.contents
                        child, child.previous_sibling, None
                        child.next_element is None
                        child.next_element is target.next_sibling
                        child.previous_element is el
                        child.previous_element is last_child
                        child.previous_sibling is None
                        el, el.next_element, child
                        el.next_element is child
                        last_child, last_child.next_element, child
                        last_child.next_element is child
                    "idna",
                    "mbcs",
                    "oem",
                    "string_escape",
                    "string-escape",
                    "undefined",
                    # bother.
                    # exception if we actually try to use them, so don't
                    # For one reason or another, these will raise an
                    )
                    ), "Bad next_element\nNODE: {}\nNEXT {}\nEXPECTED {}".format(
                    ), "Bad next_element\nNODE: {}\nNEXT: {}\nEXPECTED: {}".format(
                    ), "Bad previous_element\nNODE: {}\nPREV {}\nEXPECTED {}\nCONTENTS {}".format(
                    ), "Bad previous_element\nNODE: {}\nPREV: {}\nEXPECTED: {}".format(
                    ), "Bad previous_sibling\nNODE: {}\nPREV {}\nEXPECTED: {}".format(
                    assert (
                    break
                    child, child.next_sibling, None
                    child, child.previous_sibling, el.contents[idx - 1]
                    child.next_sibling is None
                    child.previous_sibling is el.contents[idx - 1]
                    continue
                    descendant, descendant.next_sibling, None
                    descendant.next_sibling is None
                    el.contents[idx - 1], el.contents[idx - 1].next_sibling, child
                    el.contents[idx - 1].next_sibling is child
                "idna",
                "mbcs",
                "oem",
                "string_escape",
                "string-escape",
                "undefined",
                # A bubbled up descendant should have no next siblings
                # bother.
                # exception if we actually try to use them, so don't
                # For one reason or another, these will raise an
                # hard-coded one.
                # Ignore the provided value and substitute a
                )
                ), "Bad next_sibling\nNODE: {}\nNEXT {}\nEXPECTED {}".format(
                ), "Bad previous_sibling\nNODE: {}\nPREV {}\nEXPECTED {}".format(
                ):
                assert (
                assert b'meta charset=""' in encoded
                assert descendant is not None
                assert e == earlier.next_element
                assert earlier == e.previous_element
                assert encoding.encode("ascii") not in encoded
                continue
                descendant = self.linkage_validator(child, True)
                el, el.next_sibling, None
                el, el.previous_element, None
                el, el.previous_sibling, None
                el.next_sibling is None
                el.previous_element is None
                el.previous_sibling is None
                elif target.next_sibling is not None:
                encoded = soup.encode(encoding)
                if el.parent is not None:
                if encoding in (
                if last_child is not None:
                if target is None:
                last_child = child
                last_child = descendant
                self.append("extra")
                super().__init__(*args, **kwargs)
                super().__setitem__(key, "OVERRIDDEN")
                target = target.parent
            """<foo attr="Brawls happen at &quot;Bob\'s Bar&quot;">a</foo>""",
            "</head><body>Shift-JIS markup goes here."
            "</table></td>"
            "</td></tr></table>",
            "<html><head>\n%s\n"
            "<p>&bull; AT&T is in the s&p 500</p>",
            "<p>&lt;&lt;sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</p>"
            "<p>\u2022 AT&amp;T is in the s&amp;p 500</p>",
            "<p>Bob&apos;s Bar</p>",
            "<p>Bob's Bar</p>",
            "<p>I said &quot;good day!&quot;</p>", '<p>I said "good day!"</p>'
            "<table><thead><tr><td>Foo</td></tr></thead>"
            "<tbody><tr><td>Bar</td></tr></tbody>"
            "<td>Here's another table:"
            "<tfoot><tr><td>Baz</td></tr></tfoot></table>"
            "<tr>"
            "<tr><td>foo</td></tr>"
            "area",
            "base",
            "br",
            "col",
            "embed",
            "frame",
            "hr",
            "img",
            "input",
            "keygen",
            "link",
            "menuitem",
            "meta",
            "param",
            "source",
            "spacer",
            "track",
            "wbr",
            # If last child, there are non next siblings
            # If not the first child, previous index should link as sibling to this index
            # is uppercase.
            # Make sure a Doctype object was created and that the DOCTYPE
            # Make sure that the doctype was correctly associated with the
            # Mark last child as either the bubbled up descendant or the current child
            # Parent should link next element to their first child
            # parse tree and that the rest of the document parsed.
            # Previous element should match the last index or the last bubbled up descendant
            # Return the child to the recursive caller
            # That child should have no previous sibling
            # We are done, so nothing to return
            )
            ), "Bad next_sibling\nNODE: {}\nNEXT: {}\nEXPECTED: {}".format(
            ), "Bad previous_element\nNODE: {}\nPREV: {}\nEXPECTED: {}".format(
            ), "Bad previous_sibling\nNODE: {}\nPREV: {}\nEXPECTED: {}".format(
            ):
            + b"</root>"
            + b"0" * (2**12)
            '<a href="http://example.org?a=1&amp;b=2;3">foo</a>',
            '<a href="http://example.org?a=1&b=2;3">foo</a>',
            '<meta content="text/html; charset=x-sjis" ' 'http-equiv="Content-type"/>'
            '<meta http-equiv="Content-language" content="ja"/>'
            '<table id="1">'
            '<table id="1"><tr><td>Here\'s another table:'
            '<table id="2">'
            '<table id="2"><tr><td>foo</td></tr></table>'
            '<this is="really messed up & stuff"></this>',
            '<this is="really messed up &amp; stuff"></this>',
            == "\N{LEFT SINGLE QUOTATION MARK}Foo\N{RIGHT SINGLE QUOTATION MARK}"
            assert (
            assert b'<?xml version="1.0"?>' in encoded
            assert doctype == "html"
            assert doctype.__class__ == Doctype
            assert encoding.encode("ascii") not in encoded
            assert isinstance(to_parse, str)
            assert new_tag.is_empty_element is True
            assert soup.encode("utf8")[: len(doctype_str)] == b"<!DOCTYPE html>"
            assert soup.p.contents[0] == "foo"
            assert soup.tag.string == "string"
            attribute_value_list_class=MyCustomAttributeValueList,
            b"\x82\xb1\x82\xea\x82\xcdShift-JIS\x82\xc5\x83R\x81[\x83f"
            b"\x83B\x83\x93\x83O\x82\xb3\x82\xea\x82\xbd\x93\xfa\x96{\x8c"
            b"\xea\x82\xcc\x83t\x83@\x83C\x83\x8b\x82\xc5\x82\xb7\x81B"
            b"</pre></body></html>"
            b"<html><head></head><body><pre>"
            b'<?xml version="1.0" encoding="utf-8"?>\n<root>'
            b'<meta charset="utf8"></head>' b'<meta id="encoding" charset="utf-8" />'
            child = el
            compare_parsed_to = to_parse
            def __init__(self, *args, **kwargs):
            def __setitem__(self, key: str, value: Any):
            descendant = None
            doctype = soup.contents[0]
            doctype_str, soup = self._document_with_doctype("html", doctype_fragment)
            earlier = e
            else:
            encoded = soup.encode(encoding)
            for encoding in PYTHON_SPECIFIC_ENCODINGS:
            hebrew_document.decode("iso8859-8").encode("utf-8")
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"'
            idx += 1
            if descendant is not None:
            if earlier:
            if encoding in (
            if idx == 0:
            if idx == last_idx:
            if isinstance(child, Tag) and child.contents:
            markup,
            multi_valued_attributes={"*": {"attr2"}},
            new_tag = soup.new_tag(name)
            return child
            return None
            soup = self.soup("")
            soup = self.soup(markup)
            soup.encode("latin1") == b'<?xml version="1.0" encoding="latin1"?>\n<root/>'
            soup.foo.decode(),
            soup.p.string
            target: Optional[Tag] = el
            while True:
        """
        """A <br> tag is designated as an empty-element tag.
        """A <p> tag is never designated as an empty-element tag.
        """A large XML document should come out the same as it went in."""
        """A real XHTML document should come out *exactly* the same as it went in."""
        """A real XHTML document should come out more or less the same as it went in."""
        """A tag that's not closed by the end of the document should be closed.
        """Assert that a given doctype string is handled correctly."""
        """Block elements can be nested."""
        """Build a Beautiful Soup object from markup."""
        """Ensure proper linkage throughout the document."""
        """Ensure that next_element and previous_element are properly
        """Generate and parse a document with the given doctype."""
        """Inline elements can be nested indefinitely."""
        """Make sure normal, everyday HTML doctypes are handled correctly."""
        """Make sure that the given tags have the correct IDs.
        """Make sure that the given tags have the correct text.
        """Make sure you can copy the tree builder.
        """One table can go inside another one."""
        """Parse some markup using Beautiful Soup and verify that
        """Parsers don't need to *understand* namespaces, but at the
        """Parsers should be able to work with SoupStrainers."""
        """Test the worst case (currently) for linking issues."""
        """Turn an HTML fragment into a document.
        """Verify that all HTML4 and HTML5 empty element (aka void element) tags
        """Whitespace must be preserved in <pre> and <textarea> tags,
        "Mostly to prevent a recurrence of a bug in the html5lib treebuilder."
        "multi_valued_attributes", [dict(a=["class"]), {"*": ["class"]}]
        "multi_valued_attributes", [None, {}, dict(b=["class"]), {"*": ["notclass"]}]
        "Prevent recurrence of a bug in the html5lib treebuilder."
        #
        # "&T" and "&p" look like incomplete character entities, but they are
        # &#147; and &#148; are invalid numeric entities referencing
        # <html> tag. This has caused problems with multivalued
        # A lowercase or mixed-case doctype becomes a Doctype.
        # A real-world test to make sure we can convert ISO-8859-9 (a
        # A seemingly innocuous document... but it's in Unicode! And
        # A warning is issued when parsing an XML document as HTML,
        # All of these entities should be converted to Unicode
        # Also run some checks on the BeautifulSoup object itself:
        # And it will take on a value that reflects its current
        # and use that to test.
        # And, of course, it would be in UTF-8, not Unicode.
        # as it rearranges the tree. This has caused problems with
        # attributes.
        # be treated as HTML with weird tag names.
        # be XHTML (tested with test_real_xhtml_document in the
        # because there was no XML declaration.
        # because XHTML is both.
        # behavior). But the other treebuilders can.
        # Both XML and HTML entities are converted to Unicode characters
        # but basic stuff should still work.
        # But that value is actually a CharsetMetaAttributeValue object.
        # But that value is actually a ContentMetaAttributeValue object.
        # but they shouldn't crash any of the parsers.
        # But two of them are ns1:tag and one of them is ns2:tag.
        # cause _popToTag to be called over and over again as we look
        # character only found in Unicode.
        # characters.
        # Comments are represented as Comment objects.
        # Document element should have no previous element or previous sibling.
        # document.
        # during parsing.
        # easy-to-understand document.
        # Encode it to UTF-8.
        # encoded in Shift-JIS.
        # encoding found in the  declaration! The horror!
        # encoding, but that encoding won't be mentioned _inside_ the
        # encoding.
        # encodings.
        # entity with no semicolon (see its subclass for the tested
        # even when the markup is already Unicode and there is no
        # for a <span> tag that wasn't there. The result is that 'text2'
        # For the rest of the story, see TestSubstitutions in
        # have no encoding.
        # Hebrew encoding) to UTF-8.
        # Here it is in Unicode. Note that it claims to be in ISO-8859-1.
        # Here's a document incorporating that meta tag.
        # Here's the <meta> tag saying that a document is
        # html5lib can set the attributes of the same tag many times
        # html5lib uses a different API to set the attributes ot the
        # If you search by the literal name of the class it's like the whitespace
        # invalid HTML entity with a semicolon and an invalid HTML
        # It also shouldn't have a next sibling.
        # it contains characters that can't be represented in the
        # it later.
        # it's not treated as a comment.
        # look like unicode_html, except that the META tag would say
        # lxml would have stripped this while parsing, but we can add
        # Make sure a Doctype object was created.
        # Make sure that the doctype was correctly associated with the
        # Make sure the parse tree is correctly encoded to various
        # Microsoft smart quotes are converted to Unicode characters during
        # multivalued attributes.
        # n.b. no "you're parsing XML as HTML" warning was given
        # need to process anything.
        # No matter how the <meta> tag is encoded, its charset attribute
        # No warning was issued about parsing an XML document as HTML,
        # not.
        # NOTE: the warning is not issued if the document appears to
        # Parse the document, and the charset is seemingly unaffected.
        # Parse the ISO-8859-1 HTML.
        # parse tree and that the rest of the document parsed.
        # parsing.
        # Pickling a tree, then unpickling it, yields a tree identical
        # process_markup correctly sets processing_instruction_class
        # resulting document.
        # resulting document. Instead, the document will appear to
        # Shift-JIS encoding, without choking.
        # should be ignored.
        # Since XHTML is not HTML5, HTML5 parsers are not tested to handle
        # Smoke test of interrelated functionality, using an
        # Smoke test to make sure the parser can handle a document in
        # Some tree builders call it iso8859-8, others call it iso-8859-9.
        # superclass) or if there is no XML declaration (tested with
        # Ta-da!
        # Test a namespaced doctype with a public id.
        # test_namespaced_html in the superclass).
        # test_tree.py.
        # That's because we're going to encode it into ISO-8859-1,
        # That's not a difference we really care about.
        # The comment is properly integrated into the tree.
        # The contents of the style tag resemble an HTML comment, but
        # The html.parser treebuilder can't distinguish between an
        # The only tag in the tag stack is the one for the root
        # The two tags have the same namespace prefix.
        # There are no tags in the open tag counter.
        # There are three <tag> tags.
        # to the original.
        # to Windows-1252 and Unicode, and &#9731; references a
        # UTF-8 instead of ISO-8859-1.
        # Verify that every tag that was opened was eventually closed.
        # Verify that the documents come out the same.
        # wasn't there.
        # We can handle a namespaced doctype with a system ID.
        # We don't have an official opinion on how these are parsed,
        # We test both Unicode and bytestring to verify that
        # What do we expect the result to look like? Well, it would
        # When a namespaced XML document is parsed as HTML it should
        # Whitespace separating the values of a multi-valued attribute
        # will always be accurate.
        # will show up outside the body of the document.
        # Windows-1252 characters. &#45; references a character common
        # Without BeautifulSoup.open_tag_counter, the </span> tag will
        # XHTML documents in any particular way.
        # You can encode an HTML document using a Python-specific
        # You can encode an XML document using a Python-specific
        )
        ) % meta_tag
        [warning] = w
        ]:
        are handled correctly.
        assert "" == doctype.strip()
        assert "“Hello” -☃" == soup.p.string
        assert "<body><div><p>text1</p>text2</div></body>" == soup.body.decode()
        assert "<p>a &amp;nosuchentity b</p>" == soup.p.decode()
        assert "<p>a &amp;nosuchentity; b</p>" == soup.p.decode()
        assert "html" == soup.contents[0].next_element.name
        assert "http://example.com/" == root["xmlns:a"]
        assert "http://example.net/" == root["xmlns:b"]
        assert "http://www.w3.org/1998/Math/MathML" == soup.html["xmlns:mathml"]
        assert "http://www.w3.org/1999/xhtml" == soup.a.namespace
        assert "http://www.w3.org/1999/xhtml" == soup.html["xmlns"]
        assert "http://www.w3.org/2000/svg" == soup.html["xmlns:svg"]
        assert "OVERRIDDEN" == tag["attr1"]
        assert "OVERRIDDEN" == tag["attr3"]
        assert "p" == soup.h2.string.next_element.name
        assert "p" == soup.p.name
        assert "Sacr\xe9 bleu!" == soup.body.string
        assert "Sacr\xe9 bleu!" == soup.root.string
        assert "text/html; charset=utf8" == content.substitute_encoding("utf8")
        assert "text/html; charset=x-sjis" == content
        assert "text/javascript" == soup.find("script")["type"]
        assert "utf8" == charset.substitute_encoding("utf8")
        assert "x-sjis" == charset
        assert (
        assert ["a", "b"] == soup.html["class"]
        assert ["css"] == soup.div.div["class"]
        assert ["foo", "bar"] == soup.a["class"]
        assert ["foo", "bar"] == soup.div["class"]
        assert [] == w
        assert [obj.ROOT_TAG_NAME] == [x.name for x in obj.tagStack]
        assert [tag.string for tag in tags] == should_match
        assert [tag["id"] for tag in tags] == should_match
        assert '<a foo="bar">text</a>' == data.a.decode()
        assert 1 == len(soup.find_all("ns2:tag"))
        assert 1, len(soup.find_all("ns2:tag", key="value"))
        assert 2 == len(soup.find_all("ns1:foo"))
        assert 2 == len(soup.find_all("ns1:tag"))
        assert 3 == len(soup.find_all("tag"))
        assert 3, len(soup.find_all(["ns1:tag", "ns2:tag"]))
        assert all(v == 0 for v in list(obj.open_tag_counter.values()))
        assert b"&lt; &lt; hey &gt; &gt;" in encoded
        assert b"charset=shift-jis" in parsed_meta.encode("shift-jis")
        assert b"charset=utf8" in parsed_meta.encode("utf8")
        assert b'charset="shift-jis"' in parsed_meta.encode("shift-jis")
        assert b'charset="utf8"' in parsed_meta.encode("utf8")
        assert blockquote.b.string == "Foo"
        assert blockquote.p.b.string == "Foo"
        assert comment == baz.previous_element
        assert comment == foo.next_element
        assert comment.__class__ == Comment
        assert doc == soup.encode()
        assert doctype == doctype_fragment
        assert doctype.__class__ == Doctype
        assert expect == tag.decode()
        assert isinstance(charset, CharsetMetaAttributeValue)
        assert isinstance(content, ContentMetaAttributeValue)
        assert isinstance(soup.contents[0], Comment)
        assert isinstance(soup.script.string, Script)
        assert isinstance(soup.style.string, Stylesheet)
        assert isinstance(tag.attrs, MyAttributeDict)
        assert isinstance(tag["attr2"], MyCustomAttributeValueList)
        assert isinstance(warning.message, XMLParsedAsHTMLWarning)
        assert loaded.__class__ == BeautifulSoup
        assert loaded.decode() == tree.decode()
        assert markup == soup.decode()
        assert markup == soup.encode("utf8")
        assert markup == soup.encode()
        assert namespace == soup.circle.namespace
        assert namespace == soup.math.namespace
        assert namespace == soup.msqrt.namespace
        assert namespace == soup.svg.namespace
        assert not any(isinstance(x, Doctype) for x in soup.descendants)
        assert not soup.p.is_empty_element
        assert obj.decode() == self.document_for(compare_parsed_to)
        assert result == expected
        assert soup.a.string == "\N{NO-BREAK SPACE}" * 2
        assert soup.a["class"] == "a b c"
        assert soup.a["class"] == ["a", "b", "c"]
        assert soup.br.is_empty_element
        assert soup.builder.is_xml is False
        assert soup.contents[0] == '?xml version="1.0" encoding="utf-8"?'
        assert soup.decode() == "<b>bold</b>"
        assert soup.div == soup.find("div", class_="foo bar")
        assert soup.encode("euc_jp") == unicode_html.encode("euc_jp")
        assert soup.encode("utf-8") == (
        assert soup.encode("utf-8") == markup
        assert soup.encode("utf-8") == unicode_html.encode("utf-8")
        assert soup.encode("utf-8").replace(b"\n", b"") == markup.replace(b"\n", b"")
        assert soup.encode("utf8")[: len(doctype_str)] == doctype_str
        assert soup.encode() == b'<?xml version="1.0" encoding="utf-8"?>\n<root/>'
        assert soup.html.body is not None
        assert soup.original_encoding in ("iso8859-8", "iso-8859-8")
        assert soup.p is not None
        assert soup.p.contents[0] == "foo"
        assert soup.p.encode("utf-8") == expected
        assert soup.pre.prettify() == pre_markup
        assert soup.style.string == "<!--Some CSS-->"
        assert soup.textarea.prettify() == "<textarea></textarea>\n"
        assert soup.textarea.prettify() == textarea_markup
        assert str(soup.br) == "<br/>"
        assert str(soup.foo) == markup
        assert str(soup.p) == "<p></p>"
        assert str(soup.p) == markup
        assert str(soup.rss) == markup
        assert str(warning.message) == XMLParsedAsHTMLWarning.MESSAGE
        assert tag.prefix == duplicate.prefix
        assert tag["attr1"] == "val1"
        assert tag["attr2"] == ["val2", "extra"]
        assert w == []
        b_tag = "<b>Inside a B tag</b>"
        baz = soup.find(string="baz")
        BeautifulSoup object, and we want to be able to copy that.
        blockquote = soup.blockquote
        builder = kwargs.pop("builder", self.default_builder)
        builder = self.default_builder
        builder = self.default_builder(
        builder = self.default_builder(attribute_dict_class=MyAttributeDict)
        charset = parsed_meta["charset"]
        child = descendant if descendant is not None else child
        child = None
        class MyAttributeDict:
        class MyCustomAttributeValueList:
        comment = soup.find(string="foobar")
        containing a single string, and then select certain strings by
        content = """<!DOCTYPE html>
        content = """<html><head></head>
        content = parsed_meta["content"]
        copy.deepcopy(self.default_builder)
        data = self.soup("<a>text</a>")
        data."""
        data.a["foo"] = "bar"
        descendant = None
        doc = """
        doc = """<?xml version="1.0" encoding="utf-8"?>
        doc = b"""<?xml version="1.0" encoding="utf-8"?>
        doctype = "<!{} {}>".format(doctype_string, doctype_fragment)
        doctype = 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"'
        doctype = soup.contents[0]
        doctype_str, soup = self._document_with_doctype(doctype_fragment)
        double_nested_b_tag = "<p>A <a>doubly <i>nested <b>tag</b></i></a></p>"
        dumped = pickle.dumps(tree, 2)
        dumped = pickle.dumps(tree, pickle.HIGHEST_PROTOCOL)
        duplicate = copy.copy(tag)
        earlier = None
        else:
        encoded = soup.encode()
        even if that would mean not prettifying the markup.
        Even if the markup shows it as an empty-element tag, it
        expect = "\N{REPLACEMENT CHARACTER}"
        expect = "<p>pi\N{LATIN SMALL LETTER N WITH TILDE}ata</p>"
        expect = '<a attr1="OVERRIDDEN" attr2="OVERRIDDEN" attr3="OVERRIDDEN">f</a>'
        expect = '<p id="pi\N{LATIN SMALL LETTER N WITH TILDE}ata"></p>'
        expected = "<p>&lt;&lt;sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</p>".encode()
        expected = (
        expected = expected.encode("utf-8")
        expected = unicode_html.replace("ISO-8859-1", "utf-8")
        foo = soup.find(string="foo")
        for child in el.contents:
        for doctype_fragment in ("doctype", "DocType"):
        for e in element.descendants:
        for encoding in PYTHON_SPECIFIC_ENCODINGS:
        for markup in [
        for name in [
        hebrew_document = b"<html><head><title>Hebrew (ISO 8859-8) in Visual Directionality</title></head><body><h1>Hebrew (ISO 8859-8) in Visual Directionality</h1>\xed\xe5\xec\xf9</body></html>"
        html = """<!DOCTYPE html>
        idx = 0
        if child is None:
        if compare_parsed_to is None:
        if el.parent is None:
        if not _recursive_call and child is not None:
        iso_latin_html = unicode_html.encode("iso-8859-1")
        last_child = None
        last_idx = len(el.contents) - 1
        loaded = pickle.loads(dumped)
        markup = """
        markup = """<?PITarget PIContent?>"""
        markup = "<![if word]>content<![endif]>"
        markup = "<!DOCTYPE html]ff>"
        markup = "<!DOCTYPE html>\n<html>\n</html>"
        markup = "<a>"
        markup = "<math><msqrt>5</msqrt></math>"
        markup = "<p>&#147;Hello&#148; &#45;&#9731;</p>"
        markup = "<p>a &nosuchentity b</p>"
        markup = "<p>a &nosuchentity; b</p>"
        markup = "<p>foo<!--foobar-->baz</p>"
        markup = "<svg><circle/></svg>"
        markup = (
        markup = '\N{BYTE ORDER MARK}<?xml version="1.0" encoding="euc-jp"><root>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</root>'
        markup = '<?xml version="1.0" encoding="euc-jp"><root>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</root>'
        markup = '<?xml version="1.0" encoding="utf-8"?><html></html>'
        markup = '<a attr1="val1" attr2="val2">f</a>'
        markup = '<a class="a b c">'
        markup = '<div class=" foo bar	 "></a>'
        markup = '<foo xml:lang="fr">bar</foo>'
        markup = '<foo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><bar xsi:schemaLocation="http://www.example.com"/></foo>'
        markup = '<html class="a b"></html>'
        markup = '<html xmlns="http://www.w3.org/1999/xhtml"><a class="a b c"></html>'
        markup = '<html><head><meta encoding="euc-jp"></head><body>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</body>'
        markup = '<p xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:date>20010504</dc:date></p>'
        markup = '<root xmlns:a="http://example.com/" xmlns:b="http://example.net/"><a:foo>This tag is in the a namespace</a:foo><b:foo>This tag is in the b namespace</b:foo></root>'
        markup = '<rss xmlns:dc="foo"><dc:creator>b</dc:creator><dc:date>2012-07-02T20:33:42Z</dc:date><dc:rights>c</dc:rights><image>d</image></rss>'
        markup = '<table><div><div class="css"></div></div></table>'
        markup = b"""<?PITarget PIContent?>"""
        markup = b"""<?xml version="1.0" encoding="utf-8"?>
        markup = b"""<?xml version="1.0" encoding="utf8"?>\n<?PITarget PIContent?>"""
        markup = b"""<?xml version="1.0" encoding="utf8"?>\n<foo/>"""
        markup = b"""<?xml version="1.0" encoding="utf-8"?><tag>string</tag>"""
        markup = b"""<?xml version="1.0"?>\n<foo/>"""
        markup = b"""<ns1:foo>content</ns1:foo><ns1:foo/><ns2:foo/>"""
        markup = b'<a class="foo bar">'
        markup = b'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:mathml="http://www.w3.org/1998/Math/MathML" xmlns:svg="http://www.w3.org/2000/svg"><head></head><body><mathml:msqrt>4</mathml:msqrt><b svg:fill="red"></b></body></html>'
        markup = doctype + "\n<p>foo</p>"
        meta_tag = (
        meta_tag = '<meta id="encoding" charset="x-sjis" />'
        namespace = "http://www.w3.org/1998/Math/MathML"
        namespace = "http://www.w3.org/2000/svg"
        nested_b_tag = "<p>A <i>nested <b>tag</b></i></p>"
        obj = BeautifulSoup(to_parse, builder=builder)
        parsed_meta = soup.find("meta", {"http-equiv": "Content-type"})
        parsed_meta = soup.find("meta", id="encoding")
        pass
        pickled = pickle.dumps(soup, pickle.HIGHEST_PROTOCOL)
        pre_markup = "<pre>a   z</pre>\n"
        quote = b"<p>\x91Foo\x92</p>"
        result = soup.encode("utf-8")
        return BeautifulSoup(markup, builder=builder, **kwargs)
        return default_builder
        return doctype.encode("utf8"), soup
        return self.default_builder(**kwargs).test_fragment_to_document(markup)
        root = soup.root
        self, doctype_fragment: str, doctype_string: str = "DOCTYPE"
        self, el: Tag, _recursive_call: bool = False
        self, tags: Iterable[Tag], should_match: Iterable[str]
        self, to_parse: _IncomingMarkup, compare_parsed_to: Optional[str] = None
        self.assert_soup(
        self.assert_soup("&#1000000000;", expect)
        self.assert_soup("&#10000000000000;", expect)
        self.assert_soup("&#x10000000000000;", expect)
        self.assert_soup("<b>", "<b></b>")
        self.assert_soup("<br /><br /><br />", "<br/><br/><br/>")
        self.assert_soup("<br/><br/><br/>", "<br/><br/><br/>")
        self.assert_soup("<br>", "<br/>")
        self.assert_soup("<em><em></em></em>")
        self.assert_soup("<foo attr='bar'></foo>", '<foo attr="bar"></foo>')
        self.assert_soup("<p>", "<p/>")
        self.assert_soup("<p>", "<p></p>")
        self.assert_soup("<p>foo</p>")
        self.assert_soup("<p>pi&#241;ata</p>", expect)
        self.assert_soup("<p>pi&#xf1;ata</p>", expect)
        self.assert_soup("<p>pi&#Xf1;ata</p>", expect)
        self.assert_soup("<p>pi&ntilde;ata</p>", expect)
        self.assert_soup('<a b="<a>"></a>', '<a b="&lt;a&gt;"></a>')
        self.assert_soup('<a href="http://example.org?a=1&amp;b=2;3"></a>')
        self.assert_soup('<p id="pi&#241;ata"></p>', expect)
        self.assert_soup('<p id="pi&#xf1;ata"></p>', expect)
        self.assert_soup('<p id="pi&#Xf1;ata"></p>', expect)
        self.assert_soup('<p id="pi&ntilde;ata"></p>', expect)
        self.assert_soup(b_tag)
        self.assert_soup(double_nested_b_tag)
        self.assert_soup(markup)
        self.assert_soup(nested_b_tag)
        self.assert_soup(pre_markup)
        self.assert_soup(text)
        self.assert_soup(text, expected)
        self.assert_soup(textarea_markup)
        self.assertConnectedness(soup)
        self.assertConnectedness(soup.article)
        self.assertDoctypeHandled(
        self.assertDoctypeHandled("html")
        self.assertDoctypeHandled(doctype)
        self.assertDoctypeHandled('foo SYSTEM "http://www.example.com/"')
        self.assertDoctypeHandled('xsl:stylesheet PUBLIC "htmlent.dtd"')
        self.assertDoctypeHandled('xsl:stylesheet SYSTEM "htmlent.dtd"')
        self.linkage_validator(soup)
        self.soup(markup)
        set for all descendants of the given element.
        shift_jis_html = (
        shouldn't be presented that way.
        some mechanism.
        Some parsers treat <br></br> as one <br/> tag, some parsers as
        soup = BeautifulSoup(doc, "lxml-xml")
        soup = pickle.loads(pickled)
        soup = self.soup("<!DOCTYPE>")
        soup = self.soup("<a>&nbsp;&nbsp;</a>")
        soup = self.soup("<blockquote><p><b>Foo</b></p></blockquote>")
        soup = self.soup("<body><div><p>text1</p></span>text2</div></body>")
        soup = self.soup("<br></br>")
        soup = self.soup("<html><h2>\nfoo</h2><p></p></html>")
        soup = self.soup("<p/>")
        soup = self.soup("<root/>")
        soup = self.soup("<style><!--Some CSS--></style>")
        soup = self.soup("<style>Some CSS</style><script>Some Javascript</script>")
        soup = self.soup("<textarea></textarea>")
        soup = self.soup("A <b>bold</b> <meta/> <i>statement</i>", parse_only=strainer)
        soup = self.soup(BAD_DOCUMENT)
        soup = self.soup(content)
        soup = self.soup(doc)
        soup = self.soup(hebrew_document, from_encoding="iso8859-8")
        soup = self.soup(html)
        soup = self.soup(iso_latin_html)
        soup = self.soup(markup)
        soup = self.soup(markup, builder=builder)
        soup = self.soup(markup, multi_valued_attributes=multi_valued_attributes)
        soup = self.soup(markup, parse_only=SoupStrainer(name="html"))
        soup = self.soup(pre_markup)
        soup = self.soup(quote, from_encoding="windows-1252")
        soup = self.soup(shift_jis_html)
        soup = self.soup(text)
        soup = self.soup(textarea_markup)
        soup = self.soup(unicode_html)
        soup = self.soup(xml)
        soup.foo["attr"] = 'Brawls happen at "Bob\'s Bar"'
        soup.script.string = 'console.log("< < hey > > ");'
        strainer = SoupStrainer("b")
        tag = soup.a
        tag = soup.document
        tag["attr3"] = True
        text = """<foo attr='bar "brawls" happen'>a</foo>"""
        text = "<p>&lt;&lt;sacr&eacute;&#32;bleu!&gt;&gt;</p>"
        textarea_markup = "<textarea> woo\nwoo  </textarea>\n"
        The details depend on the builder.
        the output markup is as expected.
        This applies to all tags except empty-element tags.
        This is important because the builder is part of a
        This is used in tests that define a bunch of tags, each
        tree = self.soup("<a><b>foo</a>")
        two tags, but it should always be an empty-element tag.
        unicode_html = '<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="Content-type"/></head><body><p>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</p></body></html>'
        unicode_html = shift_jis_html.decode("shift-jis")
        very least they should not choke on namespaces or lose
        with warnings.catch_warnings(record=True) as w:
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
     <a href="2"></a>
    """
    """A basic test of a treebuilder's competence.
    """Smoke test for a tree builder that supports HTML5."""
    #
    # Beautiful Soup than tests of the tree builders. But parsers are
    # Generally speaking, tests below this point are more tests of
    # Tests that are common to HTML and XML tree builders.
    # to detect any differences between them.
    # weird, so we run these tests separately for every tree builder
    )
    ) -> None:
    ) -> Optional[PageElement]:
    ) -> Tuple[bytes, BeautifulSoup]:
    @property
    @pytest.mark.parametrize(
    <ns1:tag>bar</ns1:tag>
    <ns1:tag>foo</ns1:tag>
    <ns2:tag key="value">baz</ns2:tag>
    and different parsers can handle it differently. But with the
    Any HTML treebuilder, present or future, should be able to pass
    Any,
    assertSoupEquals = assert_soup
    AttributeValueList,
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    def __init__(self, *args, **kwargs): pass
    def _document_with_doctype(
    def assert_selects(self, tags: Iterable[Tag], should_match: Iterable[str]) -> None:
    def assert_selects_ids(
    def assert_soup(
    def assertConnectedness(self, element: Tag) -> None:
    def assertDoctypeHandled(self, doctype_fragment: str) -> None:
    def default_builder(self) -> Type[TreeBuilder]:
    def document_for(self, markup: str, **kwargs: Any) -> str:
    def linkage_validator(
    def soup(self, markup: _IncomingMarkup, **kwargs: Any) -> BeautifulSoup:
    def test_ampersand_in_attribute_value_gets_escaped(self):
    def test_angle_brackets_in_attribute_values_are_escaped(self):
    def test_apos_entity(self):
    def test_attribute_multi_valued(self, multi_valued_attributes):
    def test_attribute_not_multi_valued(self, multi_valued_attributes):
    def test_attribute_values_with_double_nested_quotes_get_quoted(self):
    def test_attribute_values_with_nested_quotes_are_left_alone(self):
    def test_basic_namespaces(self):
    def test_br_is_always_empty_element_tag(self):
    def test_can_parse_unicode_document(self):
    def test_can_parse_unicode_document_begining_with_bom(self):
    def test_closing_namespaced_tag(self):
    def test_closing_tag_with_no_opening_tag(self):
    def test_comment(self):
    def test_copy_tag_preserves_namespace(self):
    def test_correctly_nested_tables(self):
    def test_custom_attribute_dict_class(self):
    def test_custom_attribute_value_list_class(self):
    def test_deepcopy(self):
    def test_deeply_nested_multivalued_attribute(self):
    def test_detect_xml_parsed_as_html(self):
    def test_docstring_generated(self):
    def test_docstring_includes_correct_encoding(self):
    def test_doctype_filtered(self):
    def test_double_head(self):
    def test_empty_doctype(self):
    def test_empty_element_tags(self):
    def test_entities_converted_on_the_way_out(self):
    def test_entities_in_attributes_converted_to_unicode(self):
    def test_entities_in_foreign_document_encoding(self):
    def test_entities_in_strings_converted_during_parsing(self):
    def test_entities_in_text_converted_to_unicode(self):
    def test_escaped_ampersand_in_attribute_value_is_left_alone(self):
    def test_find_by_prefixed_name(self):
    def test_formatter_processes_script_tag_for_xml_documents(self):
    def test_head_tag_between_head_and_body(self):
    def test_html_tags_have_namespace(self):
    def test_html5_style_meta_tag_reflects_current_encoding(self):
    def test_invalid_doctype(self):
    def test_invalid_html_entity(self):
    def test_large_xml_document(self):
    def test_mathml_tags_have_namespace(self):
    def test_meta_tag_reflects_current_encoding(self):
    def test_mixed_case_doctype(self):
    def test_multipart_strings(self):
    def test_multiple_copies_of_a_tag(self):
    def test_multivalued_attribute_on_html(self):
    def test_multivalued_attribute_value_becomes_list(self):
    def test_multivalued_attribute_with_whitespace(self):
    def test_namespaced_attributes(self):
    def test_namespaced_attributes_xml_namespace(self):
    def test_namespaced_html(self):
    def test_namespaced_public_doctype(self):
    def test_namespaced_system_doctype(self):
    def test_namespaces_are_preserved(self):
    def test_nested_block_level_elements(self):
    def test_nested_formatting_elements(self):
    def test_nested_inline_elements(self):
    def test_nested_namespaces(self):
    def test_non_breaking_spaces_converted_on_the_way_in(self):
    def test_normal_doctypes(self):
    def test_out_of_range_entity(self):
    def test_p_tag_is_never_empty_element(self):
    def test_pickle_and_unpickle_bad_markup(self):
    def test_pickle_and_unpickle_identity(self):
    def test_popping_namespaced_tag(self):
    def test_preserved_whitespace_in_pre_and_textarea(self):
    def test_processing_instruction(self):
    def test_public_doctype_with_url(self):
    def test_python_specific_encodings_not_used_in_charset(self):
    def test_python_specific_encodings_not_used_in_xml_declaration(self):
    def test_quot_entity_converted_to_quotation_mark(self):
    def test_real_hebrew_document(self):
    def test_real_iso_8859_document(self):
    def test_real_shift_jis_document(self):
    def test_real_xhtml_document(self):
    def test_single_quote_attribute_values_become_double_quotes(self):
    def test_smart_quotes_converted_on_the_way_in(self):
    def test_soupstrainer(self):
    def test_special_string_containers(self):
    def test_strings_resembling_character_entity_references(self):
    def test_svg_tags_have_namespace(self):
    def test_system_doctype(self):
    def test_tag_with_no_attributes_can_have_attributes_added(self):
    def test_tags_are_empty_element_if_and_only_if_they_are_empty(self):
    def test_unclosed_tags_get_closed(self):
    def test_worst_case(self):
    def test_xml_declaration(self):
    def test_xml_declaration_becomes_comment(self):
    Doctype,
    from soupsieve import SelectorSyntaxError
    import lxml.etree
    Iterable,
    LXML_PRESENT = False
    LXML_PRESENT = True
    LXML_VERSION = (0,)
    LXML_VERSION = lxml.etree.LXML_VERSION
    markup in these tests, there's not much room for interpretation.
    Optional,
    PageElement,
    PYTHON_SPECIFIC_ENCODINGS,
    Script,
    SOUP_SIEVE_PRESENT = False
    SOUP_SIEVE_PRESENT = True
    Stylesheet,
    Tag,
    these tests. With invalid markup, there's room for interpretation,
    Tuple,
    Type,
    xmlns:ns1="http://example.com/ns1"
    xmlns:ns2="http://example.com/ns2">
    XMLParsedAsHTMLWarning,
   </footer>
   <article id="a" >
   <div><a href="1"></div>
   <footer>
  </article>
  </body>
  </script>
  <body>foo</body>
  <link></link>
  <script type="text/javascript">
 <body>
"""
"""Helper classes for tests."""
# @pytest.mark.skipIf on the following conditionals to skip them
# if the libraries are not installed.
# Some tests depend on specific third-party libraries. We use
# Use of this source code is governed by the MIT license.
)
__license__ = "MIT"
<! DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">The doctype is invalid because it contains extra whitespace
<! This document starts with a bogus declaration ><div>a</div>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<!DOCTYPE html>
<!DOCTYPE xsl:stylesheet PUBLIC "htmlent.dtd">
<!DOCTYPE xsl:stylesheet SYSTEM "htmlent.dtd">
</body>
</child>
</Document>
</head>
</html>
</html>"""
</parent>"""
</script>
<b b="20" a="1" b="10" a="2" a="3" a="4">Multiple values for the same attribute.</b>
<body>
<body><?xml encoding="utf-8" ?><html></html></body>
<body>Goodbye.</body>
<child xmlns="http://ns2/" xmlns:ns3="http://ns3/">
<div><![CDATA[A CDATA section where it doesn't belong]]></div>
<div><a \u2603="snowman">Attribute name contains Unicode characters</a></div>
<div><a href="foo</a>, </a><a href="bar">that attribute value was closed by the subsequent tag</a></div>
<div><a href="http://example.com/</a> that attribute value never got closed</div>
<div><a style={height:21px;}>That attribute value was bogus</a></div>
<div><a><B><Cd><EFG>Mixed case tags are folded to lowercase</efg></CD></b></A></div>
<div><blockquote><p><b>This p tag is cut off by</blockquote></p>the end of the blockquote tag</div>
<div><div id="1">\n <a href="link1">This link is never closed.\n</div>\n<div id="2">\n <div id="3">\n   <a href="link2">This link is closed.</a>\n  </div>\n</div></div>
<div><our\u2603>Tag name contains Unicode characters</our\u2603></div>
<div><p>Paragraphs shouldn't contain block display elements, but this one does: <dl><dt>you see?</dt></p>
<div><script>if (i < 2) { alert("<b>Markup within script tags should be treated as literal.</b>"); }</script></div>
<div><svg><![CDATA[HTML5 does allow CDATA sections in SVG]]></svg></div>
<div><table id="1"><tr><td>Here's a nested table:<table id="2"><tr><td>foo</td></tr></table></td></div>
<div><table><div>This table contains bare markup</div></table></div>
<div><table><td nowrap>That boolean attribute had no value</td></table></div>
<div><table><tr><td>Here's a table</td></tr></table></div>
<div><textarea>Within a textarea, markup like <b> tags and <&<&amp; should be treated as literal</textarea></div>
<div>A <br> tag that supposedly has contents.</br></div>
<div>A <meta> tag</div>
<div>AT&T</div>
<div>Here's a nonexistent entity: &#foo; (do you see it?)</div>
<div>This document contains <!an incomplete declaration <div>(do you see it?)</div>
<div>This document contains a <!DOCTYPE surprise>surprise doctype</div>
<div>This document ends before the entity finishes: &gt
<div>This document ends with <!an incomplete declaration
<div>This numeric entity is missing the final semicolon: <x t="pi&#241ata"></div>
<div>This tag contains nothing but whitespace: <b>    </b></div>
<Document xmlns="http://example.com/ns0"
<grandchild ns3:attr="value" xmlns="http://ns4/"/>
<head>
<head><title>blabla</title></head>
<head><title>Hello.</title></head>
<html lang="en">
<html xmlns="http://www.w3.org/1999/xhtml">
<html>
<parent xmlns="http://ns1/">
<script type="text/javascript">
<title>Ordinary HEAD element test</title>
<w:document xmlns:w="http://example.com/ns0"/>"""
alert("Help!");
BAD_DOCUMENT: str = """A bare string
class HTML5TreeBuilderSmokeTest:
class HTMLTreeBuilderSmokeTest:
class SoupTest:
class TreeBuilderSmokeTest:
class XMLTreeBuilderSmokeTest:
default_builder: Type[TreeBuilder] = HTMLParserTreeBuilder
except ImportError:
from bs4 import BeautifulSoup
from bs4._typing import _IncomingMarkup
from bs4.builder import (
from bs4.builder import TreeBuilder
from bs4.builder._htmlparser import HTMLParserTreeBuilder
from bs4.element import (
from bs4.filter import SoupStrainer
from typing import (
Hello, world!
HTML5LIB_PRESENT = importlib.util.find_spec("html5lib") is not None
import copy
import importlib
import pickle
import pytest
import warnings
try:
