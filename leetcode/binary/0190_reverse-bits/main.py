class Solution:
    def reverseBits(self, n: str) -> int:
        num = int(n, 2)

        reverse = 0
        for i in range(len(n)):
            reverse = (reverse << 1) | (num & 1)
            num >>= 1
        return reverse
