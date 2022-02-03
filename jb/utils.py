import os


def read(rel_path):
    with open(os.path.join(rel_path)) as fp:
        return fp.read()
