from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        i = 0
        j = 0

        while j < len(nums):
            first = nums[i]
            second = nums[j]

            if (first == 0) and (second == 0):
                j += 1
            elif second != 0:
                nums[i] = second
                nums[j] = first

                i += 1
                j = i
