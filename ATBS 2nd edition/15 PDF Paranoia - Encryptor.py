#! Python3
# Walk through every PDF in a folder and its subfolders and encrypt them. Delete original files after testing.
# Note: methods used were inspired by the solution IFinners (https://github.com/IFinners) made.

"""What the program does:
Find all pdf in folder and subfolder using os.walk()
Encrypt all found pdf with a password provided on the command line
Save all encrypted pdf with an _encrypted.pdf suffix
Attempt to read and decrypt to ensure all pdf are encrypted properly
Delete original non-encrypted files"""

import PyPDF2
import os
from pathlib import Path
from sys import argv

os.chdir(Path.home()/r'Py3Projects\15-Working with PDF and Word Documents\PDF Paranoia\Decrypted files')

# password = argv[1]
password = "whale"  # using this instead of the command line for easier testing
failed_encryptions = []

for folders, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if ".pdf" in filename:
            path = str(Path(folders) / Path(filename))
            original_pdf = open(path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(original_pdf)
            if not pdf_reader.isEncrypted:
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Encrypt copy of PDF and save with _encrypted suffix
                pdf_writer.encrypt(password)
                encrypted_path = path[:-4] + '_encrypted.pdf'
                encrypted_version = open(encrypted_path, 'wb')
                pdf_writer.write(encrypted_version)
                encrypted_version.close()
                original_pdf.close()

                # Check file was encrypted properly
                encrypted_pdf = open(encrypted_path, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(encrypted_pdf)
                if pdf_reader.isEncrypted and pdf_reader.decrypt(password) == 1:
                    Path.unlink(Path(path))
                else:
                    failed_encryptions.append(filename)

if failed_encryptions:
    print('Failed to encrypt the following files:')
    for filename in failed_encryptions:
        print(filename)
else:
    print("All PDFs in the folder and its subfolders have been encrypted. The original files have been deleted.")
