def parse_version(version_str):
    return tuple(map(int, version_str.split(".")))


def compare_versions(v1, v2):
    t1 = parse_version(v1)
    t2 = parse_version(v2)
    return (t1 > t2) - (t1 < t2)
