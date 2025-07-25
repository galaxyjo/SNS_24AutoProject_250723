
    --------
    -----------
        method: The method to execute.
        params = {}
        params: The parameters to pass to the method. Default is None.
        The response from the command execution.
    """
    """Build a command iterator to send to the BiDi protocol.
    cmd = yield command
    command = {"method": method, "params": params}
    if params is None:
    Parameters:
    return cmd
    Returns:
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
def command_builder(method: str, params: Dict = None) -> Dict:
from typing import Dict
