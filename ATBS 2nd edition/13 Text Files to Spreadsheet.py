#! python3
# Read contents of text files and add them to a spreadsheet
# Note: I'm using some random poems I found online for this project

from os import chdir
from pathlib import Path
import openpyxl

chdir(Path(r"C:\Users\Beheerder\Py3Projects\13-Working with Excel Spreadsheets\Text Files to Spreadsheet"))

all_txt_files = list(Path.cwd().glob('*.txt'))  # create list of all .txt files in cwd
wb = openpyxl.Workbook()
sheet = wb.active

column = 1
for file in all_txt_files:
    # Read file
    current_file = open(Path(file))
    file_text = current_file.readlines()
    current_file.close()

    # Add the lines to a new column in the workbook
    for row in range(1, len(file_text) + 1):
        sheet.cell(row=row, column=column).value = file_text[row - 1]
    column += 1

wb.save(r'../Text Files to Spreadsheet.xlsx')
