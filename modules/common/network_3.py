
                    ExemptedSetCookieWithReason.from_json(i)
                    for i in json["exemptedCookies"]
                    json["serviceWorkerResponseSource"]
                )
                [
                [ContentSecurityPolicyStatus.from_json(i) for i in json["csp"]]
                [PostDataEntry.from_json(i) for i in json["postDataEntries"]]
                [SignedExchangeError.from_json(i) for i in json["errors"]]
                [str(i) for i in json["certificates"]]
                ]
                AlternateProtocolUsage.from_json(json["alternateProtocolUsage"])
                AssociatedCookie.from_json(i) for i in json["associatedCookies"]
                AuthChallenge.from_json(json["authChallenge"])
                BlockedReason.from_json(json["blockedReason"])
                BlockedSetCookieWithReason.from_json(i) for i in json["blockedCookies"]
                bool(json["cookiePartitionKeyOpaque"])
                bool(json["fromDiskCache"]) if "fromDiskCache" in json else None
                bool(json["fromEarlyHints"]) if "fromEarlyHints" in json else None
                bool(json["fromPrefetchCache"]) if "fromPrefetchCache" in json else None
                bool(json["fromServiceWorker"]) if "fromServiceWorker" in json else None
                bool(json["hasUserGesture"]) if "hasUserGesture" in json else None
                bool(json["isLinkPreload"]) if "isLinkPreload" in json else None
                bool(json["partitionKeyOpaque"])
                bool(json["siteHasCookieInOtherPartition"])
                ClientSecurityState.from_json(json["clientSecurityState"])
                CookieBlockedReason.from_json(i) for i in json["blockedReasons"]
                CookieExemptionReason.from_json(json["exemptionReason"])
                CookiePartitionKey.from_json(json["cookiePartitionKey"])
                CookiePartitionKey.from_json(json["partitionKey"])
                CookiePriority.from_json(json["priority"])
                CookieSameSite.from_json(json["sameSite"])
                CookieSourceScheme.from_json(json["sourceScheme"])
                CorsErrorStatus.from_json(json["corsErrorStatus"])
                CrossOriginEmbedderPolicyStatus.from_json(json["coep"])
                CrossOriginOpenerPolicyStatus.from_json(json["coop"])
                DirectSocketDnsQueryType.from_json(json["dnsQueryType"])
                else None
                ErrorReason.from_json(json["responseErrorReason"])
                float(json["columnNumber"]) if "columnNumber" in json else None
                float(json["httpStatusCode"]) if "httpStatusCode" in json else None
                float(json["keepAliveDelay"]) if "keepAliveDelay" in json else None
                float(json["receiveBufferSize"])
                float(json["sendBufferSize"]) if "sendBufferSize" in json else None
                float(json["workerCacheLookupStart"])
                float(json["workerRouterEvaluationStart"])
                for i in json["signedCertificateTimestampList"]
                Headers.from_json(json["requestHeaders"])
                Headers.from_json(json["responseHeaders"])
                if "actualSourceType" in json
                if "alternateProtocolUsage" in json
                if "authChallenge" in json
                if "blockedReason" in json
                if "bundleRequestId" in json
                if "cacheStorageCacheName" in json
                if "certificates" in json
                if "clientSecurityState" in json
                if "coep" in json
                if "cookiePartitionKey" in json
                if "cookiePartitionKeyOpaque" in json
                if "coop" in json
                if "corsErrorStatus" in json
                if "csp" in json
                if "dnsQueryType" in json
                if "errorField" in json
                if "errors" in json
                if "exemptedCookies" in json
                if "exemptionReason" in json
                if "header" in json
                if "headers" in json
                if "interceptionStage" in json
                if "matchedSourceType" in json
                if "mixedContentType" in json
                if "partitionKey" in json
                if "partitionKeyOpaque" in json
                if "postDataEntries" in json
                if "priority" in json
                if "receiveBufferSize" in json
                if "redirectResponse" in json
                if "reportOnlyReportingEndpoint" in json
                if "requestHeaders" in json
                if "requestHeadersText" in json
                if "resourceType" in json
                if "responseErrorReason" in json
                if "responseHeaders" in json
                if "responseStatusCode" in json
                if "responseTime" in json
                if "sameSite" in json
                if "securityDetails" in json
                if "serverSignatureAlgorithm" in json
                if "serviceWorkerResponseSource" in json
                if "serviceWorkerRouterInfo" in json
                if "siteHasCookieInOtherPartition" in json
                if "sourceScheme" in json
                if "trustTokenParams" in json
                if "workerCacheLookupStart" in json
                if "workerRouterEvaluationStart" in json
                Initiator.from_json(json["initiator"]) if "initiator" in json else None
                int(json["issuedTokenCount"]) if "issuedTokenCount" in json else None
                int(json["responseStatusCode"])
                int(json["ruleIdMatched"]) if "ruleIdMatched" in json else None
                int(json["serverSignatureAlgorithm"])
                int(json["signatureIndex"]) if "signatureIndex" in json else None
                InterceptionStage.from_json(json["interceptionStage"])
                io.StreamHandle.from_json(json["stream"]) if "stream" in json else None
                json["certificateTransparencyCompliance"]
                json["initiatorIPAddressSpace"]
                json["privateNetworkRequestPolicy"]
                json["reportOnlyValue"]
                json["resourceIPAddressSpace"]
                network.Headers.from_json(json["headers"])
                page.FrameId.from_json(json["frameId"]) if "frameId" in json else None
                RequestId.from_json(json["bundleRequestId"])
                RequestId.from_json(json["requestId"]) if "requestId" in json else None
                ResourceTiming.from_json(json["timing"]) if "timing" in json else None
                ResourceType.from_json(json["resourceType"])
                Response.from_json(json["redirectResponse"])
                Response.from_json(json["response"]) if "response" in json else None
                runtime.StackTrace.from_json(json["stack"]) if "stack" in json else None
                security.MixedContentType.from_json(json["mixedContentType"])
                SecurityDetails.from_json(json["securityDetails"])
                self.service_worker_response_source.to_json()
                ServiceWorkerResponseSource.from_json(
                ServiceWorkerRouterInfo.from_json(json["serviceWorkerRouterInfo"])
                ServiceWorkerRouterSource.from_json(json["actualSourceType"])
                ServiceWorkerRouterSource.from_json(json["matchedSourceType"])
                SetCookieBlockedReason.from_json(i) for i in json["blockedReasons"]
                SignedCertificateTimestamp.from_json(i)
                SignedExchangeErrorField.from_json(json["errorField"])
                SignedExchangeHeader.from_json(json["header"])
                SignedExchangeSignature.from_json(i) for i in json["signatures"]
                str(json["cacheStorageCacheName"])
                str(json["keyExchangeGroup"]) if "keyExchangeGroup" in json else None
                str(json["netErrorName"]) if "netErrorName" in json else None
                str(json["remoteIPAddress"]) if "remoteIPAddress" in json else None
                str(json["reportingEndpoint"]) if "reportingEndpoint" in json else None
                str(json["reportOnlyReportingEndpoint"])
                str(json["requestHeadersText"])
                str(json["topLevelOrigin"]) if "topLevelOrigin" in json else None
                TimeSinceEpoch.from_json(json["expires"]) if "expires" in json else None
                TimeSinceEpoch.from_json(json["responseTime"])
                TrustTokenParams.from_json(json["trustTokenParams"])
            )
            ),
            ],
            actual_source_type=(
            alternate_protocol_usage=(
            associated_cookies=[
            auth_challenge=(
            blocked_cookies=[
            blocked_reason=(
            blocked_reasons=[
            body_size=float(json["bodySize"]),
            body=dict(json["body"]),
            bundle_request_id=(
            bytes_=str(json["bytes"]) if "bytes" in json else None,
            cache_storage_cache_name=(
            canceled=bool(json["canceled"]) if "canceled" in json else None,
            cert_sha256=str(json["certSha256"]) if "certSha256" in json else None,
            cert_url=str(json["certUrl"]) if "certUrl" in json else None,
            certificate_id=security.CertificateId.from_json(json["certificateId"]),
            certificate_transparency_compliance=CertificateTransparencyCompliance.from_json(
            certificates=(
            charset=str(json["charset"]),
            cipher=str(json["cipher"]),
            client_security_state=(
            coep=(
            column_number=(
            completed_attempts=int(json["completedAttempts"]),
            connect_end=float(json["connectEnd"]),
            connect_start=float(json["connectStart"]),
            connect_timing=ConnectTiming.from_json(json["connectTiming"]),
            connection_id=float(json["connectionId"]),
            connection_reused=bool(json["connectionReused"]),
            cookie_line=str(json["cookieLine"]),
            cookie_partition_key_opaque=(
            cookie_partition_key=(
            cookie=Cookie.from_json(json["cookie"]) if "cookie" in json else None,
            cookie=Cookie.from_json(json["cookie"]),
            coop=(
            cors_error_status=(
            cors_error=CorsError.from_json(json["corsError"]),
            csp=(
            data_length=int(json["dataLength"]),
            data=str(json["data"]) if "data" in json else None,
            data=str(json["data"]),
            date=int(json["date"]),
            depth=int(json["depth"]),
            destination=str(json["destination"]),
            disable_cache=bool(json["disableCache"]),
            dns_end=float(json["dnsEnd"]),
            dns_query_type=(
            dns_start=float(json["dnsStart"]),
            document_url=str(json["documentURL"]),
            domain=str(json["domain"]) if "domain" in json else None,
            domain=str(json["domain"]),
            effective_directives=str(json["effectiveDirectives"]),
            encoded_data_length=float(json["encodedDataLength"]),
            encoded_data_length=int(json["encodedDataLength"]),
            encrypted_client_hello=bool(json["encryptedClientHello"]),
            endpoints=[ReportingApiEndpoint.from_json(i) for i in json["endpoints"]],
            error_field=(
            error_message=str(json["errorMessage"]),
            error_text=str(json["errorText"]),
            errors=(
            event_id=str(json["eventId"]),
            event_name=str(json["eventName"]),
            exempted_cookies=(
            exemption_reason=(
            exemption_reason=CookieExemptionReason.from_json(json["exemptionReason"]),
            expires=(
            expires=float(json["expires"]),
            expires=int(json["expires"]),
            failed_parameter=str(json["failedParameter"]),
            frame_id=(
            frame_id=page.FrameId.from_json(json["frameId"]),
            from_disk_cache=(
            from_early_hints=(
            from_prefetch_cache=(
            from_service_worker=(
            group_name=str(json["groupName"]),
            has_cross_site_ancestor=bool(json["hasCrossSiteAncestor"]),
            has_extra_info=bool(json["hasExtraInfo"]),
            has_post_data=bool(json["hasPostData"]) if "hasPostData" in json else None,
            has_user_gesture=(
            hash_algorithm=str(json["hashAlgorithm"]),
            header_integrity=str(json["headerIntegrity"]),
            header=(
            headers_text=str(json["headersText"]) if "headersText" in json else None,
            headers=(
            headers=Headers.from_json(json["headers"]),
            http_only=bool(json["httpOnly"]) if "httpOnly" in json else None,
            http_only=bool(json["httpOnly"]),
            http_status_code=(
            i.to_json() for i in self.signed_certificate_timestamp_list
            id_=ReportId.from_json(json["id"]),
            identifier=RequestId.from_json(json["identifier"]),
            include_credentials=bool(json["includeCredentials"]),
            info=SignedExchangeInfo.from_json(json["info"]),
            initial_priority=ResourcePriority.from_json(json["initialPriority"]),
            initiator_ip_address_space=IPAddressSpace.from_json(
            initiator_is_secure_context=bool(json["initiatorIsSecureContext"]),
            initiator_url=str(json["initiatorUrl"]),
            initiator=(
            initiator=Initiator.from_json(json["initiator"]),
            inner_request_id=RequestId.from_json(json["innerRequestId"]),
            inner_request_url=str(json["innerRequestURL"]),
            integrity=str(json["integrity"]),
            interception_id=InterceptionId.from_json(json["interceptionId"]),
            interception_stage=(
            is_download=bool(json["isDownload"]) if "isDownload" in json else None,
            is_enforced=bool(json["isEnforced"]),
            is_link_preload=(
            is_navigation_request=bool(json["isNavigationRequest"]),
            is_same_site=bool(json["isSameSite"]) if "isSameSite" in json else None,
            issued_token_count=(
            issuer_origin=str(json["issuerOrigin"]) if "issuerOrigin" in json else None,
            issuer=str(json["issuer"]),
            issuers=[str(i) for i in json["issuers"]] if "issuers" in json else None,
            json["actualSourceType"] = self.actual_source_type.to_json()
            json["alternateProtocolUsage"] = self.alternate_protocol_usage.to_json()
            json["bytes"] = self.bytes_
            json["cacheStorageCacheName"] = self.cache_storage_cache_name
            json["certificates"] = [i for i in self.certificates]
            json["certSha256"] = self.cert_sha256
            json["certUrl"] = self.cert_url
            json["coep"] = self.coep.to_json()
            json["columnNumber"] = self.column_number
            json["cookie"] = self.cookie.to_json()
            json["coop"] = self.coop.to_json()
            json["csp"] = [i.to_json() for i in self.csp]
            json["dnsQueryType"] = self.dns_query_type.to_json()
            json["domain"] = self.domain
            json["errorField"] = self.error_field.to_json()
            json["errors"] = [i.to_json() for i in self.errors]
            json["exemptionReason"] = self.exemption_reason.to_json()
            json["expires"] = self.expires.to_json()
            json["fromDiskCache"] = self.from_disk_cache
            json["fromEarlyHints"] = self.from_early_hints
            json["fromPrefetchCache"] = self.from_prefetch_cache
            json["fromServiceWorker"] = self.from_service_worker
            json["hasPostData"] = self.has_post_data
            json["header"] = self.header.to_json()
            json["headers"] = self.headers.to_json()
            json["headersText"] = self.headers_text
            json["httpOnly"] = self.http_only
            json["httpStatusCode"] = self.http_status_code
            json["interceptionStage"] = self.interception_stage.to_json()
            json["isLinkPreload"] = self.is_link_preload
            json["isSameSite"] = self.is_same_site
            json["issuers"] = [i for i in self.issuers]
            json["keepAliveDelay"] = self.keep_alive_delay
            json["keyExchangeGroup"] = self.key_exchange_group
            json["lineNumber"] = self.line_number
            json["mac"] = self.mac
            json["matchedSourceType"] = self.matched_source_type.to_json()
            json["mixedContentType"] = self.mixed_content_type.to_json()
            json["netError"] = self.net_error
            json["netErrorName"] = self.net_error_name
            json["partitionKey"] = self.partition_key.to_json()
            json["partitionKeyOpaque"] = self.partition_key_opaque
            json["password"] = self.password
            json["path"] = self.path
            json["postData"] = self.post_data
            json["postDataEntries"] = [i.to_json() for i in self.post_data_entries]
            json["priority"] = self.priority.to_json()
            json["protocol"] = self.protocol
            json["receiveBufferSize"] = self.receive_buffer_size
            json["remoteIPAddress"] = self.remote_ip_address
            json["remotePort"] = self.remote_port
            json["reportingEndpoint"] = self.reporting_endpoint
            json["reportOnlyReportingEndpoint"] = self.report_only_reporting_endpoint
            json["requestHeaders"] = self.request_headers.to_json()
            json["requestHeadersText"] = self.request_headers_text
            json["requestId"] = self.request_id.to_json()
            json["resourceType"] = self.resource_type.to_json()
            json["response"] = self.response.to_json()
            json["responseTime"] = self.response_time.to_json()
            json["ruleIdMatched"] = self.rule_id_matched
            json["sameParty"] = self.same_party
            json["sameSite"] = self.same_site.to_json()
            json["secure"] = self.secure
            json["securityDetails"] = self.security_details.to_json()
            json["sendBufferSize"] = self.send_buffer_size
            json["serverSignatureAlgorithm"] = self.server_signature_algorithm
            json["serviceWorkerResponseSource"] = (
            json["serviceWorkerRouterInfo"] = self.service_worker_router_info.to_json()
            json["signatureIndex"] = self.signature_index
            json["source"] = self.source
            json["sourcePort"] = self.source_port
            json["sourceScheme"] = self.source_scheme.to_json()
            json["stack"] = self.stack.to_json()
            json["stream"] = self.stream.to_json()
            json["timing"] = self.timing.to_json()
            json["trustTokenParams"] = self.trust_token_params.to_json()
            json["url"] = self.url
            json["urlFragment"] = self.url_fragment
            json["urlPattern"] = self.url_pattern
            json["username"] = self.username
            json["workerCacheLookupStart"] = self.worker_cache_lookup_start
            json["workerRouterEvaluationStart"] = self.worker_router_evaluation_start
            keep_alive_delay=(
            key_exchange_group=(
            key_exchange=str(json["keyExchange"]),
            label=str(json["label"]),
            line_number=float(json["lineNumber"]) if "lineNumber" in json else None,
            loader_id=LoaderId.from_json(json["loaderId"]),
            local_addr=str(json["localAddr"]) if "localAddr" in json else None,
            local_port=int(json["localPort"]) if "localPort" in json else None,
            log_description=str(json["logDescription"]),
            log_id=str(json["logId"]),
            mac=str(json["mac"]) if "mac" in json else None,
            mask=bool(json["mask"]),
            matched_source_type=(
            message=str(json["message"]),
            method=str(json["method"]),
            mime_type=str(json["mimeType"]),
            mixed_content_type=(
            name=str(json["name"]),
            net_error_name=(
            net_error=float(json["netError"]) if "netError" in json else None,
            new_priority=ResourcePriority.from_json(json["newPriority"]),
            no_delay=bool(json["noDelay"]),
            opcode=float(json["opcode"]),
            operation=TrustTokenOperationType.from_json(json["operation"]),
            options=DirectTCPSocketOptions.from_json(json["options"]),
            origin=str(json["origin"]),
            outer_response=Response.from_json(json["outerResponse"]),
            partition_key_opaque=(
            partition_key=(
            password=str(json["password"]) if "password" in json else None,
            path=str(json["path"]) if "path" in json else None,
            path=str(json["path"]),
            payload_data=str(json["payloadData"]),
            post_data_entries=(
            post_data=str(json["postData"]) if "postData" in json else None,
            priority=(
            priority=CookiePriority.from_json(json["priority"]),
            private_network_request_policy=PrivateNetworkRequestPolicy.from_json(
            protocol=str(json["protocol"]) if "protocol" in json else None,
            protocol=str(json["protocol"]),
            proxy_end=float(json["proxyEnd"]),
            proxy_start=float(json["proxyStart"]),
            push_end=float(json["pushEnd"]),
            push_start=float(json["pushStart"]),
            realm=str(json["realm"]),
            receive_buffer_size=(
            receive_headers_end=float(json["receiveHeadersEnd"]),
            receive_headers_start=float(json["receiveHeadersStart"]),
            redirect_has_extra_info=bool(json["redirectHasExtraInfo"]),
            redirect_response=(
            redirect_url=str(json["redirectUrl"]) if "redirectUrl" in json else None,
            referrer_policy=str(json["referrerPolicy"]),
            refresh_policy=str(json["refreshPolicy"]),
            remote_addr=str(json["remoteAddr"]),
            remote_ip_address=(
            remote_port=int(json["remotePort"]) if "remotePort" in json else None,
            remote_port=int(json["remotePort"]),
            report_only_reporting_endpoint=(
            report_only_value=CrossOriginEmbedderPolicyValue.from_json(
            report_only_value=CrossOriginOpenerPolicyValue.from_json(
            reporting_endpoint=(
            request_headers_text=(
            request_headers=(
            request_id=(
            request_id=RequestId.from_json(json["requestId"]),
            request_time=float(json["requestTime"]),
            request_url=str(json["requestUrl"]),
            request=Request.from_json(json["request"]),
            request=WebSocketRequest.from_json(json["request"]),
            resource_ip_address_space=IPAddressSpace.from_json(
            resource_type=(
            resource_type=ResourceType.from_json(json["resourceType"]),
            response_code=int(json["responseCode"]),
            response_error_reason=(
            response_headers=(
            response_headers=Headers.from_json(json["responseHeaders"]),
            response_status_code=(
            response_time=(
            response=(
            response=Response.from_json(json["response"]),
            response=str(json["response"]),
            response=WebSocketFrame.from_json(json["response"]),
            response=WebSocketResponse.from_json(json["response"]),
            rule_id_matched=(
            same_party=bool(json["sameParty"]) if "sameParty" in json else None,
            same_party=bool(json["sameParty"]),
            same_site=(
            san_list=[str(i) for i in json["sanList"]],
            scheme=str(json["scheme"]),
            secure=bool(json["secure"]) if "secure" in json else None,
            secure=bool(json["secure"]),
            security_details=(
            security_state=security.SecurityState.from_json(json["securityState"]),
            self.certificate_transparency_compliance.to_json()
            self.private_network_request_policy.to_json()
            send_buffer_size=(
            send_end=float(json["sendEnd"]),
            send_start=float(json["sendStart"]),
            server_signature_algorithm=(
            service_worker_response_source=(
            service_worker_router_info=(
            session=bool(json["session"]),
            signature_algorithm=str(json["signatureAlgorithm"]),
            signature_data=str(json["signatureData"]),
            signature_index=(
            signature=str(json["signature"]),
            signatures=[
            signed_certificate_timestamp_list=[
            site_has_cookie_in_other_partition=(
            size=int(json["size"]),
            source_port=int(json["sourcePort"]) if "sourcePort" in json else None,
            source_port=int(json["sourcePort"]),
            source_scheme=(
            source_scheme=CookieSourceScheme.from_json(json["sourceScheme"]),
            source=ContentSecurityPolicySource.from_json(json["source"]),
            source=str(json["source"]) if "source" in json else None,
            ssl_end=float(json["sslEnd"]),
            ssl_start=float(json["sslStart"]),
            stack=(
            status_code=int(json["statusCode"]),
            status_text=str(json["statusText"]),
            status=int(json["status"]),
            status=ReportStatus.from_json(json["status"]),
            status=str(json["status"]),
            stream=(
            subject_name=str(json["subjectName"]),
            success=bool(json["success"]),
            timestamp=float(json["timestamp"]),
            timestamp=MonotonicTime.from_json(json["timestamp"]),
            timestamp=network.TimeSinceEpoch.from_json(json["timestamp"]),
            timing=(
            top_level_origin=(
            top_level_site=str(json["topLevelSite"]),
            transport_id=RequestId.from_json(json["transportId"]),
            trust_token_params=(
            type_=ResourceType.from_json(json["type"]) if "type" in json else None,
            type_=ResourceType.from_json(json["type"]),
            type_=str(json["type"]),
            type_=TrustTokenOperationType.from_json(json["type"]),
            url_fragment=str(json["urlFragment"]) if "urlFragment" in json else None,
            url_pattern=str(json["urlPattern"]) if "urlPattern" in json else None,
            url=str(json["url"]) if "url" in json else None,
            url=str(json["url"]),
            urls=[str(i) for i in json["urls"]],
            username=str(json["username"]) if "username" in json else None,
            valid_from=TimeSinceEpoch.from_json(json["validFrom"]),
            valid_to=TimeSinceEpoch.from_json(json["validTo"]),
            validity_url=str(json["validityUrl"]),
            value=CrossOriginEmbedderPolicyValue.from_json(json["value"]),
            value=CrossOriginOpenerPolicyValue.from_json(json["value"]),
            value=str(json["value"]),
            wall_time=TimeSinceEpoch.from_json(json["wallTime"]),
            worker_cache_lookup_start=(
            worker_fetch_start=float(json["workerFetchStart"]),
            worker_ready=float(json["workerReady"]),
            worker_respond_with_settled=float(json["workerRespondWithSettled"]),
            worker_router_evaluation_start=(
            worker_start=float(json["workerStart"]),
        "coop-sandboxed-iframe-cannot-navigate-to-coop-page"
        "corp-not-same-origin-after-defaulted-to-same-origin-by-coep"
        "corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip"
        "corp-not-same-origin-after-defaulted-to-same-origin-by-dip"
        "method": "Network.canClearBrowserCache",
        "method": "Network.canClearBrowserCookies",
        "method": "Network.canEmulateNetworkConditions",
        "method": "Network.clearAcceptedEncodingsOverride",
        "method": "Network.clearBrowserCache",
        "method": "Network.clearBrowserCookies",
        "method": "Network.continueInterceptedRequest",
        "method": "Network.deleteCookies",
        "method": "Network.disable",
        "method": "Network.emulateNetworkConditions",
        "method": "Network.enable",
        "method": "Network.enableReportingApi",
        "method": "Network.getAllCookies",
        "method": "Network.getCertificate",
        "method": "Network.getCookies",
        "method": "Network.getRequestPostData",
        "method": "Network.getResponseBody",
        "method": "Network.getResponseBodyForInterception",
        "method": "Network.getSecurityIsolationStatus",
        "method": "Network.loadNetworkResource",
        "method": "Network.replayXHR",
        "method": "Network.searchInResponseBody",
        "method": "Network.setAcceptedEncodings",
        "method": "Network.setAttachDebugStack",
        "method": "Network.setBlockedURLs",
        "method": "Network.setBypassServiceWorker",
        "method": "Network.setCacheDisabled",
        "method": "Network.setCookie",
        "method": "Network.setCookieControls",
        "method": "Network.setCookies",
        "method": "Network.setExtraHTTPHeaders",
        "method": "Network.setRequestInterception",
        "method": "Network.setUserAgentOverride",
        "method": "Network.streamResourceContent",
        "method": "Network.takeResponseBodyForInterceptionAsStream",
        "params": params,
        "PreflightMissingPrivateNetworkAccessId"
        "PreflightMissingPrivateNetworkAccessName"
        "PrivateNetworkAccessPermissionUnavailable"
        "SchemefulSameSiteUnspecifiedTreatedAsLax"
        )
        ]
        0. **body** - Response body.
        1. **base64Encoded** - True, if content was sent as base64.
        if self.actual_source_type is not None:
        if self.alternate_protocol_usage is not None:
        if self.bytes_ is not None:
        if self.cache_storage_cache_name is not None:
        if self.cert_sha256 is not None:
        if self.cert_url is not None:
        if self.certificates is not None:
        if self.coep is not None:
        if self.column_number is not None:
        if self.cookie is not None:
        if self.coop is not None:
        if self.csp is not None:
        if self.dns_query_type is not None:
        if self.domain is not None:
        if self.error_field is not None:
        if self.errors is not None:
        if self.exemption_reason is not None:
        if self.expires is not None:
        if self.from_disk_cache is not None:
        if self.from_early_hints is not None:
        if self.from_prefetch_cache is not None:
        if self.from_service_worker is not None:
        if self.has_post_data is not None:
        if self.header is not None:
        if self.headers is not None:
        if self.headers_text is not None:
        if self.http_only is not None:
        if self.http_status_code is not None:
        if self.interception_stage is not None:
        if self.is_link_preload is not None:
        if self.is_same_site is not None:
        if self.issuers is not None:
        if self.keep_alive_delay is not None:
        if self.key_exchange_group is not None:
        if self.line_number is not None:
        if self.mac is not None:
        if self.matched_source_type is not None:
        if self.mixed_content_type is not None:
        if self.net_error is not None:
        if self.net_error_name is not None:
        if self.partition_key is not None:
        if self.partition_key_opaque is not None:
        if self.password is not None:
        if self.path is not None:
        if self.post_data is not None:
        if self.post_data_entries is not None:
        if self.priority is not None:
        if self.protocol is not None:
        if self.receive_buffer_size is not None:
        if self.remote_ip_address is not None:
        if self.remote_port is not None:
        if self.report_only_reporting_endpoint is not None:
        if self.reporting_endpoint is not None:
        if self.request_headers is not None:
        if self.request_headers_text is not None:
        if self.request_id is not None:
        if self.resource_type is not None:
        if self.response is not None:
        if self.response_time is not None:
        if self.rule_id_matched is not None:
        if self.same_party is not None:
        if self.same_site is not None:
        if self.secure is not None:
        if self.security_details is not None:
        if self.send_buffer_size is not None:
        if self.server_signature_algorithm is not None:
        if self.service_worker_response_source is not None:
        if self.service_worker_router_info is not None:
        if self.signature_index is not None:
        if self.source is not None:
        if self.source_port is not None:
        if self.source_scheme is not None:
        if self.stack is not None:
        if self.stream is not None:
        if self.timing is not None:
        if self.trust_token_params is not None:
        if self.url is not None:
        if self.url_fragment is not None:
        if self.url_pattern is not None:
        if self.username is not None:
        if self.worker_cache_lookup_start is not None:
        if self.worker_router_evaluation_start is not None:
        json = dict()
        json["blockedReasons"] = [i.to_json() for i in self.blocked_reasons]
        json["body"] = self.body
        json["bodySize"] = self.body_size
        json["certificateId"] = self.certificate_id.to_json()
        json["certificateTransparencyCompliance"] = (
        json["charset"] = self.charset
        json["cipher"] = self.cipher
        json["completedAttempts"] = self.completed_attempts
        json["connectEnd"] = self.connect_end
        json["connectionId"] = self.connection_id
        json["connectionReused"] = self.connection_reused
        json["connectStart"] = self.connect_start
        json["cookie"] = self.cookie.to_json()
        json["cookieLine"] = self.cookie_line
        json["corsError"] = self.cors_error.to_json()
        json["date"] = self.date
        json["depth"] = self.depth
        json["destination"] = self.destination
        json["disableCache"] = self.disable_cache
        json["dnsEnd"] = self.dns_end
        json["dnsStart"] = self.dns_start
        json["domain"] = self.domain
        json["effectiveDirectives"] = self.effective_directives
        json["encodedDataLength"] = self.encoded_data_length
        json["encryptedClientHello"] = self.encrypted_client_hello
        json["exemptionReason"] = self.exemption_reason.to_json()
        json["expires"] = self.expires
        json["failedParameter"] = self.failed_parameter
        json["groupName"] = self.group_name
        json["hasCrossSiteAncestor"] = self.has_cross_site_ancestor
        json["hashAlgorithm"] = self.hash_algorithm
        json["headerIntegrity"] = self.header_integrity
        json["headers"] = self.headers.to_json()
        json["httpOnly"] = self.http_only
        json["id"] = self.id_.to_json()
        json["includeCredentials"] = self.include_credentials
        json["initialPriority"] = self.initial_priority.to_json()
        json["initiatorIPAddressSpace"] = self.initiator_ip_address_space.to_json()
        json["initiatorIsSecureContext"] = self.initiator_is_secure_context
        json["initiatorUrl"] = self.initiator_url
        json["integrity"] = self.integrity
        json["isEnforced"] = self.is_enforced
        json["issuer"] = self.issuer
        json["keyExchange"] = self.key_exchange
        json["label"] = self.label
        json["logDescription"] = self.log_description
        json["logId"] = self.log_id
        json["mask"] = self.mask
        json["message"] = self.message
        json["method"] = self.method
        json["mimeType"] = self.mime_type
        json["name"] = self.name
        json["noDelay"] = self.no_delay
        json["opcode"] = self.opcode
        json["operation"] = self.operation.to_json()
        json["origin"] = self.origin
        json["outerResponse"] = self.outer_response.to_json()
        json["path"] = self.path
        json["payloadData"] = self.payload_data
        json["priority"] = self.priority.to_json()
        json["privateNetworkRequestPolicy"] = (
        json["protocol"] = self.protocol
        json["proxyEnd"] = self.proxy_end
        json["proxyStart"] = self.proxy_start
        json["pushEnd"] = self.push_end
        json["pushStart"] = self.push_start
        json["realm"] = self.realm
        json["receiveHeadersEnd"] = self.receive_headers_end
        json["receiveHeadersStart"] = self.receive_headers_start
        json["referrerPolicy"] = self.referrer_policy
        json["refreshPolicy"] = self.refresh_policy
        json["reportOnlyValue"] = self.report_only_value.to_json()
        json["requestTime"] = self.request_time
        json["requestUrl"] = self.request_url
        json["response"] = self.response
        json["responseCode"] = self.response_code
        json["responseHeaders"] = self.response_headers.to_json()
        json["sameParty"] = self.same_party
        json["sanList"] = [i for i in self.san_list]
        json["scheme"] = self.scheme
        json["secure"] = self.secure
        json["securityState"] = self.security_state.to_json()
        json["sendEnd"] = self.send_end
        json["sendStart"] = self.send_start
        json["session"] = self.session
        json["signature"] = self.signature
        json["signatureAlgorithm"] = self.signature_algorithm
        json["signatureData"] = self.signature_data
        json["signatures"] = [i.to_json() for i in self.signatures]
        json["signedCertificateTimestampList"] = [
        json["size"] = self.size
        json["source"] = self.source.to_json()
        json["sourcePort"] = self.source_port
        json["sourceScheme"] = self.source_scheme.to_json()
        json["sslEnd"] = self.ssl_end
        json["sslStart"] = self.ssl_start
        json["status"] = self.status
        json["status"] = self.status.to_json()
        json["statusText"] = self.status_text
        json["subjectName"] = self.subject_name
        json["success"] = self.success
        json["timestamp"] = self.timestamp
        json["timestamp"] = self.timestamp.to_json()
        json["topLevelSite"] = self.top_level_site
        json["type"] = self.type_
        json["type"] = self.type_.to_json()
        json["url"] = self.url
        json["validFrom"] = self.valid_from.to_json()
        json["validityUrl"] = self.validity_url
        json["validTo"] = self.valid_to.to_json()
        json["value"] = self.value
        json["value"] = self.value.to_json()
        json["workerFetchStart"] = self.worker_fetch_start
        json["workerReady"] = self.worker_ready
        json["workerRespondWithSettled"] = self.worker_respond_with_settled
        json["workerStart"] = self.worker_start
        params["acceptLanguage"] = accept_language
        params["authChallengeResponse"] = auth_challenge_response.to_json()
        params["caseSensitive"] = case_sensitive
        params["connectionType"] = connection_type.to_json()
        params["domain"] = domain
        params["errorReason"] = error_reason.to_json()
        params["expires"] = expires.to_json()
        params["frameId"] = frame_id.to_json()
        params["headers"] = headers.to_json()
        params["httpOnly"] = http_only
        params["isRegex"] = is_regex
        params["maxPostDataSize"] = max_post_data_size
        params["maxResourceBufferSize"] = max_resource_buffer_size
        params["maxTotalBufferSize"] = max_total_buffer_size
        params["method"] = method
        params["packetLoss"] = packet_loss
        params["packetQueueLength"] = packet_queue_length
        params["packetReordering"] = packet_reordering
        params["partitionKey"] = partition_key.to_json()
        params["path"] = path
        params["platform"] = platform
        params["postData"] = post_data
        params["priority"] = priority.to_json()
        params["rawResponse"] = raw_response
        params["sameParty"] = same_party
        params["sameSite"] = same_site.to_json()
        params["secure"] = secure
        params["sourcePort"] = source_port
        params["sourceScheme"] = source_scheme.to_json()
        params["url"] = url
        params["urls"] = [i for i in urls]
        params["userAgentMetadata"] = user_agent_metadata.to_json()
        return "Headers({})".format(super().__repr__())
        return "InterceptionId({})".format(super().__repr__())
        return "LoaderId({})".format(super().__repr__())
        return "MonotonicTime({})".format(super().__repr__())
        return "ReportId({})".format(super().__repr__())
        return "RequestId({})".format(super().__repr__())
        return "TimeSinceEpoch({})".format(super().__repr__())
        return cls(
        return cls()
        return cls(json)
        return cls(report=ReportingApiReport.from_json(json["report"]))
        return cls(request_id=RequestId.from_json(json["requestId"]))
        return json
        return self
        return self.value
    """
    #: (EC)DH group used by the connection, if applicable.
    #: A list of cookies potentially associated to the requested URL. This includes both cookies sent with
    #: A list of cookies which should have been blocked by 3PCD but are exempted and stored from
    #: A list of cookies which were not stored from the response along with the corresponding
    #: A list of URLs of resources in the subresource Web Bundle.
    #: Actual bytes received (might be less than dataLength for compressed encodings).
    #: after webbundle was parsed.
    #: 'AlreadyExists' also signifies a successful operation, as the result
    #: An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
    #: applicable or not known.
    #: are represented by the invalid cookie line string instead of a proper cookie.
    #: authentication or display a popup dialog box.
    #: available, such as in the case of HTTP/2 or QUIC.
    #: backslash. Omitting is equivalent to ``"*"``.
    #: be set, otherwiser no value will be set.
    #: Bundle request identifier. Used to match this information to another event.
    #: Cache Storage Cache Name.
    #: Cached response body size.
    #: Cached response data.
    #: Certificate ID value.
    #: Certificate subject name.
    #: Certificate valid from date.
    #: Certificate valid to (expiration) date
    #: Cipher name.
    #: concatentated using ``\n`` as the separator.
    #: Connected to the remote host.
    #: Connection timing information for the request.
    #: continueInterceptedRequest must contain an authChallengeResponse.
    #: Cookie domain.
    #: Cookie expiration date as the number of seconds since the UNIX epoch.
    #: Cookie expiration date, session cookie if not set
    #: Cookie name.
    #: Cookie partition key.
    #: Cookie partition key. If not set, the cookie will be set as not partitioned.
    #: Cookie path.
    #: Cookie Priority
    #: Cookie Priority.
    #: Cookie SameSite type.
    #: Cookie size.
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
    #: Cookie source scheme type.
    #: Cookie value.
    #: Data chunk length.
    #: Data that was received.
    #: default domain, path, source port, and source scheme values of the created cookie.
    #: deferring to the default behavior of the net stack, which will likely either the Cancel
    #: Detailed success or error status of the operation.
    #: Details of the Authorization Challenge encountered. If this is set then
    #: Duplicate headers in the response are represented as a single key with their values
    #: Each request the page makes will have a unique id, however if any redirects are encountered
    #: Error message
    #: Error message.
    #: Error message. List of network errors: https://cs.chromium.org/chromium/src/net/base/net_error_list.h
    #: Errors occurred while handling the signed exchange.
    #: errors.
    #: established the connection, so we can't send it in ``requestWillBeSentExtraInfo``.
    #: event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code
    #: Expected to be unsigned integer.
    #: field is set with ``matchedSourceType`` field, a matching rule is found.
    #: field will be set, otherwise no value will be set.
    #: Finished DNS address resolve.
    #: Finished receiving response headers.
    #: Finished resolving proxy.
    #: Finished sending request.
    #: Finished SSL handshake.
    #: Finished Starting ServiceWorker.
    #: for cached requests, where the status in responseReceived is a 200 and this will be 304.
    #: for the request which was just redirected.
    #: Fragment of the requested URL starting with hash, if present.
    #: Frame identifier.
    #: Hash algorithm.
    #: How many uploads deep the related request was.
    #: How the requested resource will be used.
    #: HTTP POST request data.
    #: HTTP request headers text.
    #: HTTP request headers text. This has been replaced by the headers in Network.requestWillBeSentExtraInfo.
    #: HTTP request headers.
    #: HTTP request method.
    #: HTTP response headers text.
    #: HTTP response headers text. This has been replaced by the headers in Network.responseReceivedExtraInfo.
    #: HTTP response headers.
    #: HTTP response status code.
    #: HTTP response status text.
    #: ID of the rule matched. If there is a matched rule, this field will
    #: If set, only requests for matching resource types will be intercepted.
    #: If successful, one of the following two fields holds the result.
    #: If the intercepted request had a corresponding requestWillBeSent event fired for it, then
    #: If the opcode is 1, this is a text message and payloadData is a UTF-8 string.
    #: If the opcode isn't 1, then payloadData is a base64 encoded string representing binary data.
    #: If this field is set without ``matchedSource``, no matching rule is found.
    #: In the case that redirectResponse is populated, this flag indicates whether
    #: Indicates if the cookie has any ancestors that are cross-site to the topLevelSite.
    #: Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be
    #: Information about how ServiceWorker Static Router API was used. If this
    #: Information about the signed exchange header.
    #: Information about the signed exchange response.
    #: Initiator column number, set for Parser type or for Script type (when script is importing
    #: Initiator JavaScript stack trace, set for Script only.
    #: Initiator line number, set for Parser type or for Script type (when script is importing
    #: Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.
    #: intercepting request or auth retry occurred.
    #: Issuance date. Unlike TimeSinceEpoch, this contains the number of
    #: Key Exchange used by the connection, or the empty string if not applicable.
    #: Likewise if HTTP authentication is needed then the same fetch id will be used.
    #: List of signed certificate timestamps (SCTs).
    #: Loader identifier. Empty string if the request is fetched from worker.
    #: Log ID.
    #: Log name / description.
    #: Message content.
    #: Message identifier.
    #: Message type.
    #: milliseconds relatively to this requestTime.
    #: milliseconds relatively to this requestTime. Matches ResourceTiming's requestTime for
    #: milliseconds since January 1, 1970, UTC, not the number of seconds.
    #: module) (0-based).
    #: Name of the endpoint group.
    #: Name of the issuing CA.
    #: New priority
    #: of the operation already exists und thus, the operation was abort
    #: of the request to the endpoint that set the cookie.
    #: only have at most one exemption reason.
    #: Only present after response is received from the server (i.e. HeadersReceived stage).
    #: Only sent when partitioned cookies are enabled.
    #: Only set for "token-redemption" operation and determine whether
    #: Optional values used for error reporting.
    #: or were emitted for this request.
    #: Origin of the challenger.
    #: Origin of the document(s) which configured the endpoints.
    #: Origin of the issuer in case of a "Issuance" or "Redemption" operation.
    #: Origin.
    #: Origins of issuers from whom to request tokens or redemption
    #: Otherwise, the API is not used.
    #: passed by the developer (e.g. via "fetch") as understood by the backend.
    #: Physical connection id that was actually used for this request.
    #: preemptively (e.g. a cache hit).
    #: Priority of the resource request at the time request is sent.
    #: Protocol name (e.g. "TLS 1.2" or "QUIC").
    #: Protocol used to fetch this request.
    #: ProvideCredentials.
    #: Raw request headers as they will be sent over the wire.
    #: Raw response header text as it was received over the wire. The raw text may not always be
    #: Raw response headers as they were received over the wire.
    #: reasons for blocking. The cookies here may not be valid due to syntax errors, which
    #: records.
    #: Redirect location, only sent if a redirect was intercepted.
    #: Redirect response data.
    #: Refined HTTP request headers that were actually transmitted over the network.
    #: Remote IP address.
    #: Remote port.
    #: represented as a TLS SignatureScheme code point. Omitted if not
    #: Request body elements (post data broken into individual entries).
    #: request corresponding to the main frame.
    #: Request data.
    #: Request identifier of the subresource request
    #: Request identifier.
    #: Request identifier. Used to match this information to an existing requestWillBeSent event.
    #: Request identifier. Used to match this information to another event.
    #: Request identifier. Used to match this information to another responseReceived event.
    #: Request initiator.
    #: request or auth retry occurred.
    #: Request URL (without fragment).
    #: request.
    #: requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted
    #: Requires the Debugger domain to be enabled.
    #: Resource charset as determined by the browser (if applicable).
    #: Resource mimeType as determined by the browser.
    #: Resource type.
    #: Resource URL. This is the url of the original network request.
    #: Response code if intercepted at response stage or if redirect occurred while intercepting
    #: Response data.
    #: Response error if intercepted at response stage or if redirect occurred while intercepting
    #: Response headers if intercepted at the response stage or if redirect occurred while
    #: Response headers.
    #: Response source of response from ServiceWorker.
    #: Response URL. This URL can be different from CachedResource.url in case of redirect.
    #: Security details for the request.
    #: Security details for the signed exchange header.
    #: Security state of the request resource.
    #: See also ``headersText`` that contains verbatim text for HTTP/1.*.
    #: Set for requests when the TrustToken API is used. Contains the parameters
    #: Set if another request triggered this request (e.g. preflight).
    #: Set if the request is a navigation that will result in a download.
    #: Settled fetch event respondWith promise.
    #: Signature algorithm.
    #: Signature data.
    #: Signed exchange header integrity hash in the form of ``sha256-<base64-hash-value>``.
    #: Signed exchange request URL.
    #: Signed exchange response code.
    #: Signed exchange response headers.
    #: Signed exchange response signature.
    #: Signed exchange signature cert Url.
    #: Signed exchange signature date.
    #: Signed exchange signature expires.
    #: Signed exchange signature integrity.
    #: Signed exchange signature label.
    #: Signed exchange signature validity Url.
    #: sometimes complete cookie information is not available, such as in the case of parsing
    #: Source of the authentication challenge.
    #: Specifies that the request was served from the disk cache.
    #: Specifies that the request was served from the prefetch cache.
    #: Specifies that the request was served from the ServiceWorker.
    #: Specifies whether physical connection was actually reused for this request.
    #: Stage at which to begin intercepting requests. Default is Request.
    #: Started cache lookup when the source was evaluated to ``cache``.
    #: Started connecting to the remote host.
    #: Started DNS address resolve.
    #: Started fetch event.
    #: Started receiving response headers.
    #: Started resolving proxy.
    #: Started running ServiceWorker.
    #: Started sending request.
    #: Started ServiceWorker static routing source evaluation.
    #: Started SSL handshake.
    #: Subject Alternative Name (SAN) DNS names and IP addresses.
    #: TCP_NODELAY option
    #: The actual router source used.
    #: The authentication scheme used, such as basic or digest
    #: The client security state set for the request.
    #: The cookie object representing the cookie which was not sent.
    #: The cookie object representing the cookie.
    #: The cookie object which represents the cookie which was not stored. It is optional because
    #: The cookie partition key that will be used to store partitioned cookies set in this response.
    #: The decision on what to do in response to the authorization challenge.  Default means
    #: The encoded certificates.
    #: The field which caused the error.
    #: The hex string of signed exchange signature cert sha256.
    #: The hex string of signed exchange signature.
    #: The id of the frame that initiated the request.
    #: The index of the signature which caused the error.
    #: The IP address space of the resource. The address space can only be determined once the transport
    #: The mixed content type of the request.
    #: The name of the endpoint group that should be used to deliver the report.
    #: The number of delivery attempts made so far, not including an active attempt.
    #: The number of obtained Trust Tokens on a successful "Issuance" operation.
    #: The outer response of signed HTTP exchange which was received from network.
    #: The password to provide, possibly empty. Should only be set if response is
    #: The realm of the challenge. May be empty.
    #: The reason the cookie should have been blocked by 3PCD but is exempted. A cookie could
    #: The reason the cookie was exempted.
    #: The reason why Chrome uses a specific transport protocol for HTTP semantics.
    #: The reason why loading was blocked by CORS, if any.
    #: The reason why loading was blocked, if any.
    #: The reason(s) the cookie was blocked. If empty means the cookie is included.
    #: The reason(s) this cookie was blocked.
    #: The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/
    #: the request and the ones not sent; the latter are distinguished by having blockedReasons field set.
    #: The request-URI to associate with the setting of the cookie. This value can affect the
    #: the response with the corresponding reason.
    #: The router source of the matched rule. If there is a matched rule, this
    #: the same request (but not for redirected requests).
    #: The signature algorithm used by the server in the TLS server signature,
    #: The site of the top-level URL the browser was visiting at the start
    #: The status code of the response. This is useful in cases the request failed and no responseReceived
    #: The string representing this individual cookie as it would appear in the header.
    #: The time at which the returned response was generated.
    #: The type of the report (specifies the set of data that is contained in the report body).
    #: The URL of the document that triggered the report.
    #: The URL of the endpoint to which reports may be delivered.
    #: The username to provide, possibly empty. Should only be set if response is
    #: This is a temporary ability and it will be removed in the future.
    #: This is not the entire "cookie" or "set-cookie" header which could have multiple cookies.
    #: This made be absent in case when the instrumentation was enabled only
    #: this requestId will be the same as the requestId present in the requestWillBeSent event.
    #: Time the server finished pushing request.
    #: Time the server started pushing request.
    #: Timestamp.
    #: Timing information for the given request.
    #: Timing's requestTime is a baseline in seconds, while the other numbers are ticks in
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.
    #: to request a fresh SRR or use a still valid cached SRR.
    #: Top level origin. The context in which the operation was attempted.
    #: Total number of bytes received for this request so far.
    #: Total number of bytes received for this request.
    #: True if cookie is http-only.
    #: True if cookie is SameParty.
    #: True if cookie is secure.
    #: True if cookie partition key is opaque.
    #: True if loading was canceled.
    #: True if partitioned cookies are enabled, but the partition key is not serializable to string.
    #: True if this resource request is considered to be the 'same site' as the
    #: True in case of session cookie.
    #: True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.
    #: Type of this initiator.
    #: Type of this resource.
    #: Unsigned int 16.
    #: URL of the document this request is loaded for.
    #: URL of the subresource resource.
    #: Use postDataEntries instead.
    #: UTC Timestamp.
    #: Validation status.
    #: WebSocket error message.
    #: WebSocket message mask.
    #: WebSocket message opcode.
    #: WebSocket message payload data.
    #: WebSocket request data.
    #: WebSocket request URL.
    #: WebSocket response data.
    #: WebTransport identifier.
    #: WebTransport request URL.
    #: When the report was generated.
    #: Whether is loaded via link preload.
    #: Whether the connection used Encrypted ClientHello
    #: Whether the request complied with Certificate Transparency policy
    #: Whether the request is initiated by a user gesture. Defaults to false.
    #: Whether the site has partitioned cookies stored in a partition different than the current one.
    #: Whether this is a navigation request, which can abort the navigation completely.
    #: while processing that fetch, they will be reported with the same id as the original fetch.
    #: Wildcards (``'*'`` -> zero or more, ``'?'`` -> exactly one) are allowed. Escape character is
    )
    **EXPERIMENTAL**
    :param accept_language: *(Optional)* Browser language to emulate.
    :param auth_challenge_response: *(Optional)* Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
    :param bypass: Bypass service worker and load from network.
    :param cache_disabled: Cache disabled state.
    :param case_sensitive: *(Optional)* If true, search is case sensitive.
    :param connection_type: *(Optional)* Connection type if known.
    :param cookies: Cookies to be set.
    :param disable_third_party_cookie_heuristics: Whether 3pc heuristics exceptions should be enabled; false by default.
    :param disable_third_party_cookie_metadata: Whether 3pc grace period exception should be enabled; false by default.
    :param domain: *(Optional)* Cookie domain.
    :param domain: *(Optional)* If specified, deletes only cookies with the exact domain.
    :param download_throughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
    :param enable: Whether to enable or disable events for the Reporting API
    :param enable_third_party_cookie_restriction: Whether 3pc restriction is enabled.
    :param enabled: Whether to attach a page script stack for debugging purpose.
    :param encodings: List of accepted content encodings.
    :param error_reason: *(Optional)* If set this causes the request to fail with the given reason. Passing ```Aborted```` for requests marked with ````isNavigationRequest``` also cancels the navigation. Must not be set in response to an authChallenge.
    :param expires: *(Optional)* Cookie expiration date, session cookie if not set
    :param frame_id: *(Optional)* Frame id to get the resource for. Mandatory for frame targets, and should be omitted for worker targets.
    :param frame_id: *(Optional)* If no frameId is provided, the status of the target is provided.
    :param headers: *(Optional)* If set this allows the request headers to be changed. Must not be set in response to an authChallenge.
    :param headers: Map with extra HTTP headers.
    :param http_only: *(Optional)* True if cookie is http-only.
    :param interception_id:
    :param interception_id: Identifier for the intercepted request to get body for.
    :param is_regex: *(Optional)* If true, treats string parameter as regex.
    :param latency: Minimum latency from request sent to response headers received (ms).
    :param max_post_data_size: *(Optional)* Longest post body size (in bytes) that would be included in requestWillBeSent notification
    :param max_resource_buffer_size: **(EXPERIMENTAL)** *(Optional)* Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
    :param max_total_buffer_size: **(EXPERIMENTAL)** *(Optional)* Buffer size in bytes to use when preserving network payloads (XHRs, etc).
    :param method: *(Optional)* If set this allows the request method to be overridden. Must not be set in response to an authChallenge.
    :param name: Cookie name.
    :param name: Name of the cookies to remove.
    :param offline: True to emulate internet disconnection.
    :param options: Options for the request.
    :param origin: Origin to get certificate for.
    :param packet_loss: **(EXPERIMENTAL)** *(Optional)* WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets.
    :param packet_queue_length: **(EXPERIMENTAL)** *(Optional)* WebRTC packet queue length (packet). 0 removes any queue length limitations.
    :param packet_reordering: **(EXPERIMENTAL)** *(Optional)* WebRTC packetReordering feature.
    :param partition_key: **(EXPERIMENTAL)** *(Optional)* Cookie partition key. If not set, the cookie will be set as not partitioned.
    :param partition_key: **(EXPERIMENTAL)** *(Optional)* If specified, deletes only cookies with the the given name and partitionKey where all partition key attributes match the cookie partition key attribute.
    :param path: *(Optional)* Cookie path.
    :param path: *(Optional)* If specified, deletes only cookies with the exact path.
    :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call.
    :param platform: *(Optional)* The platform navigator.platform should return.
    :param post_data: *(Optional)* If set this allows postData to be set. Must not be set in response to an authChallenge.
    :param priority: **(EXPERIMENTAL)** *(Optional)* Cookie Priority type.
    :param query: String to search for.
    :param raw_response: *(Optional)* If set the requests completes using with the provided base64 encoded raw response, including HTTP status line and headers etc... Must not be set in response to an authChallenge.
    :param request_id: Identifier of the network request to get content for.
    :param request_id: Identifier of the network response to search.
    :param request_id: Identifier of the request to stream.
    :param request_id: Identifier of XHR to replay.
    :param same_party: **(EXPERIMENTAL)** *(Optional)* True if cookie is SameParty.
    :param same_site: *(Optional)* Cookie SameSite type.
    :param secure: *(Optional)* True if cookie is secure.
    :param source_port: **(EXPERIMENTAL)** *(Optional)* Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future.
    :param source_scheme: **(EXPERIMENTAL)** *(Optional)* Cookie source scheme type.
    :param upload_throughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
    :param url: *(Optional)* If set the request url will be modified in a way that's not observable by page. Must not be set in response to an authChallenge.
    :param url: *(Optional)* If specified, deletes all the cookies with the given name where domain and path match provided URL.
    :param url: *(Optional)* The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie.
    :param url: URL of the resource to get content for.
    :param urls: *(Optional)* The list of URLs for which applicable cookies will be fetched. If not specified, it's assumed to be set to the list containing the URLs of the page and all of its subframes.
    :param urls: URL patterns to block. Wildcards ('*') are allowed.
    :param user_agent: User agent to use.
    :param user_agent_metadata: **(EXPERIMENTAL)** *(Optional)* To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
    :param value: Cookie value.
    :returns:
    :returns: A tuple with the following items:
    :returns: Always set to true. If an error occurs, the response indicates protocol error.
    :returns: Array of cookie objects.
    :returns: Data that has been buffered until streaming is enabled.
    :returns: List of search matches.
    :returns: Request body string, omitting files from multipart requests
    :returns: True if browser cache can be cleared.
    :returns: True if browser cookies can be cleared.
    :returns: True if emulation of network conditions is supported.
    @classmethod
    }
    A cookie associated with the request which may or may not be sent with it.
    A cookie should have been blocked by 3PCD but is exempted and stored from a response with the
    A cookie which was not stored from a response with the corresponding reason.
    a network request.
    A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme.
    ABORTED = "Aborted"
    accept_language: str | None = None,
    ACCESS_DENIED = "AccessDenied"
    Activates emulation of network conditions.
    actual_source_type: ServiceWorkerRouterSource | None = None
    ADDRESS_UNREACHABLE = "AddressUnreachable"
    ALLOW = "Allow"
    ALLOW_ORIGIN_MISMATCH = "AllowOriginMismatch"
    Allows overriding user agent with the given string.
    alternate_protocol_usage: AlternateProtocolUsage | None = None
    ALTERNATIVE_JOB_WON_RACE = "alternativeJobWonRace"
    ALTERNATIVE_JOB_WON_WITHOUT_RACE = "alternativeJobWonWithoutRace"
    An object providing the result of a network resource load.
    An object representing a report generated by the Reporting API.
    An options object that may be extended later to better support CORS,
    And after 'enableReportingApi' for all existing reports.
    ANONYMOUS_CONTEXT = "AnonymousContext"
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    associated_cookies: list[AssociatedCookie]
    attribute, user, password.
    auth_challenge: AuthChallenge | None
    auth_challenge_response: AuthChallengeResponse | None = None,
    Authorization challenge for HTTP status code 401 or 407.
    BLOCK_FROM_INSECURE_TO_MORE_PRIVATE = "BlockFromInsecureToMorePrivate"
    BLOCKED_BY_CLIENT = "BlockedByClient"
    BLOCKED_BY_RESPONSE = "BlockedByResponse"
    blocked_cookies: list[BlockedSetCookieWithReason]
    blocked_reason: BlockedReason | None
    blocked_reasons: list[CookieBlockedReason]
    blocked_reasons: list[SetCookieBlockedReason]
    Blocks URLs from loading.
    BLUETOOTH = "bluetooth"
    body: dict
    body_size: float
    BR = "br"
    BROKEN = "broken"
    bundle_request_id: RequestId | None
    bypass: bool,
    bytes_: str | None = None
    CACHE = "cache"
    cache_disabled: bool,
    CACHE_STORAGE = "cache-storage"
    cache_storage_cache_name: str | None = None
    canceled: bool | None
    case_sensitive: bool | None = None,
    CELLULAR2G = "cellular2g"
    CELLULAR3G = "cellular3g"
    CELLULAR4G = "cellular4g"
    cert_sha256: str | None = None
    cert_url: str | None = None
    certificate_id: security.CertificateId
    certificate_transparency_compliance: CertificateTransparencyCompliance
    certificates: list[str] | None = None
    charset: str
    cipher: str
    Clears accepted encodings set by setAcceptedEncodings
    Clears browser cache.
    Clears browser cookies.
    client_security_state: ClientSecurityState | None
    cmd_dict: T_JSON_DICT = {
    coep: CrossOriginEmbedderPolicyStatus | None = None
    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "coep-frame-resource-needs-coep-header"
    column_number: float | None = None
    completed_attempts: int
    COMPLIANT = "compliant"
    connect_end: float
    connect_start: float
    connect_timing: ConnectTiming
    CONNECTION_ABORTED = "ConnectionAborted"
    CONNECTION_CLOSED = "ConnectionClosed"
    CONNECTION_FAILED = "ConnectionFailed"
    connection_id: float
    CONNECTION_REFUSED = "ConnectionRefused"
    CONNECTION_RESET = "ConnectionReset"
    connection_reused: bool
    connection_type: ConnectionType | None = None,
    CONTENT_TYPE = "content-type"
    Cookie object
    Cookie parameter object
    cookie: Cookie
    cookie: Cookie | None = None
    cookie_line: str
    cookie_partition_key: CookiePartitionKey | None
    cookie_partition_key_opaque: bool | None
    cookiePartitionKey object
    cookies: list[CookieParam],
    coop: CrossOriginOpenerPolicyStatus | None = None
    COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = (
    CORB and streaming.
    CORP_NOT_SAME_ORIGIN = "corp-not-same-origin"
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP_AND_DIP = (
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_DIP = (
    CORP_NOT_SAME_SITE = "corp-not-same-site"
    corresponding reason. A cookie could only have at most one exemption reason.
    CORS_DISABLED_SCHEME = "CorsDisabledScheme"
    cors_error: CorsError
    cors_error_status: CorsErrorStatus | None
    CREDENTIALLESS = "Credentialless"
    CSP = "csp"
    csp: list[ContentSecurityPolicyStatus] | None = None
    CSP_VIOLATION_REPORT = "CSPViolationReport"
    data: str
    data: str | None
    data_length: int
    date: int
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: dict) -> Headers:
    def from_json(cls, json: float) -> MonotonicTime:
    def from_json(cls, json: float) -> TimeSinceEpoch:
    def from_json(cls, json: str) -> InterceptionId:
    def from_json(cls, json: str) -> LoaderId:
    def from_json(cls, json: str) -> ReportId:
    def from_json(cls, json: str) -> RequestId:
    def from_json(cls, json: T_JSON_DICT) -> DataReceived:
    def from_json(cls, json: T_JSON_DICT) -> DirectTCPSocketAborted:
    def from_json(cls, json: T_JSON_DICT) -> DirectTCPSocketClosed:
    def from_json(cls, json: T_JSON_DICT) -> DirectTCPSocketCreated:
    def from_json(cls, json: T_JSON_DICT) -> DirectTCPSocketOpened:
    def from_json(cls, json: T_JSON_DICT) -> EventSourceMessageReceived:
    def from_json(cls, json: T_JSON_DICT) -> LoadingFailed:
    def from_json(cls, json: T_JSON_DICT) -> LoadingFinished:
    def from_json(cls, json: T_JSON_DICT) -> PolicyUpdated:
    def from_json(cls, json: T_JSON_DICT) -> ReportingApiEndpointsChangedForOrigin:
    def from_json(cls, json: T_JSON_DICT) -> ReportingApiReportAdded:
    def from_json(cls, json: T_JSON_DICT) -> ReportingApiReportUpdated:
    def from_json(cls, json: T_JSON_DICT) -> RequestIntercepted:
    def from_json(cls, json: T_JSON_DICT) -> RequestServedFromCache:
    def from_json(cls, json: T_JSON_DICT) -> RequestWillBeSent:
    def from_json(cls, json: T_JSON_DICT) -> RequestWillBeSentExtraInfo:
    def from_json(cls, json: T_JSON_DICT) -> ResourceChangedPriority:
    def from_json(cls, json: T_JSON_DICT) -> ResponseReceived:
    def from_json(cls, json: T_JSON_DICT) -> ResponseReceivedEarlyHints:
    def from_json(cls, json: T_JSON_DICT) -> ResponseReceivedExtraInfo:
    def from_json(cls, json: T_JSON_DICT) -> SignedExchangeReceived:
    def from_json(cls, json: T_JSON_DICT) -> SubresourceWebBundleInnerResponseError:
    def from_json(cls, json: T_JSON_DICT) -> SubresourceWebBundleInnerResponseParsed:
    def from_json(cls, json: T_JSON_DICT) -> SubresourceWebBundleMetadataError:
    def from_json(cls, json: T_JSON_DICT) -> SubresourceWebBundleMetadataReceived:
    def from_json(cls, json: T_JSON_DICT) -> TrustTokenOperationDone:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketClosed:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketCreated:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketFrameError:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketFrameReceived:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketFrameSent:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketHandshakeResponseReceived:
    def from_json(cls, json: T_JSON_DICT) -> WebSocketWillSendHandshakeRequest:
    def from_json(cls, json: T_JSON_DICT) -> WebTransportClosed:
    def from_json(cls, json: T_JSON_DICT) -> WebTransportConnectionEstablished:
    def from_json(cls, json: T_JSON_DICT) -> WebTransportCreated:
    def to_json(self) -> dict:
    def to_json(self) -> float:
    def to_json(self) -> str:
    def to_json(self):
    DEFLATE = "deflate"
    Deletes browser cookies with matching name and url or domain/path/partitionKey pair.
    depending on the type, some additional parameters. The values
    Deprecated, please use Fetch.enable instead.
    Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.
    Deprecated, use Fetch.requestPaused instead.
    Deprecated. Use Storage.getCookies instead.
    depth: int
    destination: str
    detailed cookie information in the ``cookies`` field.
    Details of a signed certificate timestamp (SCT).
    Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
    Determines what type of Trust Token operation is executed and
    disable_cache: bool
    disable_third_party_cookie_heuristics: bool,
    disable_third_party_cookie_metadata: bool,
    Disables network tracking, prevents network events from being sent to the client.
    DISALLOWED_BY_MODE = "DisallowedByMode"
    DISALLOWED_CHARACTER = "DisallowedCharacter"
    DNS_ALPN_H3_JOB_WON_RACE = "dnsAlpnH3JobWonRace"
    DNS_ALPN_H3_JOB_WON_WITHOUT_RACE = "dnsAlpnH3JobWonWithoutRace"
    dns_end: float
    dns_query_type: DirectSocketDnsQueryType | None = None
    dns_start: float
    DOCUMENT = "Document"
    document_url: str
    domain: str
    domain: str | None = None
    domain: str | None = None,
    DOMAIN_MISMATCH = "DomainMismatch"
    download_throughput: float,
    effective_directives: str
    enable: bool,
    enable_third_party_cookie_restriction: bool,
    enabled: bool,
    Enables network tracking, network events will now be delivered to the client.
    Enables streaming of the response for the given requestId.
    Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
    Enabling triggers 'reportingApiReportAdded' for all existing reports.
    encoded_data_length: float
    encoded_data_length: int
    encodings: list[ContentEncoding],
    encrypted_client_hello: bool
    endpoints: list[ReportingApiEndpoint]
    ENTERPRISE_POLICY = "EnterprisePolicy"
    error_field: SignedExchangeErrorField | None = None
    error_message: str
    error_reason: ErrorReason | None = None,
    error_text: str
    errors: list[SignedExchangeError] | None = None
    ETHERNET = "ethernet"
    event will be sent with the same InterceptionId.
    event_id: str
    event_name: str
    EVENT_SOURCE = "EventSource"
    exempted_cookies: list[ExemptedSetCookieWithReason] | None
    exemption_reason: CookieExemptionReason
    exemption_reason: CookieExemptionReason | None = None
    expires: float
    expires: int
    expires: TimeSinceEpoch | None = None
    expires: TimeSinceEpoch | None = None,
    FAILED = "Failed"
    failed, the event is fired before the corresponding request was sent
    failed_parameter: str
    FALLBACK_CODE = "fallback-code"
    FETCH = "Fetch"
    fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
    FETCH_EVENT = "fetch-event"
    Fetches the resource and returns the content.
    Field type for a signed exchange related error.
    Fired exactly once for each Trust Token operation. Depending on
    Fired if request ended up loading from cache.
    Fired once security policy has been updated.
    Fired once when parsing the .wbn file has failed.
    Fired once when parsing the .wbn file has succeeded.
    Fired upon direct_socket.TCPSocket creation.
    Fired upon WebSocket creation.
    Fired upon WebTransport creation.
    Fired when 103 Early Hints headers is received in addition to the common response.
    Fired when a signed exchange was received over the network
    Fired when additional information about a requestWillBeSent event is available from the
    Fired when additional information about a responseReceived event is available from the network
    Fired when data chunk was received over the network.
    Fired when direct_socket.TCPSocket connection is opened.
    Fired when direct_socket.TCPSocket is aborted.
    Fired when direct_socket.TCPSocket is closed.
    Fired when EventSource message is received.
    Fired when handling requests for resources within a .wbn file.
    Fired when HTTP request has failed to load.
    Fired when HTTP request has finished loading.
    Fired when HTTP response is available.
    Fired when page is about to send HTTP request.
    Fired when request for resources within a .wbn file failed.
    Fired when resource loading priority is changed
    Fired when WebSocket handshake response becomes available.
    Fired when WebSocket is about to initiate handshake.
    Fired when WebSocket is closed.
    Fired when WebSocket message error occurs.
    Fired when WebSocket message is received.
    Fired when WebSocket message is sent.
    Fired when WebTransport handshake is finished.
    Fired when WebTransport is disposed.
    FONT = "Font"
    frame_id: page.FrameId
    frame_id: page.FrameId | None
    frame_id: page.FrameId | None = None,
    from_disk_cache: bool | None = None
    from_early_hints: bool | None = None
    from_prefetch_cache: bool | None = None
    from_service_worker: bool | None = None
    group_name: str
    GZIP = "gzip"
    has_cross_site_ancestor: bool
    has_extra_info: bool
    has_post_data: bool | None = None
    has_user_gesture: bool | None
    hash_algorithm: str
    header: SignedExchangeHeader | None = None
    HEADER_DISALLOWED_BY_PREFLIGHT_RESPONSE = "HeaderDisallowedByPreflightResponse"
    header_integrity: str
    headers: Headers
    headers: Headers | None = None,
    headers: Headers,
    headers: network.Headers | None = None
    HEADERS_RECEIVED = "HeadersReceived"
    headers_text: str | None
    headers_text: str | None = None
    HIGH = "High"
    HTTP = "HTTP"
    HTTP request data.
    HTTP response data.
    HTTP_CACHE = "http-cache"
    http_only: bool
    http_only: bool | None = None
    http_only: bool | None = None,
    http_status_code: float | None = None
    https://tools.ietf.org/html/draft-west-cookie-priority-00
    https://tools.ietf.org/html/draft-west-first-party-cookies
    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    id_: ReportId
    identifier: RequestId
    if accept_language is not None:
    if auth_challenge_response is not None:
    if case_sensitive is not None:
    if connection_type is not None:
    if domain is not None:
    If enabled, the dataReceived event contains the data that was received during streaming.
    if error_reason is not None:
    if expires is not None:
    if frame_id is not None:
    if headers is not None:
    if http_only is not None:
    if is_regex is not None:
    if max_post_data_size is not None:
    if max_resource_buffer_size is not None:
    if max_total_buffer_size is not None:
    if method is not None:
    if packet_loss is not None:
    if packet_queue_length is not None:
    if packet_reordering is not None:
    if partition_key is not None:
    if path is not None:
    if platform is not None:
    if post_data is not None:
    if priority is not None:
    if raw_response is not None:
    if same_party is not None:
    if same_site is not None:
    if secure is not None:
    if source_port is not None:
    if source_scheme is not None:
    if url is not None:
    if urls is not None:
    if user_agent_metadata is not None:
    IMAGE = "Image"
    include_credentials: bool
    Includes the cookies itself and reasons for blocking or exemption.
    info: SignedExchangeInfo
    Information about a signed exchange header.
    Information about a signed exchange response.
    Information about a signed exchange signature.
    Information about the cached resource.
    Information about the request initiator.
    information in the ``cookies`` field.
    initial_priority: ResourcePriority
    initiator: Initiator
    initiator: Initiator | None
    initiator_ip_address_space: IPAddressSpace
    initiator_is_secure_context: bool
    initiator_url: str
    inner_request_id: RequestId
    inner_request_url: str
    INSECURE_PRIVATE_NETWORK = "InsecurePrivateNetwork"
    INSPECTOR = "inspector"
    integrity: str
    interception_id: InterceptionId
    interception_id: InterceptionId,
    interception_stage: InterceptionStage | None = None
    INTERNET_DISCONNECTED = "InternetDisconnected"
    INVALID_ALLOW_CREDENTIALS = "InvalidAllowCredentials"
    INVALID_ALLOW_HEADERS_PREFLIGHT_RESPONSE = "InvalidAllowHeadersPreflightResponse"
    INVALID_ALLOW_METHODS_PREFLIGHT_RESPONSE = "InvalidAllowMethodsPreflightResponse"
    INVALID_ALLOW_ORIGIN_VALUE = "InvalidAllowOriginValue"
    INVALID_DOMAIN = "InvalidDomain"
    INVALID_PREFIX = "InvalidPrefix"
    INVALID_PRIVATE_NETWORK_ACCESS = "InvalidPrivateNetworkAccess"
    INVALID_RESPONSE = "InvalidResponse"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    Is sent whenever a new report is added.
    is specified.
    is_download: bool | None
    is_enforced: bool
    is_link_preload: bool | None = None
    is_navigation_request: bool
    is_regex: bool | None = None,
    is_same_site: bool | None = None
    ISSUANCE = "Issuance"
    issued_token_count: int | None
    issuer: str
    issuer_origin: str | None
    issuers: list[str] | None = None
    it, and responseReceivedExtraInfo may be fired before or after responseReceived.
    json = yield cmd_dict
    keep_alive_delay: float | None = None
    key_exchange: str
    key_exchange_group: str | None = None
    label: str
    latency: float,
    LAX = "Lax"
    line_number: float | None = None
    List of content encodings supported by the backend.
    loader_id: LoaderId
    Loading priority of a resource request.
    LOCAL = "Local"
    local_addr: str | None
    LOCAL_NETWORK_ACCESS_PERMISSION_DENIED = "LocalNetworkAccessPermissionDenied"
    local_port: int | None
    log_description: str
    log_id: str
    LOW = "Low"
    mac: str | None = None
    MAIN_JOB_WON_RACE = "mainJobWonRace"
    MANIFEST = "Manifest"
    MAPPING_MISSING = "mappingMissing"
    MARKED_FOR_REMOVAL = "MarkedForRemoval"
    mask: bool
    matched_source_type: ServiceWorkerRouterSource | None = None
    max_post_data_size: int | None = None,
    max_resource_buffer_size: int | None = None,
    max_total_buffer_size: int | None = None,
    MEDIA = "Media"
    MEDIUM = "Medium"
    message: str
    META = "Meta"
    method: str
    method: str | None = None,
    METHOD_DISALLOWED_BY_PREFLIGHT_RESPONSE = "MethodDisallowedByPreflightResponse"
    mime_type: str
    MISSING_ALLOW_ORIGIN_HEADER = "MissingAllowOriginHeader"
    MIXED_CONTENT = "mixed-content"
    mixed_content_type: security.MixedContentType | None = None
    mocked.
    modifications, or blocks it, or completes it with the provided response bytes. If a network
    Monotonically increasing time in seconds since an arbitrary point in the past.
    MULTIPLE_ALLOW_ORIGIN_VALUES = "MultipleAllowOriginValues"
    name: str
    name: str,
    NAME_NOT_RESOLVED = "NameNotResolved"
    NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE = "NameValuePairExceedsMaxSize"
    net_error: float | None = None
    net_error_name: str | None = None
    NETWORK = "network"
    Network level fetch failure reason.
    network stack. Not every requestWillBeSent event will have an additional
    new_priority: ResourcePriority
    NO_COOKIE_CONTENT = "NoCookieContent"
    NO_CORS_REDIRECT_MODE_NOT_FOLLOW = "NoCorsRedirectModeNotFollow"
    no_delay: bool
    NON_SECURE = "NonSecure"
    NONE = "None"
    NONE = "none"
    NONE = "None"
    NOOPENER_ALLOW_POPUPS = "NoopenerAllowPopups"
    Not every responseReceived event will have an responseReceivedEarlyHints fired.
    NOT_COMPLIANT = "not-compliant"
    NOT_ON_PATH = "NotOnPath"
    Note that this does not identify individual HTTP requests that are part of
    Note: this will only be fired for resources that are requested by the webpage.
    offline: bool,
    Only one responseReceivedEarlyHints may be fired for eached responseReceived event.
    opcode: float
    operation: TrustTokenOperationType
    options: DirectTCPSocketOptions
    options: LoadNetworkResourceOptions = None,
    or after the response was received.
    or requestWillBeSentExtraInfo will be fired first for the same request.
    ORIGIN = "origin"
    origin: str
    origin: str,
    OTHER = "Other"
    OTHER = "other"
    outer_response: Response
    OVERWRITE_SECURE = "OverwriteSecure"
    packet_loss: float | None = None,
    packet_queue_length: int | None = None,
    packet_reordering: bool | None = None,
    Page reload is required before the new cookie bahavior will be observed
    parameters should be identical: method, url, async, request body, extra headers, withCredentials
    params: T_JSON_DICT = dict()
    params["bypass"] = bypass
    params["cacheDisabled"] = cache_disabled
    params["cookies"] = [i.to_json() for i in cookies]
    params["disableThirdPartyCookieHeuristics"] = disable_third_party_cookie_heuristics
    params["disableThirdPartyCookieMetadata"] = disable_third_party_cookie_metadata
    params["downloadThroughput"] = download_throughput
    params["enable"] = enable
    params["enabled"] = enabled
    params["enableThirdPartyCookieRestriction"] = enable_third_party_cookie_restriction
    params["encodings"] = [i.to_json() for i in encodings]
    params["headers"] = headers.to_json()
    params["interceptionId"] = interception_id.to_json()
    params["latency"] = latency
    params["name"] = name
    params["offline"] = offline
    params["options"] = options.to_json()
    params["origin"] = origin
    params["patterns"] = [i.to_json() for i in patterns]
    params["query"] = query
    params["requestId"] = request_id.to_json()
    params["uploadThroughput"] = upload_throughput
    params["url"] = url
    params["urls"] = [i for i in urls]
    params["userAgent"] = user_agent
    params["value"] = value
    partition_key: CookiePartitionKey | None = None
    partition_key: CookiePartitionKey | None = None,
    partition_key_opaque: bool | None = None
    password: str | None = None
    path: str
    path: str | None = None
    path: str | None = None,
    patterns: list[RequestPattern],
    payload_data: str
    PENDING = "Pending"
    PERMISSION_BLOCK = "PermissionBlock"
    PERMISSION_WARN = "PermissionWarn"
    PING = "Ping"
    platform: str | None = None,
    PORT_MISMATCH = "PortMismatch"
    Post data entry for HTTP request
    post_data: str | None = None
    post_data: str | None = None,
    post_data_entries: list[PostDataEntry] | None = None
    PREFETCH = "Prefetch"
    PREFLIGHT = "Preflight"
    PREFLIGHT_ALLOW_ORIGIN_MISMATCH = "PreflightAllowOriginMismatch"
    PREFLIGHT_BLOCK = "PreflightBlock"
    PREFLIGHT_DISALLOWED_REDIRECT = "PreflightDisallowedRedirect"
    PREFLIGHT_INVALID_ALLOW_CREDENTIALS = "PreflightInvalidAllowCredentials"
    PREFLIGHT_INVALID_ALLOW_EXTERNAL = "PreflightInvalidAllowExternal"
    PREFLIGHT_INVALID_ALLOW_ORIGIN_VALUE = "PreflightInvalidAllowOriginValue"
    PREFLIGHT_INVALID_ALLOW_PRIVATE_NETWORK = "PreflightInvalidAllowPrivateNetwork"
    PREFLIGHT_INVALID_STATUS = "PreflightInvalidStatus"
    PREFLIGHT_MISSING_ALLOW_EXTERNAL = "PreflightMissingAllowExternal"
    PREFLIGHT_MISSING_ALLOW_ORIGIN_HEADER = "PreflightMissingAllowOriginHeader"
    PREFLIGHT_MISSING_ALLOW_PRIVATE_NETWORK = "PreflightMissingAllowPrivateNetwork"
    PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_ID = (
    PREFLIGHT_MISSING_PRIVATE_NETWORK_ACCESS_NAME = (
    PREFLIGHT_MULTIPLE_ALLOW_ORIGIN_VALUES = "PreflightMultipleAllowOriginValues"
    PREFLIGHT_WARN = "PreflightWarn"
    PREFLIGHT_WILDCARD_ORIGIN_NOT_ALLOWED = "PreflightWildcardOriginNotAllowed"
    priority: CookiePriority
    priority: CookiePriority | None = None
    priority: CookiePriority | None = None,
    PRIVATE = "Private"
    PRIVATE_NETWORK_ACCESS_PERMISSION_DENIED = "PrivateNetworkAccessPermissionDenied"
    PRIVATE_NETWORK_ACCESS_PERMISSION_UNAVAILABLE = (
    private_network_request_policy: PrivateNetworkRequestPolicy
    protocol: str
    protocol: str | None = None
    proxy_end: float
    proxy_start: float
    PUBLIC = "Public"
    push_end: float
    push_start: float
    query: str,
    QUEUED = "Queued"
    RACE_NETWORK_AND_FETCH_HANDLER = "race-network-and-fetch-handler"
    raw_response: str | None = None,
    realm: str
    receive_buffer_size: float | None = None
    receive_headers_end: float
    receive_headers_start: float
    REDEMPTION = "Redemption"
    REDIRECT_CONTAINS_CREDENTIALS = "RedirectContainsCredentials"
    redirect_has_extra_info: bool
    redirect_response: Response | None
    redirect_url: str | None
    referrer_policy: str
    refresh_policy: str
    remote_addr: str
    remote_ip_address: str | None = None
    remote_port: int
    remote_port: int | None = None
    report: ReportingApiReport
    report_only_reporting_endpoint: str | None = None
    report_only_value: CrossOriginEmbedderPolicyValue
    report_only_value: CrossOriginOpenerPolicyValue
    reporting_endpoint: str | None = None
    Represents the cookie's 'Priority' status:
    Represents the cookie's 'SameSite' status:
    Represents the source scheme of the origin that originally set the cookie.
    Request / response headers as keys / values of JSON object.
    REQUEST = "Request"
    Request pattern for interception.
    request: Request
    request: WebSocketRequest
    request_headers: Headers | None = None
    request_headers_text: str | None = None
    request_id: RequestId
    request_id: RequestId | None
    request_id: RequestId | None = None
    request_id: RequestId,
    request_time: float
    request_url: str
    requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
    REQUIRE_CORP = "RequireCorp"
    Resource type as it was perceived by the rendering engine.
    resource_ip_address_space: IPAddressSpace
    resource_type: ResourceType
    resource_type: ResourceType | None = None
    Response to an AuthChallenge.
    Response to Network.requestIntercepted which either modifies the request to continue with any
    response: Response
    response: Response | None = None
    response: str
    response: WebSocketFrame
    response: WebSocketResponse
    response_code: int
    response_error_reason: ErrorReason | None
    response_headers: Headers
    response_headers: Headers | None
    response_status_code: int | None
    response_time: TimeSinceEpoch | None = None
    RESTRICT_PROPERTIES = "RestrictProperties"
    RESTRICT_PROPERTIES_PLUS_COEP = "RestrictPropertiesPlusCoep"
    return (str(json["body"]), bool(json["base64Encoded"]))
    return [Cookie.from_json(i) for i in json["cookies"]]
    return [debugger.SearchMatch.from_json(i) for i in json["result"]]
    return [str(i) for i in json["tableNames"]]
    return bool(json["result"])
    return bool(json["success"])
    return io.StreamHandle.from_json(json["stream"])
    return LoadNetworkResourcePageResult.from_json(json["resource"])
    return SecurityIsolationStatus.from_json(json["status"])
    return str(json["bufferedData"])
    return str(json["postData"])
    Returns a handle to the stream representing the response body. Note that after this command,
    Returns all browser cookies for the current URL. Depending on the backend support, will return
    Returns all browser cookies. Depending on the backend support, will return detailed cookie
    Returns content served for the given currently intercepted request.
    Returns content served for the given request.
    Returns information about the COEP/COOP isolation status.
    Returns post data sent with the request. Returns an error when no data was sent with the request.
    Returns the DER-encoded certificate.
    rule_id_matched: int | None = None
    SAME_ORIGIN = "SameOrigin"
    SAME_ORIGIN_ALLOW_POPUPS = "SameOriginAllowPopups"
    SAME_ORIGIN_PLUS_COEP = "SameOriginPlusCoep"
    same_party: bool
    same_party: bool | None = None
    same_party: bool | None = None,
    SAME_PARTY_CONFLICTS_WITH_OTHER_ATTRIBUTES = "SamePartyConflictsWithOtherAttributes"
    SAME_PARTY_FROM_CROSS_PARTY_CONTEXT = "SamePartyFromCrossPartyContext"
    same_site: CookieSameSite | None = None
    same_site: CookieSameSite | None = None,
    SAME_SITE_LAX = "SameSiteLax"
    SAME_SITE_NONE_COOKIES_IN_SANDBOX = "SameSiteNoneCookiesInSandbox"
    SAME_SITE_NONE_INSECURE = "SameSiteNoneInsecure"
    SAME_SITE_STRICT = "SameSiteStrict"
    SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "SameSiteUnspecifiedTreatedAsLax"
    san_list: list[str]
    SCHEME = "Scheme"
    scheme: str
    SCHEME_MISMATCH = "SchemeMismatch"
    SCHEME_NOT_SUPPORTED = "SchemeNotSupported"
    SCHEMEFUL_SAME_SITE_LAX = "SchemefulSameSiteLax"
    SCHEMEFUL_SAME_SITE_STRICT = "SchemefulSameSiteStrict"
    SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = (
    SCRIPT = "Script"
    Searches for given string in response content.
    SECURE = "Secure"
    secure: bool
    secure: bool | None = None
    secure: bool | None = None,
    SECURE_ONLY = "SecureOnly"
    Security details about a request.
    security_details: SecurityDetails | None = None
    security_state: security.SecurityState
    send_buffer_size: float | None = None
    send_end: float
    send_start: float
    sent. Response will intercept after the response is received.
    server_signature_algorithm: int | None = None
    service_worker_response_source: ServiceWorkerResponseSource | None = None
    service_worker_router_info: ServiceWorkerRouterInfo | None = None
    session: bool
    Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.
    Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.
    Sets Controls for third-party cookie access
    Sets given cookies.
    Sets the requests to intercept that match the provided patterns and optionally resource types.
    signature: str
    signature_algorithm: str
    SIGNATURE_CERT_SHA256 = "signatureCertSha256"
    SIGNATURE_CERT_URL = "signatureCertUrl"
    signature_data: str
    signature_index: int | None = None
    SIGNATURE_INTEGRITY = "signatureIntegrity"
    SIGNATURE_SIG = "signatureSig"
    SIGNATURE_TIMESTAMPS = "signatureTimestamps"
    SIGNATURE_VALIDITY_URL = "signatureValidityUrl"
    signatures: list[SignedExchangeSignature]
    signed_certificate_timestamp_list: list[SignedCertificateTimestamp]
    SIGNED_EXCHANGE = "SignedExchange"
    SIGNING = "Signing"
    site_has_cookie_in_other_partition: bool | None
    size: int
    Source of service worker router.
    Source of serviceworker response.
    source: ContentSecurityPolicySource
    source: str | None = None
    source_port: int
    source_port: int | None = None
    source_port: int | None = None,
    source_scheme: CookieSourceScheme
    source_scheme: CookieSourceScheme | None = None
    source_scheme: CookieSourceScheme | None = None,
    Specifies whether to always send extra HTTP headers with the requests from this page.
    Specifies whether to attach a page script stack id in requests
    SRI_MESSAGE_SIGNATURE_MISMATCH = "sri-message-signature-mismatch"
    ssl_end: float
    ssl_start: float
    stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
    stack: runtime.StackTrace | None = None
    Stages of the interception to begin intercepting. Request will intercept before the request is
    status: int
    status: ReportStatus
    status: str
    status_code: int
    status_text: str
    STORAGE_ACCESS = "StorageAccess"
    stream: io.StreamHandle | None = None
    STRICT = "Strict"
    STYLESHEET = "Stylesheet"
    subject_name: str
    SUBRESOURCE_FILTER = "subresource-filter"
    SUCCESS = "Success"
    success: bool
    SYNTAX_ERROR = "SyntaxError"
    Tells whether clearing browser cache is supported.
    Tells whether clearing browser cookies is supported.
    Tells whether emulation of network conditions is supported.
    TEXT_TRACK = "TextTrack"
    The event contains the information about the web bundle contents.
    the intercepted request can't be continued as is -- you either need to cancel it or to provide
    The reason why Chrome uses a specific transport protocol for HTTP semantics.
    The reason why request was blocked.
    The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.
    the response body. The stream only supports sequential read, IO.read will fail if the position
    The status of a Reporting API report.
    the type of the operation and whether the operation succeeded or
    The underlying connection technology that the browser is supposedly using.
    THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET = "ThirdPartyBlockedInFirstPartySet"
    THIRD_PARTY_PHASEOUT = "ThirdPartyPhaseout"
    This is a temporary ability and it will be removed in the future.
    This method sends a new XMLHttpRequest which is identical to the original one. The following
    TIMED_OUT = "TimedOut"
    timestamp: float
    timestamp: MonotonicTime
    timestamp: network.TimeSinceEpoch
    Timing information for the request.
    timing: ResourceTiming | None = None
    Toggles ignoring cache for each request. If ``true``, cache will not be used.
    Toggles ignoring of service worker for each request.
    top_level_origin: str | None
    top_level_site: str
    TOP_LEVEL_STORAGE_ACCESS = "TopLevelStorageAccess"
    TOP_LEVEL_TPCD_DEPRECATION_TRIAL = "TopLevelTPCDDeprecationTrial"
    TPCD_DEPRECATION_TRIAL = "TPCDDeprecationTrial"
    TPCD_HEURISTICS = "TPCDHeuristics"
    TPCD_METADATA = "TPCDMetadata"
    transport_id: RequestId
    trust_token_params: TrustTokenParams | None = None
    type_: ResourceType
    type_: ResourceType | None
    type_: str
    type_: TrustTokenOperationType
    Types of reasons why a cookie may not be sent with a request.
    Types of reasons why a cookie may not be stored from a response.
    Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.
    typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, None]
    UNEXPECTED_PRIVATE_NETWORK_ACCESS = "UnexpectedPrivateNetworkAccess"
    Unique intercepted request identifier.
    Unique loader identifier.
    Unique network request identifier.
    UNKNOWN = "unknown"
    UNKNOWN = "Unknown"
    UNKNOWN_ERROR = "UnknownError"
    UNSAFE_NONE = "UnsafeNone"
    UNSET = "Unset"
    UNSPECIFIED_REASON = "unspecifiedReason"
    upload_throughput: float,
    url: str
    url: str | None = None
    url: str | None = None,
    url: str = None,
    url_fragment: str | None = None
    url_pattern: str | None = None
    urls: list[str]
    urls: list[str] | None = None,
    urls: list[str],
    user_agent: str,
    user_agent_metadata: emulation.UserAgentMetadata | None = None,
    USER_PREFERENCES = "UserPreferences"
    USER_SETTING = "UserSetting"
    username: str | None = None
    UTC time in seconds, counted from January 1, 1970.
    valid_from: TimeSinceEpoch
    valid_to: TimeSinceEpoch
    validity_url: str
    value: CrossOriginEmbedderPolicyValue
    value: CrossOriginOpenerPolicyValue
    value: str
    value: str,
    VERY_HIGH = "VeryHigh"
    VERY_LOW = "VeryLow"
    wall_time: TimeSinceEpoch
    WARN_FROM_INSECURE_TO_MORE_PRIVATE = "WarnFromInsecureToMorePrivate"
    WEB_SOCKET = "WebSocket"
    WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests.
    WebSocket request data.
    WebSocket response data.
    Whether the request complied with Certificate Transparency policy.
    WIFI = "wifi"
    WILDCARD_ORIGIN_NOT_ALLOWED = "WildcardOriginNotAllowed"
    WIMAX = "wimax"
    worker_cache_lookup_start: float | None = None
    worker_fetch_start: float
    worker_ready: float
    worker_respond_with_settled: float
    worker_router_evaluation_start: float | None = None
    worker_start: float
    XHR = "XHR"
    ZSTD = "zstd"
#
# CDP domain: Network
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, io.StreamHandle]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[Cookie]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[debugger.SearchMatch]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[str]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, LoadNetworkResourcePageResult]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, SecurityIsolationStatus]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[str, bool]]:
):
@dataclass
@event_class("Network.dataReceived")
@event_class("Network.directTCPSocketAborted")
@event_class("Network.directTCPSocketClosed")
@event_class("Network.directTCPSocketCreated")
@event_class("Network.directTCPSocketOpened")
@event_class("Network.eventSourceMessageReceived")
@event_class("Network.loadingFailed")
@event_class("Network.loadingFinished")
@event_class("Network.policyUpdated")
@event_class("Network.reportingApiEndpointsChangedForOrigin")
@event_class("Network.reportingApiReportAdded")
@event_class("Network.reportingApiReportUpdated")
@event_class("Network.requestIntercepted")
@event_class("Network.requestServedFromCache")
@event_class("Network.requestWillBeSent")
@event_class("Network.requestWillBeSentExtraInfo")
@event_class("Network.resourceChangedPriority")
@event_class("Network.responseReceived")
@event_class("Network.responseReceivedEarlyHints")
@event_class("Network.responseReceivedExtraInfo")
@event_class("Network.signedExchangeReceived")
@event_class("Network.subresourceWebBundleInnerResponseError")
@event_class("Network.subresourceWebBundleInnerResponseParsed")
@event_class("Network.subresourceWebBundleMetadataError")
@event_class("Network.subresourceWebBundleMetadataReceived")
@event_class("Network.trustTokenOperationDone")
@event_class("Network.webSocketClosed")
@event_class("Network.webSocketCreated")
@event_class("Network.webSocketFrameError")
@event_class("Network.webSocketFrameReceived")
@event_class("Network.webSocketFrameSent")
@event_class("Network.webSocketHandshakeResponseReceived")
@event_class("Network.webSocketWillSendHandshakeRequest")
@event_class("Network.webTransportClosed")
@event_class("Network.webTransportConnectionEstablished")
@event_class("Network.webTransportCreated")
class AlternateProtocolUsage:
class AssociatedCookie:
class AuthChallenge:
class AuthChallengeResponse:
class BlockedReason:
class BlockedSetCookieWithReason:
class CachedResource:
class CertificateTransparencyCompliance:
class ClientSecurityState:
class ConnectionType:
class ConnectTiming:
class ContentEncoding:
class ContentSecurityPolicySource:
class ContentSecurityPolicyStatus:
class Cookie:
class CookieBlockedReason:
class CookieExemptionReason:
class CookieParam:
class CookiePartitionKey:
class CookiePriority:
class CookieSameSite:
class CookieSourceScheme:
class CorsError:
class CorsErrorStatus:
class CrossOriginEmbedderPolicyStatus:
class CrossOriginEmbedderPolicyValue:
class CrossOriginOpenerPolicyStatus:
class CrossOriginOpenerPolicyValue:
class DataReceived:
class DirectSocketDnsQueryType:
class DirectTCPSocketAborted:
class DirectTCPSocketClosed:
class DirectTCPSocketCreated:
class DirectTCPSocketOpened:
class DirectTCPSocketOptions:
class ErrorReason:
class EventSourceMessageReceived:
class ExemptedSetCookieWithReason:
class Headers:
class Initiator:
class InterceptionId:
class InterceptionStage:
class IPAddressSpace:
class LoaderId:
class LoadingFailed:
class LoadingFinished:
class LoadNetworkResourceOptions:
class LoadNetworkResourcePageResult:
class MonotonicTime:
class PolicyUpdated:
class PostDataEntry:
class PrivateNetworkRequestPolicy:
class ReportId:
class ReportingApiEndpoint:
class ReportingApiEndpointsChangedForOrigin:
class ReportingApiReport:
class ReportingApiReportAdded:
class ReportingApiReportUpdated:
class ReportStatus:
class Request:
class RequestId:
class RequestIntercepted:
class RequestPattern:
class RequestServedFromCache:
class RequestWillBeSent:
class RequestWillBeSentExtraInfo:
class ResourceChangedPriority:
class ResourcePriority:
class ResourceTiming:
class ResourceType:
class Response:
class ResponseReceived:
class ResponseReceivedEarlyHints:
class ResponseReceivedExtraInfo:
class SecurityDetails:
class SecurityIsolationStatus:
class ServiceWorkerResponseSource:
class ServiceWorkerRouterInfo:
class ServiceWorkerRouterSource:
class SetCookieBlockedReason:
class SignedCertificateTimestamp:
class SignedExchangeError:
class SignedExchangeErrorField:
class SignedExchangeHeader:
class SignedExchangeInfo:
class SignedExchangeReceived:
class SignedExchangeSignature:
class SubresourceWebBundleInnerResponseError:
class SubresourceWebBundleInnerResponseParsed:
class SubresourceWebBundleMetadataError:
class SubresourceWebBundleMetadataReceived:
class TimeSinceEpoch:
class TrustTokenOperationDone:
class TrustTokenOperationType:
class TrustTokenParams:
class WebSocketClosed:
class WebSocketCreated:
class WebSocketFrame:
class WebSocketFrameError:
class WebSocketFrameReceived:
class WebSocketFrameSent:
class WebSocketHandshakeResponseReceived:
class WebSocketRequest:
class WebSocketResponse:
class WebSocketWillSendHandshakeRequest:
class WebTransportClosed:
class WebTransportConnectionEstablished:
class WebTransportCreated:
def can_clear_browser_cache() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]:
def can_clear_browser_cookies() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]:
def can_emulate_network_conditions() -> (
def clear_accepted_encodings_override() -> (
def clear_browser_cache() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_browser_cookies() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def continue_intercepted_request(
def delete_cookies(
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def emulate_network_conditions(
def enable(
def enable_reporting_api(
def get_all_cookies() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[Cookie]]:
def get_certificate(
def get_cookies(
def get_request_post_data(
def get_response_body(
def get_response_body_for_interception(
def get_security_isolation_status(
def load_network_resource(
def replay_xhr(
def search_in_response_body(
def set_accepted_encodings(
def set_attach_debug_stack(
def set_blocked_ur_ls(
def set_bypass_service_worker(
def set_cache_disabled(
def set_cookie(
def set_cookie_controls(
def set_cookies(
def set_extra_http_headers(
def set_request_interception(
def set_user_agent_override(
def stream_resource_content(
def take_response_body_for_interception_as_stream(
from . import debugger
from . import emulation
from . import io
from . import page
from . import runtime
from . import security
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import network
import typing
