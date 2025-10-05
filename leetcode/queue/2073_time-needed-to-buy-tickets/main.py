from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        target = tickets[k]

        for i in range(len(tickets)):
            curr = tickets[i]

            if i <= k:
                counter += min(target, curr)
            else:
                counter += min(target - 1, curr)

        return counter
