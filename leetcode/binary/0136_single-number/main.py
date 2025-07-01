from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]

        for num in nums[1:]:
            single ^= num

        return single
