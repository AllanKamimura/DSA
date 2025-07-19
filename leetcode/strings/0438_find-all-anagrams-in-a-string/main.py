from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        anagram = Counter(p)
        window = Counter()

        n_s = len(s)
        n_p = len(p)

        for i in range(n_p):
            letter = s[i]
            window[letter] += 1

        indices = []
        if window == anagram:
            indices.append(0)

        for i in range(n_p, n_s):
            letter_new = s[i]
            letter_old = s[i - n_p]

            window[letter_new] += 1
            window[letter_old] -= 1

            if window[letter_old] == 0:
                del window[letter_old]

            if window == anagram:
                indices.append(i - n_p + 1)

        return indices
