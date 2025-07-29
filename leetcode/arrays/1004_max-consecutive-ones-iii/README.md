# 1004. Max Consecutive Ones Iii

[🔗 LeetCode Link](https://leetcode.com/problems/max-consecutive-ones-iii/description/)

## Solution

### Sliding Window with Dynamic size

#### Explanation

This problem is actually very simple.
We just need to know how many zeros are in the window.
And compare it with our flip budget.

So for each num,
if num is zero, we increase our zero_counter,
if zero_counter > k,
we remove elements from the left until we return to a valid window.

#### Manual Run

```python
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
```

left | right | num | zero_counter | curr_size 
--- | --- | --- | --- | ---
0 | 0 | 1 | 0 | 1
0 | 1 | 1 | 0 | 2
0 | 2 | 1 | 0 | 3
0 | 3 | 0 | 1 | 4
0 | 4 | 0 | 2 | 5
0 | 5 | 0 | 3 | 5*
1 | 5 | 0 | 3 | 5
2 | 5 | 0 | 3 | 4
3 | 5 | 0 | 3 | 3
4 | 5 | 0 | 2 | 2
4 | 6 | 1 | 2 | 3
4 | 7 | 1 | 2 | 4
4 | 8 | 1 | 2 | 5
4 | 9 | 1 | 2 | 6
4 | 10 | 0 | 3 | 6*
5 | 10 | 0 | 2 | 6

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
