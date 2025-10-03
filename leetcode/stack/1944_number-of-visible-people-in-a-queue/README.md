# 1944. Number Of Visible People In A Queue

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/)

## Solution

### Monotonic Decreasing Stack

#### Explanation

The core idea is to scan the array starting from the end.

We use a monotonic stack to keep track of the heights in decreasing order.

If the current height is greater than the top of the stack, we pop from the stack.
Since all popped values are less than the current height,
these are the heights we can see.

The last height we can see can be higher than the current height,
so we need to handle this case separately.

#### Manual Run

```python
heights = [10,6,8,5,11,9]
```

height | stack | popped | output
--- | --- | ---- | ----
9 | [] | [] | [0, 0, 0, 0, 0, 0]
11 | [9] | [9] | [0, 0, 0, 0, 1, 0]
5 | [11] | | [0, 0, 0, 1, 1, 0]
8 | [11, 5] | [5] | [0, 0, 2, 1, 1, 0]
6 | [11, 8, 6] | [] | [0, 1, 2, 1, 1, 0]
10 | [11, 10] | [8, 6] | [3, 1, 2, 1, 1, 0]

#### Time Complexity

- O(n) -> We transverse the array a single time.
  - Since each value is only added and removed at most once from the stack, this is linear time.

#### Space Complexity

- O(n) -> In the worst case, the stack have n heights.
