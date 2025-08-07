from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subsets = [curr + [num] for curr in result]
            result.extend(new_subsets)
        return result
