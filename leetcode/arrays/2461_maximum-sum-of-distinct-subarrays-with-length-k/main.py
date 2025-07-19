from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        n = len(nums)

        curr_sum = 0
        for i in range(k):
            num = nums[i]

            window[num] += 1
            curr_sum += num

        max_sum = curr_sum if len(window) == k else 0

        for i in range(k, n):
            new_num = nums[i]
            old_num = nums[i - k]

            window[new_num] += 1
            window[old_num] -= 1

            curr_sum += new_num
            curr_sum -= old_num

            if window[old_num] == 0:
                del window[old_num]

            if len(window) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
