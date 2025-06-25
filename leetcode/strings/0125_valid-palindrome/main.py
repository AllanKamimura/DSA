import re


def remove_non_alphanumeric(s):
    return re.sub(r"[^a-zA-Z0-9]", "", s)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # converting all uppercase letters into lowercase letters
        s = remove_non_alphanumeric(s)

        start = 0
        end = len(s) - 1

        while (end - start) > 0:
            start_value = s[start]
            end_value = s[end]

            if start_value == end_value:
                start += 1
                end -= 1

            else:
                return False

        return True
