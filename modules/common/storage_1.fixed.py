
for i in json["urlsWithMetadata"]
                    SharedStorageUrlWithMetadata.from_json(i)
                [
                ]
                AttributionReportingAggregatableDebugReportingData.from_json(i)
                AttributionReportingAggregatableDedupKey.from_json(i)
                AttributionReportingAggregatableTriggerData.from_json(i)
                AttributionReportingAggregatableValueDictEntry.from_json(i)
                AttributionReportingAggregatableValueEntry.from_json(i)
                AttributionReportingAggregationKeysEntry.from_json(i)
                AttributionReportingEventTriggerData.from_json(i)
                AttributionReportingFilterConfig.from_json(i)
                AttributionReportingFilterConfig.from_json(i) for i in json["filters"]
                AttributionReportingFilterDataEntry.from_json(i)
                AttributionReportingTriggerSpec.from_json(i)
                AttributionScopesData.from_json(json["scopesData"])
                bool(json["ignoreIfPresent"]) if "ignoreIfPresent" in json else None
                dict(json["auctionConfig"]) if "auctionConfig" in json else None
                else None
                for i in json["aggregatableDedupKeys"]
                for i in json["aggregatableTriggerData"]
                for i in json["aggregatableValues"]
                for i in json["aggregationKeys"]
                for i in json["debugData"]
                for i in json["eventTriggerData"]
                for i in json["filterData"]
                for i in json["filterValues"]
                for i in json["notFilters"]
                for i in json["reportingMetadata"]
                for i in json["triggerSpecs"]
                for i in json["values"]
                if "aggregationCoordinatorOrigin" in json
                if "componentSellerOrigin" in json
                if "debugKey" in json
                if "dedupKey" in json
                if "parentAuctionId" in json
                if "scopesData" in json
                if "uniqueAuctionId" in json
                if "urlsWithMetadata" in json
                int(json["lookbackWindow"]) if "lookbackWindow" in json else None
                InterestGroupAuctionId.from_json(json["parentAuctionId"])
                InterestGroupAuctionId.from_json(json["uniqueAuctionId"])
                json["aggregatable"]
                json["aggregatableDebugReportingConfig"]
                json["aggregatableFilteringIdMaxBytes"]
                json["destinationLimitPriority"]
                json["eventLevel"]
                json["eventReportWindows"]
                json["registration"]
                json["result"]
                json["sourceRegistrationTimeConfig"]
                json["triggerDataMatching"]
                SharedStorageReportingMetadata.from_json(i)
                str(json["aggregationCoordinatorOrigin"])
                str(json["componentSellerOrigin"])
                str(json["operationName"]) if "operationName" in json else None
                str(json["scriptSourceUrl"]) if "scriptSourceUrl" in json else None
                str(json["serializedData"]) if "serializedData" in json else None
                str(json["triggerContextId"]) if "triggerContextId" in json else None
                UnsignedInt64AsBase10.from_json(json["debugKey"])
                UnsignedInt64AsBase10.from_json(json["dedupKey"])
            ),
            ],
            access_time=network.TimeSinceEpoch.from_json(json["accessTime"]),
            aggregatable_debug_reporting_config=AttributionReportingAggregatableDebugReportingConfig.from_json(
            aggregatable_dedup_keys=[
            aggregatable_filtering_id_max_bytes=int(
            aggregatable_report_window=int(json["aggregatableReportWindow"]),
            aggregatable_trigger_data=[
            aggregatable_values=[
            aggregatable=AttributionReportingAggregatableResult.from_json(
            aggregation_coordinator_origin=(
            aggregation_keys=[
            associated_sites=[str(i) for i in json["associatedSites"]],
            auction_config=(
            auctions=[InterestGroupAuctionId.from_json(i) for i in json["auctions"]],
            bid_currency=str(json["bidCurrency"]) if "bidCurrency" in json else None,
            bid=float(json["bid"]) if "bid" in json else None,
            bucket_id=str(json["bucketId"]),
            bucket=StorageBucket.from_json(json["bucket"]),
            budget=float(json["budget"]) if "budget" in json else None,
            bytes_used=int(json["bytesUsed"]),
            cache_name=str(json["cacheName"]),
            component_seller_origin=(
            count=float(json["count"]),
            creation_time=network.TimeSinceEpoch.from_json(json["creationTime"]),
            data=UnsignedInt64AsBase10.from_json(json["data"]),
            database_name=str(json["databaseName"]),
            debug_data=[
            debug_key=(
            debug_reporting=bool(json["debugReporting"]),
            dedup_key=(
            destination_limit_priority=SignedInt64AsBase10.from_json(
            destination_sites=[str(i) for i in json["destinationSites"]],
            durability=StorageBucketsDurability.from_json(json["durability"]),
            ends=[int(i) for i in json["ends"]],
            event_id=UnsignedInt64AsBase10.from_json(json["eventId"]),
            event_level=AttributionReportingEventLevelResult.from_json(
            event_report_windows=AttributionReportingEventReportWindows.from_json(
            event_time=network.TimeSinceEpoch.from_json(json["eventTime"]),
            event_trigger_data=[
            event_type=str(json["eventType"]),
            expiration=network.TimeSinceEpoch.from_json(json["expiration"]),
            expiry=int(json["expiry"]),
            filter_data=[
            filter_values=[
            filtering_id=UnsignedInt64AsBase10.from_json(json["filteringId"]),
            filters=[
            filters=AttributionReportingFilterPair.from_json(json["filters"]),
            i.to_json() for i in self.aggregatable_dedup_keys
            i.to_json() for i in self.aggregatable_trigger_data
            id_=str(json["id"]),
            ignore_if_present=(
            issuer_origin=str(json["issuerOrigin"]),
            json["aggregationCoordinatorOrigin"] = self.aggregation_coordinator_origin
            json["budget"] = self.budget
            json["debugKey"] = self.debug_key.to_json()
            json["dedupKey"] = self.dedup_key.to_json()
            json["ignoreIfPresent"] = self.ignore_if_present
            json["key"] = self.key
            json["lookbackWindow"] = self.lookback_window
            json["name"] = self.name
            json["operationName"] = self.operation_name
            json["scopesData"] = self.scopes_data.to_json()
            json["scriptSourceUrl"] = self.script_source_url
            json["serializedData"] = self.serialized_data
            json["triggerContextId"] = self.trigger_context_id
            json["urlsWithMetadata"] = [i.to_json() for i in self.urls_with_metadata]
            json["value"] = self.value
            key_piece=UnsignedInt128AsBase16.from_json(json["keyPiece"]),
            key=str(json["key"]) if "key" in json else None,
            key=str(json["key"]),
            length=int(json["length"]),
            limit=float(json["limit"]),
            lookback_window=(
            main_frame_id=page.FrameId.from_json(json["mainFrameId"]),
            max_event_level_reports=int(json["maxEventLevelReports"]),
            max_event_states=float(json["maxEventStates"]),
            method=SharedStorageAccessMethod.from_json(json["method"]),
            name=str(json["name"]) if "name" in json else None,
            name=str(json["name"]),
            not_filters=[
            object_store_name=str(json["objectStoreName"]),
            operation_name=(
            origin=str(json["origin"]),
            owner_origin=str(json["ownerOrigin"]),
            owner_site=str(json["ownerSite"]),
            params=SharedStorageAccessParams.from_json(json["params"]),
            parent_auction_id=(
            persistent=bool(json["persistent"]),
            primary_sites=[str(i) for i in json["primarySites"]],
            priority=SignedInt64AsBase10.from_json(json["priority"]),
            quota=float(json["quota"]),
            registration=AttributionReportingSourceRegistration.from_json(
            registration=AttributionReportingTriggerRegistration.from_json(
            remaining_budget=float(json["remainingBudget"]),
            reporting_metadata=[
            reporting_origin=str(json["reportingOrigin"]),
            reporting_url=str(json["reportingUrl"]),
            request_id=network.RequestId.from_json(json["requestId"]),
            result=AttributionReportingSourceRegistrationResult.from_json(
            scope=SharedStorageAccessScope.from_json(json["scope"]),
            scopes_data=(
            scopes=[str(i) for i in json["scopes"]],
            script_source_url=(
            self.aggregatable_debug_reporting_config.to_json()
            self.aggregatable_filtering_id_max_bytes
            self.source_registration_time_config.to_json()
            serialized_data=(
            service_sites=[str(i) for i in json["serviceSites"]],
            source_keys=[str(i) for i in json["sourceKeys"]],
            source_origin=str(json["sourceOrigin"]),
            source_registration_time_config=AttributionReportingSourceRegistrationTimeConfig.from_json(
            start=int(json["start"]),
            storage_key=SerializedStorageKey.from_json(json["storageKey"]),
            storage_key=str(json["storageKey"]),
            storage_type=StorageType.from_json(json["storageType"]),
            time=network.TimeSinceEpoch.from_json(json["time"]),
            trigger_context_id=(
            trigger_data_matching=AttributionReportingTriggerDataMatching.from_json(
            trigger_data=[float(i) for i in json["triggerData"]],
            trigger_specs=[
            type_=AttributionReportingSourceType.from_json(json["type"]),
            type_=InterestGroupAccessType.from_json(json["type"]),
            type_=InterestGroupAuctionEventType.from_json(json["type"]),
            type_=InterestGroupAuctionFetchType.from_json(json["type"]),
            types=[str(i) for i in json["types"]],
            unique_auction_id=(
            unique_auction_id=InterestGroupAuctionId.from_json(json["uniqueAuctionId"]),
            url=str(json["url"]),
            urls_with_metadata=(
            usage=float(json["usage"]),
            value=float(json["value"]),
            value=str(json["value"]) if "value" in json else None,
            value=str(json["value"]),
            value=UnsignedInt128AsBase16.from_json(json["value"]),
            values=[
            values=[str(i) for i in json["values"]],
        "destinationPerDayReportingLimitReached"
        "method": "Storage.clearCookies",
        "method": "Storage.clearDataForOrigin",
        "method": "Storage.clearDataForStorageKey",
        "method": "Storage.clearSharedStorageEntries",
        "method": "Storage.clearTrustTokens",
        "method": "Storage.deleteSharedStorageEntry",
        "method": "Storage.deleteStorageBucket",
        "method": "Storage.getAffectedUrlsForThirdPartyCookieMetadata",
        "method": "Storage.getCookies",
        "method": "Storage.getInterestGroupDetails",
        "method": "Storage.getRelatedWebsiteSets",
        "method": "Storage.getSharedStorageEntries",
        "method": "Storage.getSharedStorageMetadata",
        "method": "Storage.getStorageKeyForFrame",
        "method": "Storage.getTrustTokens",
        "method": "Storage.getUsageAndQuota",
        "method": "Storage.overrideQuotaForOrigin",
        "method": "Storage.resetSharedStorageBudget",
        "method": "Storage.runBounceTrackingMitigations",
        "method": "Storage.sendPendingAttributionReports",
        "method": "Storage.setAttributionReportingLocalTestingMode",
        "method": "Storage.setAttributionReportingTracking",
        "method": "Storage.setCookies",
        "method": "Storage.setInterestGroupAuctionTracking",
        "method": "Storage.setInterestGroupTracking",
        "method": "Storage.setSharedStorageEntry",
        "method": "Storage.setSharedStorageTracking",
        "method": "Storage.setStorageBucketTracking",
        "method": "Storage.trackCacheStorageForOrigin",
        "method": "Storage.trackCacheStorageForStorageKey",
        "method": "Storage.trackIndexedDBForOrigin",
        "method": "Storage.trackIndexedDBForStorageKey",
        "method": "Storage.untrackCacheStorageForOrigin",
        "method": "Storage.untrackCacheStorageForStorageKey",
        "method": "Storage.untrackIndexedDBForOrigin",
        "method": "Storage.untrackIndexedDBForStorageKey",
        "params": params,
        )
        [UsageForType.from_json(i) for i in json["usageBreakdown"]],
        ]
        0. **usage** - Storage usage (bytes).
        1. **quota** - Storage quota (bytes).
        2. **overrideActive** - Whether or not the origin has an active storage quota override
        3. **usageBreakdown** - Storage usage per type (bytes).
        AttributionReportingAggregatableDebugReportingConfig
        bool(json["overrideActive"]),
        float(json["quota"]),
        float(json["usage"]),
        if self.aggregation_coordinator_origin is not None:
        if self.budget is not None:
        if self.debug_key is not None:
        if self.dedup_key is not None:
        if self.ignore_if_present is not None:
        if self.key is not None:
        if self.lookback_window is not None:
        if self.name is not None:
        if self.operation_name is not None:
        if self.scopes_data is not None:
        if self.script_source_url is not None:
        if self.serialized_data is not None:
        if self.trigger_context_id is not None:
        if self.urls_with_metadata is not None:
        if self.value is not None:
        json = dict()
        json["aggregatableDebugReportingConfig"] = (
        json["aggregatableDedupKeys"] = [
        json["aggregatableFilteringIdMaxBytes"] = (
        json["aggregatableReportWindow"] = self.aggregatable_report_window
        json["aggregatableTriggerData"] = [
        json["aggregatableValues"] = [i.to_json() for i in self.aggregatable_values]
        json["aggregationKeys"] = [i.to_json() for i in self.aggregation_keys]
        json["associatedSites"] = [i for i in self.associated_sites]
        json["bucket"] = self.bucket.to_json()
        json["bytesUsed"] = self.bytes_used
        json["count"] = self.count
        json["creationTime"] = self.creation_time.to_json()
        json["data"] = self.data.to_json()
        json["debugData"] = [i.to_json() for i in self.debug_data]
        json["debugReporting"] = self.debug_reporting
        json["destinationLimitPriority"] = self.destination_limit_priority.to_json()
        json["destinationSites"] = [i for i in self.destination_sites]
        json["durability"] = self.durability.to_json()
        json["ends"] = [i for i in self.ends]
        json["eventId"] = self.event_id.to_json()
        json["eventReportWindows"] = self.event_report_windows.to_json()
        json["eventTriggerData"] = [i.to_json() for i in self.event_trigger_data]
        json["eventType"] = self.event_type
        json["expiration"] = self.expiration.to_json()
        json["expiry"] = self.expiry
        json["filterData"] = [i.to_json() for i in self.filter_data]
        json["filteringId"] = self.filtering_id.to_json()
        json["filters"] = [i.to_json() for i in self.filters]
        json["filters"] = self.filters.to_json()
        json["filterValues"] = [i.to_json() for i in self.filter_values]
        json["id"] = self.id_
        json["issuerOrigin"] = self.issuer_origin
        json["key"] = self.key
        json["keyPiece"] = self.key_piece.to_json()
        json["length"] = self.length
        json["limit"] = self.limit
        json["maxEventLevelReports"] = self.max_event_level_reports
        json["maxEventStates"] = self.max_event_states
        json["notFilters"] = [i.to_json() for i in self.not_filters]
        json["persistent"] = self.persistent
        json["primarySites"] = [i for i in self.primary_sites]
        json["priority"] = self.priority.to_json()
        json["quota"] = self.quota
        json["remainingBudget"] = self.remaining_budget
        json["reportingMetadata"] = [i.to_json() for i in self.reporting_metadata]
        json["reportingOrigin"] = self.reporting_origin
        json["reportingUrl"] = self.reporting_url
        json["scopes"] = [i for i in self.scopes]
        json["serviceSites"] = [i for i in self.service_sites]
        json["sourceKeys"] = [i for i in self.source_keys]
        json["sourceOrigin"] = self.source_origin
        json["sourceRegistrationTimeConfig"] = (
        json["start"] = self.start
        json["storageKey"] = self.storage_key.to_json()
        json["storageType"] = self.storage_type.to_json()
        json["time"] = self.time.to_json()
        json["triggerData"] = [i for i in self.trigger_data]
        json["triggerDataMatching"] = self.trigger_data_matching.to_json()
        json["triggerSpecs"] = [i.to_json() for i in self.trigger_specs]
        json["type"] = self.type_.to_json()
        json["types"] = [i for i in self.types]
        json["url"] = self.url
        json["usage"] = self.usage
        json["value"] = self.value
        json["value"] = self.value.to_json()
        json["values"] = [i for i in self.values]
        json["values"] = [i.to_json() for i in self.values]
        params["browserContextId"] = browser_context_id.to_json()
        params["ignoreIfPresent"] = ignore_if_present
        params["quotaSize"] = quota_size
        return "InterestGroupAuctionId({})".format(super().__repr__())
        return "SerializedStorageKey({})".format(super().__repr__())
        return "SignedInt64AsBase10({})".format(super().__repr__())
        return "UnsignedInt128AsBase16({})".format(super().__repr__())
        return "UnsignedInt64AsBase10({})".format(super().__repr__())
        return cls(
        return cls(bucket_id=str(json["bucketId"]))
        return cls(bucket_info=StorageBucketInfo.from_json(json["bucketInfo"]))
        return cls(json)
        return json
        return self
        return self.value
    """
    #: Any associated reporting metadata.
    #: Array of candidate URLs' specs, along with any associated metadata.
    #: Current amount of bits of entropy remaining in the navigation budget.
    #: Database to update.
    #: DevTools Frame Token for the primary frame tree's root.
    #: duration in seconds
    #: Enum value indicating the access scope.
    #: Enum value indicating the Shared Storage API method invoked.
    #: For bid or somethingBid event, if done locally and not on a server.
    #: For non-global events --- links to interestGroupAuctionEvent
    #: For topLevelBid/topLevelAdditionalBid, and when appropriate,
    #: If not specified, it is the default bucket of the storageKey.
    #: int
    #: int, only present for source registrations
    #: Key for a specific entry in an origin's shared storage.
    #: Name of cache in origin.
    #: Name of storage type.
    #: Name of the registered operation to be run.
    #: number instead of integer because not all uint32 can be represented by
    #: Number of key-value pairs stored in origin's shared storage.
    #: ObjectStore to update.
    #: Origin to update.
    #: presence/absence depends on ``type``.
    #: Present only for SharedStorageAccessType.documentAddModule.
    #: Present only for SharedStorageAccessType.documentRun and
    #: Present only for SharedStorageAccessType.documentSelectURL.
    #: Present only for SharedStorageAccessType.documentSet,
    #: request.  In the case of trusted signals, it's possible that only some of
    #: Serialization of the origin owning the Shared Storage data.
    #: Serialization of the site owning the Shared Storage data.
    #: Set for child auctions.
    #: Set for started and configResolved
    #: SharedStorageAccessType.documentAppend,
    #: SharedStorageAccessType.documentDelete,
    #: SharedStorageAccessType.documentSelectURL.
    #: SharedStorageAccessType.headerAppend, and
    #: SharedStorageAccessType.headerAppend.
    #: SharedStorageAccessType.headerDelete.
    #: SharedStorageAccessType.headerSet,
    #: SharedStorageAccessType.headerSet, and
    #: SharedStorageAccessType.headerSet.
    #: SharedStorageAccessType.workletAppend,
    #: SharedStorageAccessType.workletDelete,
    #: SharedStorageAccessType.workletGet,
    #: SharedStorageAccessType.workletSet,
    #: SharedStorageAccessType.workletSet, and
    #: Spec of candidate URL.
    #: Spec of the module script URL.
    #: Storage bucket to update.
    #: Storage key to update.
    #: Storage quota (bytes).
    #: Storage usage (bytes).
    #: storage.
    #: The associated sites of this set, along with the ccTLDs if there is any.
    #: The operation's serialized data in bytes (converted to a string).
    #: The primary site of this set, along with the ccTLDs if there is any.
    #: The service sites of this set, along with the ccTLDs if there is any.
    #: The sub-parameters wrapped by ``params`` are all optional and their
    #: them actually care about the keys being queried.
    #: This is the set of the auctions using the worklet that issued this
    #: Time of the access.
    #: Time when the origin's shared storage was last created.
    #: Total number of bytes stored as key-value pairs in origin's shared
    #: Value for a specific entry in an origin's shared storage.
    #: Whether or not to set an entry for a key if that key is already present.
    #: win and additionalBidWin
    )
    **EXPERIMENTAL**
    :param browser_context_id: *(Optional)* Browser context to use when called on the browser endpoint.
    :param bucket:
    :param cookies: Cookies to be set.
    :param enable:
    :param enabled: If enabled, noise is suppressed and reports are sent immediately.
    :param first_party_url: The URL of the page currently being visited.
    :param frame_id:
    :param ignore_if_present: *(Optional)* If ```ignoreIfPresent```` is included and true, then only sets the entry if ````key``` doesn't already exist.
    :param issuer_origin:
    :param key:
    :param name:
    :param origin: Security origin.
    :param owner_origin:
    :param quota_size: *(Optional)* The quota size (in bytes) to override the original quota with. If this is called multiple times, the overridden quota will be equal to the quotaSize provided in the final call. If this is called without specifying a quotaSize, the quota will be reset to the default value for the specified origin. If this is called multiple times with different origins, the override will be maintained for each origin until it is disabled (called without a quotaSize).
    :param storage_key:
    :param storage_key: Storage key.
    :param storage_types: Comma separated list of StorageType to clear.
    :param third_party_urls: The list of embedded resource URLs from the page.
    :param value:
    :returns:
    :returns: A tuple with the following items:
    :returns: Array of cookie objects.
    :returns: Array of matching URLs. If there is a primary pattern match for the first- party URL, only the first-party URL is returned in the array.
    :returns: The number of reports that were sent.
    :returns: This largely corresponds to: https://wicg.github.io/turtledove/#dictdef-generatebidinterestgroup but has absolute expirationTime instead of relative lifetimeMs and also adds joiningOrigin.
    :returns: True if any tokens were deleted, false otherwise.
    @classmethod
    }
    A cache has been added/deleted.
    A cache's contents have been modified.
    A single Related Website Set object.
    access_time: network.TimeSinceEpoch
    ADD_MODULE = "addModule"
    ADDITIONAL_BID = "additionalBid"
    ADDITIONAL_BID_WIN = "additionalBidWin"
    aggregatable: AttributionReportingAggregatableResult
    aggregatable_debug_reporting_config: (
    aggregatable_dedup_keys: list[AttributionReportingAggregatableDedupKey]
    aggregatable_filtering_id_max_bytes: int
    aggregatable_report_window: int
    aggregatable_trigger_data: list[AttributionReportingAggregatableTriggerData]
    aggregatable_values: list[AttributionReportingAggregatableValueEntry]
    aggregation_coordinator_origin: str | None = None
    aggregation_keys: list[AttributionReportingAggregationKeysEntry]
    ALL_ = "all"
    An auction involving interest groups is taking place. These events are
    APPEND = "append"
    associated_sites: list[str]
    auction_config: dict | None
    auctions: list[InterestGroupAuctionId]
    BATCH_UPDATE = "batchUpdate"
    BID = "bid"
    bid: float | None
    bid_currency: str | None
    BIDDER_JS = "bidderJs"
    BIDDER_TRUSTED_SIGNALS = "bidderTrustedSignals"
    BIDDER_WASM = "bidderWasm"
    browser_context_id: browser.BrowserContextID | None = None,
    bucket: StorageBucket
    bucket: StorageBucket,
    bucket_id: str
    bucket_info: StorageBucketInfo
    budget: float | None = None
    Bundles a candidate URL with its reporting metadata.
    Bundles the parameters for shared storage access events whose
    bytes_used: int
    cache_name: str
    CACHE_STORAGE = "cache_storage"
    CLEAR = "clear"
    Clears all entries for a given origin's shared storage.
    Clears cookies.
    Clears storage for origin.
    Clears storage for storage key.
    cmd_dict: T_JSON_DICT = {
    component_seller_origin: str | None
    CONFIG_RESOLVED = "configResolved"
    COOKIES = "cookies"
    cookies: list[network.CookieParam],
    count: float
    CREATE_WORKLET = "createWorklet"
    creation_time: network.TimeSinceEpoch
    current browsing context.
    data: UnsignedInt64AsBase10
    database_name: str
    debug_data: list[AttributionReportingAggregatableDebugReportingData]
    debug_key: UnsignedInt64AsBase10 | None = None
    debug_reporting: bool
    dedup_key: UnsignedInt64AsBase10 | None = None
    DEDUPLICATED = "deduplicated"
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: str) -> InterestGroupAuctionId:
    def from_json(cls, json: str) -> SerializedStorageKey:
    def from_json(cls, json: str) -> SignedInt64AsBase10:
    def from_json(cls, json: str) -> UnsignedInt128AsBase16:
    def from_json(cls, json: str) -> UnsignedInt64AsBase10:
    def from_json(cls, json: T_JSON_DICT) -> AttributionReportingSourceRegistered:
    def from_json(cls, json: T_JSON_DICT) -> AttributionReportingTriggerRegistered:
    def from_json(cls, json: T_JSON_DICT) -> CacheStorageContentUpdated:
    def from_json(cls, json: T_JSON_DICT) -> CacheStorageListUpdated:
    def from_json(cls, json: T_JSON_DICT) -> IndexedDBContentUpdated:
    def from_json(cls, json: T_JSON_DICT) -> IndexedDBListUpdated:
    def from_json(cls, json: T_JSON_DICT) -> InterestGroupAccessed:
    def from_json(cls, json: T_JSON_DICT) -> InterestGroupAuctionEventOccurred:
    def from_json(cls, json: T_JSON_DICT) -> InterestGroupAuctionNetworkRequestCreated:
    def from_json(cls, json: T_JSON_DICT) -> SharedStorageAccessed:
    def from_json(cls, json: T_JSON_DICT) -> StorageBucketCreatedOrUpdated:
    def from_json(cls, json: T_JSON_DICT) -> StorageBucketDeleted:
    def to_json(self) -> str:
    def to_json(self):
    DELETE = "delete"
    Deletes entry for ``key`` (if it exists) for a given origin's shared storage.
    Deletes state for sites identified as potential bounce trackers, immediately.
    Deletes the Storage Bucket with the given storage key and bucket name.
    DESTINATION_BOTH_LIMITS_REACHED = "destinationBothLimitsReached"
    DESTINATION_GLOBAL_LIMIT_REACHED = "destinationGlobalLimitReached"
    destination_limit_priority: SignedInt64AsBase10
    DESTINATION_PER_DAY_REPORTING_LIMIT_REACHED = (
    DESTINATION_REPORTING_LIMIT_REACHED = "destinationReportingLimitReached"
    destination_sites: list[str]
    Details for an origin's shared storage.
    durability: StorageBucketsDurability
    enable: bool,
    enabled: bool,
    Enables/disables issuing of Attribution Reporting events.
    Enables/Disables issuing of interestGroupAccessed events.
    Enables/Disables issuing of interestGroupAuctionEventOccurred and
    Enables/disables issuing of sharedStorageAccessed events.
    ends: list[int]
    ENTRIES = "entries"
    Enum of auction events.
    Enum of interest group access types.
    Enum of network fetches auctions can do.
    Enum of possible storage types.
    Enum of shared storage access methods.
    Enum of shared storage access scopes.
    EVENT = "event"
    event_id: UnsignedInt64AsBase10
    event_level: AttributionReportingEventLevelResult
    event_report_windows: AttributionReportingEventReportWindows
    event_time: network.TimeSinceEpoch
    event_trigger_data: list[AttributionReportingEventTriggerData]
    event_type: str
    EXACT = "exact"
    EXCEEDS_MAX_CHANNEL_CAPACITY = "exceedsMaxChannelCapacity"
    EXCEEDS_MAX_EVENT_STATES_LIMIT = "exceedsMaxEventStatesLimit"
    EXCEEDS_MAX_SCOPES_CHANNEL_CAPACITY = "exceedsMaxScopesChannelCapacity"
    EXCEEDS_MAX_TRIGGER_STATE_CARDINALITY = "exceedsMaxTriggerStateCardinality"
    EXCESSIVE_ATTRIBUTIONS = "excessiveAttributions"
    EXCESSIVE_REPORTING_ORIGINS = "excessiveReportingOrigins"
    EXCESSIVE_REPORTS = "excessiveReports"
    EXCLUDE = "exclude"
    existing grace period URL pattern rules.
    expiration: network.TimeSinceEpoch
    expiry: int
    FALSELY_ATTRIBUTED_SOURCE = "falselyAttributedSource"
    FILE_SYSTEMS = "file_systems"
    filter_data: list[AttributionReportingFilterDataEntry]
    filter_values: list[AttributionReportingFilterDataEntry]
    filtering_id: UnsignedInt64AsBase10
    filters: AttributionReportingFilterPair
    filters: list[AttributionReportingFilterConfig]
    first_party_url: str, third_party_urls: list[str]
    frame_id: page.FrameId,
    GET = "get"
    Gets details for a named interest group.
    Gets metadata for an origin's shared storage.
    Gets the entries in an given origin's shared storage.
    HEADER = "header"
    https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
    https://wicg.github.io/attribution-reporting-api/
    id_: str
    if browser_context_id is not None:
    if ignore_if_present is not None:
    if quota_size is not None:
    ignore_if_present: bool | None = None
    ignore_if_present: bool | None = None,
    in what role. Note that it is not ordered with respect to
    INCLUDE = "include"
    INDEXEDDB = "indexeddb"
    INSUFFICIENT_BUDGET = "insufficientBudget"
    INSUFFICIENT_NAMED_BUDGET = "insufficientNamedBudget"
    INSUFFICIENT_SOURCE_CAPACITY = "insufficientSourceCapacity"
    INSUFFICIENT_UNIQUE_DESTINATION_CAPACITY = "insufficientUniqueDestinationCapacity"
    INTEREST_GROUPS = "interest_groups"
    interestGroupAuctionNetworkRequestCreated.
    INTERNAL_ERROR = "internalError"
    issuer_origin: str
    issuer_origin: str,
    JOIN = "join"
    json = yield cmd_dict
    key: str
    key: str | None = None
    key: str,
    key_piece: UnsignedInt128AsBase16
    KEYS = "keys"
    LEAVE = "leave"
    Leaves other stored data, including the issuer's Redemption Records, intact.
    LENGTH = "length"
    length: int
    limit: float
    LOADED = "loaded"
    loadingFailed).
    LOCAL_STORAGE = "local_storage"
    lookback_window: int | None = None
    main_frame_id: page.FrameId
    max_event_level_reports: int
    max_event_states: float
    method: SharedStorageAccessMethod
    MODULUS = "modulus"
    name: str
    name: str | None = None
    NAVIGATION = "navigation"
    Network.requestWillBeSent (but will happen before loadingFinished
    NEVER_ATTRIBUTED_SOURCE = "neverAttributedSource"
    NO_CAPACITY_FOR_ATTRIBUTION_DESTINATION = "noCapacityForAttributionDestination"
    NO_HISTOGRAMS = "noHistograms"
    NO_MATCHING_CONFIGURATIONS = "noMatchingConfigurations"
    NO_MATCHING_SOURCE_FILTER_DATA = "noMatchingSourceFilterData"
    NO_MATCHING_SOURCES = "noMatchingSources"
    NO_MATCHING_TRIGGER_DATA = "noMatchingTriggerData"
    not_filters: list[AttributionReportingFilterConfig]
    NOT_REGISTERED = "notRegistered"
    object_store_name: str
    One of the interest groups was accessed. Note that these events are global
    operation_name: str | None = None
    origin: str
    origin: str,
    origin: str, quota_size: float | None = None
    origin: str, storage_types: str
    OTHER = "other"
    Override quota for the specified origin
    owner_origin: str
    owner_origin: str,
    owner_origin: str, key: str
    owner_origin: str, name: str
    owner_site: str
    Pair of issuer origin and number of available (signed, but not used) Trust
    Pair of reporting metadata details for a candidate URL for ``selectURL()``.
    params: SharedStorageAccessParams
    params: T_JSON_DICT = dict()
    params["bucket"] = bucket.to_json()
    params["cookies"] = [i.to_json() for i in cookies]
    params["enable"] = enable
    params["enabled"] = enabled
    params["firstPartyUrl"] = first_party_url
    params["frameId"] = frame_id.to_json()
    params["issuerOrigin"] = issuer_origin
    params["key"] = key
    params["name"] = name
    params["origin"] = origin
    params["ownerOrigin"] = owner_origin
    params["storageKey"] = storage_key
    params["storageTypes"] = storage_types
    params["thirdPartyUrls"] = [i for i in third_party_urls]
    params["value"] = value
    parent_auction_id: InterestGroupAuctionId | None
    persistent: bool
    presence/absence can vary according to SharedStorageAccessType.
    primary_sites: list[str]
    priority: SignedInt64AsBase10
    PRIORITY_TOO_LOW = "priorityTooLow"
    PROHIBITED_BY_BROWSER_POLICY = "prohibitedByBrowserPolicy"
    Protected audience interest group auction identifier.
    PROTECTED_AUDIENCE_WORKLET = "protectedAudienceWorklet"
    quota: float
    Registers origin to be notified when an update occurs to its cache storage list.
    Registers origin to be notified when an update occurs to its IndexedDB.
    Registers storage key to be notified when an update occurs to its cache storage list.
    Registers storage key to be notified when an update occurs to its IndexedDB.
    registration: AttributionReportingSourceRegistration
    registration: AttributionReportingTriggerRegistration
    RELAXED = "relaxed"
    REMAINING_BUDGET = "remainingBudget"
    remaining_budget: float
    Removes all Trust Tokens issued by the provided issuerOrigin.
    REPORT_WINDOW_NOT_STARTED = "reportWindowNotStarted"
    REPORT_WINDOW_PASSED = "reportWindowPassed"
    reporting_metadata: list[SharedStorageReportingMetadata]
    reporting_origin: str
    REPORTING_ORIGINS_PER_SITE_LIMIT_REACHED = "reportingOriginsPerSiteLimitReached"
    reporting_url: str
    request_id: network.RequestId
    Resets the budget for ``ownerOrigin`` by clearing all budget withdrawals.
    result: AttributionReportingSourceRegistrationResult
    return (
    return [network.Cookie.from_json(i) for i in json["cookies"]]
    return [RelatedWebsiteSet.from_json(i) for i in json["sets"]]
    return [SharedStorageEntry.from_json(i) for i in json["entries"]]
    return [str(i) for i in json["deletedSites"]]
    return [str(i) for i in json["matchedUrls"]]
    return [TrustTokens.from_json(i) for i in json["tokens"]]
    return bool(json["didDeleteTokens"])
    return dict(json["details"])
    return int(json["numSent"])
    return SerializedStorageKey.from_json(json["storageKey"])
    return SharedStorageMetadata.from_json(json["metadata"])
    Returns a storage key given a frame id.
    Returns all browser cookies.
    Returns the effective Related Website Sets in use by this profile for the browser
    Returns the list of URLs from a page and its embedded resources that match
    Returns the number of stored Trust Tokens per issuer for the
    Returns usage and quota in bytes.
    RUN = "run"
    scheduled report time.
    scope: SharedStorageAccessScope
    scopes: list[str]
    scopes_data: AttributionScopesData | None = None
    script_source_url: str | None = None
    SELECT_URL = "selectURL"
    SELLER_JS = "sellerJs"
    SELLER_TRUSTED_SIGNALS = "sellerTrustedSignals"
    Sends all pending Attribution Reports immediately, regardless of their
    serialized_data: str | None = None
    service_sites: list[str]
    SERVICE_WORKERS = "service_workers"
    session. The effective Related Website Sets will not change during a browser session.
    Set tracking for a storage key's buckets.
    SET_ = "set"
    Sets entry with ``key`` and ``value`` for a given origin's shared storage.
    Sets given cookies.
    SHADER_CACHE = "shader_cache"
    Shared storage was accessed by the associated page.
    SHARED_STORAGE = "shared_storage"
    SHARED_STORAGE_WORKLET = "sharedStorageWorklet"
    source_keys: list[str]
    source_origin: str
    source_registration_time_config: AttributionReportingSourceRegistrationTimeConfig
    Specifies which auctions a particular network fetch may be related to, and
    start: int
    STARTED = "started"
    STORAGE_BUCKETS = "storage_buckets"
    storage_key: SerializedStorageKey
    storage_key: str
    storage_key: str,
    storage_key: str, enable: bool
    storage_key: str, storage_types: str
    storage_type: StorageType
    STRICT = "strict"
    Struct for a single key-value pair in an origin's shared storage.
    SUCCESS = "success"
    SUCCESS_DROPPED_LOWER_PRIORITY = "successDroppedLowerPriority"
    SUCCESS_NOISED = "successNoised"
    T_JSON_DICT,
    target-specific.
    The following parameters are included in all events.
    The origin's IndexedDB database list has been modified.
    The origin's IndexedDB object store has been modified.
    time: network.TimeSinceEpoch
    to all targets sharing an interest group store.
    Tokens from that issuer.
    TOP_LEVEL_ADDITIONAL_BID = "topLevelAdditionalBid"
    TOP_LEVEL_BID = "topLevelBid"
    trigger_context_id: str | None = None
    trigger_data: list[float]
    trigger_data_matching: AttributionReportingTriggerDataMatching
    trigger_specs: list[AttributionReportingTriggerSpec]
    tuple[float, float, bool, list[UsageForType]],
    type_: AttributionReportingSourceType
    type_: InterestGroupAccessType
    type_: InterestGroupAuctionEventType
    type_: InterestGroupAuctionFetchType
    types: list[str]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, int]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[RelatedWebsiteSet]]
    typing.Generator[T_JSON_DICT, T_JSON_DICT, list[str]]
    unique_auction_id: InterestGroupAuctionId
    unique_auction_id: InterestGroupAuctionId | None
    Unregisters origin from receiving notifications for cache storage.
    Unregisters origin from receiving notifications for IndexedDB.
    Unregisters storage key from receiving notifications for cache storage.
    Unregisters storage key from receiving notifications for IndexedDB.
    UPDATE = "update"
    url: str
    urls_with_metadata: list[SharedStorageUrlWithMetadata] | None = None
    Usage for a storage type.
    usage: float
    value: float
    value: str
    value: str | None = None
    value: str,
    value: UnsignedInt128AsBase16
    VALUES = "values"
    values: list[AttributionReportingAggregatableValueDictEntry]
    values: list[str]
    WEBSQL = "websql"
    WIN = "win"
    WINDOW = "window"
#
# CDP domain: Storage (experimental)
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, dict]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[network.Cookie]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[SharedStorageEntry]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[str]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, SerializedStorageKey]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, SharedStorageMetadata]:
):
@dataclass
@event_class("Storage.attributionReportingSourceRegistered")
@event_class("Storage.attributionReportingTriggerRegistered")
@event_class("Storage.cacheStorageContentUpdated")
@event_class("Storage.cacheStorageListUpdated")
@event_class("Storage.indexedDBContentUpdated")
@event_class("Storage.indexedDBListUpdated")
@event_class("Storage.interestGroupAccessed")
@event_class("Storage.interestGroupAuctionEventOccurred")
@event_class("Storage.interestGroupAuctionNetworkRequestCreated")
@event_class("Storage.sharedStorageAccessed")
@event_class("Storage.storageBucketCreatedOrUpdated")
@event_class("Storage.storageBucketDeleted")
]:
class AttributionReportingAggregatableDebugReportingConfig:
class AttributionReportingAggregatableDebugReportingData:
class AttributionReportingAggregatableDedupKey:
class AttributionReportingAggregatableResult:
class AttributionReportingAggregatableTriggerData:
class AttributionReportingAggregatableValueDictEntry:
class AttributionReportingAggregatableValueEntry:
class AttributionReportingAggregationKeysEntry:
class AttributionReportingEventLevelResult:
class AttributionReportingEventReportWindows:
class AttributionReportingEventTriggerData:
class AttributionReportingFilterConfig:
class AttributionReportingFilterDataEntry:
class AttributionReportingFilterPair:
class AttributionReportingSourceRegistered:
class AttributionReportingSourceRegistration:
class AttributionReportingSourceRegistrationResult:
class AttributionReportingSourceRegistrationTimeConfig:
class AttributionReportingSourceType:
class AttributionReportingTriggerDataMatching:
class AttributionReportingTriggerRegistered:
class AttributionReportingTriggerRegistration:
class AttributionReportingTriggerSpec:
class AttributionScopesData:
class CacheStorageContentUpdated:
class CacheStorageListUpdated:
class IndexedDBContentUpdated:
class IndexedDBListUpdated:
class InterestGroupAccessed:
class InterestGroupAccessType:
class InterestGroupAuctionEventOccurred:
class InterestGroupAuctionEventType:
class InterestGroupAuctionFetchType:
class InterestGroupAuctionId:
class InterestGroupAuctionNetworkRequestCreated:
class RelatedWebsiteSet:
class SerializedStorageKey:
class SharedStorageAccessed:
class SharedStorageAccessMethod:
class SharedStorageAccessParams:
class SharedStorageAccessScope:
class SharedStorageEntry:
class SharedStorageMetadata:
class SharedStorageReportingMetadata:
class SharedStorageUrlWithMetadata:
class SignedInt64AsBase10:
class StorageBucket:
class StorageBucketCreatedOrUpdated:
class StorageBucketDeleted:
class StorageBucketInfo:
class StorageBucketsDurability:
class StorageType:
class TrustTokens:
class UnsignedInt128AsBase16:
class UnsignedInt64AsBase10:
class UsageForType:
def clear_cookies(
def clear_data_for_origin(
def clear_data_for_storage_key(
def clear_shared_storage_entries(
def clear_trust_tokens(
def delete_shared_storage_entry(
def delete_storage_bucket(
def get_affected_urls_for_third_party_cookie_metadata(
def get_cookies(
def get_interest_group_details(
def get_related_website_sets() -> (
def get_shared_storage_entries(
def get_shared_storage_metadata(
def get_storage_key_for_frame(
def get_trust_tokens() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[TrustTokens]]:
def get_usage_and_quota(
def override_quota_for_origin(
def reset_shared_storage_budget(
def run_bounce_tracking_mitigations() -> (
def send_pending_attribution_reports() -> (
def set_attribution_reporting_local_testing_mode(
def set_attribution_reporting_tracking(
def set_cookies(
def set_interest_group_auction_tracking(
def set_interest_group_tracking(
def set_shared_storage_entry(
def set_shared_storage_tracking(
def set_storage_bucket_tracking(
def track_cache_storage_for_origin(
def track_cache_storage_for_storage_key(
def track_indexed_db_for_origin(
def track_indexed_db_for_storage_key(
def untrack_cache_storage_for_origin(
def untrack_cache_storage_for_storage_key(
def untrack_indexed_db_for_origin(
def untrack_indexed_db_for_storage_key(
from . import browser
from . import network
from . import page
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing

pass
