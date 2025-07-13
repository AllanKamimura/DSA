# 974. Subarray Sums Divisible By K

[🔗 LeetCode Link](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)

## Solution

### Prefix sum array

#### Explanation

The idea is very similat to [560. Subarray Sum Equals K](../0560_subarray-sum-equals-k/).

The `prefix_sum[j+1]` be the cumulative sum up to index j.

The sum of numbers from i to j (inclusive) is `prefix_sum[j+1]` - `prefix_sum[i]`.

(prefix_sum[j+1] - prefix_sum[i]) % k → (prefix_sum[j+1] % k) = (prefix_sum[i] % k)

So for each prefix_sum modulo k, we count how many times it has occurred before using a hashmap.

To handle the case of subarrays starting from index 0,
we initialize `mod_frequency[0] = 1`.

#### Manual Run

```python
nums = [4,5,0,-2,-3,1], k = 5
```

num | curr_sum | curr_mod | count | mod_frequency
--- | --- | --- | --- | ---
4   | 4 | 4 | 0 | {0: 1, 4: 1}
5   | 9 | 4 | 1 | {0: 1, 4: 2}
0   | 9 | 4 | 3 | {0: 1, 4: 3}
-2  | 7 | 2 | 3 | {0: 1, 4: 3, 2: 1}
-3  | 4 | 4 | 6 | {0: 1, 4: 4, 2: 1}
1   | 5 | 0 | 7 | {0: 2, 4: 4, 2: 1}

```python
return count = 7
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(k) -> In the worst case scenario, the sum_frequency has k elements.
