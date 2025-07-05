from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_index = defaultdict(list)

        for i, word in enumerate(strs):
            alphabet = [0] * 26

            for letter in word:
                index = ord(letter) - ord("a")
                alphabet[index] += 1

            key = tuple(alphabet)

            anagram_index[key].append(i)

        anagram_groups = [
            [strs[indice] for indice in x] for x in anagram_index.values()
        ]
        return anagram_groups
