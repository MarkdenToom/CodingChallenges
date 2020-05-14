#! python3 -O
# Copies an entire folder and its contents into a ZIP file whose filename increments based on version.

import zipfile
import os
from pathlib import Path

os.chdir(Path.home()/r'Py3Projects\10 Backing Up a Folder into a ZIP File')


def backup_to_zip(folder):
    # Backup the entire contents of a 'folder' into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out what the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolder, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')


backup_to_zip('delicious')
