import pytest
from modules.common.version_util import parse_version, compare_versions


def test_parse_version():
    assert parse_version("1.2.3") == (1, 2, 3)
    assert parse_version("0.0.1") == (0, 0, 1)


@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        ("1.2.3", "1.2.3", 0),
        ("1.2.4", "1.2.3", 1),
        ("1.2.2", "1.2.3", -1),
        ("1.10.0", "1.2.9", 1),
        ("2.0.0", "10.0.0", -1),
    ],
)
def test_compare_versions(v1, v2, expected):
    assert compare_versions(v1, v2) == expected
