
                [UserAgentBrandVersion.from_json(i) for i in json["brands"]]
                [UserAgentBrandVersion.from_json(i) for i in json["fullVersionList"]]
                else None
                float(json["maximumFrequency"]) if "maximumFrequency" in json else None
                float(json["minimumFrequency"]) if "minimumFrequency" in json else None
                if "brands" in json
                if "fullVersionList" in json
                if "quaternion" in json
                if "single" in json
                SensorReadingQuaternion.from_json(json["quaternion"])
                SensorReadingSingle.from_json(json["single"])
            ),
            angle=int(json["angle"]),
            architecture=str(json["architecture"]),
            available=bool(json["available"]) if "available" in json else None,
            bitness=str(json["bitness"]) if "bitness" in json else None,
            bottom_max=int(json["bottomMax"]) if "bottomMax" in json else None,
            bottom=int(json["bottom"]) if "bottom" in json else None,
            brand=str(json["brand"]),
            brands=(
            full_version_list=(
            full_version=str(json["fullVersion"]) if "fullVersion" in json else None,
            json["available"] = self.available
            json["bitness"] = self.bitness
            json["bottom"] = self.bottom
            json["bottomMax"] = self.bottom_max
            json["brands"] = [i.to_json() for i in self.brands]
            json["fullVersion"] = self.full_version
            json["fullVersionList"] = [i.to_json() for i in self.full_version_list]
            json["left"] = self.left
            json["leftMax"] = self.left_max
            json["maximumFrequency"] = self.maximum_frequency
            json["minimumFrequency"] = self.minimum_frequency
            json["quaternion"] = self.quaternion.to_json()
            json["right"] = self.right
            json["rightMax"] = self.right_max
            json["single"] = self.single.to_json()
            json["top"] = self.top
            json["topMax"] = self.top_max
            json["wow64"] = self.wow64
            json["xyz"] = self.xyz.to_json()
            left_max=int(json["leftMax"]) if "leftMax" in json else None,
            left=int(json["left"]) if "left" in json else None,
            mask_length=int(json["maskLength"]),
            max_virtual_time_task_starvation_count
            maximum_frequency=(
            minimum_frequency=(
            mobile=bool(json["mobile"]),
            model=str(json["model"]),
            name=str(json["name"]),
            offset=int(json["offset"]),
            orientation=str(json["orientation"]),
            platform_version=str(json["platformVersion"]),
            platform=str(json["platform"]),
            quaternion=(
            right_max=int(json["rightMax"]) if "rightMax" in json else None,
            right=int(json["right"]) if "right" in json else None,
            single=(
            top_max=int(json["topMax"]) if "topMax" in json else None,
            top=int(json["top"]) if "top" in json else None,
            type_=str(json["type"]),
            value=float(json["value"]),
            value=str(json["value"]),
            version=str(json["version"]),
            w=float(json["w"]),
            wow64=bool(json["wow64"]) if "wow64" in json else None,
            x=float(json["x"]),
            xyz=SensorReadingXYZ.from_json(json["xyz"]) if "xyz" in json else None,
            y=float(json["y"]),
            z=float(json["z"]),
        "method": "Emulation.canEmulate",
        "method": "Emulation.clearDeviceMetricsOverride",
        "method": "Emulation.clearDevicePostureOverride",
        "method": "Emulation.clearDisplayFeaturesOverride",
        "method": "Emulation.clearGeolocationOverride",
        "method": "Emulation.clearIdleOverride",
        "method": "Emulation.getOverriddenSensorInformation",
        "method": "Emulation.resetPageScaleFactor",
        "method": "Emulation.setAutoDarkModeOverride",
        "method": "Emulation.setAutomationOverride",
        "method": "Emulation.setCPUThrottlingRate",
        "method": "Emulation.setDefaultBackgroundColorOverride",
        "method": "Emulation.setDeviceMetricsOverride",
        "method": "Emulation.setDevicePostureOverride",
        "method": "Emulation.setDisabledImageTypes",
        "method": "Emulation.setDisplayFeaturesOverride",
        "method": "Emulation.setDocumentCookieDisabled",
        "method": "Emulation.setEmitTouchEventsForMouse",
        "method": "Emulation.setEmulatedMedia",
        "method": "Emulation.setEmulatedVisionDeficiency",
        "method": "Emulation.setFocusEmulationEnabled",
        "method": "Emulation.setGeolocationOverride",
        "method": "Emulation.setHardwareConcurrencyOverride",
        "method": "Emulation.setIdleOverride",
        "method": "Emulation.setLocaleOverride",
        "method": "Emulation.setNavigatorOverrides",
        "method": "Emulation.setPageScaleFactor",
        "method": "Emulation.setPressureSourceOverrideEnabled",
        "method": "Emulation.setPressureStateOverride",
        "method": "Emulation.setSafeAreaInsetsOverride",
        "method": "Emulation.setScriptExecutionDisabled",
        "method": "Emulation.setScrollbarsHidden",
        "method": "Emulation.setSensorOverrideEnabled",
        "method": "Emulation.setSensorOverrideReadings",
        "method": "Emulation.setTimezoneOverride",
        "method": "Emulation.setTouchEmulationEnabled",
        "method": "Emulation.setUserAgentOverride",
        "method": "Emulation.setVirtualTimePolicy",
        "method": "Emulation.setVisibleSize",
        "params": params,
        )
        if self.available is not None:
        if self.bitness is not None:
        if self.bottom is not None:
        if self.bottom_max is not None:
        if self.brands is not None:
        if self.full_version is not None:
        if self.full_version_list is not None:
        if self.left is not None:
        if self.left_max is not None:
        if self.maximum_frequency is not None:
        if self.minimum_frequency is not None:
        if self.quaternion is not None:
        if self.right is not None:
        if self.right_max is not None:
        if self.single is not None:
        if self.top is not None:
        if self.top_max is not None:
        if self.wow64 is not None:
        if self.xyz is not None:
        json = dict()
        json["angle"] = self.angle
        json["architecture"] = self.architecture
        json["brand"] = self.brand
        json["maskLength"] = self.mask_length
        json["mobile"] = self.mobile
        json["model"] = self.model
        json["name"] = self.name
        json["offset"] = self.offset
        json["orientation"] = self.orientation
        json["platform"] = self.platform
        json["platformVersion"] = self.platform_version
        json["type"] = self.type_
        json["value"] = self.value
        json["version"] = self.version
        json["w"] = self.w
        json["x"] = self.x
        json["y"] = self.y
        json["z"] = self.z
        params["acceptLanguage"] = accept_language
        params["accuracy"] = accuracy
        params["budget"] = budget
        params["color"] = color.to_json()
        params["configuration"] = configuration
        params["devicePosture"] = device_posture.to_json()
        params["displayFeature"] = display_feature.to_json()
        params["dontSetVisibleSize"] = dont_set_visible_size
        params["enabled"] = enabled
        params["features"] = [i.to_json() for i in features]
        params["initialVirtualTime"] = initial_virtual_time.to_json()
        params["latitude"] = latitude
        params["locale"] = locale
        params["longitude"] = longitude
        params["maxTouchPoints"] = max_touch_points
        params["maxVirtualTimeTaskStarvationCount"] = (
        params["media"] = media
        params["metadata"] = metadata.to_json()
        params["platform"] = platform
        params["positionX"] = position_x
        params["positionY"] = position_y
        params["scale"] = scale
        params["screenHeight"] = screen_height
        params["screenOrientation"] = screen_orientation.to_json()
        params["screenWidth"] = screen_width
        params["userAgentMetadata"] = user_agent_metadata.to_json()
        params["viewport"] = viewport.to_json()
        return cls(
        return cls()
        return cls(json)
        return json
        return self.value
    """
    #: A display feature may mask content such that it is not physically
    #: A display feature that only splits content will have a 0 mask_length.
    #: Brands appearing in Sec-CH-UA.
    #: Brands appearing in Sec-CH-UA-Full-Version-List.
    #: Current posture of the device
    #: displayed - this length along with the offset describes this area.
    #: Orientation angle.
    #: Orientation of a display feature in relation to screen
    #: Orientation type.
    #: orientation) or y (for horizontal orientation) direction.
    #: Overrides safe-area-inset-bottom.
    #: Overrides safe-area-inset-left.
    #: Overrides safe-area-inset-right.
    #: Overrides safe-area-inset-top.
    #: Overrides safe-area-max-inset-bottom.
    #: Overrides safe-area-max-inset-left.
    #: Overrides safe-area-max-inset-right.
    #: Overrides safe-area-max-inset-top.
    #: The offset from the screen origin in either the x (for vertical
    (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
    **EXPERIMENTAL**
    :param accept_language: *(Optional)* Browser language to emulate.
    :param accuracy: *(Optional)* Mock accuracy
    :param budget: *(Optional)* If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
    :param color: *(Optional)* RGBA of the default background color. If not specified, any existing override will be cleared.
    :param configuration: *(Optional)* Touch/gesture events configuration. Default: current platform.
    :param device_posture: **(EXPERIMENTAL)** *(Optional)* If set, the posture of a foldable device. If not set the posture is set to continuous. Deprecated, use Emulation.setDevicePostureOverride.
    :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
    :param disabled: Whether document.coookie API should be disabled.
    :param display_feature: **(EXPERIMENTAL)** *(Optional)* If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off. Deprecated, use Emulation.setDisplayFeaturesOverride.
    :param dont_set_visible_size: **(EXPERIMENTAL)** *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
    :param enabled:
    :param enabled: *(Optional)* Whether to enable or disable automatic dark mode. If not specified, any existing override will be cleared.
    :param enabled: Whether the override should be enabled.
    :param enabled: Whether the touch event emulation should be enabled.
    :param enabled: Whether to enable to disable focus emulation.
    :param enabled: Whether touch emulation based on mouse input should be enabled.
    :param features:
    :param features: *(Optional)* Media features to emulate.
    :param hardware_concurrency: Hardware concurrency to report
    :param height: Frame height (DIP).
    :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param hidden: Whether scrollbars should be always hidden.
    :param image_types: Image types to disable.
    :param initial_virtual_time: *(Optional)* If set, base::Time::Now will be overridden to initially return this value.
    :param insets:
    :param is_screen_unlocked: Mock isScreenUnlocked
    :param is_user_active: Mock isUserActive
    :param latitude: *(Optional)* Mock latitude
    :param locale: *(Optional)* ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and restores default host system locale.
    :param longitude: *(Optional)* Mock longitude
    :param max_touch_points: *(Optional)* Maximum touch points supported. Defaults to one.
    :param max_virtual_time_task_starvation_count: *(Optional)* If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock.
    :param media: *(Optional)* Media type to emulate. Empty string disables the override.
    :param metadata: *(Optional)*
    :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
    :param page_scale_factor: Page scale factor.
    :param platform: *(Optional)* The platform navigator.platform should return.
    :param platform: The platform navigator.platform should return.
    :param policy:
    :param position_x: **(EXPERIMENTAL)** *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
    :param position_y: **(EXPERIMENTAL)** *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
    :param posture:
    :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
    :param reading:
    :param scale: **(EXPERIMENTAL)** *(Optional)* Scale to apply to resulting view image.
    :param screen_height: **(EXPERIMENTAL)** *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
    :param screen_orientation: *(Optional)* Screen orientation override.
    :param screen_width: **(EXPERIMENTAL)** *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
    :param source:
    :param state:
    :param timezone_id: The timezone identifier. List of supported timezones: https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt If empty, disables the override and restores default host system timezone.
    :param type_:
    :param type_: Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies.
    :param user_agent: User agent to use.
    :param user_agent_metadata: **(EXPERIMENTAL)** *(Optional)* To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
    :param value: Whether script execution should be disabled in the page.
    :param viewport: **(EXPERIMENTAL)** *(Optional)* If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions.
    :param width: Frame width (DIP).
    :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :returns:
    :returns: Absolute timestamp at which virtual time was first enabled (up time in milliseconds).
    :returns: True if emulation is supported.
    @classmethod
    ``userAgentMetadata`` must be set for Client Hint headers to be sent.
    }
    ABSOLUTE_ORIENTATION = "absolute-orientation"
    ACCELEROMETER = "accelerometer"
    accept_language: str | None = None,
    accuracy: float | None = None,
    ADVANCE = "advance"
    advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
    allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
    Allows overriding the automation flag.
    Allows overriding user agent with the given string.
    AMBIENT_LIGHT = "ambient-light"
    angle: int
    architecture: str
    Automatically render all web contents using a dark theme.
    available: bool | None = None
    AVIF = "avif"
    bitness: str | None = None
    bottom: int | None = None
    bottom_max: int | None = None
    brand: str
    brands: list[UserAgentBrandVersion] | None = None
    budget: float | None = None,
    by setSensorOverrideEnabled.
    Clears a device posture override set with either setDeviceMetricsOverride()
    Clears Idle state overrides.
    Clears the display features override set with either setDeviceMetricsOverride()
    Clears the overridden device metrics.
    Clears the overridden Geolocation Position and Error.
    cmd_dict: T_JSON_DICT = {
    color: dom.RGBA | None = None,
    CPU = "cpu"
    CRITICAL = "critical"
    data from a real hardware sensor. Otherwise, existing virtual
    def __init__(self, *args, **kwargs): pass
    def from_json(cls, json):
    def from_json(cls, json: T_JSON_DICT) -> VirtualTimeBudgetExpired:
    def to_json(self):
    delivered to PressureObserver users. ``source`` must have been previously
    device_posture: DevicePosture | None = None,
    device_scale_factor: float,
    disabled: bool,
    display_feature: DisplayFeature | None = None,
    Does nothing if no override is set.
    dont_set_visible_size: bool | None = None,
    Emulates the given media type or media feature for CSS media queries.
    Emulates the given vision deficiency.
    enabled: bool | None = None,
    enabled: bool,
    enabled: bool, configuration: str | None = None
    enabled: bool, max_touch_points: int | None = None
    enabled: bool, type_: SensorType, metadata: SensorMetadata | None = None
    Enables CPU throttling to emulate slow CPUs.
    Enables or disables simulating a focused and active page.
    Enables touch on platforms which do not support them.
    Enum of image types that can be disabled.
    FAIR = "fair"
    features: list[DisplayFeature],
    features: list[MediaFeature] | None = None,
    full_version: str | None = None
    full_version_list: list[UserAgentBrandVersion] | None = None
    GRAVITY = "gravity"
    GYROSCOPE = "gyroscope"
    hardware_concurrency: int,
    height: int,
    hidden: bool,
    if accept_language is not None:
    if accuracy is not None:
    if budget is not None:
    if color is not None:
    if configuration is not None:
    if device_posture is not None:
    if display_feature is not None:
    if dont_set_visible_size is not None:
    if enabled is not None:
    if features is not None:
    if initial_virtual_time is not None:
    if latitude is not None:
    if locale is not None:
    if longitude is not None:
    if max_touch_points is not None:
    if max_virtual_time_task_starvation_count is not None:
    if media is not None:
    if metadata is not None:
    if platform is not None:
    if position_x is not None:
    if position_y is not None:
    if scale is not None:
    if screen_height is not None:
    if screen_orientation is not None:
    if screen_width is not None:
    if the content does not specify one.
    if user_agent_metadata is not None:
    if viewport is not None:
    image_types: list[DisabledImageType],
    initial_virtual_time: network.TimeSinceEpoch | None = None,
    insets: SafeAreaInsets,
    is_user_active: bool, is_screen_unlocked: bool
    json = yield cmd_dict
    latitude: float | None = None,
    left: int | None = None
    left_max: int | None = None
    LINEAR_ACCELERATION = "linear-acceleration"
    locale: str | None = None,
    longitude: float | None = None,
    MAGNETOMETER = "magnetometer"
    mask_length: int
    max_virtual_time_task_starvation_count: int | None = None,
    maximum_frequency: float | None = None
    media: str | None = None,
    metadata: PressureMetadata | None = None,
    minimum_frequency: float | None = None
    Missing optional values will be filled in by the target with what it would normally use.
    mobile: bool
    mobile: bool,
    model: str
    name: str
    NOMINAL = "nominal"
    Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.
    offset: int
    on Android.
    or setDevicePostureOverride() and starts using posture information from the
    or setDisplayFeaturesOverride() and starts using display features from the
    orientation: str
    overridden by setPressureSourceOverrideEnabled.
    Overrides a platform sensor of a given type. If ``enabled`` is true, calls to
    Overrides a pressure source of a given type, as used by the Compute
    Overrides default host system locale with the specified one.
    Overrides default host system timezone with the specified one.
    Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
    Overrides the Idle state.
    Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
    Overrides value returned by the javascript navigator object.
    page_scale_factor: float,
    params: T_JSON_DICT = dict()
    params["deviceScaleFactor"] = device_scale_factor
    params["disabled"] = disabled
    params["enabled"] = enabled
    params["features"] = [i.to_json() for i in features]
    params["hardwareConcurrency"] = hardware_concurrency
    params["height"] = height
    params["hidden"] = hidden
    params["imageTypes"] = [i.to_json() for i in image_types]
    params["insets"] = insets.to_json()
    params["isScreenUnlocked"] = is_screen_unlocked
    params["isUserActive"] = is_user_active
    params["mobile"] = mobile
    params["pageScaleFactor"] = page_scale_factor
    params["platform"] = platform
    params["policy"] = policy.to_json()
    params["posture"] = posture.to_json()
    params["rate"] = rate
    params["reading"] = reading.to_json()
    params["source"] = source.to_json()
    params["state"] = state.to_json()
    params["timezoneId"] = timezone_id
    params["type"] = type_
    params["type"] = type_.to_json()
    params["userAgent"] = user_agent
    params["value"] = value
    params["width"] = width
    PAUSE = "pause"
    PAUSE_IF_NETWORK_FETCHES_PENDING = "pauseIfNetworkFetchesPending"
    pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
    platform again.
    platform: str
    platform: str | None = None,
    platform: str,
    platform_version: str
    platform-provided telemetry data.
    policy: VirtualTimePolicy,
    position_x: int | None = None,
    position_y: int | None = None,
    posture: DevicePosture,
    Pressure API, so that updates to PressureObserver.observe() are provided
    Provides a given pressure state that will be processed and eventually be
    quaternion: SensorReadingQuaternion | None = None
    query results).
    rate: float,
    RELATIVE_ORIENTATION = "relative-orientation"
    Requests that page scale factor is reset to initial values.
    Resizes the frame/viewport of the page. Note that this does not affect the frame's container
    resource fetches.
    respective variables to be undefined, even if previously overridden.
    return bool(json["result"])
    return float(json["requestedSamplingFrequency"])
    return float(json["virtualTimeTicksBase"])
    right: int | None = None
    right_max: int | None = None
    scale: float | None = None,
    Screen orientation.
    screen_height: int | None = None,
    screen_orientation: ScreenOrientation | None = None,
    screen_width: int | None = None,
    See https://w3c.github.io/sensors/#automation for more information.
    Sensor.start() will attempt to use a real sensor instead.
    Sensor.start() will use a virtual sensor as backend rather than fetching
    sensor-backend Sensor objects will fire an error event and new calls to
    SERIOUS = "serious"
    Sets a specified page scale factor.
    Sets or clears an override of the default background color of the frame. This override is used
    single: SensorReadingSingle | None = None
    source: PressureSource,
    source: PressureSource, state: PressureState
    Start reporting the given posture value to the Device Posture API.
    Start using the given display features to pupulate the Viewport Segments API.
    Switches script execution in the page.
    Tells whether emulation is supported.
    the current virtual time policy.  Note this supersedes any previous time budget.
    This override can also be set in setDeviceMetricsOverride().
    timezone_id: str,
    top: int | None = None
    top_max: int | None = None
    Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
    type_: SensorType,
    type_: SensorType, reading: SensorReading
    type_: str
    type_: str,
    typing.Generator[T_JSON_DICT, T_JSON_DICT, None]
    unavailable.
    Updates the sensor readings reported by a sensor type previously overridden
    Used to specify sensor types to emulate.
    Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints
    user_agent: str,
    user_agent_metadata: UserAgentMetadata | None = None,
    value: bool,
    value: float
    value: str
    version: str
    via setPressureStateOverride instead of being retrieved from
    viewport: page.Viewport | None = None,
    w: float
    WEBP = "webp"
    width: int,
    width: int, height: int
    window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
    wow64: bool | None = None
    x: float
    xyz: SensorReadingXYZ | None = None
    y: float
    z: float
#
# CDP domain: Emulation
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, float]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
):
@dataclass
@event_class("Emulation.virtualTimeBudgetExpired")
class DevicePosture:
class DisabledImageType:
class DisplayFeature:
class MediaFeature:
class PressureMetadata:
class PressureSource:
class PressureState:
class SafeAreaInsets:
class ScreenOrientation:
class SensorMetadata:
class SensorReading:
class SensorReadingQuaternion:
class SensorReadingSingle:
class SensorReadingXYZ:
class SensorType:
class UserAgentBrandVersion:
class UserAgentMetadata:
class VirtualTimeBudgetExpired:
class VirtualTimePolicy:
def can_emulate() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, bool]:
def clear_device_metrics_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_device_posture_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_display_features_override() -> (
def clear_geolocation_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def clear_idle_override() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def get_overridden_sensor_information(
def reset_page_scale_factor() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def set_auto_dark_mode_override(
def set_automation_override(
def set_cpu_throttling_rate(
def set_default_background_color_override(
def set_device_metrics_override(
def set_device_posture_override(
def set_disabled_image_types(
def set_display_features_override(
def set_document_cookie_disabled(
def set_emit_touch_events_for_mouse(
def set_emulated_media(
def set_emulated_vision_deficiency(
def set_focus_emulation_enabled(
def set_geolocation_override(
def set_hardware_concurrency_override(
def set_idle_override(
def set_locale_override(
def set_navigator_overrides(
def set_page_scale_factor(
def set_pressure_source_override_enabled(
def set_pressure_state_override(
def set_safe_area_insets_override(
def set_script_execution_disabled(
def set_scrollbars_hidden(
def set_sensor_override_enabled(
def set_sensor_override_readings(
def set_timezone_override(
def set_touch_emulation_enabled(
def set_user_agent_override(
def set_virtual_time_policy(
def set_visible_size(
from . import dom
from . import network
from . import page
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing
