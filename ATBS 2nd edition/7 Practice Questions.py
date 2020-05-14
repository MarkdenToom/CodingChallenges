import re

print("Practice Questions")


def find(string):
    if re.compile(r'^\d{1,3}(,\d{3})*$').search(string):
        return True


def surname(string):
    if re.compile('[A-Z]\w+ Watanabe').search(string):
        return True


print(find('42'))
print(find('1,234'))
print(find('6,368,745'))
print(find('12,34,567'))
print(find('1234'), "\n")

print(surname("Haruto Watanabe"))
print(surname("Alice Watanabe"))
print(surname("RoboCop Watanabe"))
print(surname("haruto Watanabe"))
print(surname("Mr. Watanabe"))
print(surname("Watanabe"))
print(surname("Haruto watanabe"))
