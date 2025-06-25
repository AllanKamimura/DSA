class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        len_s = len(s)
        len_t = len(t)

        for j in range(len_t):
            if i >= len_s:
                break

            s_value = s[i]
            t_value = t[j]

            if s_value == t_value:
                i += 1

        if i == len_s:
            return True
        else:
            return False
