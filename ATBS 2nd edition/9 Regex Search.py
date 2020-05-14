#! python3 -O
# Open all .txt files in a folder and print any line that matches a certain regex.
# Done

import re
from os import chdir
from pathlib import Path

chdir(Path(r"C:\Users\Beheerder\Py3Projects\9 Practice projects"))

all_txt = list(Path.cwd().glob('*.txt'))  # create list of all .txt files in cwd
keyword = input("Enter a keyword to search the files for: ")

print('Matches found:')
# find and print matches
for i in all_txt:  # for all text files:
    current_file = open(Path(i))  # open text file
    lines = current_file.readlines()  # create list of sentences, separated by newline
    for p in lines:  # for every sentence:
        match = re.compile(f'.*{keyword}.*', re.I).search(p)  # add to list if the sentence has the keyword in it
        if match is not None:
            print(match.group())  # print all sentences that match the keyword
    current_file.close()  # close file
