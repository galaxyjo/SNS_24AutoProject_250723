
        ------
        -------
        -----------
            active=data.get("active"),
            bool: True if the client window is active, False otherwise.
            client_window=data.get("clientWindow"),
            ClientWindowInfo.from_dict(window) for window in result["clientWindows"]
            ClientWindowInfo: A new instance of ClientWindowInfo.
            data: A dictionary containing the client window information.
            Exception: If the user context ID is "default" or does not exist.
            height=data.get("height"),
            int: The height of the client window.
            int: The width of the client window.
            int: The x coordinate of the client window.
            int: The y coordinate of the client window.
            List[ClientWindowInfo]: A list of client window information.
            List[str]: A list of user context IDs.
            raise Exception("Cannot remove the default user context")
            state=data.get("state"),
            str: The client window identifier.
            str: The ID of the created user context.
            str: The state of the client window (one of the ClientWindowState constants).
            user_context_id: The ID of the user context to remove.
            width=data.get("width"),
            x=data.get("x"),
            y=data.get("y"),
        """
        """Checks if the client window is active.
        """Creates a ClientWindowInfo instance from a dictionary.
        """Creates a new user context.
        """Gets all client windows.
        """Gets all user contexts.
        """Gets the client window identifier.
        """Gets the height of the client window.
        """Gets the state of the client window.
        """Gets the width of the client window.
        """Gets the x coordinate of the client window.
        """Gets the y coordinate of the client window.
        """Removes a user context.
        )
        ]
        active: bool,
        client_window: str,
        height: int,
        if user_context_id == "default":
        Parameters:
        params = {"userContext": user_context_id}
        Raises:
        result = self.conn.execute(command_builder("browser.createUserContext", {}))
        result = self.conn.execute(command_builder("browser.getClientWindows", {}))
        result = self.conn.execute(command_builder("browser.getUserContexts", {}))
        return [
        return [context_info["userContext"] for context_info in result["userContexts"]]
        return cls(
        return result["userContext"]
        return self.active
        return self.client_window
        return self.height
        return self.state
        return self.width
        return self.x
        return self.y
        Returns:
        self,
        self.active = active
        self.client_window = client_window
        self.conn = conn
        self.conn.execute(command_builder("browser.removeUserContext", params))
        self.height = height
        self.state = state
        self.width = width
        self.x = x
        self.y = y
        state: str,
        width: int,
        x: int,
        y: int,
    """
    """Represents a client window information."""
    """Represents a window state."""
    ):
    @classmethod
    BiDi implementation of the browser module.
    def __init__(
    def __init__(self, conn):
    def create_user_context(self) -> str:
    def from_dict(cls, data: Dict) -> "ClientWindowInfo":
    def get_client_window(self) -> str:
    def get_client_windows(self) -> List[ClientWindowInfo]:
    def get_height(self) -> int:
    def get_state(self) -> str:
    def get_user_contexts(self) -> List[str]:
    def get_width(self) -> int:
    def get_x(self) -> int:
    def get_y(self) -> int:
    def is_active(self) -> bool:
    def remove_user_context(self, user_context_id: str) -> None:
    FULLSCREEN = "fullscreen"
    MAXIMIZED = "maximized"
    MINIMIZED = "minimized"
    NORMAL = "normal"
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
class Browser:
class ClientWindowInfo:
class ClientWindowState:
from selenium.webdriver.common.bidi.common import command_builder
from typing import Dict
from typing import List
