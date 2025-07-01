from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter_list = []

        for number in range(n + 1):
            counter_list.append(self.hammingWeight(number))

        return counter_list

    def hammingWeight(self, n: int) -> int:
        counter = 0

        for i in range(32):
            counter += (n >> i) & 1

        return counter
