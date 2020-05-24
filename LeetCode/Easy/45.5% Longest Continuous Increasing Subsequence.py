# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

input1 = [1, 3, 5, 4, 7]
input2 = [2, 2, 2, 2, 2]


class Solution(object):
    def findLengthOfLCIS(self, nums):
        highest_subsequence_count = 0
        current_subsequence_count = 0

        for i in range(len(nums)):
            if nums[i] > nums[i - 1]:
                current_subsequence_count += 1
                highest_subsequence_count = max(current_subsequence_count, highest_subsequence_count)
            else:
                current_subsequence_count = 1

        if highest_subsequence_count == 0:
            highest_subsequence_count = 1

        return print(highest_subsequence_count)


result = Solution()
result.findLengthOfLCIS(input1)
result.findLengthOfLCIS(input2)
