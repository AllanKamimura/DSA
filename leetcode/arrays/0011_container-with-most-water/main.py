from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        max_area = 0

        while (right - left) > 0:
            left_value = height[left]
            right_value = height[right]

            curr_area = (right - left) * min(right_value, left_value)

            if curr_area > max_area:
                max_area = curr_area

            if right_value > left_value:
                left += 1
            else:
                right -= 1

        return max_area
