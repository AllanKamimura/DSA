from typing import List


class Solution:
    """
    1. Each rotation consists of 4 elements that are cyclically moved.
        1. Ex: (0, 2) -> (2, 3) -> (3, 1) -> (1, 0)
    2. Mathematically, the rotation does
        1. Column to row
        2. Row to (n - 1 - i)
    3. Partial matrix that:
        1. Are part of distinct cycles
        2. Covers all the unique cycles

        [1, 0]
        [0, 0]

        [1, 1, 0]
        [0, 1, 0]
        [0, 0, 0]

        [1, 1, 1, 0]
        [0, 1, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]

        [1, 1, 1, 1, 0]
        [0, 1, 1, 0, 0]
        [0, 0, 1, 0, 0]
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]

        The logic seems to inductive:
            for each n: solve the first row + solve the n-2 problem
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n - 1):
            for j in range(i, n - 1 - i):
                i_new, j_new = i, j
                first_value = matrix[i_new][j_new]

                for _ in range(4):
                    i_new, j_new = j_new, (n - 1 - i_new)
                    curr_value = matrix[i_new][j_new]
                    matrix[i_new][j_new] = first_value
                    first_value = curr_value

        return matrix
