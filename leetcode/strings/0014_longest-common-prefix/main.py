from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        common = ""
        stop = False

        while not stop:
            string = strs[0]

            if i >= len(string):
                return common

            letter = string[i]

            for string in strs:
                if i >= len(string):
                    return common

                if string[i] != letter:
                    return common

            i += 1
            common += letter
