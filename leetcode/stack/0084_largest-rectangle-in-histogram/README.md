# 84. Largest Rectangle In Histogram

[🔗 LeetCode Link](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

## Solution

### Monotonic Increasing Stack

#### Explanation

The core idea is to use an increasing monotonic stack to keep track of the heights. 
Each element is going to be a tuple of (index, height).

- If the new height is greater than the top of the stack,
we append it. This means that we can extent the rectangle with height = "top of the stack" one width to the right.
- If the new height is smaller, it means that we can't extent the current rectangle to the right, but we can extent the new rectangle to the left.

For example:

```python
heights = [2,1,5,6,2,3]
```

- index = 1: since `heights[1]=1 < 2`,
this means we can't extent the rectangle with `height=2` to the right,
but we can extend the rectangle with `height=1` to the left.
- index = 2: since `heights[2]=5 > 1`,
this means we can extent the rectangle with `height=1` to the right.

#### Manual Run

```python
heights = [2,1,5,6,2,3]
```

index | height | stack | max_area
--- | -- | --- | ----
0 | 2 | [(0, 2)] | 0
1 | 1 | [(0, 1)] | 2
2 | 5 | [(0, 1), (2, 5)] | 2
3 | 6 | [(0, 1), (2, 5), (3, 6)] | 2
4 | 2 | [(0, 1), (4, 2)] | 10
5 | 3 | [(0, 1), (4, 2), (5, 3)] | 10

#### Time Complexity

- O(n) -> We transverse the array a single time.
  - Since each value is only added and removed at most once from the stack, this is linear time.

#### Space Complexity

- O(n) -> In the worst case, the stack have n heights.
