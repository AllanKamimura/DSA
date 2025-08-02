from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_start = values[0]
        max_result = float("-inf")

        for j in range(1, len(values)):
            max_result = max(max_result, (best_start + values[j] - j))
            best_start = max(best_start, values[j] + j)

        return max_result
