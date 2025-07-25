
        return SourceDistribution(install_req)
        return WheelDistribution(install_req)
    """Returns a Distribution for the given InstallRequirement"""
    # Editable requirements will always be source distributions. They use the
    # If it's a wheel, it's a WheelDistribution
    # legacy logic until we create a modern standard for them.
    # Otherwise, a SourceDistribution
    if install_req.editable:
    if install_req.is_wheel:
    install_req: InstallRequirement,
    return SourceDistribution(install_req)
) -> AbstractDistribution:
def make_distribution_for_install_requirement(
from pip._internal.distributions.base import AbstractDistribution
from pip._internal.distributions.sdist import SourceDistribution
from pip._internal.distributions.wheel import WheelDistribution
from pip._internal.req.req_install import InstallRequirement
