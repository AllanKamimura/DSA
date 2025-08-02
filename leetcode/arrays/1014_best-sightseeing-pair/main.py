from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        start_index = 0
        start_value = values[start_index]

        max_result = 0

        for i in range(1, len(values)):
            curr_value = values[i]

            curr_result = start_value + start_index + curr_value - i

            if curr_result > max_result:
                max_result = curr_result

            if (curr_value + i) > (start_value + start_index):
                start_value = curr_value
                start_index = i

        return max_result
