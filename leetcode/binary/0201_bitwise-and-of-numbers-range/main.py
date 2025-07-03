class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        for i in range(32):
            if right != left:
                right >>= 1
                left >>= 1
            else:
                return left << i
