from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        end_at = defaultdict(list)

        for num in nums:
            if end_at[num - 1]:
                prev_len = heappop(end_at[num - 1])
                heappush(end_at[num], prev_len + 1)

            else:
                heappush(end_at[num], 1)

        for heap in end_at.values():
            if heap and heap[0] < 3:
                return False

        return True
