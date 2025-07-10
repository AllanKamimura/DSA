# 88. Merge Sorted Array

[🔗 LeetCode Link](https://leetcode.com/problems/merge-sorted-array/description/)

## Solution

### Three points approach

#### Explanation

We initialize 3 points,
`first` at the end of the nums1 sequence, 
`second` at the end of the nums2 array,
`curr_index` to keep track of the current index in nums1.

We then transverse both arrays starting from the end.
Compare `first_value` and `second_value`.
And swap `nums1[curr_index]` with the greater one.

We do this until either first or second reaches the start of their array.

If `second` reaches the start before `first`,
then all remaining numbers in nums1 are already going to be in the correct order.

If `first` reaches it before `second`,
then we just need to fill the rest of index with the values from nums2.

#### Manual Run

```python
nums1 = [2,2,3,0,0,0], nums2 = [1,5,6]
```

curr_index | first_value | second_value | nums1
--- | --- | --- | ---
5   |   3 | 6   | [2,2,3,0,0,6]
4   |   3 | 5   | [2,2,3,0,5,6]
3   |   3 | 1   | [2,2,3,3,5,6]
2   |   2 | 1   | [2,2,2,3,5,6]
1   |   2 | 1   | [2,2,2,3,5,6]
break 
0   |   2 | 1   | [1,2,3,3,5,6]

#### Time Complexity

- O(n + m) -> We transverse each array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
