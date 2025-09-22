import os


def resolve_path(base_path, relative_path):
    return os.path.abspath(os.path.join(base_path, relative_path))


def file_exists(path):
    return os.path.isfile(path)


def dir_exists(path):
    return os.path.isdir(path)
