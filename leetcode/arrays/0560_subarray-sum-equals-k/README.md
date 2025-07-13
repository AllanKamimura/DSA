# 560. Subarray Sum Equals K

[🔗 LeetCode Link](https://leetcode.com/problems/subarray-sum-equals-k/description/)

## Solution

### Prefix sum

#### Explanation

The prefix sum array is the cumulative sum up to that index,
in such that, prefix[i] is the sum of all elements from index 0 to i-1.

One property of the prefix sum is that,
The sum of elements from index i to j (inclusive) is `prefix[j+1] - prefix[i]`.

We want to find `K = prefix[j+1] - prefix[i]`, 
subarray starting at `i` and ending at `j+1` in which the sum is `K`.

`K = prefix[j+1] - prefix[i] => prefix[i] = prefix[j+1] - K`

So given that we know the value of `prefix[j+1]`,
the problem now is to know how many `i`s before `j+1` exist.
For this, we can keep track of the prefix frequency using a hashmap.

To handle the case of subarray that start at index i=0,
we add the trivial case of an empty subarray `sum_frequency[0] = 1`.

#### Manual Run

```python
nums = [1,2,3], k = 3
```

num | curr_sum | sum_frequency | diff | count
--- | --- | --- | --- | ---
1 | 1 | {0: 1, 1: 1} | -2 | 0
2 | 3 | {0: 1, 1: 1, 3: 1} | 0 | 1
3 | 6 | {0: 1, 1: 1, 3: 1, 6: 1} | 3 | 2

```python
return count = 2
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(k) -> In the worst case scenario, the sum_frequency has k elements.
