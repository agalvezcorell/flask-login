import shutil
import os
import pandas as pd

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


def make_tree2():
    path = "./files"
    try: 
        lst = os.listdir(path)
        lst_all = []
        for el in lst:
            lst_all.append({
                    "name": f"{el}",
                    "info": "wait"
                })
    except OSError:
        return ("no hay archivos en el servidor")
    data = pd.DataFrame.from_dict(lst_all)
    return data