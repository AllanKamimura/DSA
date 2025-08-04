from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        MARKER = int(1e9 + 7)

        for i in range(n):
            for j in range(m):
                number = matrix[i][j]

                if number == 0:
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = MARKER
                    for l in range(m):
                        if matrix[i][l] != 0:
                            matrix[i][l] = MARKER

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == MARKER:
                    matrix[i][j] = 0

        return matrix
