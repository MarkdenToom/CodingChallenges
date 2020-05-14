#! Python3
# Walk through every PDF in a folder and its subfolders and decrypt them. Print incorrect passwords.
# Note: methods used were inspired by the solution IFinners (https://github.com/IFinners) made.

"""What the program does:
Find all pdf in folder and subfolder using os.walk()
Find all encrypted pdf with a password provided on the command line
Save all encrypted pdf with the ' (copy).pdf' suffix
Print message and continue if the password is incorrect"""

import PyPDF2
import os
from pathlib import Path
from sys import argv

os.chdir(Path.home()/r'Py3Projects\15-Working with PDF and Word Documents\PDF Paranoia\Encrypted files')

# password = argv[1]
password = "whale"  # using this instead of the command line for easier testing

for folders, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if ".pdf" in filename:
            path = str(Path(folders) / Path(filename))
            pdf_reader = PyPDF2.PdfFileReader(open(path, 'rb'))

            if pdf_reader.isEncrypted and pdf_reader.decrypt(password) == 1:
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                decrypted_path = path[:-4] + ' (copy).pdf'
                decrypted_version = open(decrypted_path, 'wb')
                pdf_writer.write(decrypted_version)
                decrypted_version.close()
            if pdf_reader.isEncrypted and pdf_reader.decrypt(password) == 0:
                print('Wrong password for the following PDF:\n' + str(Path.cwd() / Path(filename)))
