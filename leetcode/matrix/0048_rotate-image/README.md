# 48. Rotate Image

[🔗 LeetCode Link](https://leetcode.com/problems/rotate-image/description/)

## Solution

### Matrix Rotation in place

#### Explanation

First, to gather some intuition, we draw an example

```python
(0, 0), (0, 1), (0, 2), (0, 3)
(1, 0), (1, 1), (1, 2), (1, 3)
(2, 0), (2, 1), (2, 2), (2, 3)
(3, 0), (3, 1), (3, 2), (3, 3)
```

Clock-wise 90 degree rotation:

- i = j
- j = (n - 1 - i)

Rotation is a 4 elements cycle

```shell
(0, 2) → (2, 3)
↓             ↑
(1, 0) ← (3, 1)
```

How to find elements that:

- Are part of distinct cycles
- Covers all the unique cycles

Below are binary heatmaps representing which positions participate in cycles for increasing n:

```shell
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
```

The logic seems to inductive:
    for each n: solve the first row + solve the n-2 problem

#### Manual Run

```python
matrix = [
    [ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11],
    [12, 13, 14, 15]
]
n = 4
```

| Base (i,j) | 1st → | 2nd → | 3rd → | 4th (back) |
| ---------- | ----- | ----- | ----- | ---------- |
| (0,0)      | (0,3) | (3,3) | (3,0) | (0,0)      |
| (0,1)      | (1,3) | (3,2) | (2,0) | (0,1)      |
| (0,2)      | (2,3) | (3,1) | (1,0) | (0,2)      |
| (1,1)      | (1,2) | (2,2) | (2,1) | (1,1)      |


#### Time Complexity

- O(n²) -> Every element is moved once in a 4-way cycle.

#### Space Complexity

- O(1) -> In-place rotation using constant space.
