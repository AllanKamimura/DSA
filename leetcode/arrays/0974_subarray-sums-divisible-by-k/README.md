# 974. Subarray Sums Divisible By K

[🔗 LeetCode Link](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)

## Solution

### Prefix sum array

#### Explanation

The idea is exactly the same as [560. Subarray Sum Equals K](../0560_subarray-sum-equals-k/).

`K = prefix[j] - prefix[i] => prefix[i] = prefix[j] - K`

`prefix[i] = prefix[j] - K => mod(prefix[i], k) = mod(prefix[j], k) - mod(K, k) => prefix[i] % k = prefix[j] % k`

So our problem now is to count for each `j` how many subarrays starting at `i` have the same modulo.

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

- O(n) -> In the worst case scenario, the sum_frequency has n elements.
