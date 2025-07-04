from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_at = {}

        for i, num in enumerate(nums):
            if num in last_seen_at:
                if i - last_seen_at[num] <= k:
                    return True
                else:
                    last_seen_at[num] = i
            else:
                last_seen_at[num] = i

        return False
