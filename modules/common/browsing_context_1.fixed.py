
------
        -------
        ----------
        -----------
                # For navigation events
                BrowsingContextInfo.from_json(child) for child in json.get("children")
                callback(info)
                callback(params)
                event_name == self.EVENTS["context_created"]
                info = BrowsingContextInfo.from_json(event_data.params)
                info = NavigationInfo.from_json(event_data.params)
                or event_name == self.EVENTS["context_destroyed"]
                params = DownloadWillBeginParams.from_json(event_data.params)
                params = HistoryUpdatedParams.from_json(event_data.params)
                params = UserPromptClosedParams.from_json(event_data.params)
                params = UserPromptOpenedParams.from_json(event_data.params)
                params["browsingContexts"] = contexts
                self.conn.remove_callback(event, callback_id)
            "background": background,
            "context": context,
            "orientation": orientation,
            "scale": scale,
            "shrinkToFit": shrink_to_fit,
            ):
            ]
            accept: Whether to accept the prompt.
            accepted=json.get("accepted"),
            background: Whether to create the new navigable in the background.
            background: Whether to include the background.
            BrowsingContextEvent: A new instance of BrowsingContextEvent.
            BrowsingContextInfo.from_json(context) for context in result["contexts"]
            BrowsingContextInfo: A new instance of BrowsingContextInfo.
            callback: The callback function to execute on event.
            callback_id: The callback id to remove.
            children = [
            children=children,
            client_window=json.get("clientWindow"),
            clip: The clip rectangle of the screenshot.
            command_builder("browsingContext.captureScreenshot", params)
            command_builder("browsingContext.locateNodes", params)
            command_builder("browsingContext.traverseHistory", params)
            context: The browsing context ID to activate.
            context: The browsing context ID to capture.
            context: The browsing context ID to close.
            context: The browsing context ID.
            context=json.get("context"),
            contexts: The browsing context IDs to subscribe to.
            default_value=json.get("defaultValue"),
            del self.subscriptions[event_name]
            delta: The delta to traverse by.
            device_pixel_ratio: The device pixel ratio.
            Dict: A dictionary containing the navigation result.
            Dict: A dictionary containing the traverse history result.
            DownloadWillBeginParams: A new instance of DownloadWillBeginParams.
            elif event_name == self.EVENTS["download_will_begin"]:
            elif event_name == self.EVENTS["history_updated"]:
            elif event_name == self.EVENTS["user_prompt_closed"]:
            elif event_name == self.EVENTS["user_prompt_opened"]:
            else:
            event = BrowsingContextEvent(event_name)
            event: The event to subscribe to.
            event: The event to unsubscribe from.
            event_name = self.EVENTS[event]
            event_name: The event to subscribe to.
            Exception: If the browsing context is not a top-level traversable.
            for callback_id in self.subscriptions[event_name]:
            format: The format of the screenshot.
            handler=json.get("handler"),
            HistoryUpdatedParams: A new instance of HistoryUpdatedParams.
            if (
            if contexts is not None:
            ignore_cache: Whether to ignore the cache.
            int: callback id
            json: A dictionary containing the browsing context information.
            json: A dictionary containing the download parameters.
            json: A dictionary containing the event information.
            json: A dictionary containing the history updated parameters.
            json: A dictionary containing the navigation information.
            json: A dictionary containing the user prompt closed parameters.
            json: A dictionary containing the user prompt parameters.
            List[BrowsingContextInfo]: A list of browsing context information.
            List[Dict]: A list of nodes.
            locator: The locator to use.
            margin: The margin parameters.
            max_depth: The maximum depth of the tree.
            max_node_count: The maximum number of nodes to return.
            message=json.get("message"),
            navigation=json.get("navigation"),
            NavigationInfo: A new instance of NavigationInfo.
            orientation: The orientation, either "portrait" or "landscape".
            origin: The origin of the screenshot, either "viewport" or "document".
            original_opener=json.get("originalOpener"),
            page: The page parameters.
            page_ranges: The page ranges.
            params = {"events": [event_name]}
            params["accept"] = accept
            params["background"] = background
            params["clip"] = clip
            params["context"] = context
            params["devicePixelRatio"] = device_pixel_ratio
            params["format"] = format
            params["ignoreCache"] = ignore_cache
            params["margin"] = margin
            params["maxDepth"] = max_depth
            params["maxNodeCount"] = max_node_count
            params["page"] = page
            params["pageRanges"] = page_ranges
            params["referenceContext"] = reference_context
            params["root"] = root
            params["serializationOptions"] = serialization_options
            params["startNodes"] = start_nodes
            params["userContext"] = user_context
            params["userContexts"] = user_contexts
            params["userText"] = user_text
            params["viewport"] = viewport
            params["wait"] = wait
            parent=json.get("parent"),
            prompt_unload: Whether to prompt to unload.
            raise Exception(f"Event {event} not found")
            reference_context: The reference browsing context ID.
            root: The root browsing context ID.
            scale: The scale.
            self.callbacks[event_name] = [callback_id]
            self.callbacks[event_name].append(callback_id)
            self.conn.execute(session.subscribe(**params))
            self.conn.execute(session.unsubscribe(**params))
            self.subscriptions[event_name] = [callback_id]
            self.subscriptions[event_name].append(callback_id)
            serialization_options: The serialization options.
            session = Session(self.conn)
            shrink_to_fit: Whether to shrink to fit.
            start_nodes: The start nodes.
            str: The Base64-encoded PDF document.
            str: The Base64-encoded screenshot.
            str: The browsing context ID of the created navigable.
            suggested_filename=json.get("suggestedFilename"),
            timestamp=json.get("timestamp"),
            type: The type of the new navigable, either "tab" or "window".
            type=json.get("type"),
            url: The URL to navigate to.
            url=json.get("url"),
            user_context: The user context ID.
            user_context=json.get("userContext"),
            user_contexts: The user context IDs.
            user_text: The text to enter in the prompt.
            user_text=json.get("userText"),
            UserPromptClosedParams: A new instance of UserPromptClosedParams.
            UserPromptOpenedParams: A new instance of UserPromptOpenedParams.
            viewport: The viewport parameters.
            wait: The readiness state to wait for.
        """
        """Activates and focuses the given top-level traversable.
        """Add an event handler to the browsing context.
        """Allows closing an open prompt.
        """Captures an image of the given navigable, and returns it as a Base64-encoded string.
        """Clear all event handlers from the browsing context."""
        """Closes a top-level traversable.
        """Creates a BrowsingContextEvent instance from a dictionary.
        """Creates a BrowsingContextInfo instance from a dictionary.
        """Creates a DownloadWillBeginParams instance from a dictionary.
        """Creates a HistoryUpdatedParams instance from a dictionary.
        """Creates a NavigationInfo instance from a dictionary.
        """Creates a new navigable, either in a new tab or in a new window, and returns its navigable id.
        """Creates a paginated representation of a document, and returns it as a PDF document represented as a Base64-encoded string.
        """Creates a UserPromptClosedParams instance from a dictionary.
        """Creates a UserPromptOpenedParams instance from a dictionary.
        """Modifies specific viewport characteristics on the given top-level traversable.
        """Navigates a navigable to the given URL.
        """Reloads a navigable.
        """Remove an event handler from the browsing context.
        """Returns a list of all nodes matching the specified locator.
        """Returns a tree of all descendent navigables including the given parent itself, or all top-level contexts when no parent is provided.
        """Set a callback function to subscribe to a browsing context event.
        """Traverses the history of a given navigable by a delta.
        "context_created": "browsingContext.contextCreated",
        "context_destroyed": "browsingContext.contextDestroyed",
        "dom_content_loaded": "browsingContext.domContentLoaded",
        "download_will_begin": "browsingContext.downloadWillBegin",
        "fragment_navigated": "browsingContext.fragmentNavigated",
        "history_updated": "browsingContext.historyUpdated",
        "load": "browsingContext.load",
        "navigation_aborted": "browsingContext.navigationAborted",
        "navigation_committed": "browsingContext.navigationCommitted",
        "navigation_failed": "browsingContext.navigationFailed",
        "navigation_started": "browsingContext.navigationStarted",
        "user_prompt_closed": "browsingContext.userPromptClosed",
        "user_prompt_opened": "browsingContext.userPromptOpened",
        )
        ]
        }
        accept: Optional[bool] = None,
        accepted: bool,
        background: bool = False,
        callback_id = self._on_event(event_name, callback)
        callback_id = self.conn.add_callback(event, _callback)
        children = None
        children: Optional[List["BrowsingContextInfo"]],
        client_window: Optional[str] = None,
        clip: Optional[Dict] = None,
        context: Optional[str] = None,
        context: str,
        def _callback(event_data):
        default_value: Optional[str] = None,
        device_pixel_ratio: Optional[float] = None,
        else:
        event = BrowsingContextEvent(event_name)
        except KeyError:
        for event_name in self.subscriptions:
        format: Optional[Dict] = None,
        handler: str,
        if accept is not None:
        if background is not None:
        if clip is not None:
        if context is not None:
        if device_pixel_ratio is not None:
        if event_name in self.callbacks:
        if event_name in self.subscriptions:
        if format is not None:
        if ignore_cache is not None:
        if json.get("children") is not None:
        if len(self.subscriptions[event_name]) == 0:
        if margin is not None:
        if max_depth is not None:
        if max_node_count is not None:
        if page is not None:
        if page_ranges is not None:
        if reference_context is not None:
        if root is not None:
        if serialization_options is not None:
        if start_nodes is not None:
        if user_context is not None:
        if user_contexts is not None:
        if user_text is not None:
        if viewport is not None:
        if wait is not None:
        ignore_cache: Optional[bool] = None,
        locator: Dict,
        margin: Optional[Dict] = None,
        max_depth: Optional[int] = None,
        max_node_count: Optional[int] = None,
        message: str,
        navigation: Optional[str],
        orientation: str = "portrait",
        origin: str = "viewport",
        original_opener: Optional[str] = None,
        page: Optional[Dict] = None,
        page_ranges: Optional[List[Union[int, str]]] = None,
        Parameters:
        params = {
        params = {"context": context, "delta": delta}
        params = {"context": context, "locator": locator}
        params = {"context": context, "origin": origin}
        params = {"context": context, "promptUnload": prompt_unload}
        params = {"context": context, "url": url}
        params = {"context": context}
        params = {"type": type}
        params = {}
        parent: Optional[str] = None,
        Raises:
        reference_context: Optional[str] = None,
        result = self.conn.execute(
        result = self.conn.execute(command_builder("browsingContext.create", params))
        result = self.conn.execute(command_builder("browsingContext.getTree", params))
        result = self.conn.execute(command_builder("browsingContext.navigate", params))
        result = self.conn.execute(command_builder("browsingContext.print", params))
        result = self.conn.execute(command_builder("browsingContext.reload", params))
        return [
        return callback_id
        return cls(
        return cls(event_class=json.get("event_class"), **json)
        return result
        return result["context"]
        return result["data"]
        return result["nodes"]
        Returns:
        root: Optional[str] = None,
        scale: float = 1.0,
        self,
        self, event: str, callback: callable, contexts: Optional[List[str]] = None
        self.accepted = accepted
        self.callbacks = {}
        self.children = children
        self.client_window = client_window
        self.conn = conn
        self.conn.execute(command_builder("browsingContext.activate", params))
        self.conn.execute(command_builder("browsingContext.close", params))
        self.conn.execute(command_builder("browsingContext.handleUserPrompt", params))
        self.conn.execute(command_builder("browsingContext.setViewport", params))
        self.conn.remove_callback(event, callback_id)
        self.context = context
        self.default_value = default_value
        self.event_class = event_class
        self.handler = handler
        self.message = message
        self.navigation = navigation
        self.original_opener = original_opener
        self.params = kwargs
        self.parent = parent
        self.subscriptions = {}
        self.subscriptions[event_name].remove(callback_id)
        self.suggested_filename = suggested_filename
        self.timestamp = timestamp
        self.type = type
        self.url = url
        self.user_context = user_context
        self.user_text = user_text
        serialization_options: Optional[Dict] = None,
        shrink_to_fit: bool = True,
        start_nodes: Optional[List[Dict]] = None,
        suggested_filename: str,
        super().__init__(context, navigation, timestamp, url)
        timestamp: int,
        try:
        type: str,
        url: str,
        user_context: Optional[str] = None,
        user_contexts: Optional[List[str]] = None,
        user_text: Optional[str] = None,
        viewport: Optional[Dict] = None,
        wait: Optional[str] = None,
    """Base class for browsing context events."""
    """BiDi implementation of the browsingContext module."""
    """Parameters for the downloadWillBegin event."""
    """Parameters for the historyUpdated event."""
    """Parameters for the userPromptClosed event."""
    """Parameters for the userPromptOpened event."""
    """Provides details of an ongoing navigation."""
    """Represents the possible user prompt types."""
    """Represents the properties of a navigable."""
    """Represents the stage of document loading at which a navigation command will return."""
    ) -> Dict:
    ) -> int:
    ) -> List[BrowsingContextInfo]:
    ) -> List[Dict]:
    ) -> None:
    ) -> str:
    ):
    @classmethod
    }
    ALERT = "alert"
    BEFORE_UNLOAD = "beforeunload"
    COMPLETE = "complete"
    CONFIRM = "confirm"
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, conn):
    def __init__(self, event_class: str, **kwargs):
    def _on_event(self, event_name: str, callback: callable) -> int:
    def activate(self, context: str) -> None:
    def add_event_handler(
    def capture_screenshot(
    def clear_event_handlers(self) -> None:
    def close(self, context: str, prompt_unload: bool = False) -> None:
    def create(
    def from_json(cls, json: Dict) -> "BrowsingContextEvent":
    def from_json(cls, json: Dict) -> "BrowsingContextInfo":
    def from_json(cls, json: Dict) -> "DownloadWillBeginParams":
    def from_json(cls, json: Dict) -> "HistoryUpdatedParams":
    def from_json(cls, json: Dict) -> "NavigationInfo":
    def from_json(cls, json: Dict) -> "UserPromptClosedParams":
    def from_json(cls, json: Dict) -> "UserPromptOpenedParams":
    def get_tree(
    def handle_user_prompt(
    def locate_nodes(
    def navigate(
    def print(
    def reload(
    def remove_event_handler(self, event: str, callback_id: int) -> None:
    def set_viewport(
    def traverse_history(self, context: str, delta: int) -> Dict:
    EVENTS = {
    INTERACTIVE = "interactive"
    NONE = "none"
    PROMPT = "prompt"
#
#   http://www.apache.org/licenses/LICENSE-2.0
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# "License"); you may not use this file except in compliance
# distributed with this work for additional information
# KIND, either express or implied.  See the License for the
# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# regarding copyright ownership.  The SFC licenses this file
# software distributed under the License is distributed on an
# specific language governing permissions and limitations
# to you under the Apache License, Version 2.0 (the
# under the License.
# Unless required by applicable law or agreed to in writing,
# with the License.  You may obtain a copy of the License at
class BrowsingContext:
class BrowsingContextEvent:
class BrowsingContextInfo:
class DownloadWillBeginParams:
class HistoryUpdatedParams:
class NavigationInfo:
class ReadinessState:
class UserPromptClosedParams:
class UserPromptOpenedParams:
class UserPromptType:
from .session import Session
from selenium.webdriver.common.bidi.common import command_builder
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

pass
