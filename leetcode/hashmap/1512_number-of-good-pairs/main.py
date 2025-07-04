from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)

        result = 0
        for val in counter.values():
            result += val * (val - 1) // 2

        return result
