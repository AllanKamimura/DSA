# 1438. Longest Continuous Subarray With Absolute Diff Less Than Or Equal To Limit

[🔗 LeetCode Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/)

## Solution

### Monotonic Increasing/Decreasing Deque

#### Explanation

The core idea is to use 2 monotonic deques
to keep track of the indices of the min/max values as well as the next candidates.

- `increase`: keeps indices of elements in increasing order (for minimum)
- `decrease`: keeps indices of elements in decreasing order (for maximum)

The idea is that we can get the maximum absolute difference
looking only at the min and max values in the current window.

We use this with a sliding window that defines the subarray size.

#### Manual Run

```python
nums = [10,1,2,4,7,2], limit = 5
```

right | num | increase_pop (value) | decrease_pop (value) | left | increase_popleft (value) | decrease_popleft (value) | window
--- | --- | --- | --- | --- | ---- | --- | ----
0 | 10 | [10] | [10] | 0 |  [10] | [10] | [10]
1 | 1 | [1] | [10, 1] | 1 | [1] | [1] | [1]
2 | 2 | [1, 2] | [2] | 1 | [1, 2] | [2] | [1, 2]
3 | 4 | [1, 2, 4] | [4] | 1 | [1, 2, 4] | [4] | [1, 2, 4]
4 | 7 | [1, 2, 4, 7] | [7] | 2 | [2, 4, 7] | [7] | [2, 4, 7]
5 | 2 | [2, 2] | [7, 2, 2] | 2 | [2, 2] | [7, 2, 2] | [2, 4, 7, 2]

```python
return max_window = 4
```

#### Time Complexity

- O(n) -> each element is inserted and removed at most once (for each queue).

#### Space Complexity

- O(n) -> In the worst case, we have n elements in the queue
