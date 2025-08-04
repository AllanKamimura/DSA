# 289. Game Of Life

[🔗 LeetCode Link](https://leetcode.com/problems/game-of-life/description/)

1. Any live cell with fewer than **two live neighbours dies**, as if by underpopulation.
2. Any live cell with **two or three live neighbours lives** on to the next generation.
3. Any live cell with **more than three live neighbours dies**, as if by overpopulation.
4. Any dead cell with **exactly three live neighbours becomes a live cell**, as if by reproduction.

## Solution

### Just do it

There is no clever solution here, it's a just do it.

#### Explanation

There is a similar caveat to [73. Set Matrix Zeroes](../0073_set-matrix-zeroes/) here.
We can't check and replace in the same loop,
otherwise we won't be able to tell apart old and new values.

Here, however, the solution for this is a lot easier,
since we know that all old value are either a 0 or a 1,
we can encode new states (2–5).

- 2: dead now, dead later
- 3: dead now, live later
- 4: live now, dead later
- 5: live now, live later

The heavy lifting is implementing the check neighbours,
since we need to handle the borders and corners.

Checking each neighbour later is pretty straightforward.

#### Manual Run

```python
board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
    ]
```

i | j | current | live_neighbors | next
-- | -- | -- | -- | --
0 | 0 | dead | 1 | dead
0 | 1 | live | 1 | dead
0 | 2 | dead | 2 | dead
1 | 0 | dead | 3 | live
1 | 1 | dead | 5 | dead
1 | 2 | live | 3 | live
2 | 0 | live | 1 | dead
2 | 1 | live | 3 | live
2 | 2 | live | 2 | live
3 | 0 | dead | 2 | dead
3 | 1 | dead | 3 | live
3 | 2 | dead | 2 | dead

#### Time Complexity

- O(n * m) -> We visit each value 2 times, the first time we check at most 8 neighbours.

#### Space Complexity

- O(1) -> Aside from the integer variables, we create a set with at most 8 (int, int) tuples.
