# 239. Sliding Window Maximum

[🔗 LeetCode Link](https://leetcode.com/problems/sliding-window-maximum/description/)

## Solution

### Decreasing Monotonic Queue

#### Explanation

The core idea is to use a queue to keep track of valid max candidates.
We use a decreasing queue because when we find a number greater than the top of the queue,
all the numbers before can't be the maximum of the window.

We also need to keep track of the index of the number in the queue,
since we need to left pop the numbers after the window passes.

Since we are using a decreasing queue,
the max value of the window is the first element in the queue.

#### Manual Run

```python
nums = [1,3,-1,-3,5,3,6,7], k = 3
```

index | queue | output
--- | --- | ----
0 | [1] | []
1 | [3] | []
2 | [3, -1] | [3]
3 | [3, -1, -3] | [3, 3]
4 | [5] | [3, 3, 5]
5 | [5, 3] | [3, 3, 5, 5]
6 | [6] | [3, 3, 5, 5, 6]
7 | [7] | [3, 3, 5, 5, 6, 7]

#### Time Complexity

- O(n) -> We append and pop each value only 1 time.

#### Space Complexity

- O(n) -> In the worst case, the queue holds n elements.