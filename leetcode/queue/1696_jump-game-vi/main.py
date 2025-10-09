from collections import deque
from typing import List


class Solution:
    """
    - must stand at index 0 and end at index (n-1)
    - must always jump (1, k) steps forward
    - some spots contains negative numbers
    """

    def maxResult(self, nums: List[int], k: int) -> int:
        behind_window = deque([(0, nums[0])])  # decreasing
        n = len(nums)

        for i in range(1, n):
            score = nums[i] + behind_window[0][1]

            if i - behind_window[0][0] > (k - 1):
                behind_window.popleft()

            while behind_window and behind_window[-1][1] < score:
                behind_window.pop()

            behind_window.append((i, score))

        return behind_window[-1][1]
