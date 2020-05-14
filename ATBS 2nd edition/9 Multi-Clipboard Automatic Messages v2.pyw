#! python3 -O
# Saves and loads pieces of text to the clipboard based on keywords.
# Done

r"""How to use:
1.  create 'zclip.bat' in 'C:\Windows' with the following line:
    @pyw.exe "[insert the directory you saved 9 Multi-Clipboard Automatic Messages v2.pyw in]" %*
2.  change cwd to where you saved this .pyw
2.  type in run window: 'py.exe zclip.pyw save spam' to save current clipboard with keyword spam.
3.  type in run window: 'py.exe zclip.pyw spam' to copy the content of the keyword to the clipboard.
    type in run window: 'py.exe zclip.pyw list' to copy a list of keywords you've created to the clipboard.

Here’s what the program does:
The command line argument for the keyword is checked.
If the argument is save, then the clipboard contents are saved to the keyword.
If the argument is list, then all the keywords are copied to the clipboard.
Otherwise, the text for the keyword is copied to the clipboard.

This means the code will need to do the following:
Read the command line arguments from sys.argv.
Read and write to the clipboard.
Save and load to a shelf file."""

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('9 Multi-Clipboard Automatic Messages v2')  # set variable mcbShelf to open this .pyw

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':  # if we want to save a clipboard, then do:
    mcbShelf[sys.argv[2]] = pyperclip.paste()  # the keyword will be used as the key for mcbShelf and pasted to clipboar
elif len(sys.argv) == 2:  # if we want to show list of keywords / copy the content of a keyword to our clipboard, do:
    if sys.argv[1].lower() == 'list':  # if requesting a list of keywords, do:
        pyperclip.copy(str(list(mcbShelf.keys())))  # copy list of keywords to clipboard
    elif sys.argv[1] in mcbShelf:  # if requesting the content of a keyword, do:
        pyperclip.copy(mcbShelf[sys.argv[1]])  # copy content of keyword to clipboard

mcbShelf.close()
