from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}

        for i, x in enumerate(nums):
            y = target - x

            if y in number_map:
                j = number_map[y]

                return [j, i]

            number_map[x] = i
