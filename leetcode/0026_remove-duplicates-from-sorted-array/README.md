# 26. Remove Duplicates From Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Example 1

```shell
Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k.
```

## Example 2

```shell
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k.
```

## Constraints:

```python
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
```

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
