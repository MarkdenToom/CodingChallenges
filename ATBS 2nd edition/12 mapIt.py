# !python3
# Launches google maps in the browser using an address from the command line or clipboard.

"""This is what the program does:
Gets a street address from the command line arguments or clipboard
Opens the web browser to the Google Maps page for the address
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Read the clipboard contents.
Call the webbrowser.open() function to open the web browser."""

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:  # if address is present in the command line:
    address = ''.join(sys.argv[1:])  # get address from command line
else:
    address = pyperclip.paste()  # get address from clipboard

webbrowser.open('https://www.google.com/maps/place/' + address)
