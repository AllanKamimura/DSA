from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        objective = len(nums) - 1

        back_step = 1

        while objective > 0:
            if (objective - back_step) < 0:
                return False

            prev_step = nums[objective - back_step]

            if prev_step >= back_step:
                objective -= back_step
                back_step = 1
            else:
                back_step += 1

        return True
