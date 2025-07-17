# 523. Continuous Subarray Sum

[🔗 LeetCode Link](https://leetcode.com/problems/continuous-subarray-sum/description/)

## Solution

### Hashmap tracker

#### Explanation

The core idea is very similar to [Subarray Sums Divisible By K](../0974_subarray-sums-divisible-by-k/).

The caveat here is there is that, we require a subarray in which its length is at least two.

Instead of counting the occurences of each modulo,
we keep track of the index position it first shows.

So our problem is to find two values in the prefix sum array,
with the same modulo,
and we want index (j - i) > 1,
so we don't end up with a single number in the subarray.

#### Manual Run

```python
nums = [1,0,1,0,1], k = 4
```

i | num | curr_sum | curr_mod | mod_seen_at
--- | --- | --- | --- | ---
0 | 1 | 1 | 1 | {0: -1, 1: 0}
1 | 0 | 1 | 1 | {0: -1, 1: 0}
2 | 1 | 2 | 2 | {0: -1, 1: 0, 2: 2}
3 | 0 | 2 | 2 | {0: -1, 1: 0, 2: 2}
4 | 1 | 3 | 3 | {0: -1, 1: 0, 2: 2, 3: 4}

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(k) -> In the worst case scenario, the sum_frequency has k elements.
