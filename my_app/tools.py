import shutil
import os

def move_file(file):
    shutil.move(f"{file}", "./files")


def change_name(file):
    name = file.split(" ")
    c_name = "_".join(name)
    return c_name.lower()


def make_tree():
    path = "./files"
    
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors

    return lst