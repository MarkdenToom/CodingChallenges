#! python3 -O
# Detects adjectives, nouns, adverbs and verbs in a text file and prompts users to replace them, followed by saving it.
# Done

import re

madLibsText = open(r'C:\Users\Beheerder\Py3Projects\9 Practice projects\9 Mad Libs.txt')  # open file
list_of_text = madLibsText.read().split('\n')  # read file and create list separated by newlines
text = ' '.join(list_of_text)  # create single string from list
print(text)  # display the text we found in the file

found_keywords = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB').findall(text)  # create list of all found keywords
# prompt user to enter alternatives to the found keywords
for i in found_keywords:
    text = re.compile(i).sub(input(f'Enter a {i.lower()}:\n'), text, count=1)
print(text)  # print the new content of text file
madLibsText.close()  # close file

# overwrite old text in file with new text
madLibsText = open(r'C:\Users\Beheerder\Py3Projects\9 Practice projects\9 Mad Libs.txt', 'w')  # open file, write mode
madLibsText.write(text)
madLibsText.close()
print("The file has been updated!")

# (optional) reset text for future use
reset = open(r"C:\Users\Beheerder\Py3Projects\9 Practice projects\9 Mad Libs.txt", 'w')
reset.write("""The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.""")
reset.close()
print("The file has been reset!")
