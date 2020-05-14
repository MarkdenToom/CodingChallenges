# Done
# Testing purposes

import random

shuffle = "You came to the wrong house, fool!"
shuffle = shuffle.split()  # I split up these functions to improve readability
random.shuffle(shuffle)
for i in range(len(shuffle)):
    print(f"{shuffle[i]} ", end="")
