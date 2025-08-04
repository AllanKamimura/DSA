# 73. Set Matrix Zeroes

[🔗 LeetCode Link](https://leetcode.com/problems/set-matrix-zeroes/description/)

## Solution

### Hashset

#### Explanation

The tricky part in this problem is that:

- If we first check the zeros and replace later,
we are going to increase the memory used.
- If we check for zeros and replace the zeros at the same time,
we don't have a way to know if a zero was originally there or we just replaced it.

Iterate over the array,
and use a hashset to keep track of the rows and cols to be zeroed.

#### Manual Run

```python
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
```

number | zero_rows | zero_cols
--- | --- | ----
0 | {0} | {0}
1 | {0} | {0}
2 | {0} | {0}
0 | {0} | {0, 3}
3 | {0} | {0, 3}
4 | {0} | {0, 3}
5 | {0} | {0, 3}
2 | {0} | {0, 3}
1 | {0} | {0, 3}
3 | {0} | {0, 3}
1 | {0} | {0, 3}
5 | {0} | {0, 3}

#### Time Complexity

- O(n * m) -> We visit each value 2 times.

#### Space Complexity

- O(n + m) -> In the worst case, we need to replace all rows and all cols.

### Strange Character Marker

#### Explanation

Iterate over the array,
and when we find one, we mark its entire row and column for zeroing.

This way, we use the matrix itself to keep track of the to be replaced.
And since we have an integer matrix,
we can use a stranger character like 'x',
to ensure we won't conflict with any 0s.

One point of attention is that we are mixing different types inside the array.

#### Manual Run

```python
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
```

number | matrix
--- | ---
0 | [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
0 | [[0,x,2,0],[3,4,5,2],[1,3,1,5]]
0 | [[0,x,x,0],[3,4,5,2],[1,3,1,5]]
0 | [[0,x,x,0],[x,4,5,2],[1,3,1,5]]
0 | [[0,x,x,0],[x,4,5,x],[1,3,1,5]]
0 | [[0,x,x,0],[x,4,5,x],[x,3,1,5]]
1 | [[0,x,x,0],[x,4,5,x],[x,3,1,5]]
2 | [[0,x,x,0],[x,4,5,x],[x,3,1,5]]
0 | [[0,x,x,0],[x,4,5,x],[x,3,1,5]]
0 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
3 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
4 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
5 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
2 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
1 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
3 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
1 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]
5 | [[0,x,x,0],[x,4,5,x],[x,3,1,x]]

#### Time Complexity

- O(n * m * (n + m)) -> For each 0, we scan all rows and columns.

#### Space Complexity

- O(1) -> We use the matrix itself to mark the zeros.

### Zero point marker

#### Explanation

The main problem is to know if a zero is part of the original,
or was replaced by our algorithm.

Once we find a 0, we know for sure its row and column will be zeroed in the final output.
We can therefore safely use it's row to mark which columns to zero,
and it's column to mark which rows to zero.

This special zero, the "zero point marker",
is used as a reference coordinate (i_mark, j_mark) that acts as a pivot for tracking the zeroing operations.

#### Manual Run

```python
matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13,14,15, 0]
]
i_mark, j_mark = 1, 1
```

🖊️ Marking

(i,j) | matrix
--- | ---
... | ...
(3,3) | [1, 2, 3, 4],<br>[5, 0, 7, 0],<br>[9, 10, 11, 12],<br>[13, 0, 15, 0]

🔁 Replace rows

(i,j) | matrix
--- | ---
... | ...
(1,1) | i = i_mark
(3,1) | [1, 2, 3, 4],<br>[5, 0, 7, 0],<br>[9, 10, 11, 12],<br>[0, 0, 0, 0]

🔁 Replace columns

(i,j) | matrix
--- | ---
... | ...
(1,1) | [1, 0, 3, 4],<br>[5, 0, 7, 0],<br>[9, 0, 11, 12],<br>[0, 0, 0, 0]
(1,3) | [1, 0, 3, 0],<br>[5, 0, 7, 0],<br>[9, 0, 11, 0],<br>[0, 0, 0, 0]

🔁 Replace the i_mark row

(i,j) | matrix
--- | ---
... | ...
(1,1) | [1, 0, 3, 0],<br>[0, 0, 0, 0],<br>[9, 0, 11, 0],<br>[0, 0, 0, 0]

#### Time Complexity

- O(n * m) -> We visit each value 2 times.

#### Space Complexity

- O(1) -> We use the matrix itself to mark the rows/cols to be zeroed.