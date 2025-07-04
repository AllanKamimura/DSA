class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        if len(t) != n:
            return False

        translate = {}
        back_translate = {}

        for i in range(n):
            s_letter = s[i]
            t_letter = t[i]

            if s_letter in translate.keys():
                if t_letter != translate[s_letter]:
                    return False
            else:
                translate[s_letter] = t_letter

            if t_letter in back_translate.keys():
                if s_letter != back_translate[t_letter]:
                    return False
            else:
                back_translate[t_letter] = s_letter

        return True
