from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        found = False

        # Step 1: Find the first 0 to use its row/col as marker space
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    i_mark, j_mark = i, j
                    found = True
                    break

            if found:
                break

        if not found:
            return matrix  # no zero found, nothing to do

        # Step 2: Use i_mark row and j_mark col as marker storage
        for i in range(n):
            for j in range(m):
                if i == i_mark or j == j_mark:
                    continue

                if matrix[i][j] == 0:
                    matrix[i_mark][j] = 0
                    matrix[i][j_mark] = 0

        # Step 3: Zero rows based on j_mark
        for i in range(n):
            if (matrix[i][j_mark] == 0) and i != i_mark:
                # Don't zero the i_mark yet
                for j in range(m):
                    matrix[i][j] = 0

        # Step 4: Zero columns based on i_mark
        for j in range(m):
            if matrix[i_mark][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        # Step 5: Zero the i_mark row
        for j in range(m):
            matrix[i_mark][j] = 0

        return matrix
