class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)

        i = 0
        j = len(x_str) - 1

        while i < j:
            left = x_str[i]
            right = x_str[j]

            if left != right:
                return False

            else:
                i += 1
                j -= 1

        return True
