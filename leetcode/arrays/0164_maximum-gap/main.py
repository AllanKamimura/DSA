import math
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_gap = 0

        if len(nums) < 2:
            return max_gap

        min_value = min(nums)
        max_value = max(nums)

        range_ = max_value - min_value

        bucket_size = max(1, math.ceil(range_ / (len(nums) - 1)))
        n_buckets = range_ // bucket_size + 1

        buckets = {i: [] for i in range(n_buckets)}

        for num in nums:
            bucket_index = (num - min_value) // bucket_size

            buckets[bucket_index].append(num)

        prev_max = min_value

        for i in range(n_buckets):
            if buckets[i]:
                max_gap = max(max_gap, min(buckets[i]) - prev_max)

                prev_max = max(buckets[i])

        return max_gap
