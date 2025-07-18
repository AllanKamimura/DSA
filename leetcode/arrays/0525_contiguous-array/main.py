from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        prefix_index = {0.5: -1}
        max_size = 0

        for j, num in enumerate(nums):
            sum += num

            prefix_comp = sum - (j) / 2

            if prefix_comp in prefix_index:
                i = prefix_index[prefix_comp]

                curr_size = j - i

                if curr_size > max_size:
                    max_size = curr_size
            else:
                prefix_index[prefix_comp] = j

        return max_size
