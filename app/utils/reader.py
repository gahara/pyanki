import os


def read_file_names(path):
    (_, _, filenames) = next(os.walk(path))
    return filenames
