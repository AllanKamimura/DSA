from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 1
        zeros = 0

        # handles the case where the array ends before
        # we can determine the size of the substring
        nums.append(10)

        while right <= n:
            left_value = nums[left]
            right_value = nums[right]

            if left_value == 0:
                if right_value != 0:
                    zero_lenght = right - left
                    zeros += zero_lenght * (zero_lenght + 1) // 2
                    left = right

            elif right_value == 0:
                left = right

            right += 1

        return zeros
