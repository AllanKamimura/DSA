from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_seen_at = {0: -1}
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            curr_mod = curr_sum % k

            if curr_mod in mod_seen_at:
                j = mod_seen_at[curr_mod]
                if (i - j) > 1:
                    return True
            else:
                mod_seen_at[curr_mod] = i

        return False
