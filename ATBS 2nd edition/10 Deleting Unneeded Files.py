#! python3 -O
# Walk through folder tree and display absolute path of files and folders larger than 100MB.

import os
from pathlib import Path

detect_size = 100  # enter detection size in MB
search_folder_path = Path.home()/'Documents/Zooi/games'  # enter folder path you would like to search

print(f'Now searching through {search_folder_path} for all folders and files larger than {detect_size}MB!')
for folderName, subfolders, filenames in os.walk(search_folder_path):
    for subfolder in subfolders:  # detect folders
        subfoldersize = sum(y.stat().st_size for y in (Path(folderName) / Path(subfolder)).glob("**/*") if y.is_file())
        subfoldersize = round(subfoldersize / 1000000)  # convert bytes to rounded size in MB
        if subfoldersize > detect_size:  # only print if it's larger than the detect_size
            print(f'The folder {folderName}\\{subfolder} is {subfoldersize}MB!')
    for filename in filenames:  # detect files
        filenamesize = round((Path(folderName) / Path(filename)).stat().st_size / 1000000)
        if filenamesize > detect_size:  # only print if it's larger than the detect_size
            print(f'The file {folderName}\\{filename} is {filenamesize}MB!')
