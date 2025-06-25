from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        left = 0
        center = 1
        right = 2

        while center < n - 1:
            left_value = nums[left]
            center_value = nums[center]
            right_value = nums[right]

            if left_value < center_value:
                if center_value < right_value:
                    return True

                elif right == (n - 1):
                    center += 1
                    right = center + 1
                    left = 0

                else:
                    right += 1

            else:
                if left < center - 1:
                    left += 1
                else:
                    center += 1
                    right = center + 1

        return False
