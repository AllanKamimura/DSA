class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        for i in range(32):
            counter += (n >> i) & 1

        return counter
