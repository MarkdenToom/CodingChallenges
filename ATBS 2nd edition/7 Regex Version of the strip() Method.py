# Does the same as the strip() method, but using regex
# Done

import re


def stripper(string, strip=' '):
    return re.compile(f'^{strip}*(.*?){strip}*$').search(string).group(1)


# tests
print(stripper('PASSWORD'))  # remove nothing
print(stripper(' AbiaoaJ   HFGfhb821 '))  # space on both ends
print(stripper(' Pass300'))  # space on just the left side
print(stripper('password77 '))  # space on just the right side
print(stripper('  AbiaoaJHFGfhb821  '))  # more than one space on both ends
print(stripper('xCHAMEL30Nx', 'x'))  # 'x' on both ends
print(stripper('xxPaSsWo  Rddxx', 'x'))  # more than one 'x' on both ends
