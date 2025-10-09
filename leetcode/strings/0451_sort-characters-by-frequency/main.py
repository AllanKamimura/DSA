from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        output = ""

        for letter, repetitions in sorted(
            counter.items(), key=lambda item: -1 * item[1]
        ):
            output += (letter) * repetitions

        return output
