# https://leetcode.com/problems/sort-array-by-parity/

input1 = [3, 1, 2, 4]


def sort_even(input):
    result = []
    for i in input:
        if i % 2 == 1:
            result.append(i)
        else:
            result.insert(0, i)
    return print(result)


sort_even(input1)
