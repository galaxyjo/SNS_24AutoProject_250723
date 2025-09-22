
for i in json["mismatchedHeaders"]
                    PrerenderMismatchedHeaders.from_json(i)
                [
                ]
                dom.BackendNodeId.from_json(json["backendNodeId"])
                else None
                for i in json["preloadingAttemptSources"]
                if "backendNodeId" in json
                if "disallowedMojoInterface" in json
                if "errorType" in json
                if "mismatchedHeaders" in json
                if "prerenderStatus" in json
                if "requestId" in json
                if "targetHint" in json
                json["disabledByHoldbackPrefetchSpeculationRules"]
                json["disabledByHoldbackPrerenderSpeculationRules"]
                network.RequestId.from_json(json["requestId"])
                PreloadingAttemptSource.from_json(i)
                PrerenderFinalStatus.from_json(json["prerenderStatus"])
                RuleSetErrorType.from_json(json["errorType"])
                SpeculationTargetHint.from_json(json["targetHint"])
                str(json["activationValue"]) if "activationValue" in json else None
                str(json["disallowedMojoInterface"])
            ),
            ],
            action=SpeculationAction.from_json(json["action"]),
            activation_value=(
            backend_node_id=(
            disabled_by_battery_saver=bool(json["disabledByBatterySaver"]),
            disabled_by_data_saver=bool(json["disabledByDataSaver"]),
            disabled_by_holdback_prefetch_speculation_rules=bool(
            disabled_by_holdback_prerender_speculation_rules=bool(
            disabled_by_preference=bool(json["disabledByPreference"]),
            disallowed_mojo_interface=(
            error_message=str(json["errorMessage"]) if "errorMessage" in json else None,
            error_type=(
            header_name=str(json["headerName"]),
            id_=RuleSetId.from_json(json["id"]),
            initial_value=str(json["initialValue"]) if "initialValue" in json else None,
            initiating_frame_id=page.FrameId.from_json(json["initiatingFrameId"]),
            json["activationValue"] = self.activation_value
            json["backendNodeId"] = self.backend_node_id.to_json()
            json["errorMessage"] = self.error_message
            json["errorType"] = self.error_type.to_json()
            json["initialValue"] = self.initial_value
            json["requestId"] = self.request_id.to_json()
            json["targetHint"] = self.target_hint.to_json()
            json["url"] = self.url
            key=PreloadingAttemptKey.from_json(json["key"]),
            loader_id=network.LoaderId.from_json(json["loaderId"]),
            mismatched_headers=(
            node_ids=[dom.BackendNodeId.from_json(i) for i in json["nodeIds"]],
            pipeline_id=PreloadPipelineId.from_json(json["pipelineId"]),
            prefetch_status=PrefetchStatus.from_json(json["prefetchStatus"]),
            prefetch_url=str(json["prefetchUrl"]),
            preloading_attempt_sources=[
            prerender_status=(
            request_id=(
            request_id=network.RequestId.from_json(json["requestId"]),
            rule_set_ids=[RuleSetId.from_json(i) for i in json["ruleSetIds"]],
            source_text=str(json["sourceText"]),
            status=PreloadingStatus.from_json(json["status"]),
            target_hint=(
            url=str(json["url"]) if "url" in json else None,
            url=str(json["url"]),
        "ActivatedWithAuxiliaryBrowsingContexts"
        "ActivationNavigationDestroyedBeforeSuccess"
        "CrossSiteNavigationInInitialNavigation"
        "CrossSiteNavigationInMainFrameNavigation"
        "CrossSiteRedirectInMainFrameNavigation"
        "MaxNumOfRunningEagerPrerendersExceeded"
        "MaxNumOfRunningEmbedderPrerendersExceeded"
        "MaxNumOfRunningNonEagerPrerendersExceeded"
        "method": "Preload.disable",
        "method": "Preload.enable",
        "PrefetchEvictedAfterBrowsingDataRemoved"
        "PrefetchNotEligibleBatterySaverEnabled"
        "PrefetchNotEligibleBrowserContextOffTheRecord"
        "PrefetchNotEligibleNonDefaultStoragePartition"
        "PrefetchNotEligibleRedirectFromServiceWorker"
        "PrefetchNotEligibleRedirectToServiceWorker"
        "PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy"
        "PrefetchNotEligibleUserHasServiceWorker"
        "PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler"
        "PrimaryMainFrameRendererProcessCrashed"
        "RedirectedPrerenderingUrlHasEffectiveUrl"
        "SameSiteCrossOriginNavigationNotOptInInInitialNavigation"
        "SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation"
        "SameSiteCrossOriginRedirectNotOptInInInitialNavigation"
        "SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation"
        )
        if self.activation_value is not None:
        if self.backend_node_id is not None:
        if self.error_message is not None:
        if self.error_type is not None:
        if self.initial_value is not None:
        if self.request_id is not None:
        if self.target_hint is not None:
        if self.url is not None:
        json = dict()
        json["action"] = self.action.to_json()
        json["headerName"] = self.header_name
        json["id"] = self.id_.to_json()
        json["key"] = self.key.to_json()
        json["loaderId"] = self.loader_id.to_json()
        json["nodeIds"] = [i.to_json() for i in self.node_ids]
        json["ruleSetIds"] = [i.to_json() for i in self.rule_set_ids]
        json["sourceText"] = self.source_text
        json["url"] = self.url
        return "PreloadPipelineId({})".format(super().__repr__())
        return "RuleSetId({})".format(super().__repr__())
        return cls(
        return cls(id_=RuleSetId.from_json(json["id"]))
        return cls(json)
        return cls(rule_set=RuleSet.from_json(json["ruleSet"]))
        return json
        return self
        return self.value
    """
    #:
    #: - https://github.com/WICG/nav-speculation/blob/main/triggers.md
    #: - https://wicg.github.io/nav-speculation/speculation-rules.html
    #: - https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-header
    #: - https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-script
    #: ``errorMessage`` is null iff ``errorType`` is null.
    #: ``script`` tag or through an external resource via the
    #: ``script`` tag, it is the textContent of the node. Note that it is
    #: a JSON for valid case.
    #: A speculation rule set is either added through an inline
    #: case, we include the external URL where the rule set was loaded
    #: Error information
    #: from, and also RequestId if Network domain is enabled.
    #: Identifies a document which the rule set is associated with.
    #: See also:
    #: Source text of JSON representing the rule set. If it comes from
    #: 'Speculation-Rules' HTTP header. For the first case, we include
    #: that is incompatible with prerender and has caused the cancellation of the attempt.
    #: the BackendNodeId of the relevant ``script`` tag. For the second
    #: The frame id of the frame initiating prefetch.
    #: This is used to give users more information about the name of Mojo interface
    #: TODO(https://crbug.com/1425354): Replace this property with structured error.
    )
    @classmethod
    ``PreloadPipelineId``.
    }
    A key that identifies a preloading attempt.
    action: SpeculationAction
    ACTIVATED = "Activated"
    ACTIVATED_BEFORE_STARTED = "ActivatedBeforeStarted"
    ACTIVATED_DURING_MAIN_FRAME_NAVIGATION = "ActivatedDuringMainFrameNavigation"
    ACTIVATED_IN_BACKGROUND = "ActivatedInBackground"
    ACTIVATED_WITH_AUXILIARY_BROWSING_CONTEXTS = (
    ACTIVATION_FRAME_POLICY_NOT_COMPATIBLE = "ActivationFramePolicyNotCompatible"
    ACTIVATION_NAVIGATION_DESTROYED_BEFORE_SUCCESS = (
    ACTIVATION_NAVIGATION_PARAMETER_MISMATCH = "ActivationNavigationParameterMismatch"
    ACTIVATION_URL_HAS_EFFECTIVE_URL = "ActivationUrlHasEffectiveUrl"
    activation_value: str | None = None
    ALL_PRERENDERING_CANCELED = "AllPrerenderingCanceled"
    attempt (in the case of attempts triggered by a document rule). It is
    AUDIO_OUTPUT_DEVICE_REQUESTED = "AudioOutputDeviceRequested"
    backend_node_id: dom.BackendNodeId | None = None
    BackendNodeIds of <a href> or <area href> elements that triggered the
    BATTERY_SAVER_ENABLED = "BatterySaverEnabled"
    BLANK = "Blank"
    BLOCKED_BY_CLIENT = "BlockedByClient"
    BROWSING_DATA_REMOVED = "BrowsingDataRemoved"
    CANCEL_ALL_HOSTS_FOR_TESTING = "CancelAllHostsForTesting"
    CDP events for them are emitted separately but they share
    Chrome manages different types of preloads together using a
    CLIENT_CERT_REQUESTED = "ClientCertRequested"
    cmd_dict: T_JSON_DICT = {
    concept of preloading pipeline. For example, if a site uses a
    Corresponds to mojom::SpeculationTargetHint.
    Corresponds to SpeculationRuleSet
    CROSS_SITE_NAVIGATION_IN_INITIAL_NAVIGATION = (
    CROSS_SITE_NAVIGATION_IN_MAIN_FRAME_NAVIGATION = (
    CROSS_SITE_REDIRECT_IN_INITIAL_NAVIGATION = "CrossSiteRedirectInInitialNavigation"
    CROSS_SITE_REDIRECT_IN_MAIN_FRAME_NAVIGATION = (
    DATA_SAVER_ENABLED = "DataSaverEnabled"
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: str) -> PreloadPipelineId:
    def from_json(cls, json: str) -> RuleSetId:
    def from_json(cls, json: T_JSON_DICT) -> PrefetchStatusUpdated:
    def from_json(cls, json: T_JSON_DICT) -> PreloadEnabledStateUpdated:
    def from_json(cls, json: T_JSON_DICT) -> PreloadingAttemptSourcesUpdated:
    def from_json(cls, json: T_JSON_DICT) -> PrerenderStatusUpdated:
    def from_json(cls, json: T_JSON_DICT) -> RuleSetRemoved:
    def from_json(cls, json: T_JSON_DICT) -> RuleSetUpdated:
    def to_json(self) -> str:
    def to_json(self):
    DESTROYED = "Destroyed"
    DID_FAIL_LOAD = "DidFailLoad"
    disabled_by_battery_saver: bool
    disabled_by_data_saver: bool
    disabled_by_holdback_prefetch_speculation_rules: bool
    disabled_by_holdback_prerender_speculation_rules: bool
    disabled_by_preference: bool
    disallowed_mojo_interface: str | None
    DOWNLOAD = "Download"
    EMBEDDER_HOST_DISALLOWED = "EmbedderHostDisallowed"
    error_message: str | None = None
    error_type: RuleSetErrorType | None = None
    FAILURE = "Failure"
    filter out the ones that aren't necessary to the developers.
    Fired when a prefetch attempt is updated.
    Fired when a preload enabled state is updated.
    Fired when a prerender attempt is updated.
    header_name: str
    id_: RuleSetId
    INACTIVE_PAGE_RESTRICTION = "InactivePageRestriction"
    Information of headers to be displayed when the header mismatch occurred.
    initial_value: str | None = None
    initiating_frame_id: page.FrameId
    INVALID_RULES_SKIPPED = "InvalidRulesSkipped"
    INVALID_SCHEME_NAVIGATION = "InvalidSchemeNavigation"
    INVALID_SCHEME_REDIRECT = "InvalidSchemeRedirect"
    isn't being used by clients).
    JAVA_SCRIPT_INTERFACE_ADDED = "JavaScriptInterfaceAdded"
    JAVA_SCRIPT_INTERFACE_REMOVED = "JavaScriptInterfaceRemoved"
    json = yield cmd_dict
    key: PreloadingAttemptKey
    List of FinalStatus reasons for Prerender2.
    Lists sources for a preloading attempt, specifically the ids of rule sets
    loader_id: network.LoaderId
    LOGIN_AUTH_REQUESTED = "LoginAuthRequested"
    LOW_END_DEVICE = "LowEndDevice"
    MAIN_FRAME_NAVIGATION = "MainFrameNavigation"
    MAX_NUM_OF_RUNNING_EAGER_PRERENDERS_EXCEEDED = (
    MAX_NUM_OF_RUNNING_EMBEDDER_PRERENDERS_EXCEEDED = (
    MAX_NUM_OF_RUNNING_NON_EAGER_PRERENDERS_EXCEEDED = (
    MEMORY_LIMIT_EXCEEDED = "MemoryLimitExceeded"
    MEMORY_PRESSURE_AFTER_TRIGGERED = "MemoryPressureAfterTriggered"
    MEMORY_PRESSURE_ON_TRIGGER = "MemoryPressureOnTrigger"
    mismatched_headers: list[PrerenderMismatchedHeaders] | None
    MIXED_CONTENT = "MixedContent"
    MOJO_BINDER_POLICY = "MojoBinderPolicy"
    mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it
    NAVIGATION_BAD_HTTP_STATUS = "NavigationBadHttpStatus"
    NAVIGATION_NOT_COMMITTED = "NavigationNotCommitted"
    NAVIGATION_REQUEST_BLOCKED_BY_CSP = "NavigationRequestBlockedByCsp"
    NAVIGATION_REQUEST_NETWORK_ERROR = "NavigationRequestNetworkError"
    node_ids: list[dom.BackendNodeId]
    not the final url that is navigated to. For example, prerendering allows
    NOT_SUPPORTED = "NotSupported"
    OTHER_PRERENDERED_PAGE_ACTIVATED = "OtherPrerenderedPageActivated"
    PENDING = "Pending"
    pipeline_id: PreloadPipelineId
    possible for multiple rule sets and links to trigger a single attempt.
    PREFETCH = "Prefetch"
    PREFETCH_ALLOWED = "PrefetchAllowed"
    PREFETCH_EVICTED_AFTER_BROWSING_DATA_REMOVED = (
    PREFETCH_EVICTED_AFTER_CANDIDATE_REMOVED = "PrefetchEvictedAfterCandidateRemoved"
    PREFETCH_EVICTED_FOR_NEWER_PREFETCH = "PrefetchEvictedForNewerPrefetch"
    PREFETCH_FAILED_INELIGIBLE_REDIRECT = "PrefetchFailedIneligibleRedirect"
    PREFETCH_FAILED_INVALID_REDIRECT = "PrefetchFailedInvalidRedirect"
    PREFETCH_FAILED_MIME_NOT_SUPPORTED = "PrefetchFailedMIMENotSupported"
    PREFETCH_FAILED_NET_ERROR = "PrefetchFailedNetError"
    PREFETCH_FAILED_NON2_XX = "PrefetchFailedNon2XX"
    PREFETCH_HELDBACK = "PrefetchHeldback"
    PREFETCH_INELIGIBLE_RETRY_AFTER = "PrefetchIneligibleRetryAfter"
    PREFETCH_IS_PRIVACY_DECOY = "PrefetchIsPrivacyDecoy"
    PREFETCH_IS_STALE = "PrefetchIsStale"
    PREFETCH_NOT_ELIGIBLE_BATTERY_SAVER_ENABLED = (
    PREFETCH_NOT_ELIGIBLE_BROWSER_CONTEXT_OFF_THE_RECORD = (
    PREFETCH_NOT_ELIGIBLE_DATA_SAVER_ENABLED = "PrefetchNotEligibleDataSaverEnabled"
    PREFETCH_NOT_ELIGIBLE_EXISTING_PROXY = "PrefetchNotEligibleExistingProxy"
    PREFETCH_NOT_ELIGIBLE_HOST_IS_NON_UNIQUE = "PrefetchNotEligibleHostIsNonUnique"
    PREFETCH_NOT_ELIGIBLE_NON_DEFAULT_STORAGE_PARTITION = (
    PREFETCH_NOT_ELIGIBLE_PRELOADING_DISABLED = "PrefetchNotEligiblePreloadingDisabled"
    PREFETCH_NOT_ELIGIBLE_REDIRECT_FROM_SERVICE_WORKER = (
    PREFETCH_NOT_ELIGIBLE_REDIRECT_TO_SERVICE_WORKER = (
    PREFETCH_NOT_ELIGIBLE_SAME_SITE_CROSS_ORIGIN_PREFETCH_REQUIRED_PROXY = (
    PREFETCH_NOT_ELIGIBLE_SCHEME_IS_NOT_HTTPS = "PrefetchNotEligibleSchemeIsNotHttps"
    PREFETCH_NOT_ELIGIBLE_USER_HAS_COOKIES = "PrefetchNotEligibleUserHasCookies"
    PREFETCH_NOT_ELIGIBLE_USER_HAS_SERVICE_WORKER = (
    PREFETCH_NOT_ELIGIBLE_USER_HAS_SERVICE_WORKER_NO_FETCH_HANDLER = (
    PREFETCH_NOT_FINISHED_IN_TIME = "PrefetchNotFinishedInTime"
    PREFETCH_NOT_STARTED = "PrefetchNotStarted"
    PREFETCH_NOT_USED_COOKIES_CHANGED = "PrefetchNotUsedCookiesChanged"
    PREFETCH_NOT_USED_PROBE_FAILED = "PrefetchNotUsedProbeFailed"
    PREFETCH_PROXY_NOT_AVAILABLE = "PrefetchProxyNotAvailable"
    PREFETCH_RESPONSE_USED = "PrefetchResponseUsed"
    prefetch_status: PrefetchStatus
    PREFETCH_SUCCESSFUL_BUT_NOT_USED = "PrefetchSuccessfulButNotUsed"
    prefetch_url: str
    Preloading status values, see also PreloadingTriggeringOutcome. This
    preloading_attempt_sources: list[PreloadingAttemptSource]
    PRELOADING_DISABLED = "PreloadingDisabled"
    PRELOADING_UNSUPPORTED_BY_WEB_CONTENTS = "PreloadingUnsupportedByWebContents"
    PRERENDER = "Prerender"
    PRERENDER_FAILED_DURING_PREFETCH = "PrerenderFailedDuringPrefetch"
    prerender_status: PrerenderFinalStatus | None
    PRERENDERING_DISABLED_BY_DEV_TOOLS = "PrerenderingDisabledByDevTools"
    PRERENDERING_URL_HAS_EFFECTIVE_URL = "PrerenderingUrlHasEffectiveUrl"
    PRIMARY_MAIN_FRAME_RENDERER_PROCESS_CRASHED = (
    PRIMARY_MAIN_FRAME_RENDERER_PROCESS_KILLED = "PrimaryMainFrameRendererProcessKilled"
    READY = "Ready"
    REDIRECTED_PRERENDERING_URL_HAS_EFFECTIVE_URL = (
    RENDERER_PROCESS_CRASHED = "RendererProcessCrashed"
    RENDERER_PROCESS_KILLED = "RendererProcessKilled"
    request_id: network.RequestId
    request_id: network.RequestId | None = None
    rule_set: RuleSet
    rule_set_ids: list[RuleSetId]
    RUNNING = "Running"
    SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_INITIAL_NAVIGATION = (
    SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION = (
    SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_INITIAL_NAVIGATION = (
    SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION = (
    same-origin main frame navigations during the attempt, but the attempt is
    See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
    SELF = "Self"
    Send a list of sources for all preloading attempts in a document.
    SLOW_NETWORK = "SlowNetwork"
    SOURCE_IS_NOT_JSON_OBJECT = "SourceIsNotJsonObject"
    source_text: str
    SPECULATION_RULE_REMOVED = "SpeculationRuleRemoved"
    SpeculationRules for prerender, Chrome first starts a prefetch and
    SSL_CERTIFICATE_ERROR = "SslCertificateError"
    START_FAILED = "StartFailed"
    status is shared by prefetchStatusUpdated and prerenderStatusUpdated.
    status: PreloadingStatus
    still keyed with the initial URL.
    STOP = "Stop"
    SUCCESS = "Success"
    TAB_CLOSED_BY_USER_GESTURE = "TabClosedByUserGesture"
    TAB_CLOSED_WITHOUT_USER_GESTURE = "TabClosedWithoutUserGesture"
    target_hint: SpeculationTargetHint | None = None
    that had a speculation rule that triggered the attempt, and the
    The type of preloading attempted. It corresponds to
    The url used is the url specified by the trigger (i.e. the initial URL), and
    then upgrades it to prerender.
    TIMEOUT_BACKGROUNDED = "TimeoutBackgrounded"
    TODO(https://crbug.com/1384419): revisit the list of PrefetchStatus and
    TRIGGER_BACKGROUNDED = "TriggerBackgrounded"
    TRIGGER_DESTROYED = "TriggerDestroyed"
    TRIGGER_URL_HAS_EFFECTIVE_URL = "TriggerUrlHasEffectiveUrl"
    UA_CHANGE_REQUIRES_RELOAD = "UaChangeRequiresReload"
    Unique id
    Upsert. Currently, it is only emitted when a rule set added.
    url: str
    url: str | None = None
    V8_OPTIMIZER_DISABLED = "V8OptimizerDisabled"
    WINDOW_CLOSED = "WindowClosed"
#
# CDP domain: Preload (experimental)
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
@dataclass
@event_class("Preload.prefetchStatusUpdated")
@event_class("Preload.preloadEnabledStateUpdated")
@event_class("Preload.preloadingAttemptSourcesUpdated")
@event_class("Preload.prerenderStatusUpdated")
@event_class("Preload.ruleSetRemoved")
@event_class("Preload.ruleSetUpdated")
class PrefetchStatus:
class PrefetchStatusUpdated:
class PreloadEnabledStateUpdated:
class PreloadingAttemptKey:
class PreloadingAttemptSource:
class PreloadingAttemptSourcesUpdated:
class PreloadingStatus:
class PreloadPipelineId:
class PrerenderFinalStatus:
class PrerenderMismatchedHeaders:
class PrerenderStatusUpdated:
class RuleSet:
class RuleSetErrorType:
class RuleSetId:
class RuleSetRemoved:
class RuleSetUpdated:
class SpeculationAction:
class SpeculationTargetHint:
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
from . import dom
from . import network
from . import page
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing

pass
