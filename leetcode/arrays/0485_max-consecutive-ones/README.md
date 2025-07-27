# 485. Max Consecutive Ones

[🔗 LeetCode Link](https://leetcode.com/problems/max-consecutive-ones/description/)

## Solution

### Just count it

#### Explanation

We iterate over the array,
if the number is an 1,
we increase our current counter
and check if it's greater than our max_tracker,
if the number is a 0,
we reset the counter.

#### Manual Run

```python
nums = [1,1,0,1,1,1]
```

num | curr_size | max_size
-- | -- | --
1 | 1 | 1
1 | 2 | 2
0 | 0 | 2
1 | 1 | 2
1 | 2 | 2
1 | 3 | 3

```python
return max_size = 3
```


#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
