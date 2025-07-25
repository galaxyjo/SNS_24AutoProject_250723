
                    global_options,
                    home=home,
                    prefix=prefix,
                    pycompile=pycompile,
                    root=root,
                    uninstalled_pathset = requirement.uninstall(auto_confirm=True)
                    uninstalled_pathset.commit()
                    uninstalled_pathset.rollback()
                    use_user_site=use_user_site,
                    warn_script_location=warn_script_location,
                # if install did not succeed, rollback previous uninstall
                )
                if uninstalled_pathset and not requirement.install_succeeded:
                if uninstalled_pathset and requirement.install_succeeded:
                logger.info("Attempting uninstall: %s", req_name)
                raise
                requirement.install(
                uninstalled_pathset = None
                with indent_log():
            ", ".join(to_install.keys()),
            "Installing collected packages: %s",
            else:
            except Exception:
            if requirement.should_reinstall:
            installed.append(InstallationResult(req_name))
            try:
        )
        assert req.name, f"invalid to-be-installed requirement: {req}"
        for req_name, requirement in to_install.items():
        logger.info(
        yield req.name, req
    """
    "install_given_reqs",
    "InstallRequirement",
    "parse_requirements",
    "RequirementSet",
    (to be called after having downloaded and unpacked the packages)
    for req in requirements:
    global_options: Sequence[str],
    home: Optional[str],
    if to_install:
    Install everything in the given list.
    installed = []
    name: str
    prefix: Optional[str],
    pycompile: bool,
    requirements: List[InstallRequirement],
    return installed
    root: Optional[str],
    to_install = collections.OrderedDict(_validate_requirements(requirements))
    use_user_site: bool,
    warn_script_location: bool,
    with indent_log():
) -> Generator[Tuple[str, InstallRequirement], None, None]:
) -> List[InstallationResult]:
@dataclass(frozen=True)
]
__all__ = [
class InstallationResult:
def _validate_requirements(
def install_given_reqs(
from .req_file import parse_requirements
from .req_install import InstallRequirement
from .req_set import RequirementSet
from dataclasses import dataclass
from pip._internal.utils.logging import indent_log
from typing import Generator, List, Optional, Sequence, Tuple
import collections
import logging
logger = logging.getLogger(__name__)
