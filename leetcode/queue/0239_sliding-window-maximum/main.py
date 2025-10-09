from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        queue = deque()

        output = []

        for i in range(n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            if queue and (i - queue[0]) >= k:
                queue.popleft()

            queue.append(i)

            if i >= (k - 1):
                output.append(nums[queue[0]])

        return output
