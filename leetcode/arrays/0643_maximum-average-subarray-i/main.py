from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        max_average = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_average = max(max_average, window_sum / k)

        return max_average
