# 53. Maximum Subarray

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-subarray/description/)

## Solution

### Prefix Sum 

#### Explanation

Using the prefix sum property that the sum of elements from i to j (inclusive) inclusive
`prefix_sum[j+1] - prefix_sum[i]`.

Since we are looking to maximize this difference,
we want to always use the smallest `prefix_sum[i]` found so far.

So we keep track of 2 numbers,
the `max_diff`, for the maximum sum of elements from i to j.
And `min_sum`, for the minimum `prefix_sum[i]`.

#### Manual Run

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

num | curr_sum | max_diff | min_sum
-- | -- | --- | ---
-2 | -2 | -2 | -2
 1 | -1 |  1 | -2
-3 | -4 |  1 | -4
 4 |  0 |  4 | -4
-1 | -1 |  4 | -4
 2 |  1 |  5 | -4
 1 |  2 |  6 | -4
-5 | -3 |  6 | -4
 4 |  1 |  6 | -4

```python
return max_diff = 6
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.

### Kadane's Algorithm

#### Explanation-2

The Kadane's Algorithm is very simple.

We iterate over the array
and compute the current subarray sum.

If this sum is positive, we increase the subarray,
if it's negative, we start a new subarray at the current position.

#### Manual Run-2

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

num | curr_sum | max_sum
-- | -- | ---
-2 | -2 | -2
 1 |  1 |  1
-3 | -2 |  1
 4 |  4 |  4
-1 |  3 |  4
 2 |  5 |  5
 1 |  6 |  6
-5 |  1 |  6
 4 |  5 |  6

```python
return max_sum = 6
```

#### Time Complexity-2

- O(n) -> We transverse the array a single time.

#### Space Complexity-2

- O(1) -> We only create integer variables.