# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

input1_1 = [2, 3, 5, 1, 3]
input1_2 = 3

input2_1 = [4, 2, 1, 1, 2]
input2_2 = 1

input3_1 = [12, 1, 12]
input3_2 = 10


def solution(candies, extraCandies):
    output = []
    maxCandies = max(candies)
    for i in candies:
        if i + extraCandies >= maxCandies:
            output.append('true')
        else:
            output.append('false')
    return print(output)


solution(input1_1, input1_2)
solution(input2_1, input2_2)
solution(input3_1, input3_2)
