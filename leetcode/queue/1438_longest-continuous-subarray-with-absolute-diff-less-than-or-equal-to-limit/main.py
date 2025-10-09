from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase = deque()
        decrease = deque()

        max_range = 0
        left = 0

        for right, num in enumerate(nums):
            while increase and nums[increase[-1]] > num:
                increase.pop()

            while decrease and nums[decrease[-1]] < num:
                decrease.pop()

            increase.append(right)
            decrease.append(right)

            while (nums[decrease[0]] - nums[increase[0]]) > limit:
                left += 1

                if decrease[0] < left:
                    decrease.popleft()

                if increase[0] < left:
                    increase.popleft()

            max_range = max(max_range, (right - left + 1))

        return max_range
