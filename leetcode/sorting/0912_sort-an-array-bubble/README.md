# 912. Sort An Array

[🔗 LeetCode Link](https://leetcode.com/problems/sort-an-array/description/)

## Solution

### Bubble Sort

#### Explanation

The idea is to iteratively move the largest value to the end of the array.
We do this by comparing the current value to the next,
if the current is greater, we swap those.

We need at most n-1 swaps to sort the array.

#### Manual Run

```python
[5,1,1,2,0,0]
```

i | j | nums
-- | --- | ---
0 | 0 | [1,5,1,2,0,0]
0 | 1 | [1,1,5,2,0,0]
0 | 2 | [1,1,2,5,0,0]
0 | 3 | [1,1,2,0,5,0]
0 | 4 | [1,1,2,0,0,5]
1 | 0 | [1,1,2,0,0,5]
1 | 1 | [1,1,2,0,0,5]
1 | 2 | [1,1,0,2,0,5]
1 | 3 | [1,1,0,0,2,5]
2 | 0 | [1,1,0,0,2,5]
2 | 1 | [1,0,1,0,2,5]
2 | 2 | [1,0,0,1,2,5]
3 | 0 | [0,1,0,1,2,5]
3 | 1 | [0,0,1,1,2,5]
4 | 0 | [0,0,1,1,2,5]

```python
return nums = [0,0,1,1,2,5]
```

#### Time Complexity

- O(n²) -> For each value i, we do (n - i) comparisons

#### Space Complexity

- O(1) -> In place sorting.
