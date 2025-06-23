from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # this handles the case where k > len(nums)
        k %= len(nums)

        if len(nums) > 1 and k != 0:
            nums[:] = nums[-k:] + nums[: len(nums) - k]
        return nums
