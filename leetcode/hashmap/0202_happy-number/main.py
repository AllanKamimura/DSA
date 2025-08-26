class Solution:
    squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

    def sum_of_squares(self, n: int) -> int:
        num = n
        sum_ = 0

        while num:
            num, digit = divmod(num, 10)
            sum_ += self.squares[digit]

        return sum_

    def isHappy(self, n: int) -> bool:
        seen = set()

        curr_num = n

        while True:
            curr_sum = self.sum_of_squares(curr_num)

            if curr_sum == 1:
                return True

            if curr_sum in seen:
                return False

            seen.add(curr_sum)

            curr_num = curr_sum
