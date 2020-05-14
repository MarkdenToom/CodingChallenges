# copied
# simple 'add to library'-program

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        birthday = input(f"I do not have birthday information for {name}. What is their birthday?")
        birthdays[name] = birthday
        print('Birthday database updated.')
