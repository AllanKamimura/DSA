# 209. Minimum Size Subarray Sum

[🔗 LeetCode Link](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

## Solution

### Sliding Window

#### Explanation

We use a sliding window with dynamic size to compute the sum in the subarray.

We move the window to the right, step by step, and accumulate the sum.

If the sum is greater or equal than the target,
we keep track of the window's size,
and shrink the window size (from the left),
to see if we can achieve an even smaller window.

#### Manual Run

```python
nums = [2,3,1,2,4,3]
target = 7
```

left | right | num | curr_sum | min_size
--- | --- | --- | --- | ---
0 | 0 | 2 | 2 | inf
0 | 1 | 3 | 5 | inf
0 | 2 | 1 | 6 | inf
0 | 3 | 2 | 8 | 4
1 | 3 | 2 | 6 | 4
1 | 4 | 4 | 10 | 4
2 | 4 | 4 | 7 | 3
3 | 4 | 4 | 6 | 3
3 | 5 | 3 | 9 | 3
4 | 5 | 3 | 7 | 2

```python
return min_size = 2
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
