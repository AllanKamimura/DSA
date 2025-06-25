from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = []

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        prefix.pop()
        product = 1
        for num in nums[::-1]:
            product *= num
            suffix.append(product)

        suffix.reverse()
        suffix.pop(0)
        suffix.append(1)

        output = [prefix[i] * suffix[i] for i in range(len(nums))]

        return output
