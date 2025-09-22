
-----
        ------
        -------
        ----------
                        "network.removeIntercept", {"intercept": intercept_id}
                    "goog:resourceType", None
                    )
                    command_builder(
                    command_builder("network.removeIntercept", {"intercept": intercept})
                "password": password,
                "type": "password",
                "username": username,
                )
                ),
                body_size=event_data.params["request"].get("bodySize", None),
                cookies=event_data.params["request"].get("cookies", None),
                Default is empty list.
                Default is None.
                del self.callbacks[callback_id]
                headers_size=event_data.params["request"].get("headersSize", None),
                network=self,
                raise Exception(f"Exception: {e}")
                request_id=event_data.params["request"].get("request", None),
                resource_type=event_data.params["request"].get(
                self._remove_intercept(self.callbacks[callback_id])
                self.conn.execute(
                self.conn.remove_callback(net_event, callback_id)
                self.intercepts.copy()
                self.intercepts.remove(intercept)
                self.intercepts.remove(intercept_id)
                Takes Request object as argument.
                timings=event_data.params["request"].get("timings", None),
                url=event_data.params["request"].get("url", None),
            )
            )  # create a copy before iterating
            }
            callback (function): The callback function to execute on event.
            callback (function): The callback function to execute on request interception
            callback(request)
            callback_id (int): The callback id to remove.
            contexts (list, optional): A list of contexts to intercept.
            del self.subscriptions[event_name]
            event (str): The event to subscribe to.
            event_name (str): The event to subscribe to.
            event_name (str): The event to unsubscribe from.
            event_name = self.EVENTS[event]
            except Exception as e:
            Exception: If intercept is not found.
            for callback_id in self.subscriptions[event_name]:
            for intercept_id in intercepts_to_remove:  # remove all intercepts
            If intercept is None, all intercepts will be removed.
            If username or password is None, it attempts auth with no credentials
            int : callback id
            intercept (str, optional): The intercept to remove.
            intercepts_to_remove = (
            net_event = NetworkEvent(event_name)
            params = {}
            params["action"] = "default"
            params["action"] = "provideCredentials"
            params["body"] = body
            params["contexts"] = contexts
            params["cookies"] = cookies
            params["credentials"] = {
            params["events"] = [event_name]
            params["headers"] = headers
            params["method"] = method
            params["phases"] = ["beforeRequestSent"]
            params["phases"] = phases
            params["url"] = url
            params["urlPatterns"] = url_patterns
            password (str): The password to authenticate with.
            phase_name = self.PHASES[event]
            phases (list, optional): A list of phases to intercept.
            phases=[phase_name], url_patterns=url_patterns, contexts=contexts
            raise Exception(f"Event {event} not found")
            raise ValueError("Request not found.")
            request (Request): The request to continue with.
            request = Request(
            request._continue_with_auth(username, password)
            self.callbacks[event_name] = [callback_id]
            self.callbacks[event_name].append(callback_id)
            self.conn.execute(command_builder("session.subscribe", params))
            self.conn.execute(command_builder("session.unsubscribe", params))
            self.subscriptions[event_name] = [callback_id]
            self.subscriptions[event_name].append(callback_id)
            str : intercept id
            try:
            url_patterns (list, optional): A list of URL patterns to intercept.
            username (str): The username to authenticate with.
        """
        """Add a request handler to the network.
        """Add an authentication handler to the network.
        """Add an intercept to the network.
        """Clear all request handlers from the network."""
        """Continue after intercepting this request."""
        """Continue with authentication.
        """Fail this request."""
        """Remove a request handler from the network.
        """Remove a specific intercept, or all intercepts.
        """Remove an authentication handler from the network.
        """Set a callback function to subscribe to a network event.
        "auth_required": "authRequired",
        "auth_required": "network.authRequired",
        "before_request": "beforeRequestSent",
        "before_request": "network.beforeRequestSent",
        "continue_auth": "network.continueWithAuth",
        "continue_request": "network.continueRequest",
        "fetch_error": "network.fetchError",
        "response_completed": "network.responseCompleted",
        "response_started": "network.responseStarted",
        "response_started": "responseStarted",
        )
        body_size=None,
        callback_id = self._on_request(event_name, callback)
        callback_id = self.conn.add_callback(event, _callback)
        cmd = command_builder("network.addIntercept", params)
        cookies=None,
        def _callback(event_data):
        def _callback(request):
        del self.callbacks[callback_id]
        else:
        event = "auth_required"
        event = NetworkEvent(event_name)
        except KeyError:
        for event_name in self.subscriptions:
        headers_size=None,
        headers=None,
        if body is not None:
        if contexts is not None:
        if cookies is not None:
        if event_name in self.callbacks:
        if event_name in self.subscriptions:
        if headers is not None:
        if intercept is None:
        if len(phases) > 0:
        if len(self.subscriptions[event_name]) == 0:
        if method is not None:
        if not self.request_id:
        if not username or not password:  # no credentials is valid option
        if url is not None:
        if url_patterns is not None:
        method=None,
        net_event = NetworkEvent(event_name)
        network: Network,
        Notes:
        Parameters:
        params = {"request": self.request_id}
        params = {}
        params["request"] = self.request_id
        Raises:
        request_id,
        resource_type=None,
        result = self._add_intercept(
        result = self.conn.execute(cmd)
        return callback_id
        return cls(event_class=json.get("event_class"), **json)
        return result
        return self.add_request_handler(event, _callback)
        Returns:
        self,
        self, body=None, method=None, headers=None, cookies=None, url=None
        self._remove_intercept(self.callbacks[callback_id])
        self.body_size = body_size
        self.callbacks = {}
        self.callbacks[callback_id] = result["intercept"]
        self.conn = conn
        self.conn.remove_callback(net_event, callback_id)
        self.cookies = cookies
        self.event_class = event_class
        self.headers = headers
        self.headers_size = headers_size
        self.intercepts = []
        self.intercepts.append(result["intercept"])
        self.method = method
        self.network = network
        self.network.conn.execute(command_builder("network.continueRequest", params))
        self.network.conn.execute(command_builder("network.continueWithAuth", params))
        self.network.conn.execute(command_builder("network.failRequest", params))
        self.params = kwargs
        self.remove_request_handler(event, callback_id)
        self.request_id = request_id
        self.resource_type = resource_type
        self.subscriptions = {}
        self.subscriptions[event_name].remove(callback_id)
        self.timings = timings
        self.url = url
        timings=None,
        try:
        url=None,
    """Represents a network event."""
    """Represents an intercepted network request."""
    ):
    @classmethod
    }
    def __init__(
    def __init__(self, conn):
    def __init__(self, event_class, **kwargs):
    def _add_intercept(self, phases=[], contexts=None, url_patterns=None):
    def _continue_with_auth(self, username=None, password=None):
    def _on_request(self, event_name, callback):
    def _remove_intercept(self, intercept=None):
    def add_auth_handler(self, username, password):
    def add_request_handler(self, event, callback, url_patterns=None, contexts=None):
    def clear_request_handlers(self):
    def continue_request(
    def fail_request(self):
    def from_json(cls, json):
    def remove_auth_handler(self, callback_id):
    def remove_request_handler(self, event, callback_id):
    EVENTS = {
    PHASES = {
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
class Network:
class NetworkEvent:
class Request:
from selenium.webdriver.common.bidi.common import command_builder

pass
