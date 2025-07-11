# 167. Two Sum Ii Input Array Is Sorted

[🔗 LeetCode Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Solution

### Two Pointers Approach

#### Explanation

We use two pointers, `left` and `right` at the beginning and end of the array.

At each step, we compare the sum of these values with the target value.
We know that the array is sorted and that we are guaranted to find a unique solution,

If this sum is greater than the target value, we move the right pointer 1 step to the left,
and if this sum is less than the target value, we move the left pointer 1 steps to the right.

To grab the intution behind this, let's take an example situation.
`sum > target`, if left is our lowest number and when we sum it with right,
the sum is greater than the target, that means that any pair using right
is bound to be greater than the target, so we can discart it.

The same idea applies for `sum < target`.


#### Manual Run

```python
numbers = [2,7,11,15], target = 9
```

left_value | right_value | sum | compare
--- | --- | --- | ----
2 | 15 | 17 | right-=1
2 | 11 | 13 | right-=1
2 | 7 | 9 | target

```python
return [0 + 1, 1 + 1]
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
