# 303. Range Sum Query Immutable

[🔗 LeetCode Link](https://leetcode.com/problems/range-sum-query-immutable/description/)

## Solution

### Prefix Sum Array

#### Explanation

Sometimes called cumsum, the prefix sum is the cummulative sum of an array,
in such a way that cumsum[i] is the sum of all values from [0:i].

#### Time Complexity

- O(n) -> To find subarrays sum.

#### Space Complexity

- O(1) -> Inplace array.
- O(n) -> We create an array of same size as input.
