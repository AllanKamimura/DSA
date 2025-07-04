from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = nums[0]

        for i in range(1, len(nums)):
            result ^= nums[i]

        for i in range(32):
            if (result >> i) & 1:
                print(i)
                break

        num1 = 0
        num2 = 0

        for num in nums:
            if (num >> i) & 1:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
