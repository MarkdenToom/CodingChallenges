# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

input1 = 4
input2 = 2


def odd_strings(input):
    result = ''
    if input % 2 == 1:  # if the input is uneven
        for i in range(input):
            result += 'a'
    else:
        for i in range(input - 1):
            result += 'a'
        result += 'b'
    return print(result)


odd_strings(input1)
odd_strings(input2)
