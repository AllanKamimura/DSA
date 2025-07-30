from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_diff = float("-inf")

        min_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum - min_sum > max_diff:
                max_diff = curr_sum - min_sum

            if curr_sum < min_sum:
                min_sum = curr_sum

        return max_diff
