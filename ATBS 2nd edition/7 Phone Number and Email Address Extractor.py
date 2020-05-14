#! python3 -O
# Finds all phone numbers and email addresses on your clipboard and copies only them to your clipboard
# Done

import pyperclip
import re

# phone number regex
phoneRegex = re.compile(r"""(         # all of this is (group 0)
    (\d{3}|\(\d{3}\))?                # area code (group 1), eg: '823' or '(137)'
    (\s|-|\.)?                        # separator (group 2), eg: ' ' or '-' or '.'
    (\d{3})                           # first 3 digits (group 3), eg: '344'
    (\s|-|\.)                         # separator (group 4), eg: ' ' or '-' or '.'
    (\d{4})                           # last 4 digits (group 5), eg: '9745'
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension (group 6 with 7 and 8 inside), eg: ' ext.91084' or 'x 01'
    )""", re.VERBOSE)

# email regex
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+      # username: any letters, numbers, dots, underscores, percent signs, plus signs and hyphens
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name: any letters, numbers, dots and hyphens
    (\.[a-zA-Z]{2,4})       # top-level domain, eg: '.com' or '.be' or '.arpa' and not '.বাংলা' and not '.academy'
    )""", re.VERBOSE)

# find matches in clipboard
text = str(pyperclip.paste())  # set current clipboard to 'text' variable

matches = []  # create empty list for all phone numbers and email-addresses
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # reformat phone numbers to ddd-ddd-dddd
    if groups[8] != '':  # check if extension is present
        phoneNum += ' x' + groups[8]  # adds extensions if present
    matches.append(phoneNum)  # add phone numbers to the 'matches' list
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # add all email to the list

# copy results to the clipboard
matches = list(dict.fromkeys(matches))  # remove duplicates
if len(matches) > 0:  # if a match is found, do the following:
    pyperclip.copy('\n'.join(matches))  # copy the list onto the clipboard with newlines in between
    print('Copied to clipboard:')
    print('\n'.join(matches))  # print the list onto the terminal for viewing purposes
else:
    print('No phone numbers or email addresses found.')
