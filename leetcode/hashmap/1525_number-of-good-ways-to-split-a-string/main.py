from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left_counter = set()
        right_counter = Counter(s)

        result = 0

        for letter in s:
            left_counter.add(letter)
            right_counter[letter] -= 1

            if right_counter[letter] == 0:
                del right_counter[letter]

            if len(left_counter) == len(right_counter):
                result += 1

        return result
