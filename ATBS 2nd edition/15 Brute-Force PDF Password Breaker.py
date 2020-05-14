#! Python3
"""What the program does:
Open dictionary.txt
Loop over the 44k words
Try every single one to decrypt encryptedminutes.pdf
Try every single word in uppercase
Break out of the loop if the password is found and print it"""

import PyPDF2
from os import chdir
from pathlib import Path
from sys import exit

chdir(Path.home()/r'Py3Projects\15-Working with PDF and Word Documents')

english_words = open('dictionary.txt').readlines()
pdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))

for word in english_words:
    word = word.strip()
    # Try using uppercase
    print('Trying word: ' + word)
    if pdfReader.decrypt(word) == 1:
        print('Password found: ' + word)
        exit()

    # Try using lowercase
    word = word.lower()
    print('Trying word: ' + word)
    if pdfReader.decrypt(word) == 1:
        print('Password found: ' + word)
        exit()
