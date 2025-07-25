
                        and original_features in builder.ALTERNATE_NAMES
                        break
                        current_data = " "
                        current_data = "\n"
                        filename = filename[:-1]
                        filename=filename,
                        GuessedAtParserWarning,
                        GuessedAtParserWarning.MESSAGE % values,
                        isinstance(original_features, str)
                        line_number=line_number,
                        markup_type=markup_type,
                        parser=builder.NAME,
                        stacklevel=2,
                        strippable = False
                    "Couldn't find a tree builder with the features you "
                    "Keyword arguments to the BeautifulSoup constructor will be ignored. These would normally be passed into the TreeBuilder constructor, but a TreeBuilder instance was passed in as `builder`."
                    "requested: %s. Do you need to install a parser library?"
                    # and the warning is not necessary.
                    # If there is no filename at all, the user is most likely in a REPL,
                    % ",".join(features)
                    % (old_name, new_name),
                    )
                    caller = sys._getframe(1)
                    DeprecationWarning,
                    else:
                    f"The given value for parse_only will exclude everything: {parse_only}",
                    fnl = filename.lower()
                    globals = caller.f_globals
                    globals = sys.__dict__
                    if "\n" in current_data:
                    if fnl.endswith((".pyc", ".pyo")):
                    if i not in self.ASCII_SPACES:
                    indent_level = 0
                    indent_level = None
                    line_number = 1
                    line_number = caller.f_lineno
                    markup_type = "HTML"
                    markup_type = "XML"
                    most_recently_popped = self.popTag()
                    or (
                    original_features == builder.NAME
                    pass
                    stacklevel=3,
                    'The "%s" argument to the BeautifulSoup constructor '
                    UserWarning,
                    values = dict(
                    warnings.warn(
                    'was renamed to "%s" in Beautiful Soup 4.0.0'
                "Beautiful Soup 4 does not respect the isHTML argument to the "
                "Beautiful Soup 4 does not respect the selfClosingTags argument to the "
                "BeautifulSoup constructor. Entities are always converted "
                "BeautifulSoup constructor. Smart quotes are always converted "
                "BeautifulSoup constructor. Suggest you use "
                "BeautifulSoup constructor. The tree builder is responsible "
                "BS4 does not respect the convertEntities argument to the "
                "BS4 does not respect the markupMassage argument to the "
                "BS4 does not respect the smartQuotesTo argument to the "
                "features='lxml' for HTML and features='lxml-xml' for "
                "for any necessary markup massage."
                "for understanding self-closing tags."
                "The markup you provided was rejected by the parser. Trying a different parser or a different encoding may help.\n\nOriginal exception(s) from parser:\n "
                "to Unicode characters."
                "XML."
                "You provided Unicode markup but also provided a value for from_encoding. Your from_encoding will be ignored."
                # (as it may be in a multithreading situation).
                # and we had to guess. Issue a warning.
                # go into an XML document because it means nothing
                # of code as our warnings.warn() call gets, even if the answer is wrong
                # outside of Python.
                # The user did not tell us which TreeBuilder to use,
                # This code adapted from warnings.py so that we get the same line
                # This is a special Python encoding; it can't actually
                )
                + "\n ".join(other_exceptions)
                and " " not in markup
                and (not self.parse_only.allow_string_creation(current_data))
                and b" " not in markup
                and len(self.tagStack) <= 1
                and markup
                and not (
                any(markup.startswith(prefix) for prefix in ("http:", "https:"))
                any(markup.startswith(prefix) for prefix in (b"http:", b"https:"))
                break
                caller = None
                declared_encoding = None
                descendant.next_element = target.next_sibling
                elif pretty_print is False:
                else:
                encoding_part = ' encoding="%s"' % declared_encoding
                except ValueError:
                f"Incoming markup is of an invalid type: {markup!r}. Markup must be a string, a bytestring, or an open filehandle."
                features = [features]
                features = self.DEFAULT_BUILDER_FEATURES
                filename = globals.get("__file__")
                for i in current_data:
                if builder.is_xml:
                if caller:
                if filename:
                if inclusivePop:
                if pretty_print is True:
                if strippable:
                indent_level = 0
                indent_level = None
                not original_builder
                prev_el.next_element = None
                previous_element = o.previous_element
                raise FeatureNotFound(
                rejections.append(e)
                return
                return False
                return kwargs.pop(old_name)
                self._feed()
                self._markup_resembles_filename(markup)
                self.parse_only
                self.string_container_stack[-1].name, container
                strippable = True
                success = True
                target.next_sibling.previous_element = child
                try:
                warning = f"As of 4.13.0, the pretty_print argument to BeautifulSoup.decode has been removed, to match Tag.decode. Pass in a value of indent_level={indent_level} instead."
                warnings.warn(
               be determined automatically.
               subclass for the current location in the document will
               use. If a document is being processed, an appropriate
            "BeautifulSoup objects don't support insert_before()."
            "fromEncoding", "from_encoding"
            "The BeautifulStoneSoup class was deprecated in version 4.0.0. Instead of using "
            # _last_decendant is typed as returning Optional[PageElement],
            # A builder class was passed in; it needs to be instantiated.
            # Beautiful Soup will still parse the input as markup,
            # but the value can't be None here, because el is a Tag
            # First child should be linked to the parent, and no previous siblings.
            # If whitespace is not preserved, and this string contains
            # involving passing non-markup to Beautiful Soup.
            # Issue a warning if we can tell in advance that
            # Issue warnings for a couple beginner problems
            # nothing but ASCII spaces, replace it with a single space
            # Nothing to pop. This shouldn't happen.
            # or newline.
            # Parent should be linked to first child
            # parse tree, so use a default we know is always available.
            # parse_only will exclude the entire tree.
            # Print the XML declaration
            # Reset the data collector.
            # Should we add this string to the tree at all?
            # since that is sometimes the intended behavior.
            # The BeautifulSoup object itself can never be popped.
            # We are no longer linked to whatever this element is
            # We don't know which builder was used to build this
            # which we know has contents.
            (isinstance(markup, bytes) and b"<" not in markup and b"\n" not in markup)
            (purportedly) found in its source document.
            )
            ):
            and len(self.tagStack) <= 1
            and not self.parse_only.allow_tag_creation(nsprefix, name, attrs)
            and tag == self.preserve_whitespace_tag_stack[-1]
            as a full HTML or XML document.
            assert not kwargs
            attr_container,
            attr_container.update(attrs)
            attrs,
            be used instead of ``kwattrs`` for attributes like 'class'
            builder = builder_class(**kwargs)
            builder = None
            builder_class = builder
            builder_class = possible_builder_class
            child.previous_element = el
            child.previous_sibling = None
            closely enough to justify issuing a warning.
            container = self.builder.string_containers.get(
            containerClass = self.string_container(containerClass)
            current_data = "".join(self.current_data)
            currently in scope in the document.
            d["builder"] = type(self.builder)
            declared_encoding: Optional[str] = eventual_encoding
            decoded = markup
            decoded = markup.decode("utf-8", "replace")
            del d["_most_recent_element"]
            del kwargs["convertEntities"]
            del kwargs["isHTML"]
            del kwargs["markupMassage"]
            del kwargs["selfClosingTags"]
            del kwargs["smartQuotesTo"]
            DeprecationWarning,
            descendant = cast(PageElement, child._last_descendant(False))
            el.next_element = child
            elif indent_level is False:
            elif target.next_sibling is not None:
            encoding_part = ""
            except ParserRejectedMarkup as e:
            filelike = True
            from_encoding = None
            if (
            if byte in b"?*#&;>$|":
            if declared_encoding is not None:
            if eventual_encoding in PYTHON_SPECIFIC_ENCODINGS:
            if features is None or len(features) == 0:
            if indent_level is True:
            if isinstance(features, str):
            if kwargs:
            if name == t.name and nsprefix == t.prefix:
            if not self._markup_is_url(markup):
            if not self.open_tag_counter.get(name):
            if not self.preserve_whitespace_tag_stack:
            if old_name in kwargs:
            if parse_only.excludes_everything:
            if possible_builder_class is None:
            if pretty_print is not None:
            if prev_el is not None and prev_el is not el:
            if previous_element is None:
            if target is None:
            If this is None, the document will be a Unicode string.
            indent_level = None
            indent_level, eventual_encoding, formatter, iterator
            'it, pass features="xml" into the BeautifulSoup constructor.',
            markup = markup.read()
            markup, from_encoding, exclude_encodings=exclude_encodings
            markup_b = markup
            markup_b = markup.encode("utf8")
            MarkupResemblesLocatorWarning,
            MarkupResemblesLocatorWarning.FILENAME_MESSAGE % dict(what="filename"),
            MarkupResemblesLocatorWarning.URL_MESSAGE % dict(what="URL"),
            most_recently_popped = self.popTag()
            name,
            namespace,
            namespaces=namespaces,
            next_element = o.next_element
            next_sibling = o.next_sibling
            None,
            nsprefix,
            o = containerClass(current_data)
            or (isinstance(markup, str) and "<" not in markup and "\n" not in markup)
            other_exceptions = [str(e) for e in rejections]
            parent = self.currentTag
            parse tree. This is only used by `Tag.decode_contents` and
            possible_builder_class = builder_registry.lookup(*features)
            prefix = ""
            prefix = '<?xml version="1.0"%s?>\n' % encoding_part
            pretty_print = kwargs.pop("pretty_print", None)
            prev_el = child.previous_element
            previous_element = most_recent_element
            previous_element = self._most_recent_element
            previous_sibling = o.previous_sibling
            problem = (
            raise ParserRejectedMarkup(
            raise TypeError(
            return False
            return None
            return tag
            self,
            self._linkage_fixer(parent)
            self._most_recent_element,
            self._most_recent_element.next_element = tag
            self.builder = HTMLParserTreeBuilder()
            self.builder = self.builder()
            self.builder,
            self.builder.feed(self.markup)
            self.builder.initialize_soup(self)
            self.contains_replacement_characters,
            self.current_data = []
            self.currentTag = self.tagStack[-1]
            self.currentTag is not None and self.currentTag.name != self.ROOT_TAG_NAME
            self.currentTag,
            self.currentTag.contents.append(tag)
            self.declared_html_encoding,
            self.markup,
            self.object_was_parsed(o)
            self.open_tag_counter[tag.name] += 1
            self.open_tag_counter[tag.name] -= 1
            self.original_encoding,
            self.parse_only
            self.popTag()
            self.preserve_whitespace_tag_stack
            self.preserve_whitespace_tag_stack.append(tag)
            self.preserve_whitespace_tag_stack.pop()
            self.reset()
            self.string_container_stack.append(tag)
            self.string_container_stack.pop()
            source document.
            sourceline=sourceline,
            sourcepos=sourcepos,
            stacklevel=2,
            stacklevel=3,
            t = self.tagStack[i]
            tag was (purportedly) found.
            tag was found.
            tag.string = string
            target = target.parent
            that are reserved words in Python.
            the standard formatters.
            try:
            Type[NavigableString], self.element_classes.get(container, container)
            warning = f"As of 4.13.0, the first argument to BeautifulSoup.decode has been changed from bool to int, to match Tag.decode. Pass in a value of {indent_level} instead."
            warnings.warn(
            warnings.warn(warning, DeprecationWarning, stacklevel=2)
            you probably won't need to use it.
           attribute values are expected to be simple strings; processing
           indented this many levels. (The ``formatter`` decides what a
           'level' means, in terms of spaces or other characters
           of multi-valued attributes such as "class" comes later.
           output.) This is used internally in recursive calls while
           pretty-printing.
          given tag.
          to but *not* including the most recent instqance of the
         "lxml-xml", "html.parser", or "html5lib") or it may be the
         `features`. You only need to use this if you've implemented a
         and virtual environments.
         Apart from this, any keyword arguments passed into the
         Beautiful Soup 3. None of these arguments do anything in
         Beautiful Soup 4; they will result in a warning and then be
         Beautiful Soup gives you the same results across platforms
         BeautifulSoup constructor are propagated to the TreeBuilder
         built. This is useful for subclassing Tag or NavigableString
         classes like Tag and NavigableString, to other classes you'd
         constructor accepts certain keyword arguments used in
         constructor. This makes it possible to configure a
         custom TreeBuilder.
         document to be parsed. Pass this in if Beautiful Soup is
         encodings known to be wrong. Pass this in if you don't know
         guessing wrongly about the document's encoding.
         ignored.
         instance to use) instead of looking one up based on
         large to fit into memory.
         like to be instantiated instead as the parse tree is
         markup to be parsed.
         matching the SoupStrainer will be considered. This is useful
         one to use.
         recommended that you name a specific parser, so that
         the document's encoding but you know Beautiful Soup's guess is
         to modify default behavior.
         TreeBuilder by passing in arguments, not just by saying which
         type of markup to be used ("html", "html5", "xml"). It's
         used. This may be the name of a specific parser ("lxml",
         when parsing part of a document that would otherwise be too
         wrong.
        """
        """Called by the tree builder when a chunk of textual data is
        """Called by the tree builder when a new tag is encountered.
        """Called by the tree builder when an ending tag is encountered.
        """Constructor.
        """Create a new `NavigableString` associated with this `BeautifulSoup`
        """Create a new BeautifulSoup object with the same TreeBuilder,
        """Create a new Tag associated with this BeautifulSoup object.
        """Ensure `markup` is Unicode so it's safe to send into warnings.warn.
        """Error-handling method to issue a warning if incoming markup
        """Error-handling method to raise a warning if incoming markup looks
        """Find the class that should be instantiated to hold a given kind of
        """Internal method called by _popToTag when a tag is closed.
        """Internal method called by handle_starttag when a tag is opened.
        """Internal method that parses previously set markup, creating a large
        """Make sure linkage of this fragment is sound."""
        """Method called by the TreeBuilder to integrate an object into the
        """Method called by the TreeBuilder when the end of a data segment
        """Pops the tag stack up to and including the most recent
        """Reset this object to a state as though it had never parsed any
        """Returns a string representation of the parse tree
        """This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
        "You are trying to use a Python 3-specific version of Beautiful Soup under Python 2. This will not work. The final version of Beautiful Soup to support Python 2 was 4.9.3."
        #
        #  backslashes, so checking that doesn't seem as helpful.)
        # (Paths to Windows network shares contain consecutive
        # A colon in any position other than position 1 (e.g. after a
        # and find a parent with a sibling. It should have no next sibling.
        # appear in Windows filenames.
        # argument to this method (or a keyword argument with the old
        # As the final step, link last descendant. It should be linked
        # Assume that this is either Tag or a subclass of Tag. If not,
        # At this point either we have a TreeBuilder instance in
        # At this point we know markup is a string or bytestring.  If
        # bool called pretty_print, which gave the method a different
        # builder, or we have a builder_class that we can instantiate
        # case someone is still passing a boolean in as the first
        # Characters that have special meaning to Unix shells. (< was
        # Check if we are inserting into an already parsed node.
        # Clear out the markup and remove the builder's circular
        # Close out any unfinished strings and close all the open tags.
        # consecutive spaces (as seen in fixed-width data).
        # container class.
        # Convert the document to Unicode.
        # custom subclass) instead of the one we'd use normally.
        # don't need it.
        # enough to a file to justify issuing a warning.
        # excluded before this method was called.)
        # Frequently a tree builder can't be pickled.
        # If _most_recent_element is present, it's a Tag object left
        # If necessary, restore the TreeBuilder by looking it up.
        # it was a file-type object, we've read from it.
        # Keep track of the encoding of the original document,
        # Many of these are also reserved characters that cannot
        # name), we can handle it and put out a DeprecationWarning.
        # On top of that, we may be inside a tag that needs a special
        # operate on the bytestring.
        # over from initial parse. It might not be picklable and we
        # print("End tag: " + name)
        # print("Pop", tag.name)
        # print("Popping to %s" % name)
        # print("Push", tag.name)
        # print("Start tag %s: %s" % (name, attrs))
        # Prior to 4.13.0, the first argument to this method was a
        # reference to this object.
        # signature from its superclass implementation, Tag.decode.
        # since we won't be parsing it again.
        # specify a parser' warning.
        # Step 1: does it end with a common textual file extension?
        # Step 2: it _might_ be a file, but there are a few things
        # Step 3: If it survived all of those checks, it's similar
        # Store the contents as a Unicode string.
        # the same tests twice, convert Unicode to a bytestring and
        # The signatures of the two methods now match, but just in
        # the user brought type-unsafety upon themselves.
        # The user may want us to use some other class (hopefully a
        # This index is a tag, dig deeper for a "last descendant"
        # to the parent's next sibling (if found), else walk up the chain
        # Two consecutive forward slashes (as seen in a URL) or two
        # was specified well enough that we can omit the 'you need to
        # we can look for that aren't very common in filenames.
        # We have no sibling as we've been appended as the last.
        # We need this information to track whether or not the builder
        # We're only checking ASCII characters, so rather than write
        # Windows drive letter).
        # with the remaining **kwargs.
        )
        ) in self.builder.prepare_markup(
        ):
        **kwargs: Any,
        **kwattrs: _RawAttributeValue,
        :meta private:
        :param attrs: A dictionary of attribute values. Note that
        :param attrs: A dictionary of this Tag's attribute values; can
        :param builder: A TreeBuilder subclass to instantiate (or
        :param containerClass: The class to use when incorporating the
        :param element_classes: A dictionary mapping BeautifulSoup
        :param eventual_encoding: The encoding of the final document.
        :param exclude_encodings: A list of strings indicating
        :param features: Desirable features of the parser to be
        :param formatter: Either a `Formatter` object, or a string naming one of
        :param from_encoding: A string indicating the encoding of the
        :param inclusivePop: It this is false, pops the tag stack up
        :param indent_level: Each line of the rendering will be
        :param iterator: The iterator to use when navigating over the
        :param kwargs: For backwards compatibility purposes, the
        :param kwattrs: Keyword arguments for the new Tag's attribute values.
        :param markup: A string of markup.
        :param markup: A string or a file-like object representing
        :param name: Name of the tag.
        :param name: Pop up to the most recent tag with this name.
        :param name: The name of the new Tag.
        :param namespace: The URI of the new Tag's XML namespace, if any.
        :param namespaces: A dictionary of all namespace prefix mappings
        :param nsprefix: Namespace prefix for the tag.
        :param nsprefix: The namespace prefix that goes with `name`.
        :param parse_only: A SoupStrainer. Only parts of the document
        :param prefix: The prefix for the new Tag's XML namespace, if any.
        :param s: The string content of the `NavigableString`
        :param sourceline: The line number where this tag was
        :param sourceline: The line number where this tag was found in its
        :param sourcepos: The character position within ``sourceline`` where this
        :param sourcepos: The character position within `sourceline` where this
        :param string: String content for the new Tag, if any.
        :param subclass: The subclass of `NavigableString`, if any, to
        :return: Whether or not the markup resembled a filename
        :return: Whether or not the markup resembled a URL
        `ElementFilter`. You should proceed as if the tag had not occurred
        assert parent is not None
        attr_container = self.builder.attribute_dict_class(**kwattrs)
        attrs: _RawAttributeValues,
        attrs: Optional[_RawAttributeValues] = None,
        builder: Optional[Union[TreeBuilder, Type[TreeBuilder]]] = None,
        builder_class: Type[TreeBuilder]
        but not associated with any markup.
        child = el.contents[-1]
        child.next_sibling = None
        clone = type(self)("", None, self.builder)
        clone.original_encoding = self.original_encoding
        colon_i = markup_b.rfind(b":")
        container = base_class or NavigableString
        container = cast(
        container = self.string_container(subclass)
        d = dict(self.__dict__)
        d["contents"] = []
        d["markup"] = self.decode()
        data segment into the parse tree.
        def deprecated_argument(old_name: str, new_name: str) -> Optional[Any]:
        descendant.next_element = None
        descendant.next_sibling = None
        descendant: PageElement = child
        don't call handle_endtag.
        element_classes: Optional[Dict[Type[PageElement], Type[PageElement]]] = None,
        elif builder is None:
        elif indent_level is False or pretty_print is False:
        elif isinstance(markup, str):
        elif len(markup) <= 256 and (
        elif not isinstance(markup, (bytes, str)) and not hasattr(markup, "__len__"):
        elif not self.builder:
        else:
        encountered.
        eventual_encoding: _Encoding = DEFAULT_OUTPUT_ENCODING,
        exclude_encodings: Optional[_Encodings] = None,
        extensions = [b".html", b".htm", b".xml", b".xhtml", b".txt"]
        features: Optional[Union[str, Sequence[str]]] = None,
        filelike = False
        first = el.contents[0]
        fix = parent.next_element is not None
        for (
        for byte in markup_b:
        for i in range(stack_size - 1, 0, -1):
        formatter: Union[Formatter, str] = "minimal",
        from_encoding = from_encoding or deprecated_argument(
        from_encoding: Optional[_Encoding] = None,
        if "_most_recent_element" in d:
        if "builder" in d and d["builder"] is not None and not self.builder.picklable:
        if "convertEntities" in kwargs:
        if "isHTML" in kwargs:
        if "markupMassage" in kwargs:
        if "selfClosingTags" in kwargs:
        if "smartQuotesTo" in kwargs:
        if (
        if any(lower.endswith(ext) for ext in extensions):
        if attrs is not None:
        if b"  " in markup_b:
        if b"//" in markup_b:
        if builder is None:
        if child is first and el.parent is not None:
        if colon_i not in (-1, 1):
        if fix:
        if from_encoding and isinstance(markup, str):
        if hasattr(markup, "read"):  # It's a file-type object.
        if isinstance(builder, type):
        if isinstance(child, Tag) and child.contents:
        if isinstance(indent_level, bool):
        if isinstance(markup, bytes):
        if isinstance(markup, str):
        if isinstance(o, Tag):
        if isinstance(self.builder, type):
        if markup_b.startswith(b":"):
        if most_recent_element is not None:
        if name == self.ROOT_TAG_NAME:
        if not filelike:
        if not problem:
        if not self.tagStack:
        if not success:
        if parent is None:
        if parse_only is not None:
        if self._most_recent_element is not None:
        if self.current_data:
        if self.currentTag is not None:
        if self.is_xml:
        if self.markup is not None:
        if self.string_container_stack and container is NavigableString:
        if self.string_container_stack and tag == self.string_container_stack[-1]:
        if self.tagStack:
        if string is not None:
        if tag is None:
        if tag.name != self.ROOT_TAG_NAME:
        if tag.name in self.builder.preserve_whitespace_tags:
        if tag.name in self.builder.string_containers:
        if tag.name in self.open_tag_counter:
        If there are no open tags with the given name, nothing will be
        If this method returns None, the tag was rejected by an active
        if warning:
        in the document. For instance, if this was a self-closing tag,
        in to the BeautifulSoup constructor.
        indent_level: Optional[int] = None,
        instance of the given tag.
        it because there is nothing before or after it in the parse tree.
        iterator: Optional[Iterator[PageElement]] = None,
        kwargs["features"] = "xml"
        like a URL.
        lower = markup_b.lower()
        markup = cast(_RawMarkup, markup)
        markup.
        markup: _IncomingMarkup = "",
        markup_b: bytes
        most_recent_element: Optional[PageElement] = None,
        most_recently_popped = None
        name: str,
        namespace: Optional[str] = None,
        namespace: Optional[str],
        namespaces: Optional[Dict[str, str]] = None,
        next_element = previous_sibling = next_sibling = None
        not anymore. This has not been used for a long time; I just
        noticed that fact while working on 4.13.0.
        nsprefix: Optional[str] = None,
        nsprefix: Optional[str],
        number of Tag and NavigableString objects.
        o.setup(parent, previous_element, next_element, previous_sibling, next_sibling)
        o: PageElement,
        object.
        occurs.
        original_builder = builder
        original_features = features
        parent.contents.append(o)
        parent: Optional[Tag] = None,
        parse tree.
        parse_only = parse_only or deprecated_argument("parseOnlyThese", "parse_only")
        parse_only: Optional[SoupStrainer] = None,
        popped.
        previous_element: Optional[PageElement]
        problem: bool = False
        raise NotImplementedError(
        raise NotImplementedError("BeautifulSoup objects don't support insert_after().")
        rejections = []
        replaced_by="nothing (private method, will be removed)", version="4.13.0"
        resembles a filename.
        return clone
        return container
        return container(s)
        return d
        return decoded
        return most_recently_popped
        return prefix + super().decode(
        return self.currentTag
        return tag
        return True
        self,
        self, base_class: Optional[Type[NavigableString]] = None
        self, name: str, nsprefix: Optional[str] = None, inclusivePop: bool = True
        self, s: str, subclass: Optional[Type[NavigableString]] = None
        self.__dict__ = state
        self._feed()
        self._most_recent_element = None
        self._most_recent_element = o
        self._most_recent_element = tag
        self._namespaces = dict()
        self._popToTag(name, nsprefix)
        self.builder = builder
        self.builder.reset()
        self.builder.soup = None
        self.builder.soup = self
        self.current_data = []
        self.current_data.append(data)
        self.currentTag = None
        self.currentTag = self.tagStack[-1]
        self.element_classes = element_classes or dict()
        self.endData()
        self.hidden = True
        self.is_xml = builder.is_xml
        self.known_xml = self.is_xml
        self.markup = None
        self.open_tag_counter = Counter()
        self.parse_only = parse_only
        self.preserve_whitespace_tag_stack = []
        self.pushTag(self)
        self.pushTag(tag)
        self.reset()
        self.string_container_stack = []
        self.tagStack = []
        self.tagStack.append(tag)
        sourceline: Optional[int] = None,
        sourcepos: Optional[int] = None,
        stack_size = len(self.tagStack)
        string.
        string: Optional[str] = None,
        success = False
        super().__init__(*args, **kwargs)
        tag = self.tagStack.pop()
        tag = tag_class(
        Tag.__init__(self, self, self.builder, self.ROOT_TAG_NAME)
        tag_class = cast(Type[Tag], tag_class)
        tag_class = self.element_classes.get(Tag, Tag)
        target: Optional[Tag] = el
        This is the first step of the deepcopy process.
        This may be a built-in Beautiful Soup class or a custom class passed
        warning: Optional[str] = None
        warnings.warn had this problem back in 2010 but fortunately
        warnings.warn(
        while (
        while True:
      * endData(containerClass) # Ends the current data node
      * feed(markup)
      * handle_data(data) # Appends to the current data node
      * handle_endtag(name)
      * handle_starttag(name, attrs) # See note about return value
      * reset()
    """
    """A data structure representing a parsed HTML or XML document.
    """Deprecated interface to an XML parser."""
    "AttributeResemblesVariableWarning",
    "BeautifulSoup",
    "CData",
    "Comment",
    "CSS",
    "Declaration",
    "Doctype",
    "ElementFilter",
    "FeatureNotFound",
    "GuessedAtParserWarning",
    "MarkupResemblesLocatorWarning",
    "ParserRejectedMarkup",
    "ProcessingInstruction",
    "ResultSet",
    "Script",
    "StopParsing",
    "Stylesheet",
    "Tag",
    "TemplateString",
    "UnicodeDammit",
    "UnusualUsageWarning",
    "XMLParsedAsHTMLWarning",
    # Exceptions
    # FUTURE PYTHON:
    # These members are only used while parsing markup.
    # Warnings
    #: `BeautifulSoup.original_encoding`.
    #: `BeautifulSoup` object isn't a real markup tag.
    #: a `Tag` with a `Tag.name`. Hoever, this name makes it clear the
    #: A string containing all ASCII whitespace characters, used in
    #: Beautiful Soup's best guess as to the character encoding of the
    #: could not be represented in Unicode.
    #: during parsing to detect data chunks that seem 'empty'.
    #: If the end-user gives no indication which tree builder they
    #: in the original document. This may or may not match
    #: in the original markup. These mark character sequences that
    #: original document.
    #: Since `BeautifulSoup` subclasses `Tag`, it's possible to treat it as
    #: The character encoding, if any, that was explicitly defined
    #: This is True if the markup that was parsed contains
    #: U+FFFD REPLACEMENT_CHARACTER characters which were not present
    #: want, look for one with these features.
    )
    ) -> NavigableString:
    ) -> None:
    ) -> Optional[Tag]:
    ) -> str:
    ) -> Tag:
    ) -> Type[NavigableString]:
    ):
    @_deprecated(
    @classmethod
    _deprecated,
    _Encoding,
    _Encodings,
    _IncomingMarkup,
    _InsertableElement,
    _most_recent_element: Optional[PageElement]  #: :meta private:
    _RawAttributeValue,
    _RawAttributeValues,
    _RawMarkup,
    able to build a tree using 'start tag' events, 'end tag' events,
    Any,
    ASCII_SPACES: str = "\x20\x0a\x09\x0c\x0d"
    AttributeResemblesVariableWarning,
    builder: TreeBuilder  #: :meta private:
    builder_registry,
    cast,
    CData,
    Comment,
    contains_replacement_characters: bool
    Counter as CounterType,
    current_data: List[str]  #: :meta private:
    currentTag: Optional[Tag]  #: :meta private:
    'data' events, and "done with data" events.
    Declaration,
    declared_html_encoding: Optional[_Encoding]
    def __getstate__(self) -> Dict[str, Any]:
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, *args: Any, **kwargs: Any):
    def __setstate__(self, state: Dict[str, Any]) -> None:
    def _decode_markup(cls, markup: _RawMarkup) -> str:
    def _feed(self) -> None:
    def _linkage_fixer(self, el: Tag) -> None:
    def _markup_is_url(cls, markup: _RawMarkup) -> bool:
    def _markup_resembles_filename(cls, markup: _RawMarkup) -> bool:
    def _popToTag(
    def copy_self(self) -> "BeautifulSoup":
    def decode(
    def endData(self, containerClass: Optional[Type[NavigableString]] = None) -> None:
    def handle_data(self, data: str) -> None:
    def handle_endtag(self, name: str, nsprefix: Optional[str] = None) -> None:
    def handle_starttag(
    def insert_after(self, *args: _InsertableElement) -> List[PageElement]:
    def insert_before(self, *args: _InsertableElement) -> List[PageElement]:
    def new_string(
    def new_tag(
    def object_was_parsed(
    def popTag(self) -> Optional[Tag]:
    def pushTag(self, tag: Tag) -> None:
    def reset(self) -> None:
    def string_container(
    DEFAULT_BUILDER_FEATURES: Sequence[str] = ["html", "fast"]
    DEFAULT_OUTPUT_ENCODING,
    Dict,
    Doctype,
    element_classes: Dict[Type[PageElement], Type[PageElement]]  #: :meta private:
    ElementFilter,
    FeatureNotFound,
    GuessedAtParserWarning,
    handle_endtag.
    If you encounter an empty-element tag (aka a self-closing tag,
    import sys
    Internally, this class defines the basic interface called by the
    is_xml: bool
    Iterator,
    known_xml: Optional[bool]
    like HTML's <br> tag), call handle_starttag and then
    List,
    markup: Optional[_RawMarkup]  #: :meta private:
    MarkupResemblesLocatorWarning,
    Most of the methods you'll call on a BeautifulSoup object are inherited from
    NavigableString,
    No matter how complicated the underlying parser is, you should be
    open_tag_counter: CounterType[str]  #: :meta private:
    Optional,
    original_encoding: Optional[_Encoding]
    PageElement or Tag.
    PageElement,
    parse_only: Optional[SoupStrainer]  #: :meta private:
    ParserRejectedMarkup,
    parsers. To write a new tree builder, you'll need to understand
    preserve_whitespace_tag_stack: List[Tag]  #: :meta private:
    print(soup.prettify())
    ProcessingInstruction,
    PYTHON_SPECIFIC_ENCODINGS,
    raise ImportError(
    ResultSet,
    ROOT_TAG_NAME: str = "[document]"
    Script,
    Sequence,
    soup = BeautifulSoup(sys.stdin)
    SoupStrainer,
    StopParsing,
    string_container_stack: List[Tag]  #: :meta private:
    structure. The interface abstracts away the differences between
    Stylesheet,
    Tag,
    tagStack: List[Tag]  #: :meta private:
    TemplateString,
    The tree builder may call these methods from its feed() implementation:
    these methods as a whole.
    These methods will be called by the BeautifulSoup constructor:
    tree builders when converting an HTML/XML document into a data
    TreeBuilder,
    Type,
    Union,
    UnusualUsageWarning,
    XMLParsedAsHTMLWarning,
"""
"""Beautiful Soup Elixir and Tonic - "The Screen-Scraper's Friend".
# Aliases to make it easier to get started quickly, e.g. 'from bs4 import _soup'
# If this file is run as a script, act as an HTML pretty-printer.
# Import all warnings and exceptions into the main package.
# running this code under Python 2.
# The very first thing we do is give a useful error if someone is
# Use of this source code is governed by the MIT license.
(possibly invalid) document into a tree representation. Beautiful Soup
)
]
__all__ = [
__author__ = "Leonard Richardson (leonardr@segfault.org)"
__copyright__ = "Copyright (c) 2004-2025 Leonard Richardson"
__license__ = "MIT"
__version__ = "4.13.4"
_s = BeautifulSoup
_soup = BeautifulSoup
and/or html5lib is installed, but they are not required.
Beautiful Soup uses a pluggable XML or HTML parser to parse a
Beautiful Soup works with Python 3.7 and up. It works better if lxml
class BeautifulSoup:
class BeautifulStoneSoup:
documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
For more than you ever wanted to know about Beautiful Soup, see the
from ._deprecation import (
from .builder import (
from .builder._htmlparser import HTMLParserTreeBuilder
from .css import CSS
from .dammit import UnicodeDammit
from .element import (
from .filter import (
from .formatter import Formatter
from bs4._typing import (
from bs4._warnings import (
from bs4.exceptions import (
from collections import Counter
from typing import (
http://www.crummy.com/software/BeautifulSoup/
if __name__ == "__main__":
if sys.version_info.major < 3:
import sys
import warnings
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.
