import glob
import os

PATH = "./"


def calculate_dir_size(path):
    size = 0

    paths = glob.glob(os.path.join(path, "*"))

    for i in paths:
        if os.path.isfile(i):
            print(i)
            size += os.path.getsize(i)
        else:
            size += calculate_dir_size(i)

    return size


print(calculate_dir_size(PATH))
