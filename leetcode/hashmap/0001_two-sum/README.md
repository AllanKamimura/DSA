# 1. Two Sum

[🔗 LeetCode Link](https://leetcode.com/problems/two-sum/description/)

## Solution

### Hashmap counter

#### Explanation

We want to find two numbers that:

x + y = target => y = target - x

The first idea is to use a hashmap,
so we can have a quick look-up given a value.

So we iterate nums, and for each x in nums,
we look-up for the corresponding y value,
if we don't find it, just store the x value and index.

Since we are guaranteed that the pair exists,
we are going to eventually find y.

#### Manual Run

```python
Input: nums = [0,4,3,0], target = 0
```

x | y | number_map
-- | -- | --
0 | 0 | {0: 0}
4 | -4 | {0: 0, 4: 1}
3 | -3 | {0: 0, 4: 1, 3: 2}
0 | 0 | Found

```python
return [i, j] = [0, 3]
```

#### Time Complexity

- O(n) -> We transverse the array a single times.

#### Space Complexity

- O(n) -> In worst case, counter has the same size as nums.
