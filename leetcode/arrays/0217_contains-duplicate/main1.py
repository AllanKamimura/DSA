from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for num in nums:
            count = counter.get(num, 0)
            if count == 1:
                return True

            counter[num] = count + 1

        return False
