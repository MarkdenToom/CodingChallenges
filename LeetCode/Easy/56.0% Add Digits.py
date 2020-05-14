# https://leetcode.com/problems/add-digits/


input1 = 38


def add_digits(n):
    while n > 9:
        new_n = 0
        for i in str(n):
            new_n += int(i)
        n = new_n
    else:
        return print(n)


add_digits(input1)
