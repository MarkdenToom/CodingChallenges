# Done
# I copied this from automate the boring stuff

catNames = []
while True:
    print(f"Enter the name of cat {str(len(catNames) + 1)} (Or enter nothing to stop): ")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
