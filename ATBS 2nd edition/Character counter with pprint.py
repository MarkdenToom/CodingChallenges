# copied

import pprint

# character counter: display count of all characters in an input individually
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count, "\n")
pprint.pprint(count)  # same as above, but using pretty print
