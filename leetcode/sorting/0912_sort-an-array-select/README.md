# 912. Sort An Array

[🔗 LeetCode Link](https://leetcode.com/problems/sort-an-array/description/)

## Solution

### Select Sort

#### Explanation

The idea is to scan the array looking for the minimum value,
then we move it to the start of the array,
and move the search space 1 step to the right.

We do this iteratively, n times,
and at the end we have the array sorted.

#### Manual Run

```python
nums = [5,1,1,2,0,0]
```

index | min | nums
--- | --- | ---
0 | 0 | [0,1,1,2,5,0]
1 | 0 | [0,0,1,2,5,1]
2 | 1 | [0,0,1,2,5,1]
3 | 1 | [0,0,1,1,5,2]
4 | 2 | [0,0,1,1,2,5]
5 | 5 | [0,0,1,1,2,5]

```python
return nums = [0,0,1,1,2,5]
```

#### Time Complexity

- O(n²) -> We scan the array looking for the minimum n times.
  
#### Space Complexity

- O(1) -> In-place sorting.
