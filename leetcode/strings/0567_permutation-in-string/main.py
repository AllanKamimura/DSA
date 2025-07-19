from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        window = Counter()

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        for i in range(n1):
            letter = s2[i]
            window[letter] += 1

        if count1 == window:
            return True

        for i in range(n1, n2):
            new_letter = s2[i]
            old_letter = s2[i - n1]

            window[new_letter] += 1
            window[old_letter] -= 1

            if window[old_letter] == 0:
                del window[old_letter]

            if count1 == window:
                return True

        return False
