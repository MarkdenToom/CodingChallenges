# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

input1 = [12, 345, 2, 6, 7896]
input2 = [555, 901, 482, 1771]


def count_even(input):
    counter = 0
    for integer in input:
        if len(str(integer)) % 2 == 0:
            counter += 1
    return print(counter)


count_even(input1)
count_even(input2)
