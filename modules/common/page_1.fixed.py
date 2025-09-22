
json["notRestoredExplanationsTree"]
                )
                [AdFrameExplanation.from_json(i) for i in json["explanations"]]
                [BackForwardCacheBlockingDetails.from_json(
                    i) for i in json["details"]]
                [FileFilter.from_json(i) for i in json["accepts"]]
                [FileFilter.from_json(i) for i in json["files"]]
                [FileHandler.from_json(i) for i in json["fileHandlers"]]
                [FrameResourceTree.from_json(i) for i in json["childFrames"]]
                [FrameTree.from_json(i) for i in json["childFrames"]]
                [ImageResource.from_json(i) for i in json["icons"]]
                [ProtocolHandler.from_json(i)
                                           for i in json["protocolHandlers"]]
                [RelatedApplication.from_json(i)
                                              for i in json["relatedApplications"]]
                [ScopeExtension.from_json(i) for i in json["scopeExtensions"]]
                [Screenshot.from_json(i) for i in json["screenshots"]]
                [Shortcut.from_json(i) for i in json["shortcuts"]]
                [str(i) for i in json["displayOverrides"]]
                AdFrameStatus.from_json(json["adFrameStatus"])
                BackForwardCacheNotRestoredExplanation.from_json(i)
                BackForwardCacheNotRestoredExplanationTree.from_json(
                BackForwardCacheNotRestoredExplanationTree.from_json(i)
                bool(json["preferRelatedApplications"])
                dom.BackendNodeId.from_json(json["backendNodeId"])
                else None
                for i in json["children"]
                for i in json["explanations"]
                for i in json["notRestoredExplanations"]
                for i in json["tokensWithStatus"]
                FrameId.from_json(
    json["parentId"]) if "parentId" in json else None
                GatedAPIFeatures.from_json(i) for i in json["gatedAPIFeatures"]
                i.to_json() for i in self.related_applications
                if "accepts" in json
                if "adFrameStatus" in json
                if "backendNodeId" in json
                if "childFrames" in json
                if "details" in json
                if "displayOverrides" in json
                if "explanations" in json
                if "fileHandlers" in json
                if "files" in json
                if "icons" in json
                if "lastModified" in json
                if "launchHandler" in json
                if "locator" in json
                if "notRestoredExplanationsTree" in json
                if "parsedToken" in json
                if "preferRelatedApplications" in json
                if "protocolHandlers" in json
                if "relatedApplications" in json
                if "scopeExtensions" in json
                if "screenshots" in json
                if "securityOriginDetails" in json
                if "shareTarget" in json
                if "shortcuts" in json
                if "timestamp" in json
                InstallabilityErrorArgument.from_json(i) for i in json["errorArguments"]
                json["crossOriginIsolatedContextType"]
                json["usageRestriction"]
                LaunchHandler.from_json(json["launchHandler"])
                network.TimeSinceEpoch.from_json(json["lastModified"])
                network.TimeSinceEpoch.from_json(json["timestamp"])
                OriginTrialToken.from_json(json["parsedToken"])
                OriginTrialTokenWithStatus.from_json(i)
                PermissionsPolicyBlockLocator.from_json(json["locator"])
                runtime.StackTrace.from_json(
    json["stack"]) if "stack" in json else None
                SecurityOriginDetails.from_json(json["securityOriginDetails"])
                ShareTarget.from_json(json["shareTarget"])
                str(json["backgroundColor"]
                    ) if "backgroundColor" in json else None
                str(json["defaultPrompt"]) if "defaultPrompt" in json else None
                str(json["unreachableUrl"]
                    ) if "unreachableUrl" in json else None
            ),
            ]
            ],
            accepts=(
            accepts=[str(i) for i in json["accepts"]] if "accepts" in json else None,
            action=str(json["action"]),
            ad_frame_status=(
            ad_frame_type=AdFrameType.from_json(json["adFrameType"]),
            allowed=bool(json["allowed"]),
            AppManifestParsedProperties.from_json(json["parsed"])
            backend_node_id=(
            background_color=(
            block_reason=PermissionsPolicyBlockReason.from_json(json["blockReason"]),
            canceled=bool(json["canceled"]) if "canceled" in json else None,
            child_frames=(
            children=[
            client_height=float(json["clientHeight"]),
            client_height=int(json["clientHeight"]),
            client_mode=str(json["clientMode"]),
            client_width=float(json["clientWidth"]),
            client_width=int(json["clientWidth"]),
            column_number=int(json["columnNumber"]),
            column=int(json["column"]),
            content_size=float(json["contentSize"]) if "contentSize" in json else None,
            context=str(json["context"]) if "context" in json else None,
            critical=int(json["critical"]),
            cross_origin_isolated_context_type=CrossOriginIsolatedContextType.from_json(
            cursive=str(json["cursive"]) if "cursive" in json else None,
            data=str(json["data"]),
            debugger_id=runtime.UniqueDebuggerId.from_json(json["debuggerId"]),
            default_prompt=(
            delay=float(json["delay"]),
            description=str(json["description"]) if "description" in json else None,
            details=(
            device_height=float(json["deviceHeight"]),
            device_width=float(json["deviceWidth"]),
            dir_=str(json["dir"]) if "dir" in json else None,
            display_overrides=(
            display=str(json["display"]) if "display" in json else None,
            disposition=ClientNavigationDisposition.from_json(json["disposition"]),
            domain_and_registry=str(json["domainAndRegistry"]),
            eager=bool(json["eager"]) if "eager" in json else None,
            else None
            enctype=str(json["enctype"]),
            error_arguments=[
            error_id=str(json["errorId"]),
            expiry_time=network.TimeSinceEpoch.from_json(json["expiryTime"]),
            explanations=(
            explanations=[
            failed=bool(json["failed"]) if "failed" in json else None,
            fantasy=str(json["fantasy"]) if "fantasy" in json else None,
            feature=PermissionsPolicyFeature.from_json(json["feature"]),
            file_handlers=(
            files=(
            fixed=int(json["fixed"]) if "fixed" in json else None,
            fixed=str(json["fixed"]) if "fixed" in json else None,
            font_families=FontFamilies.from_json(json["fontFamilies"]),
            form_factor=str(json["formFactor"]),
            frame_id=FrameId.from_json(json["frameId"]),
            frame_id=FrameId.from_json(json["frameId"]), reason=str(json["reason"])
            frame=Frame.from_json(json["frame"]),
            function=str(json["function"]) if "function" in json else None,
            gated_api_features=[
            guid=str(json["guid"]),
            has_browser_handler=bool(json["hasBrowserHandler"]),
            has_origin_wildcard=bool(json["hasOriginWildcard"]),
            height=float(json["height"]),
            icons=(
            id_=FrameId.from_json(json["id"]),
            id_=int(json["id"]),
            id_=str(json["id"]) if "id" in json else None,
            if "parsed" in json
            image=ImageResource.from_json(json["image"]),
            is_localhost=bool(json["isLocalhost"]),
            is_third_party=bool(json["isThirdParty"]),
            json["accepts"] = [i for i in self.accepts]
            json["accepts"] = [i.to_json() for i in self.accepts]
            json["adFrameStatus"] = self.ad_frame_status.to_json()
            json["backgroundColor"] = self.background_color
            json["canceled"] = self.canceled
            json["childFrames"] = [i.to_json() for i in self.child_frames]
            json["contentSize"] = self.content_size
            json["context"] = self.context
            json["cursive"] = self.cursive
            json["description"] = self.description
            json["details"] = [i.to_json() for i in self.details]
            json["dir"] = self.dir_
            json["display"] = self.display
            json["displayOverrides"] = [i for i in self.display_overrides]
            json["eager"] = self.eager
            json["explanations"] = [i.to_json() for i in self.explanations]
            json["failed"] = self.failed
            json["fantasy"] = self.fantasy
            json["fileHandlers"] = [i.to_json() for i in self.file_handlers]
            json["files"] = [i.to_json() for i in self.files]
            json["fixed"] = self.fixed
            json["function"] = self.function
            json["icons"] = [i.to_json() for i in self.icons]
            json["id"] = self.id_
            json["label"] = self.label
            json["lang"] = self.lang
            json["lastModified"] = self.last_modified.to_json()
            json["launchHandler"] = self.launch_handler.to_json()
            json["locator"] = self.locator.to_json()
            json["math"] = self.math
            json["name"] = self.name
            json["orientation"] = self.orientation
            json["parentId"] = self.parent_id.to_json()
            json["parsedToken"] = self.parsed_token.to_json()
            json["preferRelatedApplications"] = self.prefer_related_applications
            json["protocolHandlers"] = [i.to_json() for i in self.protocol_handlers]
            json["relatedApplications"] = [
            json["sansSerif"] = self.sans_serif
            json["scope"] = self.scope
            json["scopeExtensions"] = [i.to_json() for i in self.scope_extensions]
            json["screenshots"] = [i.to_json() for i in self.screenshots]
            json["securityOriginDetails"] = self.security_origin_details.to_json()
            json["serif"] = self.serif
            json["shareTarget"] = self.share_target.to_json()
            json["shortcuts"] = [i.to_json() for i in self.shortcuts]
            json["shortName"] = self.short_name
            json["sizes"] = self.sizes
            json["standard"] = self.standard
            json["startUrl"] = self.start_url
            json["text"] = self.text
            json["themeColor"] = self.theme_color
            json["timestamp"] = self.timestamp.to_json()
            json["title"] = self.title
            json["type"] = self.type_
            json["unreachableUrl"] = self.unreachable_url
            json["url"] = self.url
            json["urlFragment"] = self.url_fragment
            json["zoom"] = self.zoom
            label=str(json["label"]) if "label" in json else None,
            lang=str(json["lang"]) if "lang" in json else None,
            last_modified=(
            launch_handler=(
            launch_type=str(json["launchType"]),
            line_number=int(json["lineNumber"]),
            line=int(json["line"]),
            loader_id=network.LoaderId.from_json(json["loaderId"]),
            locator=(
            match_sub_domains=bool(json["matchSubDomains"]),
            math=str(json["math"]) if "math" in json else None,
            message=str(json["message"]),
            metadata=ScreencastFrameMetadata.from_json(json["metadata"]),
            method=str(json["method"]),
            mime_type=str(json["mimeType"]),
            mode=str(json["mode"]),
            name=str(json["name"]) if "name" in json else None,
            name=str(json["name"]),
            navigation_type=str(json["navigationType"]),
            not_restored_explanations_tree=(
            not_restored_explanations=[
            offset_top=float(json["offsetTop"]),
            offset_x=float(json["offsetX"]),
            offset_y=float(json["offsetY"]),
            orientation=str(json["orientation"]) if "orientation" in json else None,
            origin=str(json["origin"]),
            page_scale_factor=float(json["pageScaleFactor"]),
            page_x=float(json["pageX"]),
            page_x=int(json["pageX"]),
            page_y=float(json["pageY"]),
            page_y=int(json["pageY"]),
            parent_frame_id=FrameId.from_json(json["parentFrameId"]),
            parent_id=(
            parsed_token=(
            prefer_related_applications=(
            protocol_handlers=(
            protocol=str(json["protocol"]),
            raw_token_text=str(json["rawTokenText"]),
            reason=BackForwardCacheNotRestoredReason.from_json(json["reason"]),
            reason=ClientNavigationReason.from_json(json["reason"]),
            received_bytes=float(json["receivedBytes"]),
            related_applications=(
            resources=[FrameResource.from_json(i) for i in json["resources"]],
            sans_serif=str(json["sansSerif"]) if "sansSerif" in json else None,
            scale=float(json["scale"]),
            scope_extensions=(
            scope=str(json["scope"]) if "scope" in json else None,
            scope=str(json["scope"]),
            screenshots=(
            script_id=runtime.ScriptId.from_json(json["scriptId"]),
            script=str(json["script"]),
            scroll_offset_x=float(json["scrollOffsetX"]),
            scroll_offset_y=float(json["scrollOffsetY"]),
            secure_context_type=SecureContextType.from_json(json["secureContextType"]),
            security_origin_details=(
            security_origin=str(json["securityOrigin"]),
            self.cross_origin_isolated_context_type.to_json()
            serif=str(json["serif"]) if "serif" in json else None,
            session_id=int(json["sessionId"]),
            share_target=(
            short_name=str(json["shortName"]) if "shortName" in json else None,
            shortcuts=(
            sizes=str(json["sizes"]) if "sizes" in json else None,
            stack=(
            standard=int(json["standard"]) if "standard" in json else None,
            standard=str(json["standard"]) if "standard" in json else None,
            start_url=str(json["startUrl"]) if "startUrl" in json else None,
            state=str(json["state"]),
            status=OriginTrialStatus.from_json(json["status"]),
            status=OriginTrialTokenStatus.from_json(json["status"]),
            suggested_filename=str(json["suggestedFilename"]),
            text=str(json["text"]) if "text" in json else None,
            theme_color=str(json["themeColor"]) if "themeColor" in json else None,
            timestamp=(
            timestamp=network.MonotonicTime.from_json(json["timestamp"]),
            title=str(json["title"]) if "title" in json else None,
            title=str(json["title"]),
            tokens_with_status=[
            total_bytes=float(json["totalBytes"]),
            transition_type=TransitionType.from_json(json["transitionType"]),
            trial_name=str(json["trialName"]),
            type_=BackForwardCacheNotRestoredReasonType.from_json(json["type"]),
            type_=DialogType.from_json(json["type"]),
            type_=NavigationType.from_json(json["type"]),
            type_=network.ResourceType.from_json(json["type"]),
            type_=str(json["type"]) if "type" in json else None,
            unreachable_url=(
            url_fragment=str(json["urlFragment"]) if "urlFragment" in json else None,
            url=str(json["url"]) if "url" in json else None,
            url=str(json["url"]),
            usage_restriction=OriginTrialUsageRestriction.from_json(
            user_gesture=bool(json["userGesture"]),
            user_typed_url=str(json["userTypedURL"]),
            value=str(json["value"]),
            width=float(json["width"]),
            window_features=[str(i) for i in json["windowFeatures"]],
            window_name=str(json["windowName"]),
            x=float(json["x"]),
            y=float(json["y"]),
            zoom=float(json["zoom"]) if "zoom" in json else None,
        "ActivationNavigationsDisallowedForBug1234857"
        "BackForwardCacheDisabledByCommandLine"
        "CacheControlNoStoreDeviceBoundSessionTerminated"
        "CacheControlNoStoreHTTPOnlyCookieModified"
        "EmbedderChromePasswordManagerClientBindCredentialManager"
        "EmbedderDomDistillerSelfDeletingRequestDelegate"
        "EmbedderExtensionSentMessageToCachedFrame"
        "EmbedderSafeBrowsingTriggeredPopupBlocker"
        "EnteredBackForwardCacheBeforeServiceWorkerHostAdded"
        "JsNetworkRequestReceivedCacheControlNoStoreResource"
        "method": "Page.addCompilationCache",
        "method": "Page.addScriptToEvaluateOnLoad",
        "method": "Page.addScriptToEvaluateOnNewDocument",
        "method": "Page.bringToFront",
        "method": "Page.captureScreenshot",
        "method": "Page.captureSnapshot",
        "method": "Page.clearCompilationCache",
        "method": "Page.clearDeviceMetricsOverride",
        "method": "Page.clearDeviceOrientationOverride",
        "method": "Page.clearGeolocationOverride",
        "method": "Page.close",
        "method": "Page.crash",
        "method": "Page.createIsolatedWorld",
        "method": "Page.deleteCookie",
        "method": "Page.disable",
        "method": "Page.enable",
        "method": "Page.generateTestReport",
        "method": "Page.getAdScriptId",
        "method": "Page.getAppId",
        "method": "Page.getAppManifest",
        "method": "Page.getFrameTree",
        "method": "Page.getInstallabilityErrors",
        "method": "Page.getLayoutMetrics",
        "method": "Page.getManifestIcons",
        "method": "Page.getNavigationHistory",
        "method": "Page.getOriginTrials",
        "method": "Page.getPermissionsPolicyState",
        "method": "Page.getResourceContent",
        "method": "Page.getResourceTree",
        "method": "Page.handleJavaScriptDialog",
        "method": "Page.navigate",
        "method": "Page.navigateToHistoryEntry",
        "method": "Page.printToPDF",
        "method": "Page.produceCompilationCache",
        "method": "Page.reload",
        "method": "Page.removeScriptToEvaluateOnLoad",
        "method": "Page.removeScriptToEvaluateOnNewDocument",
        "method": "Page.resetNavigationHistory",
        "method": "Page.screencastFrameAck",
        "method": "Page.searchInResource",
        "method": "Page.setAdBlockingEnabled",
        "method": "Page.setBypassCSP",
        "method": "Page.setDeviceMetricsOverride",
        "method": "Page.setDeviceOrientationOverride",
        "method": "Page.setDocumentContent",
        "method": "Page.setDownloadBehavior",
        "method": "Page.setFontFamilies",
        "method": "Page.setFontSizes",
        "method": "Page.setGeolocationOverride",
        "method": "Page.setInterceptFileChooserDialog",
        "method": "Page.setLifecycleEventsEnabled",
        "method": "Page.setPrerenderingAllowed",
        "method": "Page.setRPHRegistrationMode",
        "method": "Page.setSPCTransactionMode",
        "method": "Page.setTouchEmulationEnabled",
        "method": "Page.setWebLifecycleState",
        "method": "Page.startScreencast",
        "method": "Page.stopLoading",
        "method": "Page.stopScreencast",
        "method": "Page.waitForDebugger",
        "NetworkRequestDatapipeDrainedAsBytesConsumer"
        "params": params,
        "RequestedBackForwardCacheBlockedSensors"
        (
        )
        ),
        [AppManifestError.from_json(i) for i in json["errors"]],
        [NavigationEntry.from_json(i) for i in json["entries"]],
        0. **appId** - *(Optional)* App id, either from manifest's id attribute or computed from start_url
        0. **content** - Resource content.
        0. **currentIndex** - Index of the current navigation history entry.
        0. **data** - Base64-encoded pdf data. Empty if `` returnAsStream` is specified.
        0. **frameId** - Frame id that has navigated (or failed to navigate)
        0. **layoutViewport** - Deprecated metrics relating to the layout viewport. Is in device pixels. Use ``cssLayoutViewport`` instead.
        0. **url** - Manifest location.
        1. **base64Encoded** - True, if content was served as base64.
        1. **entries** - Array of navigation history entries.
        1. **errors** -
        1. **loaderId** - *(Optional)* Loader identifier. This is omitted in case of same-document navigation, as the previously committed loaderId would not change.
        1. **recommendedId** - *(Optional)* Recommendation for manifest's id attribute to match current id computed from start_url
        1. **stream** - *(Optional)* A handle of the stream that holds resulting PDF data.
        1. **visualViewport** - Deprecated metrics relating to the visual viewport. Is in device pixels. Use ``cssVisualViewport`` instead.
        2. **contentSize** - Deprecated size of scrollable area. Is in DP. Use ``cssContentSize`` instead.
        2. **data** - *(Optional)* Manifest content.
        2. **errorText** - *(Optional)* User friendly error message, present if and only if navigation has failed.
        3. **cssLayoutViewport** - Metrics relating to the layout viewport in CSS pixels.
        3. **parsed** - *(Optional)* Parsed manifest properties. Deprecated, use manifest instead.
        4. **cssVisualViewport** - Metrics relating to the visual viewport in CSS pixels.
        4. **manifest** -
        5. **cssContentSize** - Size of scrollable area in CSS pixels.
        AppManifestParsedProperties | None,
        current document, this API errors out.
        dom.Rect,
        dom.Rect.from_json(json["contentSize"]),
        dom.Rect.from_json(json["cssContentSize"]),
        FrameId.from_json(json["frameId"]),
        if self.accepts is not None:
        if self.ad_frame_status is not None:
        if self.background_color is not None:
        if self.canceled is not None:
        if self.child_frames is not None:
        if self.content_size is not None:
        if self.context is not None:
        if self.cursive is not None:
        if self.description is not None:
        if self.details is not None:
        if self.dir_ is not None:
        if self.display is not None:
        if self.display_overrides is not None:
        if self.eager is not None:
        if self.explanations is not None:
        if self.failed is not None:
        if self.fantasy is not None:
        if self.file_handlers is not None:
        if self.files is not None:
        if self.fixed is not None:
        if self.function is not None:
        if self.icons is not None:
        if self.id_ is not None:
        if self.label is not None:
        if self.lang is not None:
        if self.last_modified is not None:
        if self.launch_handler is not None:
        if self.locator is not None:
        if self.math is not None:
        if self.name is not None:
        if self.orientation is not None:
        if self.parent_id is not None:
        if self.parsed_token is not None:
        if self.prefer_related_applications is not None:
        if self.protocol_handlers is not None:
        if self.related_applications is not None:
        if self.sans_serif is not None:
        if self.scope is not None:
        if self.scope_extensions is not None:
        if self.screenshots is not None:
        if self.security_origin_details is not None:
        if self.serif is not None:
        if self.share_target is not None:
        if self.short_name is not None:
        if self.shortcuts is not None:
        if self.sizes is not None:
        if self.standard is not None:
        if self.start_url is not None:
        if self.text is not None:
        if self.theme_color is not None:
        if self.timestamp is not None:
        if self.title is not None:
        if self.type_ is not None:
        if self.unreachable_url is not None:
        if self.url is not None:
        if self.url_fragment is not None:
        if self.zoom is not None:
        int(json["currentIndex"]),
        io.StreamHandle.from_json(json["stream"]) if "stream" in json else None,
        json = dict()
        json["action"] = self.action
        json["adFrameType"] = self.ad_frame_type.to_json()
        json["allowed"] = self.allowed
        json["blockReason"] = self.block_reason.to_json()
        json["children"] = [i.to_json() for i in self.children]
        json["clientHeight"] = self.client_height
        json["clientMode"] = self.client_mode
        json["clientWidth"] = self.client_width
        json["column"] = self.column
        json["columnNumber"] = self.column_number
        json["critical"] = self.critical
        json["crossOriginIsolatedContextType"] = (
        json["debuggerId"] = self.debugger_id.to_json()
        json["deviceHeight"] = self.device_height
        json["deviceWidth"] = self.device_width
        json["domainAndRegistry"] = self.domain_and_registry
        json["enctype"] = self.enctype
        json["errorArguments"] = [i.to_json() for i in self.error_arguments]
        json["errorId"] = self.error_id
        json["expiryTime"] = self.expiry_time.to_json()
        json["explanations"] = [i.to_json() for i in self.explanations]
        json["feature"] = self.feature.to_json()
        json["fontFamilies"] = self.font_families.to_json()
        json["formFactor"] = self.form_factor
        json["frame"] = self.frame.to_json()
        json["frameId"] = self.frame_id.to_json()
        json["gatedAPIFeatures"] = [i.to_json() for i in self.gated_api_features]
        json["hasOriginWildcard"] = self.has_origin_wildcard
        json["height"] = self.height
        json["id"] = self.id_
        json["id"] = self.id_.to_json()
        json["image"] = self.image.to_json()
        json["isLocalhost"] = self.is_localhost
        json["isThirdParty"] = self.is_third_party
        json["launchType"] = self.launch_type
        json["line"] = self.line
        json["lineNumber"] = self.line_number
        json["loaderId"] = self.loader_id.to_json()
        json["matchSubDomains"] = self.match_sub_domains
        json["message"] = self.message
        json["method"] = self.method
        json["mimeType"] = self.mime_type
        json["name"] = self.name
        json["offsetTop"] = self.offset_top
        json["offsetX"] = self.offset_x
        json["offsetY"] = self.offset_y
        json["origin"] = self.origin
        json["pageScaleFactor"] = self.page_scale_factor
        json["pageX"] = self.page_x
        json["pageY"] = self.page_y
        json["protocol"] = self.protocol
        json["rawTokenText"] = self.raw_token_text
        json["reason"] = self.reason.to_json()
        json["resources"] = [i.to_json() for i in self.resources]
        json["scale"] = self.scale
        json["scope"] = self.scope
        json["script"] = self.script
        json["scriptId"] = self.script_id.to_json()
        json["scrollOffsetX"] = self.scroll_offset_x
        json["scrollOffsetY"] = self.scroll_offset_y
        json["secureContextType"] = self.secure_context_type.to_json()
        json["securityOrigin"] = self.security_origin
        json["status"] = self.status.to_json()
        json["title"] = self.title
        json["tokensWithStatus"] = [i.to_json() for i in self.tokens_with_status]
        json["transitionType"] = self.transition_type.to_json()
        json["trialName"] = self.trial_name
        json["type"] = self.type_.to_json()
        json["url"] = self.url
        json["usageRestriction"] = self.usage_restriction.to_json()
        json["userTypedURL"] = self.user_typed_url
        json["value"] = self.value
        json["width"] = self.width
        json["x"] = self.x
        json["y"] = self.y
        LayoutViewport,
        LayoutViewport.from_json(json["cssLayoutViewport"]),
        LayoutViewport.from_json(json["layoutViewport"]),
        list[AppManifestError],
        network.LoaderId.from_json(json["loaderId"]) if "loaderId" in json else None,
        params["accuracy"] = accuracy
        params["cancel"] = cancel
        params["captureBeyondViewport"] = capture_beyond_viewport
        params["caseSensitive"] = case_sensitive
        params["clip"] = clip.to_json()
        params["configuration"] = configuration
        params["displayHeaderFooter"] = display_header_footer
        params["dontSetVisibleSize"] = dont_set_visible_size
        params["downloadPath"] = download_path
        params["enableFileChooserOpenedEvent"] = enable_file_chooser_opened_event
        params["everyNthFrame"] = every_nth_frame
        params["footerTemplate"] = footer_template
        params["format"] = format_
        params["forScripts"] = [i.to_json() for i in for_scripts]
        params["frameId"] = frame_id.to_json()
        params["fromSurface"] = from_surface
        params["generateDocumentOutline"] = generate_document_outline
        params["generateTaggedPDF"] = generate_tagged_pdf
        params["grantUniveralAccess"] = grant_univeral_access
        params["group"] = group
        params["headerTemplate"] = header_template
        params["ignoreCache"] = ignore_cache
        params["includeCommandLineAPI"] = include_command_line_api
        params["isRegex"] = is_regex
        params["landscape"] = landscape
        params["latitude"] = latitude
        params["loaderId"] = loader_id.to_json()
        params["longitude"] = longitude
        params["manifestId"] = manifest_id
        params["marginBottom"] = margin_bottom
        params["marginLeft"] = margin_left
        params["marginRight"] = margin_right
        params["marginTop"] = margin_top
        params["maxHeight"] = max_height
        params["maxWidth"] = max_width
        params["optimizeForSpeed"] = optimize_for_speed
        params["pageRanges"] = page_ranges
        params["paperHeight"] = paper_height
        params["paperWidth"] = paper_width
        params["positionX"] = position_x
        params["positionY"] = position_y
        params["preferCSSPageSize"] = prefer_css_page_size
        params["printBackground"] = print_background
        params["promptText"] = prompt_text
        params["quality"] = quality
        params["referrer"] = referrer
        params["referrerPolicy"] = referrer_policy.to_json()
        params["runImmediately"] = run_immediately
        params["scale"] = scale
        params["screenHeight"] = screen_height
        params["screenOrientation"] = screen_orientation.to_json()
        params["screenWidth"] = screen_width
        params["scriptToEvaluateOnLoad"] = script_to_evaluate_on_load
        params["transferMode"] = transfer_mode
        params["transitionType"] = transition_type.to_json()
        params["viewport"] = viewport.to_json()
        params["worldName"] = world_name
        return "FrameId({})".format(super().__repr__())
        return "ScriptIdentifier({})".format(super().__repr__())
        return cls(
        return cls()
        return cls(frame_id=FrameId.from_json(json["frameId"]))
        return cls(frame=Frame.from_json(json["frame"]))
        return cls(json)
        return cls(result=bool(json["result"]), user_input=str(json["userInput"]))
        return cls(timestamp=network.MonotonicTime.from_json(json["timestamp"]))
        return cls(url=str(json["url"]), data=str(json["data"]))
        return cls(visible=bool(json["visible"]))
        return json
        return self
        return self.value
        str | None,
        str(json["appId"]) if "appId" in json else None,
        str(json["data"]) if "data" in json else None,
        str(json["data"]),
        str(json["errorText"]) if "errorText" in json else None,
        str(json["recommendedId"]) if "recommendedId" in json else None,
        str(json["url"]),
        str,
        VisualViewport,
        VisualViewport.from_json(json["cssVisualViewport"]),
        VisualViewport.from_json(json["visualViewport"]),
        WebAppManifest,
        WebAppManifest.from_json(json["manifest"]),
      If manifestId is provided, and it does not match the manifest of the
      If there is not a loaded page, this API errors out immediately.
      This API always waits for the manifest to be loaded.
    """
    #:               http://a.b.co.uk/file.html      -> "b.co.uk"
    #: - EmbedderExtensionSentMessageToCachedFrame: the extension ID.
    #: (the actual compilation mode used is upon backend discretion).
    #: ``parsedToken`` is present only when the token is extractable and
    #: 127.0.0.0/8 or IPv6 ::1).
    #: A hint to the backend whether eager compilation is recommended.
    #: Additional details about the frame document's security origin.
    #: An array of enabled window features.
    #: Argument name (e.g. name:'minimum-icon-size-in-pixels').
    #: Argument value (e.g. value:'64').
    #: Array of children frame
    #: Array of reasons why the page could not be cached. This must not be empty.
    #: as an ad.
    #: Base64-encoded compressed image.
    #: Base64-encoded data
    #: Child frames.
    #: Column number in the script (0-based).
    #: Computed scope value
    #: consistency.
    #: Context associated with the reason. The meaning of this context is
    #: Default dialog prompt.
    #: Default fixed font size.
    #: Default standard font size.
    #: Delay (in seconds) until the navigation is scheduled to begin. The navigation is not
    #: dependent on the reason:
    #: Device screen height in DIP.
    #: Device screen width in DIP.
    #: dialog handler for given target, calling alert while Page domain is engaged will stall
    #: Dialog type.
    #: Download status.
    #: Embed the ShareTargetParams
    #: Error column.
    #: Error line.
    #: Error message.
    #: Example URLs: http://www.google.com/file.html -> "google.com"
    #: experiment. See:
    #: Extracted from the Frame's url.
    #: for easy understanding and comparison.
    #: Frame document's mimeType as determined by the browser.
    #: Frame document's registered domain, taking the public suffixes list into account.
    #: Frame document's security origin.
    #: Frame document's URL fragment including the '#'.
    #: Frame document's URL without fragment.
    #: Frame information for this tree item.
    #: Frame number.
    #: Frame object.
    #: Frame swap timestamp.
    #: Frame unique identifier.
    #: Frame url.
    #: Frame's name as specified in the tag.
    #: Frame's new url.
    #: Function name where blockage happened. Optional because of anonymous functions and tests.
    #: Generic font families collection for the script.
    #: Global unique identifier of the download.
    #: guaranteed to start.
    #: Height (CSS pixels), excludes scrollbar if present.
    #: Horizontal offset relative to the document (CSS pixels).
    #: Horizontal offset relative to the layout viewport (CSS pixels).
    #: https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md
    #: https://github.com/WICG/web-app-launch/blob/main/launch_handler.md
    #: Id of adScriptId's debugger.
    #: Id of the frame containing input node.
    #: Id of the frame that caused download to begin.
    #: Id of the frame that has been attached.
    #: Id of the frame that has been detached.
    #: Id of the frame that has cleared its scheduled navigation.
    #: Id of the frame that has scheduled a navigation.
    #: Id of the frame that has started loading.
    #: Id of the frame that has stopped loading.
    #: ID of the frame that is being navigated.
    #: Id of the frame that is being navigated.
    #: Id of the frame that is the root of the subtree that will be detached.
    #: Id of the frame.
    #: Identifier of the loader associated with this frame.
    #: If critical, this is a non-recoverable parse error.
    #: If the frame failed to load, this contains the URL that could not be loaded. Note that unlike url above, this URL may contain a fragment.
    #: Indicated which gated APIs / features are available.
    #: Indicates whether the frame document's security origin is one
    #: Indicates whether the main document is a secure context and explains why that is the case.
    #: Indicates whether this frame was tagged as an ad and why.
    #: Indicates whether this is a cross origin isolated context.
    #: Information about frame resources.
    #: Input mode.
    #: Input node id. Only present for file choosers opened via an ``<input type="file">`` element.
    #: Instead of using tuple, this field always returns the serialized string
    #: JavaScript stack trace of when frame was attached, only set if frame initiated from script.
    #: last-modified timestamp as reported by server.
    #: Line number in the script (0-based).
    #: Loader identifier. Empty string if the request is fetched from worker.
    #: Loader identifier. Even though it is present in case of same-document
    #: Message that will be displayed by the dialog.
    #: Mimic a map, name is the key, accepts is the value.
    #: Name of the script which these font families are defined for.
    #: Navigation type
    #: navigation, the previously committed loaderId would not change unless
    #: navigation.
    #: Non-standard, see
    #: Not restored reason
    #: Not restored reasons of each frame
    #: of the local hostnames (e.g. "localhost") or IP addresses (IPv4
    #: other enums below.
    #: Page scale factor.
    #: Page zoom factor (CSS to device independent pixels ratio).
    #: Parent frame identifier.
    #: parsable.
    #: Position of horizontal scroll in CSS pixels.
    #: Position of vertical scroll in CSS pixels.
    #: Rectangle height in device independent pixels (dip).
    #: Rectangle width in device independent pixels (dip).
    #: Resource content size.
    #: Resource mimeType as determined by the browser.
    #: Resource URL.
    #: Scale relative to the ideal viewport (size at width=device-width).
    #: Screencast frame metadata.
    #: Script Id of the bottom-most script which caused the frame to be labelled
    #: Suggested file name of the resource (the actual name of the file saved on disk may differ).
    #: The cursive font-family.
    #: The destination URL for the requested navigation.
    #: The destination URL for the scheduled navigation.
    #: The disposition for the navigation.
    #: The error id (e.g. 'manifest-missing-suitable-icon').
    #: The extra description provided by the manifest.
    #: The fantasy font-family.
    #: The fixed font-family.
    #: The frame id of the associated frame.
    #: The handlers to open files.
    #: The handlers to open protocols.
    #: The list of error arguments (e.g. {name:'minimum-icon-size-in-pixels', value:'64'}).
    #: The loader id for the associated navigation.
    #: The math font-family.
    #: the navigation changes from a same-document to a cross-document
    #: The overrided display mode controlled by the user.
    #: the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.
    #: The reason for the navigation.
    #: The sansSerif font-family.
    #: The screenshots used by chromium.
    #: The serif font-family.
    #: The src field in the definition, but changing to url in favor of
    #: The standard font-family.
    #: The URL for the new window.
    #: The URL of the script to produce a compilation cache entry for.
    #: The URL the navigation started with. The final URL can be different.
    #: Title of the navigation history entry.
    #: TODO(crbug.com/1231886): This field is non-standard and part of a Chrome
    #: Top offset in DIP.
    #: Total bytes received.
    #: Total expected bytes to download.
    #: Transition type.
    #: Tree structure of reasons why the page could not be cached for each frame.
    #: True if the page is visible.
    #: True if the resource failed to load.
    #: True if the resource was canceled during loading.
    #: True iff browser is capable showing or acting on the given dialog. When browser has no
    #: Type of the reason
    #: Type of this resource.
    #: Unique id of the navigation history entry.
    #: URL of each frame
    #: Url of the file where blockage happened. Optional because of tests.
    #: URL of the navigation history entry.
    #: URL of the resource being downloaded.
    #: URL that the user typed in the url bar.
    #: User input in case of prompt.
    #: Vertical offset relative to the document (CSS pixels).
    #: Vertical offset relative to the layout viewport (CSS pixels).
    #: Whether dialog was confirmed.
    #: Whether or not it was triggered by user gesture.
    #: Width (CSS pixels), excludes scrollbar if present.
    #: Window name.
    #: Won't repeat the enums, using string for easy comparison. Same as the
    #: X offset in device independent pixels (dip).
    #: Y offset in device independent pixels (dip).
    )
    **EXPERIMENTAL**
    :param accept: Whether to accept or dismiss the dialog.
    :param accuracy: *(Optional)* Mock accuracy
    :param alpha: Mock alpha
    :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
    :param beta: Mock beta
    :param cancel: **(EXPERIMENTAL)** *(Optional)* If true, cancels the dialog by emitting relevant events (if any) in addition to not showing it if the interception is enabled (default: false).
    :param capture_beyond_viewport: **(EXPERIMENTAL)** *(Optional)* Capture the screenshot beyond the viewport. Defaults to false.
    :param case_sensitive: *(Optional)* If true, search is case sensitive.
    :param clip: *(Optional)* Capture the screenshot of a given region only.
    :param configuration: *(Optional)* Touch/gesture events configuration. Default: current platform.
    :param cookie_name: Name of the cookie to remove.
    :param data: Base64-encoded data
    :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
    :param display_header_footer: *(Optional)* Display header and footer. Defaults to false.
    :param dont_set_visible_size: *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
    :param download_path: *(Optional)* The default path to save downloaded files to. This is required if behavior is set to 'allow'
    :param enable_file_chooser_opened_event: **(EXPERIMENTAL)** *(Optional)* If true, the ```Page.fileChooserOpened```` event will be emitted regardless of the state set by ````Page.setInterceptFileChooserDialog``` command (default: false).
    :param enabled:
    :param enabled: If true, starts emitting lifecycle events.
    :param enabled: Whether the touch event emulation should be enabled.
    :param enabled: Whether to block ads.
    :param enabled: Whether to bypass page CSP.
    :param entry_id: Unique id of the entry to navigate to.
    :param every_nth_frame: *(Optional)* Send every n-th frame.
    :param font_families: Specifies font families to set. If a font family is not specified, it won't be changed.
    :param font_sizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
    :param footer_template: *(Optional)* HTML template for the print footer. Should use the same format as the ````headerTemplate````.
    :param for_scripts: *(Optional)* Specifies font families to set for individual scripts.
    :param format_: *(Optional)* Format (defaults to mhtml).
    :param format_: *(Optional)* Image compression format (defaults to png).
    :param format_: *(Optional)* Image compression format.
    :param frame_id:
    :param frame_id: *(Optional)* Frame id to navigate, if not specified navigates the top frame.
    :param frame_id: Frame id for resource to search in.
    :param frame_id: Frame id to get resource for.
    :param frame_id: Frame id to set HTML for.
    :param frame_id: Id of the frame in which the isolated world should be created.
    :param from_surface: **(EXPERIMENTAL)** *(Optional)* Capture the screenshot from the surface, rather than the view. Defaults to true.
    :param gamma: Mock gamma
    :param generate_document_outline: **(EXPERIMENTAL)** *(Optional)* Whether or not to embed the document outline into the PDF.
    :param generate_tagged_pdf: **(EXPERIMENTAL)** *(Optional)* Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice.
    :param grant_univeral_access: *(Optional)* Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
    :param group: *(Optional)* Specifies the endpoint group to deliver the report to.
    :param header_template: *(Optional)* HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - ```date````: formatted print date - ````title````: document title - ````url````: document location - ````pageNumber````: current page number - ````totalPages````: total pages in the document  For example, ````<span class=title></span>```` would generate span containing the title.
    :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param html: HTML content to set.
    :param identifier:
    :param ignore_cache: *(Optional)* If true, browser cache is ignored (as if the user pressed Shift+refresh).
    :param include_command_line_api: **(EXPERIMENTAL)** *(Optional)* Specifies whether command line API should be available to the script, defaults to false.
    :param is_allowed:
    :param is_regex: *(Optional)* If true, treats string parameter as regex.
    :param landscape: *(Optional)* Paper orientation. Defaults to false.
    :param latitude: *(Optional)* Mock latitude
    :param loader_id: **(EXPERIMENTAL)** *(Optional)* If set, an error will be thrown if the target page's main frame's loader id does not match the provided id. This prevents accidentally reloading an unintended target in case there's a racing navigation.
    :param longitude: *(Optional)* Mock longitude
    :param manifest_id: *(Optional)*
    :param margin_bottom: *(Optional)* Bottom margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_left: *(Optional)* Left margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_right: *(Optional)* Right margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_top: *(Optional)* Top margin in inches. Defaults to 1cm (~0.4 inches).
    :param max_height: *(Optional)* Maximum screenshot height.
    :param max_width: *(Optional)* Maximum screenshot width.
    :param message: Message to be displayed in the report.
    :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
    :param mode:
    :param optimize_for_speed: **(EXPERIMENTAL)** *(Optional)* Optimize image encoding for speed, not for resulting size (defaults to false)
    :param page_ranges: *(Optional)* Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are printed in the document order, not in the order specified, and no more than once. Defaults to empty string, which implies the entire document is printed. The page numbers are quietly capped to actual page count of the document, and ranges beyond the end of the document are ignored. If this results in no pages to print, an error is reported. It is an error to specify a range with start greater than end.
    :param paper_height: *(Optional)* Paper height in inches. Defaults to 11 inches.
    :param paper_width: *(Optional)* Paper width in inches. Defaults to 8.5 inches.
    :param position_x: *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
    :param position_y: *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
    :param prefer_css_page_size: *(Optional)* Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size.
    :param print_background: *(Optional)* Print background graphics. Defaults to false.
    :param prompt_text: *(Optional)* The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
    :param quality: *(Optional)* Compression quality from range [0..100] (jpeg only).
    :param quality: *(Optional)* Compression quality from range [0..100].
    :param query: String to search for.
    :param referrer: *(Optional)* Referrer URL.
    :param referrer_policy: **(EXPERIMENTAL)** *(Optional)* Referrer-policy used for the navigation.
    :param run_immediately: **(EXPERIMENTAL)** *(Optional)* If true, runs the script immediately on existing execution contexts or worlds. Default: false.
    :param scale: *(Optional)* Scale of the webpage rendering. Defaults to 1.
    :param scale: *(Optional)* Scale to apply to resulting view image.
    :param screen_height: *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
    :param screen_orientation: *(Optional)* Screen orientation override.
    :param screen_width: *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
    :param script_source:
    :param script_to_evaluate_on_load: *(Optional)* If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin.
    :param scripts:
    :param session_id: Frame number.
    :param source:
    :param state: Target lifecycle state
    :param transfer_mode: **(EXPERIMENTAL)** *(Optional)* return as stream
    :param transition_type: *(Optional)* Intended transition type.
    :param url:
    :param url: URL of the resource to get content for.
    :param url: URL of the resource to search in.
    :param url: URL to match cooke domain and path.
    :param url: URL to navigate the page to.
    :param viewport: *(Optional)* The viewport dimensions and scale. If not set, the override is cleared.
    :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param world_name: *(Optional)* An optional name which is reported in the Execution Context.
    :param world_name: **(EXPERIMENTAL)** *(Optional)* If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted.
    :returns:
    :returns: *(Optional)* Identifies the bottom-most script which caused the frame to be labelled as an ad. Only sent if frame is labelled as an ad and id is available.
    :returns: A tuple with the following items:
    :returns: Base64-encoded image data.
    :returns: Execution context of the isolated world.
    :returns: Identifier of the added script.
    :returns: List of search matches.
    :returns: Present frame / resource tree structure.
    :returns: Present frame tree structure.
    :returns: Serialized page data.
    @classmethod
    ],
    ``scripts`` are appended to the list of scripts for which the cache
    }
    ACCELEROMETER = "accelerometer"
    accept: bool, prompt_text: str | None = None
    Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).
    accepts: list[FileFilter] | None = None
    accepts: list[str] | None = None
    accuracy: float | None = None,
    Acknowledges that a screencast frame has been received by the frontend.
    action: str
    ACTIVATION_NAVIGATIONS_DISALLOWED_FOR_BUG1234857 = (
    ad_frame_status: AdFrameStatus | None = None
    ad_frame_type: AdFrameType
    Additional information about the frame document's security origin.
    ADDRESS_BAR = "address_bar"
    ALERT = "alert"
    All Permissions Policy features. This enum should match the one defined
    ALL_SCREENS_CAPTURE = "all-screens-capture"
    allowed: bool
    alpha: float, beta: float, gamma: float
    AMBIENT_LIGHT_SENSOR = "ambient-light-sensor"
    ANCHOR_CLICK = "anchorClick"
    APP_BANNER = "AppBanner"
    as an ad.
    ATTRIBUTION_REPORTING = "attribution-reporting"
    AUTO_ACCEPT = "autoAccept"
    AUTO_BOOKMARK = "auto_bookmark"
    AUTO_OPT_OUT = "autoOptOut"
    AUTO_REJECT = "autoReject"
    AUTO_SUBFRAME = "auto_subframe"
    AUTO_TOPLEVEL = "auto_toplevel"
    AUTOPLAY = "autoplay"
    BACK_FORWARD_CACHE_DISABLED = "BackForwardCacheDisabled"
    BACK_FORWARD_CACHE_DISABLED_BY_COMMAND_LINE = (
    BACK_FORWARD_CACHE_DISABLED_BY_LOW_MEMORY = "BackForwardCacheDisabledByLowMemory"
    BACK_FORWARD_CACHE_DISABLED_FOR_DELEGATE = "BackForwardCacheDisabledForDelegate"
    BACK_FORWARD_CACHE_DISABLED_FOR_PRERENDER = "BackForwardCacheDisabledForPrerender"
    BACK_FORWARD_CACHE_RESTORE = "BackForwardCacheRestore"
    backend_node_id: dom.BackendNodeId | None
    background_color: str | None = None
    BEFOREUNLOAD = "beforeunload"
    behavior: str, download_path: str | None = None
    block_reason: PermissionsPolicyBlockReason
    BLUETOOTH = "bluetooth"
    Brings page to front (activates tab).
    BROADCAST_CHANNEL = "BroadcastChannel"
    BROADCAST_CHANNEL_ON_MESSAGE = "BroadcastChannelOnMessage"
    BROWSING_INSTANCE_NOT_SWAPPED = "BrowsingInstanceNotSwapped"
    BROWSING_TOPICS = "browsing-topics"
    CACHE_CONTROL_NO_STORE = "CacheControlNoStore"
    CACHE_CONTROL_NO_STORE_COOKIE_MODIFIED = "CacheControlNoStoreCookieModified"
    CACHE_CONTROL_NO_STORE_DEVICE_BOUND_SESSION_TERMINATED = (
    CACHE_CONTROL_NO_STORE_HTTP_ONLY_COOKIE_MODIFIED = (
    CACHE_FLUSHED = "CacheFlushed"
    CACHE_LIMIT = "CacheLimit"
    CACHE_LIMIT_PRUNED = "CacheLimitPruned"
    CAMERA = "camera"
    can be fired for a single navigation, for example, when a same-document
    canceled: bool | None = None
    Capture page screenshot.
    capture_beyond_viewport: bool | None = None,
    CAPTURED_SURFACE_CONTROL = "captured-surface-control"
    case_sensitive: bool | None = None,
    CH_DEVICE_MEMORY = "ch-device-memory"
    CH_DOWNLINK = "ch-downlink"
    CH_DPR = "ch-dpr"
    CH_ECT = "ch-ect"
    CH_PREFERS_COLOR_SCHEME = "ch-prefers-color-scheme"
    CH_PREFERS_REDUCED_MOTION = "ch-prefers-reduced-motion"
    CH_PREFERS_REDUCED_TRANSPARENCY = "ch-prefers-reduced-transparency"
    CH_RTT = "ch-rtt"
    CH_SAVE_DATA = "ch-save-data"
    CH_UA = "ch-ua"
    CH_UA_ARCH = "ch-ua-arch"
    CH_UA_BITNESS = "ch-ua-bitness"
    CH_UA_FORM_FACTORS = "ch-ua-form-factors"
    CH_UA_FULL_VERSION = "ch-ua-full-version"
    CH_UA_FULL_VERSION_LIST = "ch-ua-full-version-list"
    CH_UA_HIGH_ENTROPY_VALUES = "ch-ua-high-entropy-values"
    CH_UA_MOBILE = "ch-ua-mobile"
    CH_UA_MODEL = "ch-ua-model"
    CH_UA_PLATFORM = "ch-ua-platform"
    CH_UA_PLATFORM_VERSION = "ch-ua-platform-version"
    CH_UA_WOW64 = "ch-ua-wow64"
    CH_VIEWPORT_HEIGHT = "ch-viewport-height"
    CH_VIEWPORT_WIDTH = "ch-viewport-width"
    CH_WIDTH = "ch-width"
    CHILD = "child"
    child_frames: list[FrameResourceTree] | None = None
    child_frames: list[FrameTree] | None = None
    children: list[BackForwardCacheNotRestoredExplanationTree]
    CIRCUMSTANTIAL = "Circumstantial"
    Clears seeded compilation cache.
    Clears the overridden device metrics.
    Clears the overridden Device Orientation.
    Clears the overridden Geolocation Position and Error.
    client_height: float
    client_height: int
    client_mode: str
    client_width: float
    client_width: int
    clip: Viewport | None = None,
    CLIPBOARD_READ = "clipboard-read"
    CLIPBOARD_WRITE = "clipboard-write"
    closed.
    cmd_dict: T_JSON_DICT = {
    column: int
    column_number: int
    Compressed image data requested by the ``startScreencast``.
    COMPUTE_PRESSURE = "compute-pressure"
    CONFIRM = "confirm"
    CONFLICTING_BROWSING_INSTANCE = "ConflictingBrowsingInstance"
    CONTAINS_PLUGINS = "ContainsPlugins"
    CONTENT_DISCARDED = "ContentDiscarded"
    CONTENT_FILE_CHOOSER = "ContentFileChooser"
    CONTENT_FILE_SYSTEM_ACCESS = "ContentFileSystemAccess"
    CONTENT_MEDIA_DEVICES_DISPATCHER_HOST = "ContentMediaDevicesDispatcherHost"
    CONTENT_MEDIA_SESSION_SERVICE = "ContentMediaSessionService"
    CONTENT_SCREEN_READER = "ContentScreenReader"
    CONTENT_SECURITY_HANDLER = "ContentSecurityHandler"
    CONTENT_SERIAL = "ContentSerial"
    content_size: float | None = None
    CONTENT_WEB_AUTHENTICATION_API = "ContentWebAuthenticationAPI"
    CONTENT_WEB_BLUETOOTH = "ContentWebBluetooth"
    CONTENT_WEB_USB = "ContentWebUSB"
    context: str | None = None
    CONTROLLED_FRAME = "controlled-frame"
    Controls whether page will emit lifecycle events.
    COOKIE_DISABLED = "CookieDisabled"
    COOKIE_FLUSHED = "CookieFlushed"
    cookie_name: str, url: str
    Crashes renderer on the IO thread, generates minidumps.
    CREATED_BY_AD_SCRIPT = "CreatedByAdScript"
    Creates an isolated world for the given frame.
    critical: int
    CROSS_ORIGIN_ISOLATED = "cross-origin-isolated"
    cross_origin_isolated_context_type: CrossOriginIsolatedContextType
    cross-process navigation.
    CURRENT_TAB = "currentTab"
    cursive: str | None = None
    data: str
    debugger_id: runtime.UniqueDebuggerId
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: str) -> FrameId:
    def from_json(cls, json: str) -> ScriptIdentifier:
    def from_json(cls, json: T_JSON_DICT) -> BackForwardCacheNotUsed:
    def from_json(cls, json: T_JSON_DICT) -> CompilationCacheProduced:
    def from_json(cls, json: T_JSON_DICT) -> DocumentOpened:
    def from_json(cls, json: T_JSON_DICT) -> DomContentEventFired:
    def from_json(cls, json: T_JSON_DICT) -> DownloadProgress:
    def from_json(cls, json: T_JSON_DICT) -> DownloadWillBegin:
    def from_json(cls, json: T_JSON_DICT) -> FileChooserOpened:
    def from_json(cls, json: T_JSON_DICT) -> FrameAttached:
    def from_json(cls, json: T_JSON_DICT) -> FrameClearedScheduledNavigation:
    def from_json(cls, json: T_JSON_DICT) -> FrameDetached:
    def from_json(cls, json: T_JSON_DICT) -> FrameNavigated:
    def from_json(cls, json: T_JSON_DICT) -> FrameRequestedNavigation:
    def from_json(cls, json: T_JSON_DICT) -> FrameResized:
    def from_json(cls, json: T_JSON_DICT) -> FrameScheduledNavigation:
    def from_json(cls, json: T_JSON_DICT) -> FrameStartedLoading:
    def from_json(cls, json: T_JSON_DICT) -> FrameStartedNavigating:
    def from_json(cls, json: T_JSON_DICT) -> FrameStoppedLoading:
    def from_json(cls, json: T_JSON_DICT) -> FrameSubtreeWillBeDetached:
    def from_json(cls, json: T_JSON_DICT) -> InterstitialHidden:
    def from_json(cls, json: T_JSON_DICT) -> InterstitialShown:
    def from_json(cls, json: T_JSON_DICT) -> JavascriptDialogClosed:
    def from_json(cls, json: T_JSON_DICT) -> JavascriptDialogOpening:
    def from_json(cls, json: T_JSON_DICT) -> LifecycleEvent:
    def from_json(cls, json: T_JSON_DICT) -> LoadEventFired:
    def from_json(cls, json: T_JSON_DICT) -> NavigatedWithinDocument:
    def from_json(cls, json: T_JSON_DICT) -> ScreencastFrame:
    def from_json(cls, json: T_JSON_DICT) -> ScreencastVisibilityChanged:
    def from_json(cls, json: T_JSON_DICT) -> WindowOpen:
    def to_json(self) -> str:
    def to_json(self):
    Default font sizes.
    default_prompt: str | None
    DEFERRED_FETCH = "deferred-fetch"
    DEFERRED_FETCH_MINIMAL = "deferred-fetch-minimal"
    delay: float
    Deletes browser cookie with given name, domain and path.
    Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.
    Deprecated, please use addScriptToEvaluateOnNewDocument instead.
    Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
    Deprecated. Use Browser.downloadProgress instead.
    Deprecated. Use Browser.downloadWillBegin instead.
    description: str | None = None
    details: list[BackForwardCacheBlockingDetails] | None = None
    device_height: float
    device_scale_factor: float,
    device_width: float
    DIGITAL_CREDENTIALS_GET = "digital-credentials-get"
    dir_: str | None = None
    DIRECT_SOCKETS = "direct-sockets"
    DIRECT_SOCKETS_PRIVATE = "direct-sockets-private"
    DISABLE_FOR_RENDER_FRAME_HOST_CALLED = "DisableForRenderFrameHostCalled"
    Disables page domain notifications.
    display: str | None = None
    DISPLAY_CAPTURE = "display-capture"
    display_header_footer: bool | None = None,
    display_overrides: list[str] | None = None
    disposition: ClientNavigationDisposition
    DOCUMENT_DOMAIN = "document-domain"
    DOCUMENT_LOADED = "DocumentLoaded"
    domain_and_registry: str
    DOMAIN_NOT_ALLOWED = "DomainNotAllowed"
    dont_set_visible_size: bool | None = None,
    DOWNLOAD = "download"
    DUMMY = "Dummy"
    eager: bool | None = None
    EMBEDDER_APP_BANNER_MANAGER = "EmbedderAppBannerManager"
    EMBEDDER_CHROME_PASSWORD_MANAGER_CLIENT_BIND_CREDENTIAL_MANAGER = (
    EMBEDDER_DOM_DISTILLER_SELF_DELETING_REQUEST_DELEGATE = (
    EMBEDDER_DOM_DISTILLER_VIEWER_SOURCE = "EmbedderDomDistillerViewerSource"
    EMBEDDER_EXTENSION_MESSAGING = "EmbedderExtensionMessaging"
    EMBEDDER_EXTENSION_MESSAGING_FOR_OPEN_PORT = "EmbedderExtensionMessagingForOpenPort"
    EMBEDDER_EXTENSION_SENT_MESSAGE_TO_CACHED_FRAME = (
    EMBEDDER_EXTENSIONS = "EmbedderExtensions"
    EMBEDDER_MODAL_DIALOG = "EmbedderModalDialog"
    EMBEDDER_OFFLINE_PAGE = "EmbedderOfflinePage"
    EMBEDDER_OOM_INTERVENTION_TAB_HELPER = "EmbedderOomInterventionTabHelper"
    EMBEDDER_PERMISSION_REQUEST_MANAGER = "EmbedderPermissionRequestManager"
    EMBEDDER_POPUP_BLOCKER_TAB_HELPER = "EmbedderPopupBlockerTabHelper"
    EMBEDDER_SAFE_BROWSING_THREAT_DETAILS = "EmbedderSafeBrowsingThreatDetails"
    EMBEDDER_SAFE_BROWSING_TRIGGERED_POPUP_BLOCKER = (
    Emitted only when ``page.interceptFileChooser`` is enabled.
    Enable Chrome's experimental ad filter on all sites.
    Enable page Content Security Policy by-passing.
    Enable/disable prerendering manually.
    enable_file_chooser_opened_event: bool | None = None,
    ENABLED = "Enabled"
    enabled: bool,
    enabled: bool, cancel: bool | None = None
    enabled: bool, configuration: str | None = None
    Enables page domain notifications.
    ENCRYPTED_MEDIA = "encrypted-media"
    enctype: str
    ENTERED_BACK_FORWARD_CACHE_BEFORE_SERVICE_WORKER_HOST_ADDED = (
    entry_id: int,
    Enum of possible auto-response for permission / prompt dialogs.
    Error while paring app manifest.
    error_arguments: list[InstallabilityErrorArgument]
    ERROR_DOCUMENT = "ErrorDocument"
    error_id: str
    etc.
    Evaluates given script in every frame upon creation (before loading frame's scripts).
    every_nth_frame: int | None = None,
    EXECUTION_WHILE_NOT_RENDERED = "execution-while-not-rendered"
    EXECUTION_WHILE_OUT_OF_VIEWPORT = "execution-while-out-of-viewport"
    EXPIRED = "Expired"
    expiry_time: network.TimeSinceEpoch
    explanations: list[AdFrameExplanation] | None = None
    explanations: list[BackForwardCacheNotRestoredExplanation]
    Extensions for Custom Handlers API:
    failed: bool | None = None
    fantasy: str | None = None
    feature: PermissionsPolicyFeature
    FEATURE_DISABLED = "FeatureDisabled"
    FEATURE_DISABLED_FOR_USER = "FeatureDisabledForUser"
    FENCED_FRAMES_EMBEDDER = "FencedFramesEmbedder"
    FENCED_UNPARTITIONED_STORAGE_READ = "fenced-unpartitioned-storage-read"
    file_handlers: list[FileHandler] | None = None
    files: list[FileFilter] | None = None
    Fired before frame subtree is detached. Emitted before any frame of the
    Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do
    Fired for lifecycle events (navigation, load, paint, etc) in the current
    Fired once navigation of the frame has completed. Frame is now associated with the new loader.
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
    Fired when a navigation starts. This event is fired for both
    Fired when a new window is going to be opened, via window.open(), link click, form submission,
    Fired when a renderer-initiated navigation is requested.
    Fired when download makes progress. Last call has ``done`` == true.
    Fired when frame has been attached to its parent.
    Fired when frame has been detached from its parent.
    Fired when frame has started loading.
    Fired when frame has stopped loading.
    Fired when frame no longer has a scheduled navigation.
    Fired when frame schedules a potential navigation.
    Fired when interstitial page was hidden
    Fired when interstitial page was shown
    Fired when opening document to write to.
    Fired when page is about to start a download.
    Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.
    Fired when the page with currently enabled screencast was shown or hidden .
    fixed: int | None = None
    fixed: str | None = None
    FOCUS_WITHOUT_USER_ACTIVATION = "focus-without-user-activation"
    Font families collection for a script.
    font_families: FontFamilies
    font_families: FontFamilies,
    font_sizes: FontSizes,
    footer_template: str | None = None,
    for more details.
    for_scripts: list[ScriptFontFamilies] | None = None,
    Force the page stop all navigations and pending resource fetches.
    FOREGROUND_CACHE_LIMIT = "ForegroundCacheLimit"
    form_factor: str
    FORM_SUBMISSION_GET = "formSubmissionGet"
    FORM_SUBMISSION_POST = "formSubmissionPost"
    FORM_SUBMIT = "form_submit"
    format_: str | None = None,
    frame: Frame
    frame_id: FrameId
    frame_id: FrameId | None = None,
    frame_id: FrameId,
    frame_id: FrameId, html: str
    frame_id: FrameId, url: str
    frameset).
    FROBULATE = "frobulate"
    from_surface: bool | None = None,
    FULLSCREEN = "fullscreen"
    function: str | None = None
    GAMEPAD = "gamepad"
    gated_api_features: list[GatedAPIFeatures]
    generate_document_outline: bool | None = None,
    generate_tagged_pdf: bool | None = None,
    GENERATED = "generated"
    Generates a report for testing.
    Generic font families collection.
    GEOLOCATION = "geolocation"
    Get Origin Trials on given frame.
    Get Permissions Policy state on given frame.
    Gets the processed manifest for this current document.
    grant_univeral_access: bool | None = None,
    guid: str
    GYROSCOPE = "gyroscope"
    has_browser_handler: bool
    has_origin_wildcard: bool
    HAVE_INNER_CONTENTS = "HaveInnerContents"
    HEADER = "Header"
    header_template: str | None = None,
    height: float
    height: int,
    HID = "hid"
    HTTP_AUTH_REQUIRED = "HTTPAuthRequired"
    HTTP_HEADER_REFRESH = "httpHeaderRefresh"
    HTTP_METHOD_NOT_GET = "HTTPMethodNotGET"
    HTTP_STATUS_NOT_OK = "HTTPStatusNotOK"
    https://github.com/WICG/web-lifecycle/
    https://html.spec.whatwg.org/multipage/system-state.html#rph-automation
    https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
    icons: list[ImageResource] | None = None
    id_: FrameId
    id_: int
    id_: str | None = None
    identifier: ScriptIdentifier,
    Identifies the bottom-most script which caused the frame to be labelled
    IDENTITY_CREDENTIALS_GET = "identity-credentials-get"
    IDLE_DETECTION = "idle-detection"
    IDLE_MANAGER = "IdleManager"
    if accuracy is not None:
    if cancel is not None:
    if capture_beyond_viewport is not None:
    if case_sensitive is not None:
    if clip is not None:
    if configuration is not None:
    if display_header_footer is not None:
    if dont_set_visible_size is not None:
    if download_path is not None:
    if enable_file_chooser_opened_event is not None:
    if every_nth_frame is not None:
    if footer_template is not None:
    if for_scripts is not None:
    if format_ is not None:
    if frame_id is not None:
    if from_surface is not None:
    if generate_document_outline is not None:
    if generate_tagged_pdf is not None:
    if grant_univeral_access is not None:
    if group is not None:
    if header_template is not None:
    if ignore_cache is not None:
    if include_command_line_api is not None:
    if is_regex is not None:
    if landscape is not None:
    if latitude is not None:
    if loader_id is not None:
    if longitude is not None:
    if manifest_id is not None:
    if margin_bottom is not None:
    if margin_left is not None:
    if margin_right is not None:
    if margin_top is not None:
    if max_height is not None:
    if max_width is not None:
    if optimize_for_speed is not None:
    if Page.setGenerateCompilationCache is enabled.
    if page_ranges is not None:
    if paper_height is not None:
    if paper_width is not None:
    if position_x is not None:
    if position_y is not None:
    if prefer_css_page_size is not None:
    if print_background is not None:
    if prompt_text is not None:
    if quality is not None:
    if referrer is not None:
    if referrer_policy is not None:
    if run_immediately is not None:
    if scale is not None:
    if screen_height is not None:
    if screen_orientation is not None:
    if screen_width is not None:
    if script_to_evaluate_on_load is not None:
    if transfer_mode is not None:
    if transition_type is not None:
    if viewport is not None:
    if world_name is not None:
    IFRAME_ATTRIBUTE = "IframeAttribute"
    iframes, shadow DOM, external resources, and element-inline styles.
    ignore_cache: bool | None = None,
    IGNORE_EVENT_AND_EVICT = "IgnoreEventAndEvict"
    image: ImageResource
    in services/network/public/cpp/permissions_policy/permissions_policy_features.json5.
    IN_FENCED_FRAME_TREE = "InFencedFrameTree"
    IN_ISOLATED_APP = "InIsolatedApp"
    include_command_line_api: bool | None = None,
    INDEXED_DB_EVENT = "IndexedDBEvent"
    Indicates whether a frame has been identified as an ad and why.
    Indicates whether a frame has been identified as an ad.
    Indicates whether the frame is a secure context and why it is the case.
    Indicates whether the frame is cross-origin isolated and why it is the case.
    Information about the Frame hierarchy along with their cached resources.
    Information about the Frame hierarchy.
    Information about the Frame on the page.
    Information about the Resource on the page.
    INITIAL_FRAME_NAVIGATION = "initialFrameNavigation"
    INJECTED_JAVASCRIPT = "InjectedJavascript"
    INJECTED_STYLE_SHEET = "InjectedStyleSheet"
    INSECURE = "Insecure"
    INSECURE_ANCESTOR = "InsecureAncestor"
    INSECURE_SCHEME = "InsecureScheme"
    Instead, a protocol event ``Page.fileChooserOpened`` is emitted.
    Intercept file chooser requests and transfer control to protocol clients.
    INTEREST_COHORT = "interest-cohort"
    INVALID_SIGNATURE = "InvalidSignature"
    is_allowed: bool,
    is_localhost: bool
    is_regex: bool | None = None,
    is_third_party: bool
    ISOLATED = "Isolated"
    Issued for every compilation cache generated. Is only available
    It will transition the page to the given state according to:
    JAVA_SCRIPT_EXECUTION = "JavaScriptExecution"
    Javascript dialog type.
    JOIN_AD_INTEREST_GROUP = "join-ad-interest-group"
    JS_NETWORK_REQUEST_RECEIVED_CACHE_CONTROL_NO_STORE_RESOURCE = (
    json = yield cmd_dict
    KEEPALIVE_REQUEST = "KeepaliveRequest"
    KEYBOARD_LOCK = "KeyboardLock"
    KEYBOARD_MAP = "keyboard-map"
    KEYWORD = "keyword"
    KEYWORD_GENERATED = "keyword_generated"
    label: str | None = None
    landscape: bool | None = None,
    lang: str | None = None
    LANGUAGE_DETECTOR = "language-detector"
    last_modified: network.TimeSinceEpoch | None = None
    latitude: float | None = None,
    launch_handler: LaunchHandler | None = None
    launch_type: str
    Layout viewport position and dimensions.
    line: int
    line_number: int
    LINK = "link"
    List of not restored reasons for back-forward cache.
    LIVE_MEDIA_STREAM_TRACK = "LiveMediaStreamTrack"
    loader_id: network.LoaderId
    loader_id: network.LoaderId | None = None,
    LOADING = "Loading"
    LOCAL_FONTS = "local-fonts"
    locator: PermissionsPolicyBlockLocator | None = None
    longitude: float | None = None,
    MAGNETOMETER = "magnetometer"
    MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_CACHE = "MainResourceHasCacheControlNoCache"
    MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_STORE = "MainResourceHasCacheControlNoStore"
    main-frame history navigation where the document changes (non-same-document navigations),
    MALFORMED = "Malformed"
    manifest_id: str | None = None,
    MANUAL_SUBFRAME = "manual_subframe"
    margin_bottom: float | None = None,
    margin_left: float | None = None,
    margin_right: float | None = None,
    margin_top: float | None = None,
    match_sub_domains: bool
    MATCHED_BLOCKING_RULE = "MatchedBlockingRule"
    math: str | None = None
    max_height: int | None = None,
    max_width: int | None = None,
    MEDIA_PLAYBACK_WHILE_NOT_VISIBLE = "media-playback-while-not-visible"
    message: str
    message: str, group: str | None = None
    META_TAG_REFRESH = "metaTagRefresh"
    metadata: ScreencastFrameMetadata
    method: str
    MICROPHONE = "microphone"
    MIDI = "midi"
    mime_type: str
    mobile: bool,
    mode: AutoResponseMode,
    mode: str
    name: str
    name: str | None = None
    Navigates current page to the given history entry.
    Navigates current page to the given URL.
    NAVIGATION = "Navigation"
    navigation becomes a cross-document navigation (such as in the case of a
    Navigation history entry.
    Navigation may still be cancelled after the event is issued.
    Navigation may still be cancelled after the event is issued. Multiple events
    NAVIGATION_CANCELLED_WHILE_RESTORING = "NavigationCancelledWhileRestoring"
    navigation_type: str
    navigations, the event is fired after ``frameRequestedNavigation``.
    NETWORK_EXCEEDS_BUFFER_LIMIT = "NetworkExceedsBufferLimit"
    NETWORK_REQUEST_DATAPIPE_DRAINED_AS_BYTES_CONSUMER = (
    NETWORK_REQUEST_REDIRECTED = "NetworkRequestRedirected"
    NETWORK_REQUEST_TIMEOUT = "NetworkRequestTimeout"
    NEW_TAB = "newTab"
    NEW_WINDOW = "newWindow"
    NO_REFERRER = "noReferrer"
    NO_REFERRER_WHEN_DOWNGRADE = "noReferrerWhenDowngrade"
    NO_RESPONSE_HEAD = "NoResponseHead"
    NONE = "none"
    NONE = "None"
    NONE = "none"
    not assume any ordering with the Page.frameNavigated event. This event is fired only for
    NOT_ISOLATED = "NotIsolated"
    NOT_ISOLATED_FEATURE_DISABLED = "NotIsolatedFeatureDisabled"
    NOT_MOST_RECENT_NAVIGATION_ENTRY = "NotMostRecentNavigationEntry"
    NOT_PRIMARY_MAIN_FRAME = "NotPrimaryMainFrame"
    not_restored_explanations: list[BackForwardCacheNotRestoredExplanation]
    not_restored_explanations_tree: None | (BackForwardCacheNotRestoredExplanationTree)
    NOT_SUPPORTED = "NotSupported"
    offset_top: float
    offset_x: float
    offset_y: float
    Only returns values if the feature flag 'WebAppEnableManifestId' is enabled
    open.
    optimize_for_speed: bool | None = None,
    orientation: str | None = None
    ORIGIN = "origin"
    Origin Trial(https://www.chromium.org/blink/origin-trials) support.
    origin: str
    ORIGIN_WHEN_CROSS_ORIGIN = "originWhenCrossOrigin"
    OS_NOT_SUPPORTED = "OSNotSupported"
    OTHER = "other"
    OTP_CREDENTIALS = "otp-credentials"
    OUTSTANDING_NETWORK_REQUEST_DIRECT_SOCKET = "OutstandingNetworkRequestDirectSocket"
    OUTSTANDING_NETWORK_REQUEST_FETCH = "OutstandingNetworkRequestFetch"
    OUTSTANDING_NETWORK_REQUEST_OTHERS = "OutstandingNetworkRequestOthers"
    OUTSTANDING_NETWORK_REQUEST_XHR = "OutstandingNetworkRequestXHR"
    Overrides the Device Orientation.
    Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
    PAGE_BLOCK_INTERSTITIAL = "pageBlockInterstitial"
    page_ranges: str | None = None,
    page_scale_factor: float
    PAGE_SUPPORT_NEEDED = "PageSupportNeeded"
    page_x: float
    page_x: int
    page_y: float
    page_y: int
    paper_height: float | None = None,
    paper_width: float | None = None,
    params: T_JSON_DICT = dict()
    params["accept"] = accept
    params["alpha"] = alpha
    params["behavior"] = behavior
    params["beta"] = beta
    params["cookieName"] = cookie_name
    params["data"] = data
    params["deviceScaleFactor"] = device_scale_factor
    params["enabled"] = enabled
    params["entryId"] = entry_id
    params["fontFamilies"] = font_families.to_json()
    params["fontSizes"] = font_sizes.to_json()
    params["frameId"] = frame_id.to_json()
    params["gamma"] = gamma
    params["height"] = height
    params["html"] = html
    params["identifier"] = identifier.to_json()
    params["isAllowed"] = is_allowed
    params["message"] = message
    params["mobile"] = mobile
    params["mode"] = mode.to_json()
    params["query"] = query
    params["scripts"] = [i.to_json() for i in scripts]
    params["scriptSource"] = script_source
    params["sessionId"] = session_id
    params["source"] = source
    params["state"] = state
    params["url"] = url
    params["width"] = width
    parent_frame_id: FrameId
    parent_id: FrameId | None = None
    PARENT_IS_AD = "ParentIsAd"
    Parsed app manifest properties.
    parsed_token: OriginTrialToken | None = None
    PARSER_ABORTED = "ParserAborted"
    Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.
    PAYMENT = "payment"
    PAYMENT_MANAGER = "PaymentManager"
    PERFORMANCE_MEASURE_MEMORY = "PerformanceMeasureMemory"
    PERFORMANCE_PROFILE = "PerformanceProfile"
    Per-script compilation cache parameters for ``Page.produceCompilationCache`
    PICTURE_IN_PICTURE = "PictureInPicture"
    PICTURE_IN_PICTURE = "picture-in-picture"
    POPINS = "popins"
    position_x: int | None = None,
    position_y: int | None = None,
    POST_MESSAGE_BY_WEB_VIEW_CLIENT = "PostMessageByWebViewClient"
    prefer_css_page_size: bool | None = None,
    prefer_related_applications: bool | None = None
    Print page as PDF.
    print_background: bool | None = None,
    PRINTING = "Printing"
    PRIVATE_AGGREGATION = "private-aggregation"
    PRIVATE_STATE_TOKEN_ISSUANCE = "private-state-token-issuance"
    PRIVATE_STATE_TOKEN_REDEMPTION = "private-state-token-redemption"
    produced upon backend discretion, based on internal heuristics.
    PROMPT = "prompt"
    protocol: str
    protocol_handlers: list[ProtocolHandler] | None = None
    PUBLICKEY_CREDENTIALS_CREATE = "publickey-credentials-create"
    PUBLICKEY_CREDENTIALS_GET = "publickey-credentials-get"
    quality: int | None = None,
    query results).
    query: str,
    raw_token_text: str
    Reason for a permissions policy feature to be disabled.
    reason: BackForwardCacheNotRestoredReason
    reason: ClientNavigationReason
    reason: str
    received_bytes: float
    referrer: str | None = None,
    referrer_policy: ReferrerPolicy | None = None,
    RELATED_ACTIVE_CONTENTS_EXIST = "RelatedActiveContentsExist"
    related_applications: list[RelatedApplication] | None = None
    RELOAD = "reload"
    Reloads given page optionally ignoring the cache.
    Removes given script from the list.
    RENDER_FRAME_HOST_REUSED_CROSS_SITE = "RenderFrameHostReused_CrossSite"
    RENDER_FRAME_HOST_REUSED_SAME_SITE = "RenderFrameHostReused_SameSite"
    RENDERER_PROCESS_CRASHED = "RendererProcessCrashed"
    RENDERER_PROCESS_KILLED = "RendererProcessKilled"
    renderer-initiated and browser-initiated navigations. For renderer-initiated
    REQUESTED_AUDIO_CAPTURE_PERMISSION = "RequestedAudioCapturePermission"
    REQUESTED_BACK_FORWARD_CACHE_BLOCKED_SENSORS = (
    REQUESTED_BACKGROUND_WORK_PERMISSION = "RequestedBackgroundWorkPermission"
    REQUESTED_BY_WEB_VIEW_CLIENT = "RequestedByWebViewClient"
    REQUESTED_MIDI_PERMISSION = "RequestedMIDIPermission"
    REQUESTED_STORAGE_ACCESS_GRANT = "RequestedStorageAccessGrant"
    REQUESTED_VIDEO_CAPTURE_PERMISSION = "RequestedVideoCapturePermission"
    Requests backend to produce compilation cache for the specified scripts.
    Resets navigation history for the current page.
    resources: list[FrameResource]
    result: bool
    return (
    return (str(json["content"]), bool(json["base64Encoded"]))
    return [debugger.SearchMatch.from_json(i) for i in json["result"]]
    return [InstallabilityError.from_json(i) for i in json["installabilityErrors"]]
    return [OriginTrial.from_json(i) for i in json["originTrials"]]
    return [PermissionsPolicyFeatureState.from_json(i) for i in json["states"]]
    return AdScriptId.from_json(json["adScriptId"]) if "adScriptId" in json else None
    return FrameResourceTree.from_json(json["frameTree"])
    return FrameTree.from_json(json["frameTree"])
    return runtime.ExecutionContextId.from_json(json["executionContextId"])
    return ScriptIdentifier.from_json(json["identifier"])
    return str(json["data"])
    return str(json["primaryIcon"]) if "primaryIcon" in json else None
    Returns a snapshot of the page as a string. For MHTML format, the serialization includes
    Returns content of the given resource.
    Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
    Returns navigation history for the current page.
    Returns present frame / resource tree structure.
    Returns present frame tree structure.
    Returns the unique (PWA) app id.
    REWRITER = "rewriter"
    ROOT = "root"
    RUN_AD_AUCTION = "run-ad-auction"
    run_immediately: bool | None = None,
    SAME_ORIGIN = "sameOrigin"
    sans_serif: str | None = None
    scale: float
    scale: float | None = None,
    SCHEDULER_TRACKED_FEATURE_USED = "SchedulerTrackedFeatureUsed"
    SCHEME_NOT_HTTP_OR_HTTPS = "SchemeNotHTTPOrHTTPS"
    scope: str
    scope: str | None = None
    scope_extensions: list[ScopeExtension] | None = None
    screen_height: int | None = None,
    screen_orientation: emulation.ScreenOrientation | None = None,
    SCREEN_WAKE_LOCK = "screen-wake-lock"
    screen_width: int | None = None,
    Screencast frame metadata.
    screenshots: list[Screenshot] | None = None
    script: str
    script_id: runtime.ScriptId
    SCRIPT_INITIATED = "scriptInitiated"
    script_source: str,
    script_to_evaluate_on_load: str | None = None,
    scripts: list[CompilationCacheParams],
    scroll_offset_x: float
    scroll_offset_y: float
    Searches for given string in resource content.
    SECURE = "Secure"
    secure_context_type: SecureContextType
    SECURE_LOCALHOST = "SecureLocalhost"
    security_origin: str
    security_origin_details: SecurityOriginDetails | None = None
    See also: ``Page.compilationCacheProduced``.
    See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA
    Seeds compilation cache for given url. Compilation cache does not survive
    SERIAL = "serial"
    serif: str | None = None
    SERVICE_WORKER_CLAIM = "ServiceWorkerClaim"
    SERVICE_WORKER_POST_MESSAGE = "ServiceWorkerPostMessage"
    SERVICE_WORKER_UNREGISTRATION = "ServiceWorkerUnregistration"
    SERVICE_WORKER_VERSION_ACTIVATION = "ServiceWorkerVersionActivation"
    session_id: int
    session_id: int,
    SESSION_RESTORED = "SessionRestored"
    Set default font sizes.
    Set generic font families.
    Set the behavior when downloading a file.
    Sets given markup as the document's HTML.
    Sets the Secure Payment Confirmation transaction mode.
    share_target: ShareTarget | None = None
    SHARED_ARRAY_BUFFERS = "SharedArrayBuffers"
    SHARED_ARRAY_BUFFERS_TRANSFER_ALLOWED = "SharedArrayBuffersTransferAllowed"
    SHARED_AUTOFILL = "shared-autofill"
    SHARED_STORAGE = "shared-storage"
    SHARED_STORAGE_SELECT_URL = "shared-storage-select-url"
    SHARED_WORKER = "SharedWorker"
    short_name: str | None = None
    shortcuts: list[Shortcut] | None = None
    sizes: str | None = None
    SMART_CARD = "SmartCard"
    SMART_CARD = "smart-card"
    source: str,
    SPEAKER_SELECTION = "speaker-selection"
    SPEECH_RECOGNIZER = "SpeechRecognizer"
    SPEECH_SYNTHESIS = "SpeechSynthesis"
    stack: runtime.StackTrace | None
    standard: int | None = None
    standard: str | None = None
    start_url: str | None = None
    Starts sending each frame using the ``screencastFrame`` event.
    state: str
    state: str,
    Status for an Origin Trial token.
    Status for an Origin Trial.
    status: OriginTrialStatus
    status: OriginTrialTokenStatus
    Stops sending each frame in the ``screencastFrame``.
    STORAGE_ACCESS = "storage-access"
    STRICT_ORIGIN = "strictOrigin"
    STRICT_ORIGIN_WHEN_CROSS_ORIGIN = "strictOriginWhenCrossOrigin"
    SUB_APPS = "sub-apps"
    SUBFRAME_IS_NAVIGATING = "SubframeIsNavigating"
    SUBRESOURCE_HAS_CACHE_CONTROL_NO_CACHE = "SubresourceHasCacheControlNoCache"
    SUBRESOURCE_HAS_CACHE_CONTROL_NO_STORE = "SubresourceHasCacheControlNoStore"
    SUBSET = "Subset"
    subtree is actually detached.
    SUCCESS = "Success"
    suggested_filename: str
    SUMMARIZER = "summarizer"
    SUPPORT_PENDING = "SupportPending"
    SYNC_XHR = "sync-xhr"
    T_JSON_DICT,
    target (including local frames).
    text: str | None = None
    The image definition used in both icon and screenshot.
    The installability error
    The referring-policy used for the navigation.
    The type of a frameNavigated event.
    theme_color: str | None = None
    This command is a short-term solution for https://crbug.com/1440085.
    TIMEOUT = "Timeout"
    TIMEOUT_PUTTING_IN_CACHE = "TimeoutPuttingInCache"
    timestamp: network.MonotonicTime
    timestamp: network.TimeSinceEpoch | None = None
    title: str
    title: str | None = None
    TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.
    Toggles mouse event-based touch event emulation.
    TOKEN_DISABLED = "TokenDisabled"
    tokens_with_status: list[OriginTrialTokenWithStatus]
    total_bytes: float
    transfer_mode: str | None = None,
    Transition type.
    transition_type: TransitionType
    transition_type: TransitionType | None = None,
    TRANSLATOR = "translator"
    trial_name: str
    TRIAL_NOT_ALLOWED = "TrialNotAllowed"
    Tries to close page, running its beforeunload hooks, if any.
    Tries to update the web lifecycle state of the page.
    tuple[
    tuple[FrameId, network.LoaderId | None, str | None],
    tuple[str | None, str | None],
    type_: BackForwardCacheNotRestoredReasonType
    type_: DialogType
    type_: NavigationType
    type_: network.ResourceType
    type_: str | None = None
    TYPED = "typed"
    Types of not restored reasons for back-forward cache.
    typing.Generator[T_JSON_DICT, T_JSON_DICT, FrameResourceTree]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[InstallabilityError]]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, None]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[int, list[NavigationEntry]]]
    unavailable.
    Unique frame identifier.
    Unique script identifier.
    UNKNOWN = "Unknown"
    UNKNOWN_TRIAL = "UnknownTrial"
    UNLOAD = "unload"
    UNLOAD_HANDLER = "UnloadHandler"
    UNLOAD_HANDLER_EXISTS_IN_MAIN_FRAME = "UnloadHandlerExistsInMainFrame"
    UNLOAD_HANDLER_EXISTS_IN_SUB_FRAME = "UnloadHandlerExistsInSubFrame"
    unreachable_url: str | None = None
    UNSAFE_URL = "unsafeUrl"
    url: str
    url: str | None = None
    url: str,
    url: str, data: str
    url_fragment: str | None = None
    usage_restriction: OriginTrialUsageRestriction
    USB = "usb"
    USB_UNRESTRICTED = "usb-unrestricted"
    USER_AGENT_OVERRIDE_DIFFERS = "UserAgentOverrideDiffers"
    user_gesture: bool
    user_input: str
    user_typed_url: str
    VALID_TOKEN_NOT_PROVIDED = "ValidTokenNotProvided"
    value: str
    VERTICAL_SCROLL = "vertical-scroll"
    Viewport for capturing screenshot.
    viewport: Viewport | None = None,
    visible: bool
    Visual viewport position, dimensions, and scale.
    WAS_GRANTED_MEDIA_ACCESS = "WasGrantedMediaAccess"
    WEB_APP_INSTALLATION = "web-app-installation"
    WEB_DATABASE = "WebDatabase"
    WEB_HID = "WebHID"
    WEB_LOCKS = "WebLocks"
    WEB_NFC = "WebNfc"
    WEB_OTP_SERVICE = "WebOTPService"
    WEB_PRINTING = "web-printing"
    WEB_RTC = "WebRTC"
    WEB_RTC_STICKY = "WebRTCSticky"
    WEB_SHARE = "WebShare"
    WEB_SHARE = "web-share"
    WEB_SOCKET = "WebSocket"
    WEB_SOCKET_STICKY = "WebSocketSticky"
    WEB_TRANSPORT = "WebTransport"
    WEB_TRANSPORT_STICKY = "WebTransportSticky"
    WEB_VIEW_DOCUMENT_START_JAVASCRIPT_CHANGED = "WebViewDocumentStartJavascriptChanged"
    WEB_VIEW_JAVA_SCRIPT_OBJECT_CHANGED = "WebViewJavaScriptObjectChanged"
    WEB_VIEW_MESSAGE_LISTENER_INJECTED = "WebViewMessageListenerInjected"
    WEB_VIEW_SAFE_BROWSING_ALLOWLIST_CHANGED = "WebViewSafeBrowsingAllowlistChanged"
    WEB_VIEW_SETTINGS_CHANGED = "WebViewSettingsChanged"
    WEB_XR = "WebXR"
    when bfcache navigation fails.
    When file chooser interception is enabled, native file chooser dialog is not shown.
    When script with a matching URL is encountered, the cache is optionally
    width: float
    width: int,
    window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
    window_features: list[str]
    WINDOW_MANAGEMENT = "window-management"
    window_name: str
    world_name: str | None = None,
    would be produced. The list may be reset during page navigation.
    WRITER = "writer"
    WRONG_ORIGIN = "WrongOrigin"
    WRONG_VERSION = "WrongVersion"
    x: float
    XR_SPATIAL_TRACKING = "xr-spatial-tracking"
    y: float
    zoom: float | None = None
#
# CDP domain: Page
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, AdScriptId | None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[debugger.SearchMatch]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[OriginTrial]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[PermissionsPolicyFeatureState]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, runtime.ExecutionContextId]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, ScriptIdentifier]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[str, bool]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[str, io.StreamHandle | None]]:
):
@dataclass
@event_class("Page.backForwardCacheNotUsed")
@event_class("Page.compilationCacheProduced")
@event_class("Page.documentOpened")
@event_class("Page.domContentEventFired")
@event_class("Page.downloadProgress")
@event_class("Page.downloadWillBegin")
@event_class("Page.fileChooserOpened")
@event_class("Page.frameAttached")
@event_class("Page.frameClearedScheduledNavigation")
@event_class("Page.frameDetached")
@event_class("Page.frameNavigated")
@event_class("Page.frameRequestedNavigation")
@event_class("Page.frameResized")
@event_class("Page.frameScheduledNavigation")
@event_class("Page.frameStartedLoading")
@event_class("Page.frameStartedNavigating")
@event_class("Page.frameStoppedLoading")
@event_class("Page.frameSubtreeWillBeDetached")
@event_class("Page.interstitialHidden")
@event_class("Page.interstitialShown")
@event_class("Page.javascriptDialogClosed")
@event_class("Page.javascriptDialogOpening")
@event_class("Page.lifecycleEvent")
@event_class("Page.loadEventFired")
@event_class("Page.navigatedWithinDocument")
@event_class("Page.screencastFrame")
@event_class("Page.screencastVisibilityChanged")
@event_class("Page.windowOpen")
]:
class AdFrameExplanation:
class AdFrameStatus:
class AdFrameType:
class AdScriptId:
class AppManifestError:
class AppManifestParsedProperties:
class AutoResponseMode:
class BackForwardCacheBlockingDetails:
class BackForwardCacheNotRestoredExplanation:
class BackForwardCacheNotRestoredExplanationTree:
class BackForwardCacheNotRestoredReason:
class BackForwardCacheNotRestoredReasonType:
class BackForwardCacheNotUsed:
class ClientNavigationDisposition:
class ClientNavigationReason:
class CompilationCacheParams:
class CompilationCacheProduced:
class CrossOriginIsolatedContextType:
class DialogType:
class DocumentOpened:
class DomContentEventFired:
class DownloadProgress:
class DownloadWillBegin:
class FileChooserOpened:
class FileFilter:
class FileHandler:
class FontFamilies:
class FontSizes:
class Frame:
class FrameAttached:
class FrameClearedScheduledNavigation:
class FrameDetached:
class FrameId:
class FrameNavigated:
class FrameRequestedNavigation:
class FrameResized:
class FrameResource:
class FrameResourceTree:
class FrameScheduledNavigation:
class FrameStartedLoading:
class FrameStartedNavigating:
class FrameStoppedLoading:
class FrameSubtreeWillBeDetached:
class FrameTree:
class GatedAPIFeatures:
class ImageResource:
class InstallabilityError:
class InstallabilityErrorArgument:
class InterstitialHidden:
class InterstitialShown:
class JavascriptDialogClosed:
class JavascriptDialogOpening:
class LaunchHandler:
class LayoutViewport:
class LifecycleEvent:
class LoadEventFired:
class NavigatedWithinDocument:
class NavigationEntry:
class NavigationType:
class OriginTrial:
class OriginTrialStatus:
class OriginTrialToken:
class OriginTrialTokenStatus:
class OriginTrialTokenWithStatus:
class OriginTrialUsageRestriction:
class PermissionsPolicyBlockLocator:
class PermissionsPolicyBlockReason:
class PermissionsPolicyFeature:
class PermissionsPolicyFeatureState:
class ProtocolHandler:
class ReferrerPolicy:
class RelatedApplication:
class ScopeExtension:
class ScreencastFrame:
class ScreencastFrameMetadata:
class ScreencastVisibilityChanged:
class Screenshot:
class ScriptFontFamilies:
class ScriptIdentifier:
class SecureContextType:
class SecurityOriginDetails:
class ShareTarget:
class Shortcut:
class TransitionType:
class Viewport:
class VisualViewport:
class WebAppManifest:
class WindowOpen:
def add_compilation_cache(
def add_script_to_evaluate_on_load(
def add_script_to_evaluate_on_new_document(
def bring_to_front() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def capture_screenshot(
def capture_snapshot(
def clear_compilation_cache() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_device_metrics_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_device_orientation_override() -> (
def clear_geolocation_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def close() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def crash() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def create_isolated_world(
def delete_cookie(
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def enable(
def generate_test_report(
def get_ad_script_id(
def get_app_id() -> typing.Generator[
def get_app_manifest(
def get_frame_tree() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, FrameTree]:
def get_installability_errors() -> (
def get_layout_metrics() -> typing.Generator[
def get_manifest_icons() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str | None]:
def get_navigation_history() -> (
def get_origin_trials(
def get_permissions_policy_state(
def get_resource_content(
def get_resource_tree() -> (
def handle_java_script_dialog(
def navigate(
def navigate_to_history_entry(
def print_to_pdf(
def produce_compilation_cache(
def reload(
def remove_script_to_evaluate_on_load(
def remove_script_to_evaluate_on_new_document(
def reset_navigation_history() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def screencast_frame_ack(
def search_in_resource(
def set_ad_blocking_enabled(
def set_bypass_csp(enabled: bool) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def set_device_metrics_override(
def set_device_orientation_override(
def set_document_content(
def set_download_behavior(
def set_font_families(
def set_font_sizes(
def set_geolocation_override(
def set_intercept_file_chooser_dialog(
def set_lifecycle_events_enabled(
def set_prerendering_allowed(
def set_rph_registration_mode(
def set_spc_transaction_mode(
def set_touch_emulation_enabled(
def set_web_lifecycle_state(
def start_screencast(
def stop_loading() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def stop_screencast() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def wait_for_debugger() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
from . import debugger
from . import dom
from . import emulation
from . import io
from . import network
from . import runtime
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing

pass
