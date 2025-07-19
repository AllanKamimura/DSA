# 2461. Maximum Sum Of Distinct Subarrays With Length K

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/)

## Solution

### Sliding window + Frequency hashmap

#### Explanation

We use a hashmap to keep track of the occurences of each value in the window of size k.

We use a variable curr_sum to keep track of the sum in the window.
For each step, we add/subtract the new/old value.

The caveat it to only update the max_sum when the hashmap has k distinct elements.

#### Manual Run

```python
nums = [1,5,4,2,9,9,9], k = 3
window = {1: 1, 5: 1, 4: 1}
curr_sum = 10
max_sum = 10
```

num | window | curr_sum | max_sum
-- | -- | -- | --
2 | {2: 1, 5: 1, 4: 1} | 11 | 11
9 | {2: 1, 9: 1, 4: 1} | 15 | 15
9 | {1: 1, 9: 2} | 19 | 15
9 | {9: 3} | 27 | 15

```python
return max_sum = 15
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(k) -> Window has at most k elements.
