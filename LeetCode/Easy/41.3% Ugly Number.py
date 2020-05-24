# https://leetcode.com/problems/ugly-number/

input1 = 6
input2 = 8
input3 = 14


class Solution(object):
    def isUgly(self, num):
        for i in (5, 3, 2):
            while num % i == 0:
                num = num / i

        if num == 1:
            return print(True)
        else:
            return print(False)


number = Solution()
number.isUgly(input1)
number.isUgly(input2)
number.isUgly(input3)
