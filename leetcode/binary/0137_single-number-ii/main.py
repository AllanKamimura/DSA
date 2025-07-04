from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n_bits = 32
        digit_counter = [0] * n_bits

        result = 0

        for i in range(n_bits):
            for num in nums:
                digit_counter[i] += (num >> i) & 1

            if digit_counter[i] % 3 == 1:
                result |= 1 << i

        if result >= 1 << 31:
            result -= 1 << 32

        return result
