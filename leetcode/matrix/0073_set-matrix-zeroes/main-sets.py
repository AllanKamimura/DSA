from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = set()
        zero_columns = set()

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                number = matrix[i][j]

                if number == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0

        return matrix
