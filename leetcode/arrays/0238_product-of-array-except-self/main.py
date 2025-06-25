from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        outputs = [1]

        for num in nums:
            product *= num

            outputs.append(product)

        outputs.pop()

        product = 1

        for i in range(-1, -n - 1, -1):
            num = nums[i]

            outputs[i] *= product
            product *= num

        return outputs
