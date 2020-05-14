# Done

import sys

while True:
    name = input('Name: ').lower()
    if len(name) >= 20 or len(name) <= 2:
        print("invalid username")
        continue
    password = input("Password: ").lower()
    if len(password) >= 20 or len(password) <= 3:
        print("invalid password")
        continue
    elif name == "john" or name == "johnathan" and password == "polymer":
        print("Access granted")
        break
    else:
        print("Access Denied")
        continue

print("Welcome, John!")
sys.exit()
