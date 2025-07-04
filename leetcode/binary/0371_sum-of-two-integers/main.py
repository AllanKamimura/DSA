class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        digit_c = 0

        for i in range(32):
            digit_a = (a >> i) & 1
            digit_b = (b >> i) & 1

            result |= (digit_a ^ digit_b ^ digit_c) << i

            if (digit_a and digit_c) or (digit_b and digit_c) or (digit_a and digit_b):
                digit_c = 1

            else:
                digit_c = 0

        if result > (1 << 31):
            result -= 1 << 32

        return result
