from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter_list = [0]

        for number in range(1, n + 1):
            counter_list.append(counter_list[number >> 1] + (number & 1))

        return counter_list
