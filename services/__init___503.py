
        "A helper command used for command completion.",
        "Build wheels from your requirements.",
        "CacheCommand",
        "CheckCommand",
        "CompletionCommand",
        "Compute hashes of package archives.",
        "ConfigurationCommand",
        "DebugCommand",
        "Download packages.",
        "DownloadCommand",
        "FreezeCommand",
        "HashCommand",
        "HelpCommand",
        "IndexCommand",
        "Inspect and manage pip's wheel cache.",
        "Inspect information available from package indexes.",
        "Inspect the python environment.",
        "InspectCommand",
        "Install packages.",
        "InstallCommand",
        "List installed packages.",
        "ListCommand",
        "Manage local and global configuration.",
        "Output installed packages in requirements format.",
        "pip._internal.commands.cache",
        "pip._internal.commands.check",
        "pip._internal.commands.completion",
        "pip._internal.commands.configuration",
        "pip._internal.commands.debug",
        "pip._internal.commands.download",
        "pip._internal.commands.freeze",
        "pip._internal.commands.hash",
        "pip._internal.commands.help",
        "pip._internal.commands.index",
        "pip._internal.commands.inspect",
        "pip._internal.commands.install",
        "pip._internal.commands.list",
        "pip._internal.commands.search",
        "pip._internal.commands.show",
        "pip._internal.commands.uninstall",
        "pip._internal.commands.wheel",
        "Search PyPI for packages.",
        "SearchCommand",
        "Show help for commands.",
        "Show information about installed packages.",
        "Show information useful for debugging.",
        "ShowCommand",
        "Uninstall packages.",
        "UninstallCommand",
        "Verify installed packages have compatible dependencies.",
        "WheelCommand",
        return close_commands[0]
        return None
    """
    """Command name auto-correct."""
    "cache": CommandInfo(
    "check": CommandInfo(
    "completion": CommandInfo(
    "config": CommandInfo(
    "debug": CommandInfo(
    "download": CommandInfo(
    "freeze": CommandInfo(
    "hash": CommandInfo(
    "help": CommandInfo(
    "index": CommandInfo(
    "inspect": CommandInfo(
    "install": CommandInfo(
    "list": CommandInfo(
    "search": CommandInfo(
    "show": CommandInfo(
    "uninstall": CommandInfo(
    "wheel": CommandInfo(
    ),
    close_commands = get_close_matches(name, commands_dict.keys())
    command = command_class(name=name, summary=summary, **kwargs)
    command_class = getattr(module, class_name)
    Create an instance of the Command class with the given name.
    else:
    from difflib import get_close_matches
    if close_commands:
    module = importlib.import_module(module_path)
    module_path, class_name, summary = commands_dict[name]
    name = name.lower()
    return command
"""
#
# - Enables avoiding additional (costly) imports for presenting `--help`.
# - The ordering matters for help display.
# `commands_dict` in test setup / teardown).
# Even though the module path starts with the same "pip._internal.commands"
# prefix, the full path makes testing easier (specifically when modifying
# This dictionary does a bunch of heavy lifting for help output:
}
CommandInfo = namedtuple("CommandInfo", "module_path, class_name, summary")
commands_dict: Dict[str, CommandInfo] = {
def create_command(name: str, **kwargs: Any) -> Command:
def get_similar_commands(name: str) -> Optional[str]:
from collections import namedtuple
from pip._internal.cli.base_command import Command
from typing import Any, Dict, Optional
import importlib
Package containing all pip commands
