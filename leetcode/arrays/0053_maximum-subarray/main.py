from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum

        for i in range(1, len(nums)):
            num = nums[i]

            if curr_sum > 0:
                curr_sum += num

            else:
                curr_sum = num

            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
