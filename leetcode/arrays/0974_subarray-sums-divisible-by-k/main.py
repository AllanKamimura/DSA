from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_frequency = defaultdict(int)
        mod_frequency[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            curr_mod = curr_sum % k
            count += mod_frequency[curr_mod]
            mod_frequency[curr_mod] += 1

        return count
