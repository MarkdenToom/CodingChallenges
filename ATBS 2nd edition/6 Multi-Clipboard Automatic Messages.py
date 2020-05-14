#! python3 -O
# This program allows for multiple clipboards to make repetitive copy/pasting easier.
# Done

# Run the program by opening the Run window (WIN+R) and typing eg: "zclip upsell" to copy the upsell clipboard

import sys
import pyperclip

text = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:  # sys.argv is a list which contains the command-line arguments passed to the script.
    print("Usage: python 6 Multi-Clipboard Automatic Messages.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f'There is no text for {keyphrase}')
