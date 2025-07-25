
                    json["attributionReportingIssueDetails"]
                    json["blockedByResponseIssueDetails"]
                    json["contentSecurityPolicyIssueDetails"]
                    json["cookieDeprecationMetadataIssueDetails"]
                    json["federatedAuthRequestIssueDetails"]
                    json["federatedAuthUserInfoRequestIssueDetails"]
                    json["lowTextContrastIssueDetails"]
                    json["navigatorUserAgentIssueDetails"]
                    json["partitioningBlobURLIssueDetails"]
                    json["selectElementAccessibilityIssueDetails"]
                    json["sharedArrayBufferIssueDetails"]
                    json["sharedDictionaryIssueDetails"]
                    json["sriMessageSignatureIssueDetails"]
                    json["stylesheetLoadingIssueDetails"]
                )
                AffectedCookie.from_json(json["cookie"]) if "cookie" in json else None
                AffectedFrame.from_json(json["affectedFrame"])
                AffectedFrame.from_json(json["blockedFrame"])
                AffectedFrame.from_json(json["frameAncestor"])
                AffectedFrame.from_json(json["parentFrame"])
                AffectedRequest.from_json(json["request"])
                AttributionReportingIssueDetails.from_json(
                BlockedByResponseIssueDetails.from_json(
                BounceTrackingIssueDetails.from_json(json["bounceTrackingIssueDetails"])
                ClientHintIssueDetails.from_json(json["clientHintIssueDetails"])
                ContentSecurityPolicyIssueDetails.from_json(
                CookieDeprecationMetadataIssueDetails.from_json(
                CookieExclusionReason.from_json(i)
                CookieIssueDetails.from_json(json["cookieIssueDetails"])
                CookieIssueInsight.from_json(json["insight"])
                CookieWarningReason.from_json(i) for i in json["cookieWarningReasons"]
                CorsIssueDetails.from_json(json["corsIssueDetails"])
                DeprecationIssueDetails.from_json(json["deprecationIssueDetails"])
                dom.BackendNodeId.from_json(json["violatingNodeId"])
                else None
                FailedRequestInfo.from_json(json["failedRequestInfo"])
                FederatedAuthRequestIssueDetails.from_json(
                FederatedAuthUserInfoRequestIssueDetails.from_json(
                for i in json["cookieExclusionReasons"]
                GenericIssueDetails.from_json(json["genericIssueDetails"])
                HeavyAdIssueDetails.from_json(json["heavyAdIssueDetails"])
                if "affectedFrame" in json
                if "attributionReportingIssueDetails" in json
                if "blockedByResponseIssueDetails" in json
                if "blockedFrame" in json
                if "bounceTrackingIssueDetails" in json
                if "clientHintIssueDetails" in json
                if "clientSecurityState" in json
                if "contentSecurityPolicyIssueDetails" in json
                if "cookieDeprecationMetadataIssueDetails" in json
                if "cookieIssueDetails" in json
                if "corsIssueDetails" in json
                if "deprecationIssueDetails" in json
                if "failedRequestInfo" in json
                if "federatedAuthRequestIssueDetails" in json
                if "federatedAuthUserInfoRequestIssueDetails" in json
                if "frameAncestor" in json
                if "genericIssueDetails" in json
                if "heavyAdIssueDetails" in json
                if "insight" in json
                if "location" in json
                if "lowTextContrastIssueDetails" in json
                if "mixedContentIssueDetails" in json
                if "navigatorUserAgentIssueDetails" in json
                if "parentFrame" in json
                if "partitioningBlobURLIssueDetails" in json
                if "propertyRuleIssueDetails" in json
                if "quirksModeIssueDetails" in json
                if "request" in json
                if "requestId" in json
                if "resourceIPAddressSpace" in json
                if "resourceType" in json
                if "scriptId" in json
                if "selectElementAccessibilityIssueDetails" in json
                if "sharedArrayBufferIssueDetails" in json
                if "sharedDictionaryIssueDetails" in json
                if "sourceCodeLocation" in json
                if "sriMessageSignatureIssueDetails" in json
                if "stylesheetLoadingIssueDetails" in json
                if "violatingNodeAttribute" in json
                if "violatingNodeId" in json
                json["clientHintIssueReason"]
                json["contentSecurityPolicyViolationType"]
                json["corsErrorStatus"]
                json["federatedAuthRequestIssueReason"]
                json["federatedAuthUserInfoRequestIssueReason"]
                json["partitioningBlobURLInfo"]
                json["propertyRuleIssueReason"]
                json["resolutionStatus"]
                json["selectElementAccessibilityIssueReason"]
                json["sharedDictionaryError"]
                json["sourceCodeLocation"]
                json["styleSheetLoadingIssueReason"]
                json["violationType"]
                LowTextContrastIssueDetails.from_json(
                MixedContentIssueDetails.from_json(json["mixedContentIssueDetails"])
                MixedContentResourceType.from_json(json["resourceType"])
                NavigatorUserAgentIssueDetails.from_json(
                network.ClientSecurityState.from_json(json["clientSecurityState"])
                network.IPAddressSpace.from_json(json["resourceIPAddressSpace"])
                network.RequestId.from_json(json["requestId"])
                page.FrameId.from_json(json["frameId"]) if "frameId" in json else None
                PartitioningBlobURLIssueDetails.from_json(
                PropertyRuleIssueDetails.from_json(json["propertyRuleIssueDetails"])
                QuirksModeIssueDetails.from_json(json["quirksModeIssueDetails"])
                runtime.ScriptId.from_json(json["scriptId"])
                SelectElementAccessibilityIssueDetails.from_json(
                self.attribution_reporting_issue_details.to_json()
                self.blocked_by_response_issue_details.to_json()
                self.bounce_tracking_issue_details.to_json()
                self.content_security_policy_issue_details.to_json()
                self.cookie_deprecation_metadata_issue_details.to_json()
                self.federated_auth_request_issue_details.to_json()
                self.federated_auth_user_info_request_issue_details.to_json()
                self.low_text_contrast_issue_details.to_json()
                self.mixed_content_issue_details.to_json()
                self.navigator_user_agent_issue_details.to_json()
                self.partitioning_blob_url_issue_details.to_json()
                self.property_rule_issue_details.to_json()
                self.select_element_accessibility_issue_details.to_json()
                self.shared_array_buffer_issue_details.to_json()
                self.shared_dictionary_issue_details.to_json()
                self.sri_message_signature_issue_details.to_json()
                self.stylesheet_loading_issue_details.to_json()
                SharedArrayBufferIssueDetails.from_json(
                SharedDictionaryIssueDetails.from_json(
                SourceCodeLocation.from_json(json["location"])
                SourceCodeLocation.from_json(json["sourceCodeLocation"])
                SRIMessageSignatureIssueDetails.from_json(
                str(json["initiatorOrigin"]) if "initiatorOrigin" in json else None
                str(json["invalidParameter"]) if "invalidParameter" in json else None
                str(json["propertyValue"]) if "propertyValue" in json else None
                str(json["rawCookieLine"]) if "rawCookieLine" in json else None
                str(json["siteForCookies"]) if "siteForCookies" in json else None
                str(json["tableEntryUrl"]) if "tableEntryUrl" in json else None
                str(json["violatingNodeAttribute"])
                StylesheetLoadingIssueDetails.from_json(
            )
            ),
            ],
            affected_frame=(
            allowed_sites=[str(i) for i in json["allowedSites"]],
            attribution_reporting_issue_details=(
            blocked_by_response_issue_details=(
            blocked_frame=(
            blocked_url=str(json["blockedURL"]) if "blockedURL" in json else None,
            bounce_tracking_issue_details=(
            client_hint_issue_details=(
            client_hint_issue_reason=ClientHintIssueReason.from_json(
            client_security_state=(
            code=InspectorIssueCode.from_json(json["code"]),
            column_number=int(json["columnNumber"]),
            content_security_policy_issue_details=(
            content_security_policy_violation_type=ContentSecurityPolicyViolationType.from_json(
            contrast_ratio=float(json["contrastRatio"]),
            cookie_deprecation_metadata_issue_details=(
            cookie_exclusion_reasons=[
            cookie_issue_details=(
            cookie_url=str(json["cookieUrl"]) if "cookieUrl" in json else None,
            cookie_warning_reasons=[
            cookie=(
            cors_error_status=network.CorsErrorStatus.from_json(
            cors_issue_details=(
            deprecation_issue_details=(
            details=InspectorIssueDetails.from_json(json["details"]),
            document_node_id=dom.BackendNodeId.from_json(json["documentNodeId"]),
            domain=str(json["domain"]),
            error_type=GenericIssueErrorType.from_json(json["errorType"]),
            error=SRIMessageSignatureError.from_json(json["error"]),
            failed_request_info=(
            failure_message=str(json["failureMessage"]),
            federated_auth_request_issue_details=(
            federated_auth_request_issue_reason=FederatedAuthRequestIssueReason.from_json(
            federated_auth_user_info_request_issue_details=(
            federated_auth_user_info_request_issue_reason=FederatedAuthUserInfoRequestIssueReason.from_json(
            font_size=str(json["fontSize"]),
            font_weight=str(json["fontWeight"]),
            frame_ancestor=(
            frame_id=(
            frame_id=page.FrameId.from_json(json["frameId"]),
            frame=AffectedFrame.from_json(json["frame"]) if "frame" in json else None,
            frame=AffectedFrame.from_json(json["frame"]),
            generic_issue_details=(
            has_disallowed_attributes=bool(json["hasDisallowedAttributes"]),
            heavy_ad_issue_details=(
            i.to_json() for i in self.cookie_exclusion_reasons
            i.to_json() for i in self.cookie_warning_reasons
            initiator_origin=(
            insecure_url=str(json["insecureURL"]),
            insight=(
            integrity_assertions=[str(i) for i in json["integrityAssertions"]],
            invalid_parameter=(
            is_limited_quirks_mode=bool(json["isLimitedQuirksMode"]),
            is_opt_out_top_level=bool(json["isOptOutTopLevel"]),
            is_report_only=bool(json["isReportOnly"]),
            is_warning=bool(json["isWarning"]),
            issue_id=IssueId.from_json(json["issueId"]) if "issueId" in json else None,
            json["affectedFrame"] = self.affected_frame.to_json()
            json["attributionReportingIssueDetails"] = (
            json["blockedByResponseIssueDetails"] = (
            json["blockedFrame"] = self.blocked_frame.to_json()
            json["blockedURL"] = self.blocked_url
            json["bounceTrackingIssueDetails"] = (
            json["clientHintIssueDetails"] = self.client_hint_issue_details.to_json()
            json["clientSecurityState"] = self.client_security_state.to_json()
            json["contentSecurityPolicyIssueDetails"] = (
            json["cookie"] = self.cookie.to_json()
            json["cookieDeprecationMetadataIssueDetails"] = (
            json["cookieIssueDetails"] = self.cookie_issue_details.to_json()
            json["cookieUrl"] = self.cookie_url
            json["corsIssueDetails"] = self.cors_issue_details.to_json()
            json["deprecationIssueDetails"] = self.deprecation_issue_details.to_json()
            json["failedRequestInfo"] = self.failed_request_info.to_json()
            json["federatedAuthRequestIssueDetails"] = (
            json["federatedAuthUserInfoRequestIssueDetails"] = (
            json["frame"] = self.frame.to_json()
            json["frameAncestor"] = self.frame_ancestor.to_json()
            json["frameId"] = self.frame_id.to_json()
            json["genericIssueDetails"] = self.generic_issue_details.to_json()
            json["heavyAdIssueDetails"] = self.heavy_ad_issue_details.to_json()
            json["initiatorOrigin"] = self.initiator_origin
            json["insight"] = self.insight.to_json()
            json["invalidParameter"] = self.invalid_parameter
            json["issueId"] = self.issue_id.to_json()
            json["location"] = self.location.to_json()
            json["lowTextContrastIssueDetails"] = (
            json["mixedContentIssueDetails"] = (
            json["navigatorUserAgentIssueDetails"] = (
            json["parentFrame"] = self.parent_frame.to_json()
            json["partitioningBlobURLIssueDetails"] = (
            json["propertyRuleIssueDetails"] = (
            json["propertyValue"] = self.property_value
            json["quirksModeIssueDetails"] = self.quirks_mode_issue_details.to_json()
            json["rawCookieLine"] = self.raw_cookie_line
            json["request"] = self.request.to_json()
            json["requestId"] = self.request_id.to_json()
            json["resourceIPAddressSpace"] = self.resource_ip_address_space.to_json()
            json["resourceType"] = self.resource_type.to_json()
            json["scriptId"] = self.script_id.to_json()
            json["selectElementAccessibilityIssueDetails"] = (
            json["sharedArrayBufferIssueDetails"] = (
            json["sharedDictionaryIssueDetails"] = (
            json["siteForCookies"] = self.site_for_cookies
            json["sourceCodeLocation"] = self.source_code_location.to_json()
            json["sriMessageSignatureIssueDetails"] = (
            json["stylesheetLoadingIssueDetails"] = (
            json["tableEntryUrl"] = self.table_entry_url
            json["violatingNodeAttribute"] = self.violating_node_attribute
            json["violatingNodeId"] = self.violating_node_id.to_json()
            line_number=int(json["lineNumber"]),
            loader_id=network.LoaderId.from_json(json["loaderId"]),
            location=(
            low_text_contrast_issue_details=(
            main_resource_url=str(json["mainResourceURL"]),
            mixed_content_issue_details=(
            name=str(json["name"]),
            navigator_user_agent_issue_details=(
            node_id=dom.BackendNodeId.from_json(json["nodeId"]),
            operation=CookieOperation.from_json(json["operation"]),
            opt_out_percentage=float(json["optOutPercentage"]),
            parent_frame=(
            partitioning_blob_url_info=PartitioningBlobURLInfo.from_json(
            partitioning_blob_url_issue_details=(
            path=str(json["path"]),
            property_rule_issue_details=(
            property_rule_issue_reason=PropertyRuleIssueReason.from_json(
            property_value=(
            quirks_mode_issue_details=(
            raw_cookie_line=(
            reason=BlockedByResponseReason.from_json(json["reason"]),
            reason=HeavyAdReason.from_json(json["reason"]),
            request_id=(
            request=(
            request=AffectedRequest.from_json(json["request"]),
            resolution_status=MixedContentResolutionStatus.from_json(
            resolution=HeavyAdResolutionStatus.from_json(json["resolution"]),
            resource_ip_address_space=(
            resource_type=(
            script_id=(
            select_element_accessibility_issue_details=(
            select_element_accessibility_issue_reason=SelectElementAccessibilityIssueReason.from_json(
            self.content_security_policy_violation_type.to_json()
            self.federated_auth_request_issue_reason.to_json()
            self.federated_auth_user_info_request_issue_reason.to_json()
            self.select_element_accessibility_issue_reason.to_json()
            self.style_sheet_loading_issue_reason.to_json()
            shared_array_buffer_issue_details=(
            shared_dictionary_error=SharedDictionaryError.from_json(
            shared_dictionary_issue_details=(
            signature_base=str(json["signatureBase"]),
            site_for_cookies=(
            source_code_location=(
            source_code_location=SourceCodeLocation.from_json(
            sri_message_signature_issue_details=(
            style_sheet_loading_issue_reason=StyleSheetLoadingIssueReason.from_json(
            stylesheet_loading_issue_details=(
            table_entry_url=(
            threshold_aa=float(json["thresholdAA"]),
            threshold_aaa=float(json["thresholdAAA"]),
            tracking_sites=[str(i) for i in json["trackingSites"]],
            type_=InsightType.from_json(json["type"]),
            type_=SharedArrayBufferIssueType.from_json(json["type"]),
            type_=str(json["type"]),
            url=str(json["url"]),
            violated_directive=str(json["violatedDirective"]),
            violating_node_attribute=(
            violating_node_id=(
            violating_node_id=dom.BackendNodeId.from_json(json["violatingNodeId"]),
            violating_node_selector=str(json["violatingNodeSelector"]),
            violation_type=AttributionReportingIssueType.from_json(
        "CoopSandboxedIFrameCannotNavigateToCoopPage"
        "CorpNotSameOriginAfterDefaultedToSameOriginByCoep"
        "CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip"
        "CorpNotSameOriginAfterDefaultedToSameOriginByDip"
        "ExcludeSameSiteUnspecifiedTreatedAsLax"
        "ExcludeThirdPartyCookieBlockedInFirstPartySet"
        "FormEmptyIdAndNameAttributesForInputError"
        "FormInputAssignedAutocompleteValueToIdOrNameAttributeError"
        "FormInputHasWrongButWellIntendedAutocompleteValueError"
        "FormLabelForMatchesNonExistingIdError"
        "method": "Audits.checkContrast",
        "method": "Audits.checkFormsIssues",
        "method": "Audits.disable",
        "method": "Audits.enable",
        "method": "Audits.getEncodedResponse",
        "NavigationRegistrationUniqueScopeAlreadySet"
        "NavigationRegistrationWithoutTransientUserActivation"
        "params": params,
        "SignatureHeaderValueIsNotByteSequence"
        "SignatureInputHeaderInvalidComponentName"
        "SignatureInputHeaderInvalidComponentType"
        "SignatureInputHeaderInvalidDerivedComponentParameter"
        "SignatureInputHeaderInvalidHeaderComponentParameter"
        "SignatureInputHeaderMissingRequiredParameters"
        "SignatureInputHeaderValueMissingComponents"
        "SignatureInputHeaderValueNotInnerList"
        "UseErrorUnexpectedContentDictionaryHeader"
        "WarnCrossSiteRedirectDowngradeChangesInclusion"
        "WarnSameSiteStrictCrossDowngradeStrict"
        "WarnSameSiteUnspecifiedCrossSiteContext"
        "WarnSameSiteUnspecifiedLaxAllowUnsafe"
        )
        ]
        0. **body** - *(Optional)* The encoded body as a base64 string. Omitted if sizeOnly is true.
        1. **originalSize** - Size before re-encoding.
        2. **encodedSize** - Size after re-encoding.
        ContentSecurityPolicyIssueDetails
        CookieDeprecationMetadataIssueDetails
        FederatedAuthUserInfoRequestIssueDetails
        FederatedAuthUserInfoRequestIssueReason
        if self.affected_frame is not None:
        if self.attribution_reporting_issue_details is not None:
        if self.blocked_by_response_issue_details is not None:
        if self.blocked_frame is not None:
        if self.blocked_url is not None:
        if self.bounce_tracking_issue_details is not None:
        if self.client_hint_issue_details is not None:
        if self.client_security_state is not None:
        if self.content_security_policy_issue_details is not None:
        if self.cookie is not None:
        if self.cookie_deprecation_metadata_issue_details is not None:
        if self.cookie_issue_details is not None:
        if self.cookie_url is not None:
        if self.cors_issue_details is not None:
        if self.deprecation_issue_details is not None:
        if self.failed_request_info is not None:
        if self.federated_auth_request_issue_details is not None:
        if self.federated_auth_user_info_request_issue_details is not None:
        if self.frame is not None:
        if self.frame_ancestor is not None:
        if self.frame_id is not None:
        if self.generic_issue_details is not None:
        if self.heavy_ad_issue_details is not None:
        if self.initiator_origin is not None:
        if self.insight is not None:
        if self.invalid_parameter is not None:
        if self.issue_id is not None:
        if self.location is not None:
        if self.low_text_contrast_issue_details is not None:
        if self.mixed_content_issue_details is not None:
        if self.navigator_user_agent_issue_details is not None:
        if self.parent_frame is not None:
        if self.partitioning_blob_url_issue_details is not None:
        if self.property_rule_issue_details is not None:
        if self.property_value is not None:
        if self.quirks_mode_issue_details is not None:
        if self.raw_cookie_line is not None:
        if self.request is not None:
        if self.request_id is not None:
        if self.resource_ip_address_space is not None:
        if self.resource_type is not None:
        if self.script_id is not None:
        if self.select_element_accessibility_issue_details is not None:
        if self.shared_array_buffer_issue_details is not None:
        if self.shared_dictionary_issue_details is not None:
        if self.site_for_cookies is not None:
        if self.source_code_location is not None:
        if self.sri_message_signature_issue_details is not None:
        if self.stylesheet_loading_issue_details is not None:
        if self.table_entry_url is not None:
        if self.violating_node_attribute is not None:
        if self.violating_node_id is not None:
        int(json["encodedSize"]),
        int(json["originalSize"]),
        json = dict()
        json["allowedSites"] = [i for i in self.allowed_sites]
        json["clientHintIssueReason"] = self.client_hint_issue_reason.to_json()
        json["code"] = self.code.to_json()
        json["columnNumber"] = self.column_number
        json["contentSecurityPolicyViolationType"] = (
        json["contrastRatio"] = self.contrast_ratio
        json["cookieExclusionReasons"] = [
        json["cookieWarningReasons"] = [
        json["corsErrorStatus"] = self.cors_error_status.to_json()
        json["details"] = self.details.to_json()
        json["documentNodeId"] = self.document_node_id.to_json()
        json["domain"] = self.domain
        json["error"] = self.error.to_json()
        json["errorType"] = self.error_type.to_json()
        json["failureMessage"] = self.failure_message
        json["federatedAuthRequestIssueReason"] = (
        json["federatedAuthUserInfoRequestIssueReason"] = (
        json["fontSize"] = self.font_size
        json["fontWeight"] = self.font_weight
        json["frame"] = self.frame.to_json()
        json["frameId"] = self.frame_id.to_json()
        json["hasDisallowedAttributes"] = self.has_disallowed_attributes
        json["insecureURL"] = self.insecure_url
        json["integrityAssertions"] = [i for i in self.integrity_assertions]
        json["isLimitedQuirksMode"] = self.is_limited_quirks_mode
        json["isOptOutTopLevel"] = self.is_opt_out_top_level
        json["isReportOnly"] = self.is_report_only
        json["isWarning"] = self.is_warning
        json["lineNumber"] = self.line_number
        json["loaderId"] = self.loader_id.to_json()
        json["mainResourceURL"] = self.main_resource_url
        json["name"] = self.name
        json["nodeId"] = self.node_id.to_json()
        json["operation"] = self.operation.to_json()
        json["optOutPercentage"] = self.opt_out_percentage
        json["partitioningBlobURLInfo"] = self.partitioning_blob_url_info.to_json()
        json["path"] = self.path
        json["propertyRuleIssueReason"] = self.property_rule_issue_reason.to_json()
        json["reason"] = self.reason.to_json()
        json["request"] = self.request.to_json()
        json["resolution"] = self.resolution.to_json()
        json["resolutionStatus"] = self.resolution_status.to_json()
        json["selectElementAccessibilityIssueReason"] = (
        json["sharedDictionaryError"] = self.shared_dictionary_error.to_json()
        json["signatureBase"] = self.signature_base
        json["sourceCodeLocation"] = self.source_code_location.to_json()
        json["styleSheetLoadingIssueReason"] = (
        json["thresholdAA"] = self.threshold_aa
        json["thresholdAAA"] = self.threshold_aaa
        json["trackingSites"] = [i for i in self.tracking_sites]
        json["type"] = self.type_
        json["type"] = self.type_.to_json()
        json["url"] = self.url
        json["violatedDirective"] = self.violated_directive
        json["violatingNodeId"] = self.violating_node_id.to_json()
        json["violatingNodeSelector"] = self.violating_node_selector
        json["violationType"] = self.violation_type.to_json()
        None
        params["quality"] = quality
        params["reportAAA"] = report_aaa
        params["sizeOnly"] = size_only
        return "IssueId({})".format(super().__repr__())
        return cls(
        return cls(issue=InspectorIssue.from_json(json["issue"]))
        return cls(json)
        return json
        return self
        return self.value
        SelectElementAccessibilityIssueDetails
        str(json["body"]) if "body" in json else None,
    """
    #: A unique id for this issue. May be omitted if no other entity (e.g.
    #: Additional information about the Partitioning Blob URL issue.
    #: blink::mojom::RequestContextType, which will be replaced
    #: by network::mojom::RequestDestination
    #: Contains additional info when the failure was due to a request.
    #: cookie line is syntactically or semantically malformed in a way
    #: Does not always exist (e.g. for unsafe form submission urls).
    #: exception, CDP message, etc.) is referencing this issue.
    #: form,...). Marked as optional because it is mapped to from
    #: If AffectedCookie is not set then rawCookieLine contains the raw
    #: If false, it means the document's mode is "quirks"
    #: instead of "limited-quirks".
    #: Issues with the same errorType are aggregated in the frontend.
    #: Link to table entry in third-party cookie migration readiness list.
    #: may be used by the front-end as additional context.
    #: One of the deprecation names from third_party/blink/renderer/core/frame/deprecation/deprecation.json5
    #: Optional because not every mixed content issue is necessarily linked to a frame.
    #: Optionally identifies the site-for-cookies and the cookie url, which
    #: Reason why the property rule was discarded.
    #: Reason why the stylesheet couldn't be loaded.
    #: Set-Cookie header string. This hints at a problem where the
    #: Source code position of the property rule.
    #: Source code position that referenced the failing stylesheet.
    #: Specific directive that is violated, causing the CSP issue.
    #: that no valid cookie could be created.
    #: The BlobURL that failed to load.
    #: The failure message for the failed request.
    #: The following three properties uniquely identify a cookie
    #: The frame that was blocked.
    #: The mixed content request.
    #: The reason the ad was blocked, total network or cpu or peak cpu.
    #: The recommended solution to the issue.
    #: The resolution status, either blocking the content or warning.
    #: The type of resource causing the mixed content issue (css, js, iframe,
    #: The unique request id.
    #: The unsafe http url causing the mixed content issue.
    #: The url not included in allowed sources.
    #: The url responsible for the call to an unsafe url.
    #: The URL that failed to load.
    #: The value of the property rule property that failed to parse
    #: The way the mixed content issue is being resolved.
    )
    ) = None
    :param encoding: The encoding to use.
    :param quality: *(Optional)* The quality of the encoding (0-1). (defaults to 1)
    :param report_aaa: *(Optional)* Whether to report WCAG AAA level issues. Default is false.
    :param request_id: Identifier of the network request to get content for.
    :param size_only: *(Optional)* Whether to only return the size information (defaults to false).
    :returns:
    :returns: A tuple with the following items:
    @classmethod
    ``https://example.test:80/web_page`` was accessing cookies, the site reported
    ``issueAdded`` event.
    }
    A unique id for a DevTools inspector issue. Allows other entities (e.g.
    A unique identifier for the type of issue. Each type may use one of the
    ACCOUNTS_HTTP_NOT_FOUND = "AccountsHttpNotFound"
    ACCOUNTS_INVALID_CONTENT_TYPE = "AccountsInvalidContentType"
    ACCOUNTS_INVALID_RESPONSE = "AccountsInvalidResponse"
    ACCOUNTS_LIST_EMPTY = "AccountsListEmpty"
    ACCOUNTS_NO_RESPONSE = "AccountsNoResponse"
    add a new optional field to this type.
    affected_frame: AffectedFrame | None = None
    all cases except for success.
    allowed_sites: list[str]
    An inspector issue reported from the back-end.
    applies to images.
    ATTRIBUTION_REPORTING_ISSUE = "AttributionReportingIssue"
    attribution_reporting_issue_details: None | (AttributionReportingIssueDetails) = (
    ATTRIBUTION_SRC = "AttributionSrc"
    AUDIO = "Audio"
    BEACON = "Beacon"
    BLOCKED_BY_RESPONSE_ISSUE = "BlockedByResponseIssue"
    blocked_by_response_issue_details: None | (BlockedByResponseIssueDetails) = None
    BLOCKED_CROSS_PARTITION_FETCHING = "BlockedCrossPartitionFetching"
    blocked_frame: AffectedFrame | None = None
    blocked_url: str | None = None
    BOUNCE_TRACKING_ISSUE = "BounceTrackingIssue"
    bounce_tracking_issue_details: BounceTrackingIssueDetails | None = None
    CANCELED = "Canceled"
    CLIENT_HINT_ISSUE = "ClientHintIssue"
    client_hint_issue_details: ClientHintIssueDetails | None = None
    client_hint_issue_reason: ClientHintIssueReason
    CLIENT_METADATA_HTTP_NOT_FOUND = "ClientMetadataHttpNotFound"
    CLIENT_METADATA_INVALID_CONTENT_TYPE = "ClientMetadataInvalidContentType"
    CLIENT_METADATA_INVALID_RESPONSE = "ClientMetadataInvalidResponse"
    CLIENT_METADATA_NO_RESPONSE = "ClientMetadataNoResponse"
    client_security_state: network.ClientSecurityState | None = None
    cmd_dict: T_JSON_DICT = {
    code. Currently only used for COEP/COOP, but may be extended to include
    code: InspectorIssueCode
    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "CoepFrameResourceNeedsCoepHeader"
    column_number: int
    CONFIG_HTTP_NOT_FOUND = "ConfigHttpNotFound"
    CONFIG_INVALID_CONTENT_TYPE = "ConfigInvalidContentType"
    CONFIG_INVALID_RESPONSE = "ConfigInvalidResponse"
    CONFIG_NO_RESPONSE = "ConfigNoResponse"
    CONFIG_NOT_IN_WELL_KNOWN = "ConfigNotInWellKnown"
    CONTENT_SECURITY_POLICY_ISSUE = "ContentSecurityPolicyIssue"
    content_security_policy_issue_details: None | (
    content_security_policy_violation_type: ContentSecurityPolicyViolationType
    contrast_ratio: float
    cookie: AffectedCookie | None = None
    COOKIE_DEPRECATION_METADATA_ISSUE = "CookieDeprecationMetadataIssue"
    cookie_deprecation_metadata_issue_details: None | (
    cookie_exclusion_reasons: list[CookieExclusionReason]
    COOKIE_ISSUE = "CookieIssue"
    cookie_issue_details: CookieIssueDetails | None = None
    cookie_url: str | None = None
    cookie_warning_reasons: list[CookieWarningReason]
    COOP_SANDBOXED_I_FRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = (
    CORP_NOT_SAME_ORIGIN = "CorpNotSameOrigin"
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP_AND_DIP = (
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_DIP = (
    CORP_NOT_SAME_SITE = "CorpNotSameSite"
    CORS RFC1918 enforcement.
    CORS_ERROR = "CorsError"
    cors_error_status: network.CorsErrorStatus
    CORS_ISSUE = "CorsIssue"
    cors_issue_details: CorsIssueDetails | None = None
    CPU_PEAK_LIMIT = "CpuPeakLimit"
    CPU_TOTAL_LIMIT = "CpuTotalLimit"
    CREATION_ISSUE = "CreationIssue"
    CSP_REPORT = "CSPReport"
    current page, and have been permitted due to having a global metadata grant.
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: str) -> IssueId:
    def from_json(cls, json: T_JSON_DICT) -> IssueAdded:
    def to_json(self) -> str:
    def to_json(self):
    Depending on the concrete errorType, different properties are set.
    DEPRECATION_ISSUE = "DeprecationIssue"
    deprecation_issue_details: DeprecationIssueDetails | None = None
    Details for a CORS related issue, e.g. a warning or error related to
    Details for a issue arising from an SAB being instantiated in, or
    Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
    Details for issues about documents in Quirks Mode
    Details for issues around "Attribution Reporting API" usage.
    details: InspectorIssueDetails
    DISABLED_IN_FLAGS = "DisabledInFlags"
    DISABLED_IN_SETTINGS = "DisabledInSettings"
    Disables issues domain, prevents further issues from being reported to the client.
    DISALLOWED_OPT_GROUP_CHILD = "DisallowedOptGroupChild"
    DISALLOWED_SELECT_CHILD = "DisallowedSelectChild"
    document_node_id: dom.BackendNodeId
    domain: str
    DOWNLOAD = "Download"
    Enables issues domain, sends the issues collected so far to the client by means of the
    encoding: str,
    ENFORCE_NOOPENER_FOR_NAVIGATION = "EnforceNoopenerForNavigation"
    Enum indicating the reason a response has been blocked. These reasons are
    error: SRIMessageSignatureError
    ERROR_FETCHING_SIGNIN = "ErrorFetchingSignin"
    ERROR_ID_TOKEN = "ErrorIdToken"
    error_type: GenericIssueErrorType
    EVENT_SOURCE = "EventSource"
    exceptions, CDP message, console messages, etc.) to reference an issue.
    EXCLUDE_DOMAIN_NON_ASCII = "ExcludeDomainNonASCII"
    EXCLUDE_INVALID_SAME_PARTY = "ExcludeInvalidSameParty"
    EXCLUDE_PORT_MISMATCH = "ExcludePortMismatch"
    EXCLUDE_SAME_PARTY_CROSS_PARTY_CONTEXT = "ExcludeSamePartyCrossPartyContext"
    EXCLUDE_SAME_SITE_LAX = "ExcludeSameSiteLax"
    EXCLUDE_SAME_SITE_NONE_INSECURE = "ExcludeSameSiteNoneInsecure"
    EXCLUDE_SAME_SITE_STRICT = "ExcludeSameSiteStrict"
    EXCLUDE_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = (
    EXCLUDE_SCHEME_MISMATCH = "ExcludeSchemeMismatch"
    EXCLUDE_THIRD_PARTY_COOKIE_BLOCKED_IN_FIRST_PARTY_SET = (
    EXCLUDE_THIRD_PARTY_PHASEOUT = "ExcludeThirdPartyPhaseout"
    Explainer: https://github.com/WICG/attribution-reporting-api
    failed_request_info: FailedRequestInfo | None = None
    failure_message: str
    FAVICON = "Favicon"
    features, encourage the use of new ones, and provide general guidance.
    FEDERATED_AUTH_REQUEST_ISSUE = "FederatedAuthRequestIssue"
    federated_auth_request_issue_details: None | (FederatedAuthRequestIssueDetails) = (
    federated_auth_request_issue_reason: FederatedAuthRequestIssueReason
    FEDERATED_AUTH_USER_INFO_REQUEST_ISSUE = "FederatedAuthUserInfoRequestIssue"
    federated_auth_user_info_request_issue_details: None | (
    federated_auth_user_info_request_issue_reason: (
    FONT = "Font"
    font_size: str
    font_weight: str
    For example, if the URL ``https://example.test:80/bounce`` was in the
    FORM = "Form"
    FORM_ARIA_LABELLED_BY_TO_NON_EXISTING_ID = "FormAriaLabelledByToNonExistingId"
    FORM_AUTOCOMPLETE_ATTRIBUTE_EMPTY_ERROR = "FormAutocompleteAttributeEmptyError"
    FORM_DUPLICATE_ID_FOR_INPUT_ERROR = "FormDuplicateIdForInputError"
    FORM_EMPTY_ID_AND_NAME_ATTRIBUTES_FOR_INPUT_ERROR = (
    FORM_INPUT_ASSIGNED_AUTOCOMPLETE_VALUE_TO_ID_OR_NAME_ATTRIBUTE_ERROR = (
    FORM_INPUT_HAS_WRONG_BUT_WELL_INTENDED_AUTOCOMPLETE_VALUE_ERROR = (
    FORM_INPUT_WITH_NO_LABEL_ERROR = "FormInputWithNoLabelError"
    FORM_LABEL_FOR_MATCHES_NON_EXISTING_ID_ERROR = (
    FORM_LABEL_FOR_NAME_ERROR = "FormLabelForNameError"
    FORM_LABEL_HAS_NEITHER_FOR_NOR_NESTED_INPUT = "FormLabelHasNeitherForNorNestedInput"
    FRAME = "Frame"
    frame: AffectedFrame
    frame: AffectedFrame | None = None
    frame_ancestor: AffectedFrame | None = None
    frame_id: page.FrameId
    frame_id: page.FrameId | None = None
    GENERIC_ISSUE = "GenericIssue"
    generic_issue_details: GenericIssueDetails | None = None
    GIT_HUB_RESOURCE = "GitHubResource"
    GRACE_PERIOD = "GracePeriod"
    has_disallowed_attributes: bool
    HEAVY_AD_BLOCKED = "HeavyAdBlocked"
    HEAVY_AD_ISSUE = "HeavyAdIssue"
    heavy_ad_issue_details: HeavyAdIssueDetails | None = None
    HEAVY_AD_WARNING = "HeavyAdWarning"
    HEURISTICS = "Heuristics"
    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    ID_TOKEN_CROSS_SITE_IDP_ERROR_RESPONSE = "IdTokenCrossSiteIdpErrorResponse"
    ID_TOKEN_HTTP_NOT_FOUND = "IdTokenHttpNotFound"
    ID_TOKEN_IDP_ERROR_RESPONSE = "IdTokenIdpErrorResponse"
    ID_TOKEN_INVALID_CONTENT_TYPE = "IdTokenInvalidContentType"
    ID_TOKEN_INVALID_REQUEST = "IdTokenInvalidRequest"
    ID_TOKEN_INVALID_RESPONSE = "IdTokenInvalidResponse"
    ID_TOKEN_NO_RESPONSE = "IdTokenNoResponse"
    IDP_NOT_POTENTIALLY_TRUSTWORTHY = "IdpNotPotentiallyTrustworthy"
    if quality is not None:
    if report_aaa is not None:
    if size_only is not None:
    IMAGE = "Image"
    IMPORT = "Import"
    Information about a cookie that is affected by an inspector issue.
    Information about a request that is affected by an inspector issue.
    Information about the frame affected by an inspector issue.
    information about the kind of issue.
    Information about the suggested solution to a cookie issue.
    information without the cookie.
    initiator_origin: str | None = None
    INSECURE_CONTEXT = "InsecureContext"
    insecure_url: str
    insight: CookieIssueInsight | None = None
    integrity_assertions: list[str]
    INTERACTIVE_CONTENT_LEGEND_CHILD = "InteractiveContentLegendChild"
    INTERACTIVE_CONTENT_OPTION_CHILD = "InteractiveContentOptionChild"
    INVALID_ACCOUNTS_RESPONSE = "InvalidAccountsResponse"
    INVALID_CONFIG_OR_WELL_KNOWN = "InvalidConfigOrWellKnown"
    INVALID_FIELDS_SPECIFIED = "InvalidFieldsSpecified"
    INVALID_HEADER = "InvalidHeader"
    INVALID_INFO_HEADER = "InvalidInfoHeader"
    INVALID_INHERITS = "InvalidInherits"
    INVALID_INITIAL_VALUE = "InvalidInitialValue"
    INVALID_NAME = "InvalidName"
    invalid_parameter: str | None = None
    INVALID_REGISTER_OS_SOURCE_HEADER = "InvalidRegisterOsSourceHeader"
    INVALID_REGISTER_OS_TRIGGER_HEADER = "InvalidRegisterOsTriggerHeader"
    INVALID_REGISTER_TRIGGER_HEADER = "InvalidRegisterTriggerHeader"
    INVALID_SIGNATURE_HEADER = "InvalidSignatureHeader"
    INVALID_SIGNATURE_INPUT_HEADER = "InvalidSignatureInputHeader"
    INVALID_SIGNIN_RESPONSE = "InvalidSigninResponse"
    INVALID_SYNTAX = "InvalidSyntax"
    is_limited_quirks_mode: bool
    is_opt_out_top_level: bool
    is_report_only: bool
    is_warning: bool
    issue: InspectorIssue
    issue_id: IssueId | None = None
    JSON = "JSON"
    json = yield cmd_dict
    K_EVAL_VIOLATION = "kEvalViolation"
    K_INLINE_VIOLATION = "kInlineViolation"
    K_SRI_VIOLATION = "kSRIViolation"
    K_TRUSTED_TYPES_POLICY_VIOLATION = "kTrustedTypesPolicyViolation"
    K_TRUSTED_TYPES_SINK_VIOLATION = "kTrustedTypesSinkViolation"
    K_URL_VIOLATION = "kURLViolation"
    K_WASM_EVAL_VIOLATION = "kWasmEvalViolation"
    LATE_IMPORT_RULE = "LateImportRule"
    line_number: int
    loader_id: network.LoaderId
    location: SourceCodeLocation | None = None
    LOW_TEXT_CONTRAST_ISSUE = "LowTextContrastIssue"
    low_text_contrast_issue_details: LowTextContrastIssueDetails | None = None
    main_resource_url: str
    MANIFEST = "Manifest"
    META_TAG_ALLOW_LIST_INVALID_ORIGIN = "MetaTagAllowListInvalidOrigin"
    META_TAG_MODIFIED_HTML = "MetaTagModifiedHTML"
    MISSING_SIGNATURE_HEADER = "MissingSignatureHeader"
    MISSING_SIGNATURE_INPUT_HEADER = "MissingSignatureInputHeader"
    MISSING_TRANSIENT_USER_ACTIVATION = "MissingTransientUserActivation"
    MIXED_CONTENT_AUTOMATICALLY_UPGRADED = "MixedContentAutomaticallyUpgraded"
    MIXED_CONTENT_BLOCKED = "MixedContentBlocked"
    MIXED_CONTENT_ISSUE = "MixedContentIssue"
    mixed_content_issue_details: MixedContentIssueDetails | None = None
    MIXED_CONTENT_WARNING = "MixedContentWarning"
    name: str
    NAVIGATION_REGISTRATION_UNIQUE_SCOPE_ALREADY_SET = (
    NAVIGATION_REGISTRATION_WITHOUT_TRANSIENT_USER_ACTIVATION = (
    NAVIGATOR_USER_AGENT_ISSUE = "NavigatorUserAgentIssue"
    navigator_user_agent_issue_details: None | (NavigatorUserAgentIssueDetails) = None
    NETWORK_TOTAL_LIMIT = "NetworkTotalLimit"
    NO_ACCOUNT_SHARING_PERMISSION = "NoAccountSharingPermission"
    NO_API_PERMISSION = "NoApiPermission"
    NO_REGISTER_OS_SOURCE_HEADER = "NoRegisterOsSourceHeader"
    NO_REGISTER_OS_TRIGGER_HEADER = "NoRegisterOsTriggerHeader"
    NO_REGISTER_SOURCE_HEADER = "NoRegisterSourceHeader"
    NO_REGISTER_TRIGGER_HEADER = "NoRegisterTriggerHeader"
    NO_RETURNING_USER_FROM_FETCHED_ACCOUNTS = "NoReturningUserFromFetchedAccounts"
    NO_WEB_OR_OS_SUPPORT = "NoWebOrOsSupport"
    node_id: dom.BackendNodeId
    NON_PHRASING_CONTENT_OPTION_CHILD = "NonPhrasingContentOptionChild"
    NOT_IFRAME = "NotIframe"
    NOT_POTENTIALLY_TRUSTWORTHY = "NotPotentiallyTrustworthy"
    NOT_SAME_ORIGIN = "NotSameOrigin"
    NOT_SIGNED_IN_WITH_IDP = "NotSignedInWithIdp"
    Note that in this context 'site' means eTLD+1. For example, if the URL
    operation: CookieOperation
    opt_out_percentage: float
    optional fields in InspectorIssueDetails to convey more specific
    or Limited Quirks Mode that affects page layouting.
    OS_SOURCE_IGNORED = "OsSourceIgnored"
    OS_TRIGGER_IGNORED = "OsTriggerIgnored"
    params: T_JSON_DICT = dict()
    params["encoding"] = encoding
    params["requestId"] = request_id.to_json()
    parent_frame: AffectedFrame | None = None
    partitioning_blob_url_info: PartitioningBlobURLInfo
    PARTITIONING_BLOB_URL_ISSUE = "PartitioningBlobURLIssue"
    partitioning_blob_url_issue_details: None | (PartitioningBlobURLIssueDetails) = None
    path: str
    PERMISSION_POLICY_DISABLED = "PermissionPolicyDisabled"
    PING = "Ping"
    PLUGIN_DATA = "PluginData"
    PLUGIN_RESOURCE = "PluginResource"
    PREFETCH = "Prefetch"
    PROPERTY_RULE_ISSUE = "PropertyRuleIssue"
    property_rule_issue_details: PropertyRuleIssueDetails | None = None
    property_rule_issue_reason: PropertyRuleIssueReason
    property_value: str | None = None
    quality: float | None = None,
    QUIRKS_MODE_ISSUE = "QuirksModeIssue"
    quirks_mode_issue_details: QuirksModeIssueDetails | None = None
    raw_cookie_line: str | None = None
    READ_COOKIE = "ReadCookie"
    reason: BlockedByResponseReason
    reason: HeavyAdReason
    receive a user interaction. Note that in this context 'site' means eTLD+1.
    redirect chain, the site reported would be ``example.test``.
    refinements of the net error BLOCKED_BY_RESPONSE.
    registrations being ignored.
    RELYING_PARTY_ORIGIN_IS_OPAQUE = "RelyingPartyOriginIsOpaque"
    REPLACED_BY_ACTIVE_MODE = "ReplacedByActiveMode"
    report_aaa: bool | None = None,
    Represents the category of insight that a cookie issue falls under.
    Represents the failure reason when a federated authentication reason fails.
    Represents the failure reason when a getUserInfo() call fails.
    request: AffectedRequest
    request: AffectedRequest | None = None
    REQUEST_FAILED = "RequestFailed"
    request_id: network.RequestId | None = None
    request_id: network.RequestId,
    resolution: HeavyAdResolutionStatus
    resolution_status: MixedContentResolutionStatus
    RESOURCE = "Resource"
    resource_ip_address_space: network.IPAddressSpace | None = None
    resource_type: MixedContentResourceType | None = None
    RESPONSE_WAS_BLOCKED_BY_ORB = "ResponseWasBlockedByORB"
    return (
    return [GenericIssueDetails.from_json(i) for i in json["formIssues"]]
    Returns the response body and size if it were re-encoded with the specified settings. Only
    RP_PAGE_NOT_VISIBLE = "RpPageNotVisible"
    Runs the contrast check for the target page. Found issues are reported
    Runs the form issues check for the target page. Found issues are reported
    SCRIPT = "Script"
    script_id: runtime.ScriptId | None = None
    SELECT_ELEMENT_ACCESSIBILITY_ISSUE = "SelectElementAccessibilityIssue"
    select_element_accessibility_issue_details: None | (
    select_element_accessibility_issue_reason: SelectElementAccessibilityIssueReason
    SERVICE_WORKER = "ServiceWorker"
    SET_COOKIE = "SetCookie"
    SHARED_ARRAY_BUFFER_ISSUE = "SharedArrayBufferIssue"
    shared_array_buffer_issue_details: None | (SharedArrayBufferIssueDetails) = None
    shared_dictionary_error: SharedDictionaryError
    SHARED_DICTIONARY_ISSUE = "SharedDictionaryIssue"
    shared_dictionary_issue_details: SharedDictionaryIssueDetails | None = None
    SHARED_WORKER = "SharedWorker"
    Should be updated alongside FederatedAuthUserInfoRequestResult in
    Should be updated alongside RequestIdTokenStatus in
    SHOULD_EMBARGO = "ShouldEmbargo"
    signature_base: str
    SIGNATURE_HEADER_VALUE_IS_INCORRECT_LENGTH = "SignatureHeaderValueIsIncorrectLength"
    SIGNATURE_HEADER_VALUE_IS_NOT_BYTE_SEQUENCE = (
    SIGNATURE_HEADER_VALUE_IS_PARAMETERIZED = "SignatureHeaderValueIsParameterized"
    SIGNATURE_INPUT_HEADER_INVALID_COMPONENT_NAME = (
    SIGNATURE_INPUT_HEADER_INVALID_COMPONENT_TYPE = (
    SIGNATURE_INPUT_HEADER_INVALID_DERIVED_COMPONENT_PARAMETER = (
    SIGNATURE_INPUT_HEADER_INVALID_HEADER_COMPONENT_PARAMETER = (
    SIGNATURE_INPUT_HEADER_INVALID_PARAMETER = "SignatureInputHeaderInvalidParameter"
    SIGNATURE_INPUT_HEADER_KEY_ID_LENGTH = "SignatureInputHeaderKeyIdLength"
    SIGNATURE_INPUT_HEADER_MISSING_LABEL = "SignatureInputHeaderMissingLabel"
    SIGNATURE_INPUT_HEADER_MISSING_REQUIRED_PARAMETERS = (
    SIGNATURE_INPUT_HEADER_VALUE_MISSING_COMPONENTS = (
    SIGNATURE_INPUT_HEADER_VALUE_NOT_INNER_LIST = (
    SILENT_MEDIATION_FAILURE = "SilentMediationFailure"
    site_for_cookies: str | None = None
    size_only: bool | None = None,
    some CSP errors in the future.
    SOURCE_AND_TRIGGER_HEADERS = "SourceAndTriggerHeaders"
    source_code_location: SourceCodeLocation
    source_code_location: SourceCodeLocation | None = None
    SOURCE_IGNORED = "SourceIgnored"
    specific to the kind of issue. When adding a new issue code, please also
    SPECULATION_RULES = "SpeculationRules"
    SRI_MESSAGE_SIGNATURE_ISSUE = "SRIMessageSignatureIssue"
    sri_message_signature_issue_details: None | (SRIMessageSignatureIssueDetails) = None
    SRI_MESSAGE_SIGNATURE_MISMATCH = "SRIMessageSignatureMismatch"
    style_sheet_loading_issue_reason: StyleSheetLoadingIssueReason
    STYLESHEET = "Stylesheet"
    STYLESHEET_LOADING_ISSUE = "StylesheetLoadingIssue"
    stylesheet_loading_issue_details: StylesheetLoadingIssueDetails | None = None
    SUPPRESSED_BY_SEGMENTATION_PLATFORM = "SuppressedBySegmentationPlatform"
    table_entry_url: str | None = None
    that may be flagged as trackers and have their state cleared if they don't
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    third_party/blink/public/mojom/devtools/inspector_issue.mojom.
    THIRD_PARTY_COOKIES_BLOCKED = "ThirdPartyCookiesBlocked"
    This information is currently necessary, as the front-end has a difficult
    This issue tracks client hints related issues. It's used to deprecate old
    This issue tracks information needed to print a deprecation message.
    This issue warns about errors in property rules that lead to property
    This issue warns about errors in the select element content model.
    This issue warns about sites in the redirect chain of a finished navigation
    This issue warns about third-party sites that are accessing cookies on the
    This issue warns when a referenced stylesheet couldn't be loaded.
    This struct holds a list of optional fields with additional information
    threshold_aa: float
    threshold_aaa: float
    time finding a specific cookie. With this, we can convey specific error
    TOO_MANY_REQUESTS = "TooManyRequests"
    TRACK = "Track"
    tracking_sites: list[str]
    TRANSFER_ISSUE = "TransferIssue"
    transferred to a context that is not cross-origin isolated.
    TRIGGER_IGNORED = "TriggerIgnored"
    type_: InsightType
    type_: SharedArrayBufferIssueType
    type_: str
    TYPE_NOT_MATCHING = "TypeNotMatching"
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[GenericIssueDetails]]
    UI_DISMISSED_NO_EMBARGO = "UiDismissedNoEmbargo"
    UNTRUSTWORTHY_REPORTING_ORIGIN = "UntrustworthyReportingOrigin"
    url: str
    USE_ERROR_CROSS_ORIGIN_NO_CORS_REQUEST = "UseErrorCrossOriginNoCorsRequest"
    USE_ERROR_DICTIONARY_LOAD_FAILURE = "UseErrorDictionaryLoadFailure"
    USE_ERROR_MATCHING_DICTIONARY_NOT_USED = "UseErrorMatchingDictionaryNotUsed"
    USE_ERROR_UNEXPECTED_CONTENT_DICTIONARY_HEADER = (
    using Audits.issueAdded event.
    VALIDATION_FAILED_INTEGRITY_MISMATCH = "ValidationFailedIntegrityMismatch"
    VALIDATION_FAILED_INVALID_LENGTH = "ValidationFailedInvalidLength"
    VALIDATION_FAILED_SIGNATURE_EXPIRED = "ValidationFailedSignatureExpired"
    VALIDATION_FAILED_SIGNATURE_MISMATCH = "ValidationFailedSignatureMismatch"
    VIDEO = "Video"
    violated_directive: str
    violating_node_attribute: str | None = None
    violating_node_id: dom.BackendNodeId
    violating_node_id: dom.BackendNodeId | None = None
    violating_node_selector: str
    violation_type: AttributionReportingIssueType
    WARN_ATTRIBUTE_VALUE_EXCEEDS_MAX_SIZE = "WarnAttributeValueExceedsMaxSize"
    WARN_CROSS_SITE_REDIRECT_DOWNGRADE_CHANGES_INCLUSION = (
    WARN_DEPRECATION_TRIAL_METADATA = "WarnDeprecationTrialMetadata"
    WARN_DOMAIN_NON_ASCII = "WarnDomainNonASCII"
    WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_LAX = "WarnSameSiteLaxCrossDowngradeLax"
    WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_STRICT = "WarnSameSiteLaxCrossDowngradeStrict"
    WARN_SAME_SITE_NONE_INSECURE = "WarnSameSiteNoneInsecure"
    WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_LAX = "WarnSameSiteStrictCrossDowngradeLax"
    WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_STRICT = (
    WARN_SAME_SITE_STRICT_LAX_DOWNGRADE_STRICT = "WarnSameSiteStrictLaxDowngradeStrict"
    WARN_SAME_SITE_UNSPECIFIED_CROSS_SITE_CONTEXT = (
    WARN_SAME_SITE_UNSPECIFIED_LAX_ALLOW_UNSAFE = (
    WARN_THIRD_PARTY_COOKIE_HEURISTIC = "WarnThirdPartyCookieHeuristic"
    WARN_THIRD_PARTY_PHASEOUT = "WarnThirdPartyPhaseout"
    WEB_AND_OS_HEADERS = "WebAndOsHeaders"
    WELL_KNOWN_HTTP_NOT_FOUND = "WellKnownHttpNotFound"
    WELL_KNOWN_INVALID_CONTENT_TYPE = "WellKnownInvalidContentType"
    WELL_KNOWN_INVALID_RESPONSE = "WellKnownInvalidResponse"
    WELL_KNOWN_LIST_EMPTY = "WellKnownListEmpty"
    WELL_KNOWN_NO_RESPONSE = "WellKnownNoResponse"
    WELL_KNOWN_TOO_BIG = "WellKnownTooBig"
    WORKER = "Worker"
    would be ``example.test``.
    WRITE_ERROR_COSS_ORIGIN_NO_CORS_REQUEST = "WriteErrorCossOriginNoCorsRequest"
    WRITE_ERROR_DISALLOWED_BY_SETTINGS = "WriteErrorDisallowedBySettings"
    WRITE_ERROR_EXPIRED_RESPONSE = "WriteErrorExpiredResponse"
    WRITE_ERROR_FEATURE_DISABLED = "WriteErrorFeatureDisabled"
    WRITE_ERROR_INSUFFICIENT_RESOURCES = "WriteErrorInsufficientResources"
    WRITE_ERROR_INVALID_MATCH_FIELD = "WriteErrorInvalidMatchField"
    WRITE_ERROR_INVALID_STRUCTURED_HEADER = "WriteErrorInvalidStructuredHeader"
    WRITE_ERROR_NAVIGATION_REQUEST = "WriteErrorNavigationRequest"
    WRITE_ERROR_NO_MATCH_FIELD = "WriteErrorNoMatchField"
    WRITE_ERROR_NON_LIST_MATCH_DEST_FIELD = "WriteErrorNonListMatchDestField"
    WRITE_ERROR_NON_SECURE_CONTEXT = "WriteErrorNonSecureContext"
    WRITE_ERROR_NON_STRING_ID_FIELD = "WriteErrorNonStringIdField"
    WRITE_ERROR_NON_STRING_IN_MATCH_DEST_LIST = "WriteErrorNonStringInMatchDestList"
    WRITE_ERROR_NON_STRING_MATCH_FIELD = "WriteErrorNonStringMatchField"
    WRITE_ERROR_NON_TOKEN_TYPE_FIELD = "WriteErrorNonTokenTypeField"
    WRITE_ERROR_REQUEST_ABORTED = "WriteErrorRequestAborted"
    WRITE_ERROR_SHUTTING_DOWN = "WriteErrorShuttingDown"
    WRITE_ERROR_TOO_LONG_ID_FIELD = "WriteErrorTooLongIdField"
    WRITE_ERROR_UNSUPPORTED_TYPE = "WriteErrorUnsupportedType"
    XML_HTTP_REQUEST = "XMLHttpRequest"
    XSLT = "XSLT"
#
# CDP domain: Audits (experimental)
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[str | None, int, int]]:
):
@dataclass
@event_class("Audits.issueAdded")
class AffectedCookie:
class AffectedFrame:
class AffectedRequest:
class AttributionReportingIssueDetails:
class AttributionReportingIssueType:
class BlockedByResponseIssueDetails:
class BlockedByResponseReason:
class BounceTrackingIssueDetails:
class ClientHintIssueDetails:
class ClientHintIssueReason:
class ContentSecurityPolicyIssueDetails:
class ContentSecurityPolicyViolationType:
class CookieDeprecationMetadataIssueDetails:
class CookieExclusionReason:
class CookieIssueDetails:
class CookieIssueInsight:
class CookieOperation:
class CookieWarningReason:
class CorsIssueDetails:
class DeprecationIssueDetails:
class FailedRequestInfo:
class FederatedAuthRequestIssueDetails:
class FederatedAuthRequestIssueReason:
class FederatedAuthUserInfoRequestIssueDetails:
class FederatedAuthUserInfoRequestIssueReason:
class GenericIssueDetails:
class GenericIssueErrorType:
class HeavyAdIssueDetails:
class HeavyAdReason:
class HeavyAdResolutionStatus:
class InsightType:
class InspectorIssue:
class InspectorIssueCode:
class InspectorIssueDetails:
class IssueAdded:
class IssueId:
class LowTextContrastIssueDetails:
class MixedContentIssueDetails:
class MixedContentResolutionStatus:
class MixedContentResourceType:
class NavigatorUserAgentIssueDetails:
class PartitioningBlobURLInfo:
class PartitioningBlobURLIssueDetails:
class PropertyRuleIssueDetails:
class PropertyRuleIssueReason:
class QuirksModeIssueDetails:
class SelectElementAccessibilityIssueDetails:
class SelectElementAccessibilityIssueReason:
class SharedArrayBufferIssueDetails:
class SharedArrayBufferIssueType:
class SharedDictionaryError:
class SharedDictionaryIssueDetails:
class SourceCodeLocation:
class SRIMessageSignatureError:
class SRIMessageSignatureIssueDetails:
class StylesheetLoadingIssueDetails:
class StyleSheetLoadingIssueReason:
def check_contrast(
def check_forms_issues() -> (
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def get_encoded_response(
from . import dom
from . import network
from . import page
from . import runtime
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing
