import shutil

def move_file(file):
    shutil.move(f"{file}", "./files")


def change_name(file):
    name = file.split(" ")
    c_name = "_".join(name)
    return c_name.lower()
