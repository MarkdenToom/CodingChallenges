# !python3
# Find POMEG files and move them to the others folder

# TODO: set cwd to location of pomegname.txt & pomegpaths.txt

from os import chdir
from pathlib import Path
from shutil import move

chdir(Path.home()/r'Desktop\Fix pomeg')

# read names
nametxt = open('pomegname.txt')
pomegnames = nametxt.readlines()

# read and filter cluster of paths to recreate list of only POMEG paths
with open('pomegpaths.txt', 'r', errors='replace') as pathstxt:  # open & accept non-ASCII characters
    pomegpaths = pathstxt.readlines()
    for path in pomegpaths:
        path = path.strip()
        for name in pomegnames:
            name = name.strip()
            pomeg_check = "Documents\\" + name  # create list of paths with just POMEG
            if pomeg_check in path:
                try:
                    new_path = Path(path).resolve().parents[1] / r'Others'
                    print("Moved x to y:\n" + path, '\n' + str(new_path), '\n')
                    # move(path, new_path)  # un-comment this after testing on a small scale
                except FileExistsError or FileNotFoundError:
                    pass
