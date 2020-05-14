#! python3 -O
# Find numbered files and rename all to close gaps, e.g: spam001.txt and spam003.txt but no spam002.txt

import os
from pathlib import Path
import re
import shutil

os.chdir(Path.home()/r'Py3Projects/10 Filling in the Gaps')

newNumber = 1
for filename in os.listdir(Path()):  # for all files in the folder
    filename = re.compile(r'(\D*)(\d{3})(\..*)').search(str(filename))  # 1 = prefix, 2 = number, 3 = ext
    newFilename = f'{filename.group(1)}{newNumber:03}{filename.group(3)}'  # 1 = prefix, 2 = newNumber, 3 = ext
    newNumber += 1  # up the newNumber by 1 for every time we file in the folder
    shutil.move(Path.cwd()/Path(filename.group()), Path.cwd()/Path(newFilename))  # replace the old name with the new
    print(f'Old name: "{filename.group()}" Renamed to: "{newFilename}"')  # print feedback for debugging
