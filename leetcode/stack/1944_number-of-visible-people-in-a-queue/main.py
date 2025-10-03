from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        output = [0] * n

        for i in range(n - 1, -1, -1):
            height = heights[i]

            while stack and stack[-1] < height:
                output[i] += 1
                stack.pop()

            if stack:
                output[i] += 1

            stack.append(height)

        return output
