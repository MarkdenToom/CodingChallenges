#! python3 -O
# Insert gaps into numbered files to allow new files to be added.

import os
import re
import shutil
from pathlib import Path

os.chdir(Path.home()/r'Py3Projects/10 Filling in the Gaps')

gapNumber = 3  # enter number where you'd like the gap
listOfContent = os.listdir()  # create list of all contents of folder
listOfContent.reverse()  # reverse list as to no create conflicts with existing filenames
print(f'Making room for filenumber: {gapNumber:03}')  # print feedback for debugging
for filename in listOfContent:  # for all files in the folder
    filename = re.compile(r'(\D*)(\d{3})(\..*)').search(str(filename))  # 1 = prefix, 2 = number, 3 = ext
    newNumber = int(filename.group(2)) + 1  # the new number is the old number + 1
    newFilename = f'{filename.group(1)}{newNumber:03}{filename.group(3)}'  # 1 = prefix, 2 = newNumber, 3 = ext
    if int(filename.group(2)) >= gapNumber:  # for all files with a number above where we want the gap
        shutil.move(Path.cwd() / Path(filename.group()), Path.cwd() / Path(newFilename))  # insert gap in numbering
        print(f'File: "{filename.group()}" Moved up to: "{newFilename}"')  # print feedback for debugging
