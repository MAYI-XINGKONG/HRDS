import os


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def format_path(path):
    return os.path.normpath(path)