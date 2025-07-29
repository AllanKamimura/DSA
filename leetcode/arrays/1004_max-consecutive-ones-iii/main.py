from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_counter = 0
        max_size = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter += 1

                while zero_counter > k:
                    if nums[left] == 0:
                        zero_counter -= 1

                    left += 1

            max_size = max(max_size, right - left + 1)

        return max_size
