# 918. Maximum Sum Circular Subarray

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-sum-circular-subarray/description/)

## Solution

### Kadane's Algorithm

#### Explanation

This problem is similar to [53. Maximum Subarray](../0053_maximum-subarray/),
but here, there's 2 subarray types:

1, start < end (normal case)
2. start > end (the subarray goes a full loop)

The catch here is how to use Kadane's Algorithm to get a sum candidate in the second case.

The trick is to use Kadane's to actually compute the minimum subarray,
because that way, the rest of the array is actually going to be the maximum
looped array.

One simple way to see this. The total sum of the array is fixed.

Total = x + y

If x is the sum of the minimum subarray,
in another words, if x is the smallest possible,
y must be the grates looped subarray sum.

One edge case is when all numbers are negatives,
so we can fall into the case where x = Total and y = 0.

#### Manual Run

```python
nums = [9,-4,-7,9]
```

num | curr_sum | max_sum | curr_sum_negative | min_sum | total
--- | --- | --- | --- | --- | ---
9 | 9 | 9 | 9 | 9 | 9
-4 |5 | 9 | -4 | -4 | 5
-7 | -2 | 9 | -11 | -11 | -2
9 | 7 | 9 | -2 | -11 | 7

```python
max_sum = 9
total - min_sum = 7 - (-11) = 18

return max(max_sum, total - min_sum) = 18
```

#### Time Complexity

- O(n) -> We traverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
