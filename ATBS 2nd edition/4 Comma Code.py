# Done

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(len(spam)):
    if i == 0:
        print(f"'{spam[0]}, ", end="")
    elif i < len(spam) - 2:
        print(spam[i], end=", ")
    elif i == len(spam) - 1:
        print(spam[-2], end=" and ")
        print(spam[-1], end="'")
