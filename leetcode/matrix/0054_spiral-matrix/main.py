from typing import List


class Solution:
    """ "
    The first thing to notice is the spin direction
        - [right, down, left, up]
        - we can use something like index = wheel % 4
    Second point is to define the boundaries to change direction
        left | top | right | bottom
        0    |  0  | n_columns - 1 | n_rows - 1
    So the core logic is to update (i, j) index
    using the current direction and checking the boundaries
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_rows = len(matrix)
        n_columns = len(matrix[0])

        # right, down, left, up
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        top, bottom = 0, n_rows - 1
        left, right = 0, n_columns - 1

        i, j = 0, 0
        steering_wheel = 0
        results = []

        for _ in range(n_columns * n_rows):
            results.append(matrix[i][j])

            di, dj = directions[steering_wheel]

            new_i = i + di
            new_j = j + dj

            match steering_wheel:
                case 0:  # moving right
                    if new_j > right:
                        steering_wheel = 1  # turn down
                        top += 1
                case 1:  # moving down
                    if new_i > bottom:
                        steering_wheel = 2  # turn left
                        right -= 1
                case 2:  # moving left
                    if new_j < left:
                        steering_wheel = 3  # turn up
                        bottom -= 1
                case 3:  # moving up
                    if new_i < top:
                        steering_wheel = 0  # turn right
                        left += 1

            # Update direction and move
            di, dj = directions[steering_wheel]
            i += di
            j += dj

        return results
