#! python3 -O
# Adds "# " to the start of each line of text on the clipboard.
# Done

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = f"# {lines[i]}"  # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
