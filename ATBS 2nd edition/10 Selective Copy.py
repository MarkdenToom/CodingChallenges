#! python3 -O
# Walk through folder tree and copy all .txt files to a new location
# Note: The writer of the project objective insinuated the use of os.walk(), but glob() is easier.

from os import chdir
from pathlib import Path
import shutil

chdir(Path.home()/r'Py3Projects\10 Selective Copy\Find')

for filename in (Path('./')).glob('**/*.txt'):
    print(f'"{filename}" copied to Found folder!')
    shutil.copy(filename, Path('../Found'))
