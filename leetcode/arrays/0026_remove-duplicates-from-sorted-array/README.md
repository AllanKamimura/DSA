# 26. Remove Duplicates From Sorted Array

[🔗 LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Solution

### Two pointers approach

#### Explanation

We start 2 pointers, left and right.
The first is going to keep track of the unique number,
while the second "explores ahead" looking for new unique values.

When a non-dupe is found, we move left 1 step
and move the new unique value there.

If the value is a dupe, we simple move ahead with right.

At the end, we add 1 to left,
since we want the lenght of a zero-index list.

#### Manual Run

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

left | right | nums | dupe?
---  | ----- | ---- | -----
0 | 1 | [0,0,1,1,1,2,2,3,3,4] | True
1 | 2 | [0,1,1,1,1,2,2,3,3,4] | False
1 | 3 | [0,1,1,1,1,2,2,3,3,4] | True
1 | 4 | [0,1,1,1,1,2,2,3,3,4] | True
2 | 5 | [0,1,2,1,1,2,2,3,3,4] | False
2 | 6 | [0,1,2,1,1,2,2,3,3,4] | True
3 | 7 | [0,1,2,3,1,2,2,3,3,4] | False
3 | 8 | [0,1,2,3,1,2,2,3,3,4] | True
4 | 9 | [0,1,2,3,4,2,2,3,3,4] | False

```python
k = left + 1
return k = 5, nums = [0,1,2,3,4]
```

#### Time Complexity

- O(n) -> We transverse the array only 1 time.

#### Space Complexity

- O(1) -> We only create integer variables
