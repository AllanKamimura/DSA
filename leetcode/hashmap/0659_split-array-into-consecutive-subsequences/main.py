from collections import Counter, defaultdict
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        end_at = defaultdict(int)

        for num in nums:
            if count[num] == 0:
                continue

            count[num] -= 1

            if end_at[num - 1] > 0:
                end_at[num - 1] -= 1
                end_at[num] += 1

            elif (count[num + 1] > 0) and (count[num + 2] > 0):
                count[num + 1] -= 1
                count[num + 2] -= 1
                end_at[num + 2] += 1

            else:
                return False

        return True
