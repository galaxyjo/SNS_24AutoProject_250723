
        -------
            "events": events,
            browsing_contexts = []
            Dictionary containing the ready state (bool), message (str) and metadata
            params["browsingContexts"] = browsing_contexts
        """
        }
        cmd = command_builder("session.status", {})
        dict
        if browsing_contexts is None:
        if browsing_contexts:
        params = {
        return command_builder("session.subscribe", params)
        return command_builder("session.unsubscribe", params)
        return self.conn.execute(cmd)
        Returns
        self.conn = conn
        The session.status command returns information about the remote end's readiness
        to create new sessions and may include implementation-specific metadata.
    def __init__(self, conn):
    def status(self):
    def subscribe(self, *events, browsing_contexts=None):
    def unsubscribe(self, *events, browsing_contexts=None):
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
class Session:
from selenium.webdriver.common.bidi.common import command_builder
