# Done

import random
import sys

print("Type 'exit' to quit the program")

while True:
    output = ("It is certain. ",    # using tuples for learning purposes
              "Yes definitely. ",
              "Reply hazy, try again. ",
              "Ask again later. ",
              "Concentrate more and ask again. ",
              "My reply is no. ",
              "Outlook is not so good. ",
              "Very doubtful. ")
    print(random.choice(output), end='')
    if input() == "exit":
        sys.exit()
