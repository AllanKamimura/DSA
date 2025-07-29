class Solution:
    def minWindow(self, s: str, t: str) -> str:
        to_find = {}
        for letter in t:
            to_find[letter] = to_find.get(letter, 0) + 1

        required_matches = len(to_find)
        formed_matches = 0

        already_found = {}

        left = 0
        min_size = float("inf")

        for right, curr_letter in enumerate(s):
            if curr_letter in to_find:
                already_found[curr_letter] = already_found.get(curr_letter, 0) + 1

                if already_found[curr_letter] == to_find[curr_letter]:
                    formed_matches += 1

                while formed_matches == required_matches:
                    curr_size = right - left + 1

                    if curr_size < min_size:
                        min_size = curr_size
                        min_range = (left, right)

                    old_letter = s[left]

                    if old_letter in to_find:
                        if already_found[old_letter] == to_find[old_letter]:
                            formed_matches -= 1
                        already_found[old_letter] -= 1

                    left += 1

        if min_size == float("inf"):
            return ""

        else:
            left, right = min_range
            return s[left : right + 1]
