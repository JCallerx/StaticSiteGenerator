import os
from pathlib import Path
import shutil

def copy_static(src, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    files_in_src = os.listdir(src)

    for file in files_in_src:
        full_path = os.path.join(src, file)
        if os.path.isfile(full_path):
            shutil.copy(full_path, destination)
        elif os.path.isdir(full_path):
            copy_static(full_path, os.path.join(destination, file))
