#! python3 -O
# Create numbered files for testing '10 Filling in the Gaps.py' and '10 Filling in the Gaps - Create Gaps'

from os import chdir
from pathlib import Path

chdir(Path.home()/r'Py3Projects\10 Filling in the Gaps')

for i in range(20):
    create = open(f'spam{i+1:03}.txt', 'w')
    create.close()
