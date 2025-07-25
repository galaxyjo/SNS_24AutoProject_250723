
                [CSSAnimationStyle.from_json(i) for i in json["animationStyles"]]
                [CSSContainerQuery.from_json(i) for i in json["containerQueries"]]
                [CSSLayer.from_json(i) for i in json["layers"]]
                [CSSLayerData.from_json(i) for i in json["subLayers"]]
                [CSSMedia.from_json(i) for i in json["media"]]
                [CSSProperty.from_json(i) for i in json["longhandProperties"]]
                [CSSRuleType.from_json(i) for i in json["ruleTypes"]]
                [CSSScope.from_json(i) for i in json["scopes"]]
                [CSSStartingStyle.from_json(i) for i in json["startingStyles"]]
                [CSSSupports.from_json(i) for i in json["supports"]]
                [FontVariationAxis.from_json(i) for i in json["fontVariationAxes"]]
                [MediaQuery.from_json(i) for i in json["mediaList"]]
                [str(i) for i in json["nestingSelectors"]]
                bool(json["hasSourceURL"]) if "hasSourceURL" in json else None
                bool(json["loadingFailed"]) if "loadingFailed" in json else None
                bool(json["queriesScrollState"])
                CSSPropertyRegistration.from_json(i)
                CSSStyle.from_json(json["inlineStyle"])
                CSSStyle.from_json(json["transitionsStyle"])
                dom.BackendNodeId.from_json(json["ownerNode"])
                dom.LogicalAxes.from_json(json["logicalAxes"])
                dom.PhysicalAxes.from_json(json["physicalAxes"])
                else None
                float(json["computedLength"]) if "computedLength" in json else None
                for i in json["cssPropertyRegistrations"]
                for i in json["inheritedPseudoElements"]
                if "animationStyles" in json
                if "containerQueries" in json
                if "fontVariationAxes" in json
                if "initialValue" in json
                if "inlineStyle" in json
                if "layers" in json
                if "logicalAxes" in json
                if "longhandProperties" in json
                if "media" in json
                if "mediaList" in json
                if "nestingSelectors" in json
                if "ownerNode" in json
                if "physicalAxes" in json
                if "queriesScrollState" in json
                if "ruleTypes" in json
                if "scopes" in json
                if "specificity" in json
                if "startingStyles" in json
                if "styleSheetId" in json
                if "subLayers" in json
                if "supports" in json
                if "transitionsStyle" in json
                if "valueRange" in json
                InheritedPseudoElementMatches.from_json(i)
                MediaQueryExpression.from_json(i) for i in json["expressions"]
                PseudoElementMatches.from_json(i) for i in json["pseudoElements"]
                ShorthandEntry.from_json(i) for i in json["shorthandEntries"]
                SourceRange.from_json(json["valueRange"])
                Specificity.from_json(json["specificity"])
                str(json["pseudoIdentifier"]) if "pseudoIdentifier" in json else None
                str(json["sourceMapURL"]) if "sourceMapURL" in json else None
                StyleSheetId.from_json(json["styleSheetId"])
                Value.from_json(json["initialValue"])
            ),
            [
            [CSSAnimationStyle.from_json(i) for i in json["animationStyles"]]
            [CSSKeyframesRule.from_json(i) for i in json["cssKeyframesRules"]]
            [CSSPositionTryRule.from_json(i) for i in json["cssPositionTryRules"]]
            [CSSPropertyRule.from_json(i) for i in json["cssPropertyRules"]]
            [InheritedAnimatedStyleEntry.from_json(i) for i in json["inherited"]]
            [InheritedStyleEntry.from_json(i) for i in json["inherited"]]
            [PseudoElementMatches.from_json(i) for i in json["pseudoElements"]]
            [RuleMatch.from_json(i) for i in json["matchedCSSRules"]]
            [str(i) for i in json["backgroundColors"]]
            ]
            ],
            a=int(json["a"]),
            active=bool(json["active"]),
            animation_name=Value.from_json(json["animationName"]),
            animation_styles=(
            b=int(json["b"]),
            c=int(json["c"]),
            computed_length=(
            container_queries=(
            css_properties=[CSSProperty.from_json(i) for i in json["cssProperties"]],
            css_text=str(json["cssText"]) if "cssText" in json else None,
            CSSFontPaletteValuesRule.from_json(json["cssFontPaletteValuesRule"])
            CSSStyle.from_json(json["attributesStyle"])
            CSSStyle.from_json(json["transitionsStyle"])
            default_value=float(json["defaultValue"]),
            disabled=bool(json["disabled"]) if "disabled" in json else None,
            disabled=bool(json["disabled"]),
            dom.NodeId.from_json(json["parentLayoutNodeId"])
            else None
            end_column=float(json["endColumn"]),
            end_column=int(json["endColumn"]),
            end_line=float(json["endLine"]),
            end_line=int(json["endLine"]),
            end_offset=float(json["endOffset"]),
            expressions=[
            family_name=str(json["familyName"]),
            feature=str(json["feature"]),
            font_display=str(json["fontDisplay"]),
            font_family=str(json["fontFamily"]),
            font_palette_name=Value.from_json(json["fontPaletteName"]),
            font_stretch=str(json["fontStretch"]),
            font_style=str(json["fontStyle"]),
            font_variant=str(json["fontVariant"]),
            font_variation_axes=(
            font_weight=str(json["fontWeight"]),
            frame_id=page.FrameId.from_json(json["frameId"]),
            glyph_count=float(json["glyphCount"]),
            has_source_url=(
            if "activePositionFallbackIndex" in json
            if "animationStyles" in json
            if "attributesStyle" in json
            if "backgroundColors" in json
            if "cssFontPaletteValuesRule" in json
            if "cssKeyframesRules" in json
            if "cssPositionTryRules" in json
            if "cssPropertyRegistrations" in json
            if "cssPropertyRules" in json
            if "inherited" in json
            if "inheritedPseudoElements" in json
            if "matchedCSSRules" in json
            if "parentLayoutNodeId" in json
            if "pseudoElements" in json
            if "transitionsStyle" in json
            implicit=bool(json["implicit"]) if "implicit" in json else None,
            important=bool(json["important"]) if "important" in json else None,
            inherits=bool(json["inherits"]),
            initial_value=(
            inline_style=(
            int(json["activePositionFallbackIndex"])
            is_constructed=bool(json["isConstructed"]),
            is_custom_font=bool(json["isCustomFont"]),
            is_inline=bool(json["isInline"]),
            is_mutable=bool(json["isMutable"]),
            json["animationStyles"] = [i.to_json() for i in self.animation_styles]
            json["computedLength"] = self.computed_length
            json["containerQueries"] = [i.to_json() for i in self.container_queries]
            json["cssText"] = self.css_text
            json["disabled"] = self.disabled
            json["fontVariationAxes"] = [i.to_json() for i in self.font_variation_axes]
            json["hasSourceURL"] = self.has_source_url
            json["implicit"] = self.implicit
            json["important"] = self.important
            json["initialValue"] = self.initial_value.to_json()
            json["inlineStyle"] = self.inline_style.to_json()
            json["layers"] = [i.to_json() for i in self.layers]
            json["loadingFailed"] = self.loading_failed
            json["logicalAxes"] = self.logical_axes.to_json()
            json["longhandProperties"] = [i.to_json() for i in self.longhand_properties]
            json["media"] = [i.to_json() for i in self.media]
            json["mediaList"] = [i.to_json() for i in self.media_list]
            json["name"] = self.name
            json["nestingSelectors"] = [i for i in self.nesting_selectors]
            json["ownerNode"] = self.owner_node.to_json()
            json["parsedOk"] = self.parsed_ok
            json["physicalAxes"] = self.physical_axes.to_json()
            json["pseudoIdentifier"] = self.pseudo_identifier
            json["queriesScrollState"] = self.queries_scroll_state
            json["range"] = self.range_.to_json()
            json["ruleTypes"] = [i.to_json() for i in self.rule_types]
            json["scopes"] = [i.to_json() for i in self.scopes]
            json["sourceMapURL"] = self.source_map_url
            json["sourceURL"] = self.source_url
            json["specificity"] = self.specificity.to_json()
            json["startingStyles"] = [i.to_json() for i in self.starting_styles]
            json["styleSheetId"] = self.style_sheet_id.to_json()
            json["subLayers"] = [i.to_json() for i in self.sub_layers]
            json["supports"] = [i.to_json() for i in self.supports]
            json["text"] = self.text
            json["transitionsStyle"] = self.transitions_style.to_json()
            json["valueRange"] = self.value_range.to_json()
            key_text=Value.from_json(json["keyText"]),
            keyframes=[CSSKeyframeRule.from_json(i) for i in json["keyframes"]],
            layers=(
            length=float(json["length"]),
            loading_failed=(
            logical_axes=(
            longhand_properties=(
            matched_css_rules=[RuleMatch.from_json(i) for i in json["matchedCSSRules"]],
            matches=[RuleMatch.from_json(i) for i in json["matches"]],
            matching_selectors=[int(i) for i in json["matchingSelectors"]],
            max_value=float(json["maxValue"]),
            media_list=(
            media=(
            min_value=float(json["minValue"]),
            name=str(json["name"]) if "name" in json else None,
            name=str(json["name"]),
            name=Value.from_json(json["name"]),
            nesting_selectors=(
            node_for_property_syntax_validation.to_json()
            order=float(json["order"]),
            origin=StyleSheetOrigin.from_json(json["origin"]),
            owner_node=(
            parsed_ok=bool(json["parsedOk"]) if "parsedOk" in json else None,
            physical_axes=(
            platform_font_family=str(json["platformFontFamily"]),
            post_script_name=str(json["postScriptName"]),
            property_name=str(json["propertyName"]),
            property_name=Value.from_json(json["propertyName"]),
            pseudo_elements=[
            pseudo_identifier=(
            pseudo_type=dom.PseudoType.from_json(json["pseudoType"]),
            queries_scroll_state=(
            range_=SourceRange.from_json(json["range"]) if "range" in json else None,
            range_=SourceRange.from_json(json["range"]),
            rule_types=(
            rule=CSSRule.from_json(json["rule"]),
            scopes=(
            selector_list=SelectorList.from_json(json["selectorList"]),
            selectors=[Value.from_json(i) for i in json["selectors"]],
            shorthand_entries=[
            source_map_url=(
            source_url=str(json["sourceURL"]) if "sourceURL" in json else None,
            source_url=str(json["sourceURL"]),
            source=str(json["source"]),
            specificity=(
            src=str(json["src"]),
            start_column=float(json["startColumn"]),
            start_column=int(json["startColumn"]),
            start_line=float(json["startLine"]),
            start_line=int(json["startLine"]),
            start_offset=float(json["startOffset"]),
            starting_styles=(
            style_sheet_id=(
            style_sheet_id=StyleSheetId.from_json(json["styleSheetId"]),
            style=CSSStyle.from_json(json["style"]),
            sub_layers=(
            supports=(
            syntax=str(json["syntax"]),
            tag=str(json["tag"]),
            text=str(json["text"]) if "text" in json else None,
            text=str(json["text"]),
            title=str(json["title"]),
            transitions_style=(
            unicode_range=str(json["unicodeRange"]),
            unit=str(json["unit"]),
            used=bool(json["used"]),
            value_range=(
            value=float(json["value"]),
            value=str(json["value"]),
        "method": "CSS.addRule",
        "method": "CSS.collectClassNames",
        "method": "CSS.createStyleSheet",
        "method": "CSS.disable",
        "method": "CSS.enable",
        "method": "CSS.forcePseudoState",
        "method": "CSS.forceStartingStyle",
        "method": "CSS.getAnimatedStylesForNode",
        "method": "CSS.getBackgroundColors",
        "method": "CSS.getComputedStyleForNode",
        "method": "CSS.getInlineStylesForNode",
        "method": "CSS.getLayersForNode",
        "method": "CSS.getLocationForSelector",
        "method": "CSS.getLonghandProperties",
        "method": "CSS.getMatchedStylesForNode",
        "method": "CSS.getMediaQueries",
        "method": "CSS.getPlatformFontsForNode",
        "method": "CSS.getStyleSheetText",
        "method": "CSS.resolveValues",
        "method": "CSS.setContainerQueryText",
        "method": "CSS.setEffectivePropertyValueForNode",
        "method": "CSS.setKeyframeKey",
        "method": "CSS.setLocalFontsEnabled",
        "method": "CSS.setMediaText",
        "method": "CSS.setPropertyRulePropertyName",
        "method": "CSS.setRuleSelector",
        "method": "CSS.setScopeText",
        "method": "CSS.setStyleSheetText",
        "method": "CSS.setStyleTexts",
        "method": "CSS.setSupportsText",
        "method": "CSS.startRuleUsageTracking",
        "method": "CSS.stopRuleUsageTracking",
        "method": "CSS.takeComputedStyleUpdates",
        "method": "CSS.takeCoverageDelta",
        "method": "CSS.trackComputedStyleUpdates",
        "method": "CSS.trackComputedStyleUpdatesForNode",
        "params": params,
        (
        )
        ),
        [RuleUsage.from_json(i) for i in json["coverage"]],
        0. **animationStyles** - *(Optional)* Styles coming from animations.
        0. **backgroundColors** - *(Optional)* The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load).
        0. **coverage** -
        0. **inlineStyle** - *(Optional)* Inline style for the specified DOM node.
        1. **attributesStyle** - *(Optional)* Attribute-defined element style (e.g. resulting from "width=20 height=100%").
        1. **computedFontSize** - *(Optional)* The computed font size for this node, as a CSS computed value string (e.g. '12px').
        1. **timestamp** - Monotonically increasing time, in seconds.
        1. **transitionsStyle** - *(Optional)* Style coming from transitions.
        10. **cssPropertyRegistrations** - *(Optional)* A list of CSS property registrations matching this node.
        11. **cssFontPaletteValuesRule** - *(Optional)* A font-palette-values rule matching this node.
        12. **parentLayoutNodeId** - *(Optional)* Id of the first parent element that does not have display: contents.
        2. **computedFontWeight** - *(Optional)* The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or '100').
        2. **inherited** - *(Optional)* Inherited style entries for animationsStyle and transitionsStyle from the inheritance chain of the element.
        2. **matchedCSSRules** - *(Optional)* CSS rules matching this node, from all applicable stylesheets.
        3. **pseudoElements** - *(Optional)* Pseudo style matches for this node.
        4. **inherited** - *(Optional)* A chain of inherited styles (from the immediate node parent up to the DOM tree root).
        5. **inheritedPseudoElements** - *(Optional)* A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root).
        6. **cssKeyframesRules** - *(Optional)* A list of CSS keyframed animations matching this node.
        7. **cssPositionTryRules** - *(Optional)* A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property.
        8. **activePositionFallbackIndex** - *(Optional)* Index of the active fallback in the applied position-try-fallback property, will not be set if there is no active position-try fallback.
        9. **cssPropertyRules** - *(Optional)* A list of CSS at-property rules matching this node.
        CSSFontPaletteValuesRule | None,
        CSSStyle | None,
        CSSStyle.from_json(json["inlineStyle"]) if "inlineStyle" in json else None,
        dom.NodeId | None,
        float(json["timestamp"]),
        if self.animation_styles is not None:
        if self.computed_length is not None:
        if self.container_queries is not None:
        if self.css_text is not None:
        if self.disabled is not None:
        if self.font_variation_axes is not None:
        if self.has_source_url is not None:
        if self.implicit is not None:
        if self.important is not None:
        if self.initial_value is not None:
        if self.inline_style is not None:
        if self.layers is not None:
        if self.loading_failed is not None:
        if self.logical_axes is not None:
        if self.longhand_properties is not None:
        if self.media is not None:
        if self.media_list is not None:
        if self.name is not None:
        if self.nesting_selectors is not None:
        if self.owner_node is not None:
        if self.parsed_ok is not None:
        if self.physical_axes is not None:
        if self.pseudo_identifier is not None:
        if self.queries_scroll_state is not None:
        if self.range_ is not None:
        if self.rule_types is not None:
        if self.scopes is not None:
        if self.source_map_url is not None:
        if self.source_url is not None:
        if self.specificity is not None:
        if self.starting_styles is not None:
        if self.style_sheet_id is not None:
        if self.sub_layers is not None:
        if self.supports is not None:
        if self.text is not None:
        if self.transitions_style is not None:
        if self.value_range is not None:
        int | None,
        json = dict()
        json["a"] = self.a
        json["active"] = self.active
        json["animationName"] = self.animation_name.to_json()
        json["b"] = self.b
        json["c"] = self.c
        json["cssProperties"] = [i.to_json() for i in self.css_properties]
        json["defaultValue"] = self.default_value
        json["disabled"] = self.disabled
        json["endColumn"] = self.end_column
        json["endLine"] = self.end_line
        json["endOffset"] = self.end_offset
        json["expressions"] = [i.to_json() for i in self.expressions]
        json["familyName"] = self.family_name
        json["feature"] = self.feature
        json["fontDisplay"] = self.font_display
        json["fontFamily"] = self.font_family
        json["fontPaletteName"] = self.font_palette_name.to_json()
        json["fontStretch"] = self.font_stretch
        json["fontStyle"] = self.font_style
        json["fontVariant"] = self.font_variant
        json["fontWeight"] = self.font_weight
        json["frameId"] = self.frame_id.to_json()
        json["glyphCount"] = self.glyph_count
        json["inherits"] = self.inherits
        json["isConstructed"] = self.is_constructed
        json["isCustomFont"] = self.is_custom_font
        json["isInline"] = self.is_inline
        json["isMutable"] = self.is_mutable
        json["keyframes"] = [i.to_json() for i in self.keyframes]
        json["keyText"] = self.key_text.to_json()
        json["length"] = self.length
        json["matchedCSSRules"] = [i.to_json() for i in self.matched_css_rules]
        json["matches"] = [i.to_json() for i in self.matches]
        json["matchingSelectors"] = [i for i in self.matching_selectors]
        json["maxValue"] = self.max_value
        json["minValue"] = self.min_value
        json["name"] = self.name
        json["name"] = self.name.to_json()
        json["order"] = self.order
        json["origin"] = self.origin.to_json()
        json["platformFontFamily"] = self.platform_font_family
        json["postScriptName"] = self.post_script_name
        json["propertyName"] = self.property_name
        json["propertyName"] = self.property_name.to_json()
        json["pseudoElements"] = [i.to_json() for i in self.pseudo_elements]
        json["pseudoType"] = self.pseudo_type.to_json()
        json["range"] = self.range_.to_json()
        json["rule"] = self.rule.to_json()
        json["selectorList"] = self.selector_list.to_json()
        json["selectors"] = [i.to_json() for i in self.selectors]
        json["shorthandEntries"] = [i.to_json() for i in self.shorthand_entries]
        json["source"] = self.source
        json["sourceURL"] = self.source_url
        json["src"] = self.src
        json["startColumn"] = self.start_column
        json["startLine"] = self.start_line
        json["startOffset"] = self.start_offset
        json["style"] = self.style.to_json()
        json["styleSheetId"] = self.style_sheet_id.to_json()
        json["syntax"] = self.syntax
        json["tag"] = self.tag
        json["text"] = self.text
        json["title"] = self.title
        json["unicodeRange"] = self.unicode_range
        json["unit"] = self.unit
        json["used"] = self.used
        json["value"] = self.value
        list[CSSAnimationStyle] | None,
        list[CSSKeyframesRule] | None,
        list[CSSPositionTryRule] | None,
        list[CSSPropertyRegistration] | None,
        list[CSSPropertyRule] | None,
        list[InheritedAnimatedStyleEntry] | None,
        list[InheritedPseudoElementMatches] | None,
        list[InheritedStyleEntry] | None,
        list[PseudoElementMatches] | None,
        list[RuleMatch] | None,
        params["nodeForPropertySyntaxValidation"] = (
        params["nodeId"] = node_id.to_json()
        params["propertyName"] = property_name
        params["pseudoIdentifier"] = pseudo_identifier
        params["pseudoType"] = pseudo_type.to_json()
        return "StyleSheetId({})".format(super().__repr__())
        return cls(
        return cls()
        return cls(font=FontFace.from_json(json["font"]) if "font" in json else None)
        return cls(header=CSSStyleSheetHeader.from_json(json["header"]))
        return cls(json)
        return cls(node_id=dom.NodeId.from_json(json["nodeId"]))
        return cls(style_sheet_id=StyleSheetId.from_json(json["styleSheetId"]))
        return json
        return self
        return self.value
        str(json["computedFontSize"]) if "computedFontSize" in json else None,
        str(json["computedFontWeight"]) if "computedFontWeight" in json else None,
    """
    #: @scope CSS at-rule array.
    #: @starting-style CSS at-rule array.
    #: @supports CSS at-rule array.
    #: ``<link>`` element's stylesheets become mutable only if DevTools modifies them.
    #: A higher number has higher priority in the cascade order.
    #: Added stylesheet metainfo.
    #: after they have been modified via CSSOM API.
    #: Amount of glyphs that were rendered with this font.
    #: Animation name.
    #: Array of media queries.
    #: Array of media query expressions.
    #: Array of selectors from ancestor style rules, sorted by distance from the current rule.
    #: as a CSS module script).
    #: Associated font palette name.
    #: Associated key text.
    #: Associated property name.
    #: Associated style declaration.
    #: Available variation settings (a.k.a. "axes").
    #: available).
    #: Cascade layer array. Contains the layer hierarchy that this rule belongs to starting
    #: Column offset of the end of the stylesheet within the resource (zero based).
    #: Column offset of the stylesheet within the resource (zero based).
    #: Computed length of media query expression (if applicable).
    #: Computed style property name.
    #: Computed style property value.
    #: Computed values for all shorthands found in the style.
    #: Constructed stylesheets (new CSSStyleSheet()) are mutable immediately after creation.
    #: Container query list array (for rules involving container queries).
    #: Container query text.
    #: CSS module script.
    #: CSS properties in the style.
    #: CSS rule in the match.
    #: Denotes whether the stylesheet is disabled.
    #: Direct sub-layers
    #: document.written STYLE tags.
    #: End column of range (exclusive).
    #: End line of range
    #: Font's family name reported by platform.
    #: Font's PostScript name reported by platform.
    #: Human-readable variation name in the default language (normally, "en").
    #: Identifier of the removed stylesheet.
    #: Identifier of the stylesheet containing this object (if exists).
    #: If the style sheet was loaded from a network resource, this indicates when the resource failed to load
    #: Indicates if the font was downloaded or resolved locally.
    #: Indicates whether the rule was actually used by some element in the page.
    #: Layer name.
    #: Layer order. The order determines the order of the layer in the cascade order.
    #: Line offset of the end of the stylesheet within the resource (zero based).
    #: Line offset of the stylesheet within the resource (zero based).
    #: List of keyframes.
    #: Matches of CSS rules applicable to the pseudo style.
    #: Matches of CSS rules matching the ancestor node in the style inheritance chain.
    #: Matches of pseudo styles from the pseudos of an ancestor node.
    #: Matching selector indices in the rule's selectorList selectors (0-based).
    #: Media list array (for rules involving media queries). The array enumerates media queries
    #: Media query expression feature.
    #: Media query expression units.
    #: Media query expression value.
    #: Media query text.
    #: new CSSStyleSheet() (but non-empty if this is a constructed stylesheet imported
    #: New style text.
    #: Offset of the end of the rule body from the beginning of the stylesheet.
    #: Offset of the start of the rule (including selector) from the beginning of the stylesheet.
    #: Optional logical axes queried for the container.
    #: Optional name for the container.
    #: Optional physical axes queried for the container.
    #: Owner frame identifier.
    #: Parent stylesheet's origin.
    #: Parsed longhand components of this property if it is a shorthand.
    #: Pseudo element custom ident.
    #: Pseudo element type.
    #: pseudo-classes.
    #: Rule selector data.
    #: Rule selector text.
    #: Scope rule text.
    #: Selectors in the list.
    #: Shorthand name.
    #: Shorthand value.
    #: Size of the content (in characters).
    #: Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if
    #: Specificity of the selector.
    #: specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked
    #: Start column of range (inclusive).
    #: Start line of range.
    #: starting with the innermost one, going outwards.
    #: Style declaration range in the enclosing stylesheet (if available).
    #: Style declaration text (if available).
    #: Styles coming from the animations of the ancestor, if any, in the style inheritance chain.
    #: Stylesheet origin.
    #: Stylesheet resource URL. Empty if this is a constructed stylesheet created using
    #: stylesheet rules) this rule came from.
    #: Stylesheet title.
    #: stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline
    #: stylesheet's STYLE tag.
    #: Supports rule text.
    #: The a component, which represents the number of ID selectors.
    #: The ancestor node's inline style, if any, in the style inheritance chain.
    #: The array enumerates @scope at-rules starting with the innermost one, going outwards.
    #: The array enumerates @starting-style at-rules starting with the innermost one, going outwards.
    #: The array enumerates @supports at-rules starting with the innermost one, going outwards.
    #: The array enumerates container queries starting with the innermost one, going outwards.
    #: The array keeps the types of ancestor CSSRules from the innermost going outwards.
    #: The associated range of the value text in the enclosing stylesheet (if available).
    #: The associated rule (@media or @import) header range in the enclosing stylesheet (if
    #: The associated rule header range in the enclosing stylesheet (if
    #: The b component, which represents the number of class selectors, attributes selectors, and
    #: The backend id for the owner node of the stylesheet.
    #: The c component, which represents the number of type selectors and pseudo-elements.
    #: The css style sheet identifier (absent for user agent stylesheet and user-specified
    #: The css style sheet identifier.
    #: The default value.
    #: The entire property range in the enclosing style declaration (if available).
    #: The font-display.
    #: The font-family.
    #: The font-stretch.
    #: The font-style.
    #: The font-variant.
    #: The font-variation-setting tag (a.k.a. "axis tag").
    #: The font-weight.
    #: The full property text as specified in the style.
    #: The maximum value (inclusive) the font supports for this tag.
    #: The minimum value (inclusive) the font supports for this tag.
    #: The name of the animation.
    #: The node id that has updated computed styles.
    #: The prelude dashed-ident name
    #: The property name.
    #: The property value.
    #: The range of the style text in the enclosing stylesheet.
    #: The resolved platform font family
    #: The src.
    #: The style coming from the animation.
    #: The style coming from the transitions of the ancestor, if any, in the style inheritance chain.
    #: The stylesheet identifier.
    #: The unicode-range.
    #: The web font that has loaded.
    #: This field will be empty if the given property is not a shorthand.
    #: true if the query contains scroll-state() queries.
    #: True if this stylesheet is created through new CSSStyleSheet() or imported as a
    #: URL of source map associated with the stylesheet (if any).
    #: URL of the document containing the media query description.
    #: Value range in the underlying resource (if available).
    #: Value text.
    #: Whether the media query condition is satisfied.
    #: Whether the property has "!important" annotation (implies ``false`` if absent).
    #: Whether the property is disabled by the user (present for source-based properties only).
    #: Whether the property is implicit (implies ``false`` if absent).
    #: Whether the property is understood by the browser (implies ``true`` if absent).
    #: Whether the sourceURL field value comes from the sourceURL comment.
    #: Whether the supports condition is satisfied.
    #: Whether this stylesheet is created for STYLE tag by parser. This flag is not set for
    #: Whether this stylesheet is mutable. Inline stylesheets become mutable
    #: with the innermost layer and going outwards.
    )
    **EXPERIMENTAL**
    :param edits:
    :param enabled: Whether rendering of local fonts is enabled.
    :param forced: Boolean indicating if this is on or off.
    :param forced_pseudo_classes: Element pseudo classes to force when computing the element's style.
    :param frame_id: Identifier of the frame where "via-inspector" stylesheet should be created.
    :param key_text:
    :param location: Text position of a new rule in the target style sheet.
    :param node_for_property_syntax_validation: **(EXPERIMENTAL)** *(Optional)* NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example.
    :param node_id:
    :param node_id: *(Optional)*
    :param node_id: Id of the node in whose context the expression is evaluated
    :param node_id: Id of the node to get background colors for.
    :param node_id: The element id for which to force the pseudo state.
    :param node_id: The element id for which to force the starting-style state.
    :param node_id: The element id for which to set property.
    :param properties_to_track:
    :param property_name:
    :param property_name: *(Optional)* Only longhands and custom property names are accepted.
    :param pseudo_identifier: **(EXPERIMENTAL)** *(Optional)* Pseudo element custom ident.
    :param pseudo_type: **(EXPERIMENTAL)** *(Optional)* Pseudo element type, only works for pseudo elements that generate elements in the tree, such as ::before and ::after.
    :param range_:
    :param rule_text: The text of a new rule.
    :param selector:
    :param selector_text:
    :param shorthand_name:
    :param style_sheet_id:
    :param style_sheet_id: The css style sheet identifier where a new rule should be inserted.
    :param text:
    :param value:
    :param values: Substitution functions (var()/env()/attr()) and cascade-dependent keywords (revert/revert-layer) do not work.
    :returns:
    :returns: *(Optional)* URL of source map associated with script (if any).
    :returns: A tuple with the following items:
    :returns: Class name list.
    :returns: Computed style for the specified DOM node.
    :returns: Identifier of the created "via-inspector" stylesheet.
    :returns: The list of node Ids that have their tracked computed styles updated.
    :returns: The newly created rule.
    :returns: The resulting CSS container query rule after modification.
    :returns: The resulting CSS media rule after modification.
    :returns: The resulting CSS Scope rule after modification.
    :returns: The resulting CSS Supports rule after modification.
    :returns: The resulting key text after modification.
    :returns: The resulting selector list after modification.
    :returns: The resulting styles after modification.
    :returns: The stylesheet text.
    :returns: Usage statistics for every employed platform font.
    @classmethod
    ],
    ``takeCoverageDelta`` (or since start of coverage instrumentation).
    }
    a ``computedStyleUpdated`` event with throttling.
    A descriptor of operation to mutate style declaration text.
    a: int
    active: bool
    and additional information such as platformFontFamily and fontVariationAxes.
    and whenever the computed style is updated for node, it queues
    animation_name: Value
    animation_styles: list[CSSAnimationStyle] | None = None
    Applies specified style edits one after another in the given order.
    attributes) for a DOM node identified by ``nodeId``.
    b: int
    by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
    c: int
    cmd_dict: T_JSON_DICT = {
    computed_length: float | None = None
    container_queries: list[CSSContainerQuery] | None = None
    CONTAINER_RULE = "ContainerRule"
    Creates a new special "via-inspector" stylesheet in the frame with given ``frameId``.
    CSS @position-try rule representation.
    CSS container query rule descriptor.
    CSS coverage information.
    CSS font-palette-values rule representation.
    CSS keyframe rule representation.
    CSS keyframes rule representation.
    CSS Layer at-rule descriptor.
    CSS Layer data.
    CSS media rule descriptor.
    CSS property at-rule representation.
    CSS property declaration data.
    CSS rule collection for a single pseudo style.
    CSS rule representation.
    CSS Scope at-rule descriptor.
    CSS Starting Style at-rule descriptor.
    CSS style coming from animations with the name of the animation.
    CSS style representation.
    CSS stylesheet metainformation.
    CSS Supports at-rule descriptor.
    CSS try rule representation.
    css_properties: list[CSSProperty]
    css_text: str | None = None
    Data for a simple selector (these are delimited by commas in a selector list).
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: str) -> StyleSheetId:
    def from_json(cls, json: T_JSON_DICT) -> ComputedStyleUpdated:
    def from_json(cls, json: T_JSON_DICT) -> FontsUpdated:
    def from_json(cls, json: T_JSON_DICT) -> MediaQueryResultChanged:
    def from_json(cls, json: T_JSON_DICT) -> StyleSheetAdded:
    def from_json(cls, json: T_JSON_DICT) -> StyleSheetChanged:
    def from_json(cls, json: T_JSON_DICT) -> StyleSheetRemoved:
    def to_json(self) -> str:
    def to_json(self):
    default_value: float
    disabled: bool
    disabled: bool | None = None
    Disables the CSS agent for the given page.
    edits: list[StyleDeclarationEdit],
    enabled until the result of this command is received.
    enabled: bool,
    Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
    Enables the selector recording.
    Enables/disables rendering of local CSS fonts (enabled by default).
    end_column: float
    end_column: int
    end_line: float
    end_line: int
    end_offset: float
    Ensures that the given node is in its starting-style state.
    Ensures that the given node will have specified pseudo-classes whenever its style is computed by
    Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors.
    expressions: list[MediaQueryExpression]
    family_name: str
    feature: str
    Find a rule with the given active property for the given node and set the new value for this
    Fired whenever a stylesheet is changed as a result of the client operation.
    Fired whenever an active document stylesheet is added.
    Fired whenever an active document stylesheet is removed.
    Fires whenever a MediaQuery result changes (for example, after a browser window has been
    Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
    font: FontFace | None
    font_display: str
    font_family: str
    font_palette_name: Value
    font_stretch: str
    font_style: str
    font_variant: str
    font_variation_axes: list[FontVariationAxis] | None = None
    font_weight: str
    'font-size' of the element and a value 'calc(1px + 2px)' will be
    For example, a value of '1em' is evaluated according to the computed
    frame_id: page.FrameId
    frame_id: page.FrameId,
    Given a CSS selector text and a style sheet ID, getLocationForSelector
    Given a DOM element identified by nodeId, getLayersForNode returns the root
    glyph_count: float
    has_source_url: bool | None = None
    header: CSSStyleSheetHeader
    https://drafts.csswg.org/selectors/#specificity-rules
    if node_for_property_syntax_validation is not None:
    if node_id is not None:
    if property_name is not None:
    if pseudo_identifier is not None:
    if pseudo_type is not None:
    implicit: bool | None = None
    important: bool | None = None
    including the animation & transition styles coming from inheritance chain.
    Information about amount of glyphs that were rendered with given font.
    Information about font variation axes for variable fonts
    Inherited CSS rule collection from ancestor node.
    Inherited CSS style collection for animated styles from ancestor node.
    Inherited pseudo element matches from pseudos of an ancestor node.
    inherits: bool
    initial_value: Value | None = None
    INJECTED = "injected"
    inline_style: CSSStyle | None = None
    Inserts a new rule with the given ``ruleText`` in a stylesheet with given ``styleSheetId``, at the
    INSPECTOR = "inspector"
    inspector" rules), "regular" for regular stylesheets.
    instrumentation).
    is_constructed: bool
    is_custom_font: bool
    is_inline: bool
    is_mutable: bool
    json = yield cmd_dict
    key_text: Value
    keyframes: list[CSSKeyframeRule]
    layer for the nearest ancestor document or shadow root. The layer root contains
    LAYER_RULE = "LayerRule"
    layers: list[CSSLayer] | None = None
    length: float
    loading_failed: bool | None = None
    location: SourceRange,
    logical_axes: dom.LogicalAxes | None = None
    longhand_properties: list[CSSProperty] | None = None
    Match data for a CSS rule.
    matched_css_rules: list[RuleMatch]
    matches: list[RuleMatch]
    matching_selectors: list[int]
    max_value: float
    Media query descriptor.
    Media query expression descriptor.
    media: list[CSSMedia] | None = None
    media_list: list[MediaQuery] | None = None
    MEDIA_RULE = "MediaRule"
    min_value: float
    Modifies the expression of a container query.
    Modifies the expression of a scope at-rule.
    Modifies the expression of a supports at-rule.
    Modifies the keyframe rule key text.
    Modifies the property rule property name.
    Modifies the rule selector.
    name: str
    name: str | None = None
    name: Value
    nesting_selectors: list[str] | None = None
    node.
    node_for_property_syntax_validation: dom.NodeId | None = None,
    node_id: dom.NodeId
    node_id: dom.NodeId | None = None,
    node_id: dom.NodeId,
    node_id: dom.NodeId, forced: bool
    node_id: dom.NodeId, forced_pseudo_classes: list[str]
    node_id: dom.NodeId, property_name: str, value: str
    Obtain list of rules that became used since last call to this method (or since start of coverage
    order: float
    origin: StyleSheetOrigin
    owner_node: dom.BackendNodeId | None = None
    params: T_JSON_DICT = dict()
    params["edits"] = [i.to_json() for i in edits]
    params["enabled"] = enabled
    params["forced"] = forced
    params["forcedPseudoClasses"] = [i for i in forced_pseudo_classes]
    params["frameId"] = frame_id.to_json()
    params["keyText"] = key_text
    params["location"] = location.to_json()
    params["nodeId"] = node_id.to_json()
    params["propertiesToTrack"] = [i.to_json() for i in properties_to_track]
    params["propertyName"] = property_name
    params["range"] = range_.to_json()
    params["ruleText"] = rule_text
    params["selector"] = selector
    params["selectorText"] = selector_text
    params["shorthandName"] = shorthand_name
    params["styleSheetId"] = style_sheet_id.to_json()
    params["text"] = text
    params["value"] = value
    params["values"] = [i for i in values]
    parsed_ok: bool | None = None
    Pass ``undefined`` to disable tracking.
    physical_axes: dom.PhysicalAxes | None = None
    platform_font_family: str
    Polls the next batch of computed style updates.
    position specified by ``location``.
    post_script_name: str
    Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
    properties_to_track: list[CSSComputedStyleProperty],
    property
    property_name: str
    property_name: str | None = None,
    property_name: Value
    pseudo_elements: list[PseudoElementMatches]
    pseudo_identifier: str | None = None
    pseudo_identifier: str | None = None,
    pseudo_type: dom.PseudoType
    pseudo_type: dom.PseudoType | None = None,
    queries_scroll_state: bool | None = None
    range_: SourceRange
    range_: SourceRange | None = None
    REGULAR = "regular"
    replaces the one previously specified. Pass empty array to disable tracking.
    Representation of a custom property registration through CSS.registerProperty
    Requests information about platform fonts which we used to render child TextNodes in the given
    resized.) The current implementation considers only viewport-dependent media features.
    Resolve the specified values in the context of the provided element.
    resolved to '3px'.
    return (
    return [CSSComputedStyleProperty.from_json(i) for i in json["computedStyle"]]
    return [CSSMedia.from_json(i) for i in json["medias"]]
    return [CSSProperty.from_json(i) for i in json["longhandProperties"]]
    return [CSSStyle.from_json(i) for i in json["styles"]]
    return [dom.NodeId.from_json(i) for i in json["nodeIds"]]
    return [PlatformFontUsage.from_json(i) for i in json["fonts"]]
    return [RuleUsage.from_json(i) for i in json["ruleUsage"]]
    return [SourceRange.from_json(i) for i in json["ranges"]]
    return [str(i) for i in json["classNames"]]
    return [str(i) for i in json["results"]]
    return CSSContainerQuery.from_json(json["containerQuery"])
    return CSSLayerData.from_json(json["rootLayer"])
    return CSSMedia.from_json(json["media"])
    return CSSRule.from_json(json["rule"])
    return CSSScope.from_json(json["scope"])
    return CSSSupports.from_json(json["supports"])
    return SelectorList.from_json(json["selectorList"])
    return str(json["sourceMapURL"]) if "sourceMapURL" in json else None
    return str(json["text"])
    return StyleSheetId.from_json(json["styleSheetId"])
    return Value.from_json(json["keyText"])
    return Value.from_json(json["propertyName"])
    Returns all class names from specified stylesheet.
    Returns all layers parsed by the rendering engine for the tree scope of a node.
    Returns all media queries parsed by the rendering engine.
    returns an array of locations of the CSS selector in the style sheet.
    Returns requested styles for a DOM node identified by ``nodeId``.
    Returns the computed style for a DOM node identified by ``nodeId``.
    Returns the current textual content for a stylesheet.
    Returns the styles coming from animations & transitions
    Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
    rule: CSSRule
    rule_text: str,
    rule_types: list[CSSRuleType] | None = None
    SCOPE_RULE = "ScopeRule"
    scopes: list[CSSScope] | None = None
    Selector list data.
    selector_list: SelectorList
    selectors: list[Value]
    Sets the new stylesheet text.
    shorthand_entries: list[ShorthandEntry]
    shorthand_name: str, value: str
    so passing a new node id removes tracking from the previous node.
    source: str
    source_map_url: str | None = None
    source_url: str
    source_url: str | None = None
    Specificity:
    specificity: Specificity | None = None
    src: str
    start_column: float
    start_column: int
    start_line: float
    start_line: int
    start_offset: float
    STARTING_STYLE_RULE = "StartingStyleRule"
    starting_styles: list[CSSStartingStyle] | None = None
    Starts tracking the given computed styles for updates. The specified array of properties
    Starts tracking the given node for the computed style updates
    Stop tracking rule usage and return the list of rules that were used since last call to
    style: CSSStyle
    STYLE_RULE = "StyleRule"
    style_sheet_id: StyleSheetId
    style_sheet_id: StyleSheetId | None = None
    style_sheet_id: StyleSheetId,
    style_sheet_id: StyleSheetId, range_: SourceRange, key_text: str
    style_sheet_id: StyleSheetId, range_: SourceRange, property_name: str
    style_sheet_id: StyleSheetId, range_: SourceRange, selector: str
    style_sheet_id: StyleSheetId, range_: SourceRange, text: str
    style_sheet_id: StyleSheetId, selector_text: str
    style_sheet_id: StyleSheetId, text: str
    Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent
    stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via
    sub_layers: list[CSSLayerData] | None = None
    supports: list[CSSSupports] | None = None
    SUPPORTS_RULE = "SupportsRule"
    syntax: str
    T_JSON_DICT,
    tag: str
    Text range within a resource. All numbers are zero-based.
    text: str
    text: str | None = None
    the browser.
    The changes to computed style properties are only tracked for nodes pushed to the front-end
    the full layer tree for the tree scope and their ordering.
    There can only be 1 node tracked for computed style updates
    This list only contains rule types that are collected during the ancestor rule collection.
    title: str
    to the front-end, no updates will be issued for the node.
    transitions_style: CSSStyle | None = None
    tuple[
    tuple[CSSStyle | None, CSSStyle | None],
    tuple[list[str] | None, str | None, str | None],
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[dom.NodeId]]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[RuleUsage]]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[list[RuleUsage], float]]
    unicode_range: str
    unit: str
    Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
    used: bool
    USER_AGENT = "user-agent"
    value: float
    value: str
    value_range: SourceRange | None = None
    values: list[str],
    web font.
#
# CDP domain: CSS (experimental)
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSContainerQuery]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSLayerData]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSMedia]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSRule]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSScope]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, CSSSupports]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[CSSComputedStyleProperty]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[CSSProperty]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[CSSStyle]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[PlatformFontUsage]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[SourceRange]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[str]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, SelectorList]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str | None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, StyleSheetId]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, Value]:
):
@dataclass
@event_class("CSS.computedStyleUpdated")
@event_class("CSS.fontsUpdated")
@event_class("CSS.mediaQueryResultChanged")
@event_class("CSS.styleSheetAdded")
@event_class("CSS.styleSheetChanged")
@event_class("CSS.styleSheetRemoved")
]:
class ComputedStyleUpdated:
class CSSAnimationStyle:
class CSSComputedStyleProperty:
class CSSContainerQuery:
class CSSFontPaletteValuesRule:
class CSSKeyframeRule:
class CSSKeyframesRule:
class CSSLayer:
class CSSLayerData:
class CSSMedia:
class CSSPositionTryRule:
class CSSProperty:
class CSSPropertyRegistration:
class CSSPropertyRule:
class CSSRule:
class CSSRuleType:
class CSSScope:
class CSSStartingStyle:
class CSSStyle:
class CSSStyleSheetHeader:
class CSSSupports:
class CSSTryRule:
class FontFace:
class FontsUpdated:
class FontVariationAxis:
class InheritedAnimatedStyleEntry:
class InheritedPseudoElementMatches:
class InheritedStyleEntry:
class MediaQuery:
class MediaQueryExpression:
class MediaQueryResultChanged:
class PlatformFontUsage:
class PseudoElementMatches:
class RuleMatch:
class RuleUsage:
class SelectorList:
class ShorthandEntry:
class SourceRange:
class Specificity:
class StyleDeclarationEdit:
class StyleSheetAdded:
class StyleSheetChanged:
class StyleSheetId:
class StyleSheetOrigin:
class StyleSheetRemoved:
class Value:
def add_rule(
def collect_class_names(
def create_style_sheet(
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def force_pseudo_state(
def force_starting_style(
def get_animated_styles_for_node(
def get_background_colors(
def get_computed_style_for_node(
def get_inline_styles_for_node(
def get_layers_for_node(
def get_location_for_selector(
def get_longhand_properties(
def get_matched_styles_for_node(
def get_media_queries() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[CSSMedia]]:
def get_platform_fonts_for_node(
def get_style_sheet_text(
def resolve_values(
def set_container_query_text(
def set_effective_property_value_for_node(
def set_keyframe_key(
def set_local_fonts_enabled(
def set_media_text(
def set_property_rule_property_name(
def set_rule_selector(
def set_scope_text(
def set_style_sheet_text(
def set_style_texts(
def set_supports_text(
def start_rule_usage_tracking() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def stop_rule_usage_tracking() -> (
def take_computed_style_updates() -> (
def take_coverage_delta() -> (
def track_computed_style_updates(
def track_computed_style_updates_for_node(
from . import dom
from . import page
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing
