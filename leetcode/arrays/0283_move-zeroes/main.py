from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
        Modify nums in-place instead.
        """
        i = 0
        j = 0

        while j < len(nums):
            first = nums[i]
            second = nums[j]

            if second != 0:
                nums[i] = second
                nums[j] = first

                i += 1
            j += 1

        return nums
