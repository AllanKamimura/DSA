from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_frequency = defaultdict(int)
        sum_frequency[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            sum_frequency[curr_sum] += 1

            diff = curr_sum - k
            count += sum_frequency[diff]

        return count
