#! python3
# Converts MM-DD-YYYY style dates to DD-MM-YYYY

"""Here’s what the program does:
1. It searches all the filenames in the current working directory for American-style dates.
2. When one is found, it renames the file with the month and day swapped to make it European-style.

This means the code will need to do the following:
1. Create a regex that can identify the text pattern of American-style dates.
2. Call os.listdir() to find all the files in the working directory.
3. Loop over each filename, using the regex to check whether it has a date.
4. If it has a date, rename the file with shutil.move()."""

import shutil
import os
import re
from pathlib import Path

os.chdir(Path.home()/r'Py3Projects\10 Renaming Files with American-Style Dates to European-Style Dates')

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # all text before the date
    (([01])?\d)-                     # one or two digits for the month
    (([0123])?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                           # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different part of filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    # shutil.move(amerFilename, euroFilename)  # uncomment after testing
