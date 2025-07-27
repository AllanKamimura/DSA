from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_size = 0
        max_size = curr_size

        for num in nums:
            if num == 1:
                curr_size += 1
                max_size = max(max_size, curr_size)

            else:
                curr_size = 0

        return max_size
