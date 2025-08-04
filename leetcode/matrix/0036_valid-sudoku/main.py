import math
from typing import List


class Solution:
    """
    Use 27 sets (9 rows, 9 cols, 9 boxes) to keep track of numbers.

    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        l = int(math.sqrt(n))
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxs = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # box index
                k = (i // l) + l * (j // l)

                row = rows[i]
                col = cols[j]
                box = boxs[k]

                number = board[i][j]

                if not number.isalnum():
                    continue

                if (number in row) or (number in col) or (number in box):
                    return False

                row.add(number)
                col.add(number)
                box.add(number)

        return True
