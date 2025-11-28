from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i, -1, -1):
                if i == j:
                    pass
                elif nums[i] < nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i = j
                else:
                    break

        return nums
