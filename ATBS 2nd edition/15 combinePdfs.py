#! python3
# Combines all the PDFs in the current working directory into a single PDF.

"""At a high level, here’s what the program will do:
1. Find all PDF files in the current working directory.
2. Sort the filenames so the PDFs are added in order.
3. Write each page, excluding the first page, of each PDF to the output file.

In terms of implementation, your code will need to do the following:
1. Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
2. Call Python’s sort() list method to alphabetize the filenames.
3. Create a PdfFileWriter object for the output PDF.
4. Loop over each PDF file, creating a PdfFileReader object for it.
5. Loop over each page (except the first) in each PDF file.
6. Add the pages to the output PDF.
7. Write the output PDF to a file named allminutes.pdf."""

import PyPDF2
import os
from pathlib import Path

os.chdir(Path.home()/r'Py3Projects\15-Working with PDF and Word Documents')

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
