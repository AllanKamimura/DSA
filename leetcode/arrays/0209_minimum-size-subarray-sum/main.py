from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        min_size = float("inf")

        curr_sum = 0

        for right in range(n):
            num = nums[right]

            curr_sum += num

            while curr_sum >= target:
                min_size = min(min_size, right - left + 1)

                curr_sum -= nums[left]
                left += 1

        if min_size > n:
            min_size = 0

        return min_size
