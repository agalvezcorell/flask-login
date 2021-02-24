from datetime import datetime
import hashlib
import pandas as pd
import os
import shutil



def move_file(file):
    path = "./files"
    if os.path.exists(f"./files/{file}"):
        os.remove(f"{path}/{file}")
        os.remove(f"./{file}")
        existe = "El archivo ya existe"
        return existe
    else:
        shutil.move(f"{file}", "./files")
        ok = "Archivo subido al servidor"
        return ok
    


def change_name(file):
    name = file.split(" ")
    c_name = "_".join(name)
    return c_name.lower()


def make_tree():
    path = "./files/"
    try: 
        lst = os.listdir(path)
        lst_all = []
        for el in lst:
            lst_all.append({
                    "name": f"{el}",
                    "date": datetime.now(),
                "hash": getsha256file(f"{path}{el}"),
                "size":getsize(f"{path}{el}")
                })
            
    except OSError:
        return ("No hay archivos en el servidor")
    data = pd.DataFrame.from_dict(lst_all)
    return data


def delete_file(file):
    path = "./files"
    if os.path.exists(f"{path}/{file}"):
        os.remove(f"{path}/{file}")
        ok = "Archivo borrado correctamente"
        return ok
    else:
        error = "El archivo no existe"
        return error


def getsha256file(archivo):
    try:
        hashsha = hashlib.sha256()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashsha.update(bloque)
        return hashsha.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""


def getsize(archivo):
    sizefile= os.path.getsize(archivo)
    return f"{sizefile} bytes"

def getfecha():
    now = datetime.now()
    return now




