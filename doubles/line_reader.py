import os


def read_file(filename):
    is_exists = os.path.exists(filename)
    if not is_exists:
        raise OSError("File name is not exists")
    with open(filename, "r") as file:
        return file.readline()
