# This program simply replaces all of the characters within a piece of text
# Done


text = input("Enter the text you would like to replace: ")
replace = input("What character would you like to replace? ")
replace_with = input("What would you like to replace this character with? ")
print(replace_with.join(text.split(replace)))  # join a piece of text you first split into a list to replace
