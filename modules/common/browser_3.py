
                bool(json["allowWithoutGesture"])
                bool(json["allowWithoutSanitization"])
                bool(json["userVisibleOnly"]) if "userVisibleOnly" in json else None
                else None
                if "allowWithoutGesture" in json
                if "allowWithoutSanitization" in json
                if "windowState" in json
                WindowState.from_json(json["windowState"])
            ),
            allow_without_gesture=(
            allow_without_sanitization=(
            buckets=[Bucket.from_json(i) for i in json["buckets"]],
            count=int(json["count"]),
            frame_id=page.FrameId.from_json(json["frameId"]),
            guid=str(json["guid"]),
            height=int(json["height"]) if "height" in json else None,
            high=int(json["high"]),
            json["allowWithoutGesture"] = self.allow_without_gesture
            json["allowWithoutSanitization"] = self.allow_without_sanitization
            json["height"] = self.height
            json["left"] = self.left
            json["panTiltZoom"] = self.pan_tilt_zoom
            json["sysex"] = self.sysex
            json["top"] = self.top
            json["userVisibleOnly"] = self.user_visible_only
            json["width"] = self.width
            json["windowState"] = self.window_state.to_json()
            left=int(json["left"]) if "left" in json else None,
            low=int(json["low"]),
            name=str(json["name"]),
            pan_tilt_zoom=bool(json["panTiltZoom"]) if "panTiltZoom" in json else None,
            received_bytes=float(json["receivedBytes"]),
            state=str(json["state"]),
            suggested_filename=str(json["suggestedFilename"]),
            sum_=int(json["sum"]),
            sysex=bool(json["sysex"]) if "sysex" in json else None,
            top=int(json["top"]) if "top" in json else None,
            total_bytes=float(json["totalBytes"]),
            url=str(json["url"]),
            user_visible_only=(
            width=int(json["width"]) if "width" in json else None,
            window_state=(
        "method": "Browser.addPrivacySandboxCoordinatorKeyConfig",
        "method": "Browser.addPrivacySandboxEnrollmentOverride",
        "method": "Browser.cancelDownload",
        "method": "Browser.close",
        "method": "Browser.crash",
        "method": "Browser.crashGpuProcess",
        "method": "Browser.executeBrowserCommand",
        "method": "Browser.getBrowserCommandLine",
        "method": "Browser.getHistogram",
        "method": "Browser.getHistograms",
        "method": "Browser.getVersion",
        "method": "Browser.getWindowBounds",
        "method": "Browser.getWindowForTarget",
        "method": "Browser.grantPermissions",
        "method": "Browser.resetPermissions",
        "method": "Browser.setDockTile",
        "method": "Browser.setDownloadBehavior",
        "method": "Browser.setPermission",
        "method": "Browser.setWindowBounds",
        "params": params,
        )
        0. **protocolVersion** - Protocol version.
        0. **windowId** - Browser window id.
        1. **bounds** - Bounds information of the window. When window state is 'minimized', the restored window position and size are returned.
        1. **product** - Product name.
        2. **revision** - Product revision.
        3. **userAgent** - User-Agent.
        4. **jsVersion** - V8 version.
        if self.allow_without_gesture is not None:
        if self.allow_without_sanitization is not None:
        if self.height is not None:
        if self.left is not None:
        if self.pan_tilt_zoom is not None:
        if self.sysex is not None:
        if self.top is not None:
        if self.user_visible_only is not None:
        if self.width is not None:
        if self.window_state is not None:
        json = dict()
        json["buckets"] = [i.to_json() for i in self.buckets]
        json["count"] = self.count
        json["high"] = self.high
        json["low"] = self.low
        json["name"] = self.name
        json["sum"] = self.sum_
        params["badgeLabel"] = badge_label
        params["browserContextId"] = browser_context_id.to_json()
        params["delta"] = delta
        params["downloadPath"] = download_path
        params["eventsEnabled"] = events_enabled
        params["image"] = image
        params["origin"] = origin
        params["query"] = query
        params["targetId"] = target_id.to_json()
        return "BrowserContextID({})".format(super().__repr__())
        return "WindowID({})".format(super().__repr__())
        return cls(
        return cls(json)
        return json
        return self
        return self.value
        str(json["jsVersion"]),
        str(json["product"]),
        str(json["protocolVersion"]),
        str(json["revision"]),
        str(json["userAgent"]),
    """
    #: Buckets.
    #: Download status.
    #: For "camera" permission, may specify panTiltZoom.
    #: For "clipboard" permission, may specify allowWithoutSanitization.
    #: For "fullscreen" permission, must specify allowWithoutGesture:true.
    #: For "midi" permission, may also specify sysex control.
    #: For "push" permission, may specify userVisibleOnly.
    #: Global unique identifier of the download.
    #: Id of the frame that caused the download to begin.
    #: Maximum value (exclusive).
    #: Minimum value (inclusive).
    #: Name of permission.
    #: Name.
    #: Note that userVisibleOnly = true is the only currently supported type.
    #: Number of samples.
    #: See https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl for valid permission names.
    #: Suggested file name of the resource (the actual name of the file saved on disk may differ).
    #: Sum of sample values.
    #: The offset from the left edge of the screen to the window in pixels.
    #: The offset from the top edge of the screen to the window in pixels.
    #: The window height in pixels.
    #: The window state. Default to normal.
    #: The window width in pixels.
    #: Total bytes received.
    #: Total expected bytes to download.
    #: Total number of samples.
    #: URL of the resource being downloaded.
    )
    **EXPERIMENTAL**
    :param api:
    :param badge_label: *(Optional)*
    :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). ``allowAndName`` allows download and names files according to their download guids.
    :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
    :param browser_context_id: *(Optional)* BrowserContext to override permissions. When omitted, default browser context is used.
    :param browser_context_id: *(Optional)* BrowserContext to perform the action in. When omitted, default browser context is used.
    :param browser_context_id: *(Optional)* BrowserContext to reset permissions. When omitted, default browser context is used.
    :param browser_context_id: *(Optional)* BrowserContext to set download behavior. When omitted, default browser context is used.
    :param browser_context_id: *(Optional)* Context to override. When omitted, default browser context is used.
    :param command_id:
    :param coordinator_origin:
    :param delta: *(Optional)* If true, retrieve delta since last delta call.
    :param download_path: *(Optional)* The default path to save downloaded files to. This is required if behavior is set to 'allow' or 'allowAndName'.
    :param events_enabled: *(Optional)* Whether to emit download events (defaults to false).
    :param guid: Global unique identifier of the download.
    :param image: *(Optional)* Png encoded image.
    :param key_config:
    :param name: Requested histogram name.
    :param origin: *(Optional)* Origin the permission applies to, all origins if not specified.
    :param permission: Descriptor of permission to override.
    :param permissions:
    :param query: *(Optional)* Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
    :param setting: Setting of the permission.
    :param target_id: *(Optional)* Devtools agent host id. If called as a part of the session, associated targetId is used.
    :param url:
    :param window_id: Browser window id.
    :returns: A tuple with the following items:
    :returns: Bounds information of the window. When window state is 'minimized', the restored window position and size are returned.
    :returns: Commandline parameters
    :returns: Histogram.
    :returns: Histograms.
    @classmethod
    }
    allow_without_gesture: bool | None = None
    allow_without_sanitization: bool | None = None
    Allows a site to use privacy sandbox features that require enrollment
    api: PrivacySandboxAPI,
    AR = "ar"
    AUDIO_CAPTURE = "audioCapture"
    AUTOMATIC_FULLSCREEN = "automaticFullscreen"
    BACKGROUND_FETCH = "backgroundFetch"
    BACKGROUND_SYNC = "backgroundSync"
    badge_label: str | None = None, image: str | None = None
    behavior: str,
    BIDDING_AND_AUCTION_SERVICES = "BiddingAndAuctionServices"
    Browser command ids used by executeBrowserCommand.
    Browser window bounds information
    browser_context_id: BrowserContextID | None = None,
    buckets: list[Bucket]
    CAMERA_PAN_TILT_ZOOM = "cameraPanTiltZoom"
    Cancel a download if in progress
    CAPTURED_SURFACE_CONTROL = "capturedSurfaceControl"
    Chrome histogram bucket.
    Chrome histogram.
    CLIPBOARD_READ_WRITE = "clipboardReadWrite"
    CLIPBOARD_SANITIZED_WRITE = "clipboardSanitizedWrite"
    Close browser gracefully.
    CLOSE_TAB_SEARCH = "closeTabSearch"
    cmd_dict: T_JSON_DICT = {
    command_id: BrowserCommandId,
    configuration for the origin may exist.
    Configures encryption keys used with a given privacy sandbox API to talk
    coordinator_origin: str,
    coordinatorOrigin must be a .test domain. No existing coordinator
    count: int
    Crashes browser on the main thread.
    Crashes GPU process.
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def from_json(cls, json):
    def from_json(cls, json: int) -> WindowID:
    def from_json(cls, json: str) -> BrowserContextID:
    def from_json(cls, json: T_JSON_DICT) -> DownloadProgress:
    def from_json(cls, json: T_JSON_DICT) -> DownloadWillBegin:
    def to_json(self) -> int:
    def to_json(self) -> str:
    def to_json(self):
    Definition of PermissionDescriptor defined in the Permissions API:
    DENIED = "denied"
    DISPLAY_CAPTURE = "displayCapture"
    download_path: str | None = None,
    DURABLE_STORAGE = "durableStorage"
    --enable-automation is on the commandline.
    events_enabled: bool | None = None,
    Fired when download makes progress. Last call has ``done`` == true.
    Fired when page is about to start a download.
    frame_id: page.FrameId
    FULLSCREEN = "fullscreen"
    GEOLOCATION = "geolocation"
    Get a Chrome histogram by name.
    Get Chrome histograms.
    Get position and size of the browser window.
    Get the browser window that contains the devtools target.
    Grant specific permissions to the given origin and reject all others.
    GRANTED = "granted"
    guid: str
    guid: str, browser_context_id: BrowserContextID | None = None
    HAND_TRACKING = "handTracking"
    height: int | None = None
    high: int
    https://w3c.github.io/permissions/#dom-permissiondescriptor.
    IDLE_DETECTION = "idleDetection"
    if badge_label is not None:
    if browser_context_id is not None:
    if delta is not None:
    if download_path is not None:
    if events_enabled is not None:
    if image is not None:
    if origin is not None:
    if query is not None:
    if target_id is not None:
    Invoke custom browser commands used by telemetry.
    json = yield cmd_dict
    key_config: str,
    KEYBOARD_LOCK = "keyboardLock"
    left: int | None = None
    LOCAL_FONTS = "localFonts"
    LOCAL_NETWORK_ACCESS = "localNetworkAccess"
    low: int
    MAXIMIZED = "maximized"
    MIDI = "midi"
    MIDI_SYSEX = "midiSysex"
    MINIMIZED = "minimized"
    name: str
    name: str, delta: bool | None = None
    NFC = "nfc"
    NORMAL = "normal"
    NOTIFICATIONS = "notifications"
    OPEN_TAB_SEARCH = "openTabSearch"
    origin: str | None = None,
    pan_tilt_zoom: bool | None = None
    params: T_JSON_DICT = dict()
    params["api"] = api.to_json()
    params["behavior"] = behavior
    params["bounds"] = bounds.to_json()
    params["commandId"] = command_id.to_json()
    params["coordinatorOrigin"] = coordinator_origin
    params["guid"] = guid
    params["keyConfig"] = key_config
    params["name"] = name
    params["permission"] = permission.to_json()
    params["permissions"] = [i.to_json() for i in permissions]
    params["setting"] = setting.to_json()
    params["url"] = url
    params["windowId"] = window_id.to_json()
    PAYMENT_HANDLER = "paymentHandler"
    PERIODIC_BACKGROUND_SYNC = "periodicBackgroundSync"
    permission: PermissionDescriptor,
    permissions: list[PermissionType],
    POINTER_LOCK = "pointerLock"
    PROMPT = "prompt"
    PROTECTED_MEDIA_IDENTIFIER = "protectedMediaIdentifier"
    query: str | None = None, delta: bool | None = None
    received_bytes: float
    Reset all permission management for all origins.
    return (
    return (WindowID.from_json(json["windowId"]), Bounds.from_json(json["bounds"]))
    return [Histogram.from_json(i) for i in json["histograms"]]
    return [str(i) for i in json["arguments"]]
    return Bounds.from_json(json["bounds"])
    return Histogram.from_json(json["histogram"])
    Returns the command line switches for the browser process if, and only if
    Returns version information.
    SENSORS = "sensors"
    Set dock tile details, platform-specific.
    Set permission settings for given origin.
    Set position and/or size of the browser window.
    Set the behavior when downloading a file.
    setting: PermissionSetting,
    SMART_CARD = "smartCard"
    SPEAKER_SELECTION = "speakerSelection"
    state: str
    STORAGE_ACCESS = "storageAccess"
    suggested_filename: str
    sum_: int
    sysex: bool | None = None
    target_id: target.TargetID | None = None,
    The state of the browser window.
    to a trusted coordinator.  Since this is intended for test automation only,
    top: int | None = None
    TOP_LEVEL_STORAGE_ACCESS = "topLevelStorageAccess"
    total_bytes: float
    TRUSTED_KEY_VALUE = "TrustedKeyValue"
    typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[str, str, str, str, str]]
    url: str
    url: str,
    user_visible_only: bool | None = None
    VIDEO_CAPTURE = "videoCapture"
    VR = "vr"
    WAKE_LOCK_SCREEN = "wakeLockScreen"
    WAKE_LOCK_SYSTEM = "wakeLockSystem"
    WEB_APP_INSTALLATION = "webAppInstallation"
    WEB_PRINTING = "webPrinting"
    width: int | None = None
    window_id: WindowID,
    window_id: WindowID, bounds: Bounds
    WINDOW_MANAGEMENT = "windowManagement"
    window_state: WindowState | None = None
    without the site actually being enrolled. Only supported on page targets.
#
# CDP domain: Browser
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, Bounds]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, Histogram]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[Histogram]]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, tuple[WindowID, Bounds]]:
):
@dataclass
@event_class("Browser.downloadProgress")
@event_class("Browser.downloadWillBegin")
class Bounds:
class BrowserCommandId:
class BrowserContextID:
class Bucket:
class DownloadProgress:
class DownloadWillBegin:
class Histogram:
class PermissionDescriptor:
class PermissionSetting:
class PermissionType:
class PrivacySandboxAPI:
class WindowID:
class WindowState:
def add_privacy_sandbox_coordinator_key_config(
def add_privacy_sandbox_enrollment_override(
def cancel_download(
def close() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def crash() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def crash_gpu_process() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def execute_browser_command(
def get_browser_command_line() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, list[str]]:
def get_histogram(
def get_histograms(
def get_version() -> (
def get_window_bounds(
def get_window_for_target(
def grant_permissions(
def reset_permissions(
def set_dock_tile(
def set_download_behavior(
def set_permission(
def set_window_bounds(
from . import page
from . import target
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing
