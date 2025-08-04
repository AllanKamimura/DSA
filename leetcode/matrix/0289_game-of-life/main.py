from typing import List, Set, Tuple


class Solution:
    """
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    The problem here is similar to 0073,
    We need to know if the value is the original or the replaced.

    I think the solution is pretty straightforward, we have 2 states:
        - 0: dead
        - 1: live
    So we can just create 4 more states:
        - 2: dead now, dead later
        - 3: dead now, live later
        - 4: live now, dead later
        - 5: live now, live later
    """

    def _get_neighbours(self, i: int, j: int) -> Set[Tuple[int, int]]:
        n = self.n
        m = self.m
        neighbours = set()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ni, nj = i + dx, j + dy
                if 0 <= ni < self.n and 0 <= nj < self.m:
                    neighbours.add((ni, nj))

        return neighbours

    def _check_neighbours(self, value: int, neighbours: Set[Tuple[int, int]]) -> int:
        live_neighbour = 0

        die = False

        for x, y in neighbours:
            neighbour = self.board[x][y]

            if neighbour in self.live_states:
                live_neighbour += 1

                if live_neighbour > 3:
                    die = True
                    break

        if value == 0:
            if live_neighbour == 3:
                return 3
            else:
                return 2

        elif value == 1:
            if die or (live_neighbour < 2):
                return 4
            else:
                return 5

    def _translate(self, new_value: int) -> int:
        if new_value in self.live_next:
            return 1
        elif new_value in self.dead_next:
            return 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.dead_states = {0, 2, 3}
        self.live_states = {1, 4, 5}

        self.dead_next = {2, 4}
        self.live_next = {3, 5}

        self.n = len(board)
        self.m = len(board[0])
        self.board = board

        # First pass: encode next state
        for i in range(self.n):
            for j in range(self.m):
                value = board[i][j]
                neighbours = self._get_neighbours(i, j)

                board[i][j] = self._check_neighbours(value, neighbours)

        # Second pass: decode to final state
        for i in range(self.n):
            for j in range(self.m):
                board[i][j] = self._translate(board[i][j])

        return board
