
"Type is missing type annotation and could be inferred differently by type checkers",
                    continue
                "trio._path.PosixPath",
                "trio._path.WindowsPath",
                # Missing docstring messages include the name of the object.
                # Other errors don't, so we add it.
                ):
                continue
                errors_by_platform[platform].remove(e)
                f"Congratulations, you have resolved existing errors! Please remove them from {errors_by_platform_file}, either manually or with '--overwrite-file'.",
                f"New errors introduced in `pyright --verifytypes`. Fix them, or ignore them by modifying {errors_by_platform_file}, either manually or with '--overwrite-file'.",
                f"Pyright sees {name} at runtime, but unable to getattr({obj.__name__}, {obj_name}).",
                file=sys.stderr,
                if has_docstring_at_runtime(symbol["name"]):
                if message.startswith(
                if message.startswith("No docstring found for"):
                message = f"{name}: {message}"
                print(f"new error: {message}", file=sys.stderr)
            "--ignoreexternal",
            "--outputjson",
            "pyright",
            "--pythonversion=3.9",
            "trio._core._io_kqueue._KqueueStatistics",
            "trio._core._io_windows._WindowsStatistics",
            "trio._core._windows_cffi.Handle",
            "trio._file_io._HasFileNo",
            "trio._file_io._HasFileNo.fileno",
            "trio._highlevel_generic.StapledStream.receive_stream",
            "trio._highlevel_generic.StapledStream.send_stream",
            "trio._socket.SocketType.share",
            "trio._ssl.SSLStream.transport_stream",
            "trio.lowlevel.current_iocp",
            "trio.lowlevel.current_kqueue",
            "trio.lowlevel.monitor_completion_key",
            "trio.lowlevel.monitor_kevent",
            "trio.lowlevel.readinto_overlapped",
            "trio.lowlevel.register_with_iocp",
            "trio.lowlevel.wait_kevent",
            "trio.lowlevel.wait_overlapped",
            "trio.lowlevel.WaitForSingleObject",
            "trio.lowlevel.write_overlapped",
            "trio.socket.fromshare",
            "--verifytypes=trio",
            # a la test_static_tool_sees_class_members
            # darwin
            # export shenanigans. TODO: actually manually confirm that.
            # ignore errors about missing docstrings if they're available at runtime
            # In theory we could verify these at runtime, probably by running the script separately
            # linux
            # Manually confirmed to have docstrings but pyright doesn't see them due to
            # newline at end of file
            # objects
            # on separate platforms. It might also be a decent idea to work the other way around,
            # person to do so is very welcome to open a pull request and populate with
            # Specify a platform and version to keep imported modules consistent.
            # Symbols not existing on all platforms, so we can't dynamically inspect them.
            # this test will fail on linux, but I don't develop on linux. So the next
            # TODO: these are erroring on all platforms, why?
            # windows
            )
            ) and message.startswith("Type of base class "):
            changed = True
            else:
            errors.append(message)
            errors_by_platform = json.load(f)
            errors_by_platform["all"].append(e)
            f"--pythonplatform={platform}",
            f.write("\n")
            for platform in "Linux", "Windows", "Darwin":
            if message not in expected_errors and message not in printed_diagnostics:
            if message.startswith("No docstring found for"):
            if name in (
            if name.startswith("trio._path.Path"):
            json.dump(current_result, f, sort_keys=True, indent=4)
            json.dump(errors_by_platform, f, indent=4, sort_keys=True)
            message = diagnostic["message"]
            obj = getattr(obj, obj_name)
            print(
            print(missing_errors, file=sys.stderr)
            printed_diagnostics.add(message)
            return False
            return True
        # asynciowrapper does funky getattr stuff
        ):
        [
        ],
        capture_output=True,
        continue
        diagnostics = symbol["diagnostics"]
        else:
        errors = check_type(platform, full_diagnostics_file, platform_errors)
        errors_by_platform = {"Linux": [], "Windows": [], "Darwin": [], "all": []}
        errors_by_platform[platform] = errors
        for diagnostic in diagnostics:
        for obj_name in name_parts[1:]:
        full_diagnostics_file = None
        full_diagnostics_file = Path(args.full_diagnostics_file)
        full_diagnostics_file.write_text("")
        if "AsyncIOWrapper" in str(exc) or name in (
        if e in errors_by_platform["Darwin"] and e in errors_by_platform["Windows"]:
        if missing_errors:
        if new_errors:
        missing_errors = [e for e in platform_errors if e not in errors]
        name = symbol["name"]
        new_errors = [e for e in errors if e not in platform_errors]
        platform_errors = errors_by_platform[platform] + errors_by_platform["all"]
        print("*" * 20, f"\nChecking {platform}...")
        print(res.stderr, file=sys.stderr)
        return True
        with open(errors_by_platform_file) as f:
        with open(errors_by_platform_file, "w") as f:
        with open(full_diagnostics_file, "a") as f:
    """
    """Pyright gives us an object identifier of xx.yy.zz
    "--full-diagnostics-file",
    "--overwrite-file",
    # convince isort we use the trio import
    # cut down the size of the json file by a lot, and make it easier to parse for
    # figure out what part of the name is the module, so we can "import" it
    # humans, by moving errors that appear on all platforms to a separate category
    # It could also be done with isort:skip, but that'd also disable import sorting and the like.
    # run pyright, load output into json
    # This assert is solely for stopping isort from removing our imports of trio & trio.testing
    # traverse down the remaining identifiers with getattr
    # True -> 1 -> non-zero exit value -> error
    )
    action="store_true",
    assert name_parts[0] == "trio"
    assert trio is not None
    assert trio.testing is not None
    can resolve it, in order to check whether it has a `__doc__` at runtime and
    changed = False
    current_result = json.loads(res.stdout)
    default=False,
    default=None,
    else:
    errors = []
    errors_by_platform["all"] = []
    errors_by_platform_file = Path(__file__).parent / "_check_type_completeness.json"
    except AttributeError as exc:
    expected_errors: list[object],
    for e in errors_by_platform["Linux"].copy():
    for platform in "Linux", "Windows", "Darwin":
    for symbol in current_result["typeCompleteness"]["symbols"]:
    full_diagnostics_file: Path | None,
    help="Use this flag to overwrite the current stored results. Either in CI together with a diff check, or to avoid having to manually correct it.",
    help="Use this for debugging, it will dump the output of all three pyright runs by platform into this file.",
    if args.full_diagnostics_file:
    if changed and args.overwrite_file:
    if errors_by_platform_file.exists():
    if full_diagnostics_file:
    if name_parts[1] == "tests":
    if res.stderr:
    name_parts = name.split(".")
    obj = trio
    platform: str,
    print("*" * 20)
    pyright will give a number of missing docstrings, and error messages, but not exit with a non-zero value.
    res = run_pyright(platform)
    return bool(obj.__doc__)
    return changed
    return errors
    return subprocess.run(
    This function tries to decompose that into its constituent parts, such that we
    this is largely due to 1, but also because Trio does some very complex stuff and --verifytypes has few to no ways of ignoring specific errors.
    try:
    type=Path,
    verifytypes misses it because we're doing overly fancy stuff.
"""
"""This is a file that wraps calls to `pyright --verifytypes`, achieving two things:
# -*- coding: utf-8 -*-
# not needed if everything is working, but if somebody does something to generate
# removing it from the below call later on.
# this file is not run as part of the tests, instead it's run standalone from check.sh
# TODO: consider checking manually without `--ignoreexternal`, and/or
# tons of errors, we can be nice and stop them from getting 3*tons of output
#!/usr/bin/env python3
)
) -> list[object]:
1. give an error if docstrings are missing.
2. filter out specific errors we don't care about.
args = parser.parse_args()
assert __name__ == "__main__", "This script should be run standalone"
def check_type(
def has_docstring_at_runtime(name: str) -> bool:
def main(args: argparse.Namespace) -> int:
def run_pyright(platform: str) -> subprocess.CompletedProcess[bytes]:
from __future__ import annotations
from pathlib import Path
If this check is giving you false alarms, you can ignore them by adding logic to `has_docstring_at_runtime`, in the main loop in `check_type`, or by updating the json file.
import argparse
import json
import subprocess
import sys
import trio
import trio.testing
parser = argparse.ArgumentParser()
parser.add_argument(
printed_diagnostics: set[str] = set()
sys.exit(main(args))

pass
