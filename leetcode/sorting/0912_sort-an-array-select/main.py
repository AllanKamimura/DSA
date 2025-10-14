from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(n):
            curr_min_index = j
            curr_min = nums[j]

            for i in range(j, n):
                num = nums[i]

                if num < curr_min:
                    curr_min = num
                    curr_min_index = i

            nums[curr_min_index], nums[j] = nums[j], nums[curr_min_index]

        return nums
