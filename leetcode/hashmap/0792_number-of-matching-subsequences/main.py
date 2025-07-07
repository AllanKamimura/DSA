import bisect
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charmap = defaultdict(list)

        for i, char in enumerate(s):
            charmap[char].append(i)

        result = 0
        for word in words:
            prev_index = -1

            is_subsequence = True

            for char in word:
                if char not in charmap:
                    is_subsequence = False
                    break

                indices = charmap[char]
                i = bisect.bisect_right(indices, prev_index)

                if i == len(indices):
                    is_subsequence = False
                    break

                prev_index = indices[i]

            if is_subsequence:
                result += 1

        return result
