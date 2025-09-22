
args = json["args"],
            level = json["level"],
            method = json["method"],
            return ConsoleLogEntry.from_json(json)
            return JavaScriptLogEntry.from_json(json)
            stacktrace = json["stackTrace"],
            text = json["text"],
            timestamp = json["timestamp"],
            type_ = json["type"],
        )
        elif json["type"] == "javascript":
        if json["type"] == "console":
        return cls(
    @classmethod
    args: List[dict]
    def from_json(cls, json):
    event_class = "log.entryAdded"
    level: str
    method: str
    stacktrace: dict
    text: str
    timestamp: str
    type_: str
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
@dataclass
class ConsoleLogEntry:
class JavaScriptLogEntry:
class LogEntryAdded:
from dataclasses import dataclass
from typing import List

pass
