from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # min stack (index, height)
        max_area = 0

        for i, height in enumerate(heights):
            j = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()

                max_area = max(max_area, h * (i - j))

            i = j
            stack.append((i, height))

        n = len(heights)

        while stack:
            j, h = stack.pop()
            max_area = max(max_area, h * (n - j))

        return max_area
