class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2**31

        if x < 2:
            return x

        while (right - left) > 1:
            mid = (left + right) // 2

            if mid < (x // mid):
                left = mid

            elif mid > (x // mid):
                right = mid

            else:
                return mid

        return left
