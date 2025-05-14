from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            middle_point = (i + j) // 2
            middle_value = nums[middle_point]

            if target > middle_value:
                i = middle_point + 1

            elif target < middle_value:
                j = middle_point - 1

            else:
                return middle_point

        return i
