# https://leetcode.com/problems/fizz-buzz/

input1 = 15


def fizzbuzzify(n):
    result = []
    for i in range(n):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0:
            result.append('Fizz')
        else:
            result.append(i)
    return print(result)


fizzbuzzify(input1)
