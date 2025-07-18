# 525. Contiguous Array

[🔗 LeetCode Link](https://leetcode.com/problems/contiguous-array/description/)

## Solution

### Prefix sum + hashmap index tracker

#### Explanation

Using the prefix sum property that the sum of elements from i to j (inclusive) inclusive
`prefix_sum[j+1] - prefix_sum[i]`.

To have an equal number of 0s and 1s,
the sum of elements from i to j (inclusive) is equal to
half the number of elements (j + 1 - i) in this interval,
because half the numbers are 1s and the other half are 0s.

In another words, if `prefix_sum[j+1] - prefix_sum[i] = (j + 1 - i) / 2`,
then we have an equal number of 0s and 1s.

Shuffling things around, we get our core idea.

`prefix_sum[i] - (i) / 2 = prefix_sum[j+1] - (j+1) / 2`,
which I'm going to call complementary prefix_sums.

Now we want to, for each value in the prefix_sum,
we want to know if it's complementary prefix_sum exists.

Then we look for the max value of (j + 1 - i) to find the max sequence.

#### Manual Run

```python
nums = [0,1,1,1,1,1,0,0,0]
```

j | num | sum | `prefix_comp` | `curr_size` | `prefix_index`
--- | --- | --- | --- | --- | ----
0 | 0 | 0 | 0   | 0 | {0.5: -1, 0: 0}
1 | 1 | 1 | 0.5 | 2 | {0.5: -1, 0: 0}
2 | 1 | 2 | 1   | 2 | {0.5: -1, 0: 0, 1: 2}
3 | 1 | 3 | 1.5 | 2 | {0.5: -1, 0: 0, 1: 2, 1.5: 3}
4 | 1 | 4 | 2   | 2 | {0.5: -1, 0: 0, 1: 2, 1.5: 3, 2: 4}
5 | 1 | 5 | 2.5 | 2 | {0.5: -1, 0: 0, 1: 2, 1.5: 3, 2: 4, 2.5: 5}
6 | 0 | 5 | 3   | 2 | {0.5: -1, 0: 0, 1: 2, 1.5: 3, 2: 4, 2.5: 5, 3: 6}
7 | 0 | 5 | 1.5 | 4 | {0.5: -1, 0: 0, 1: 2, 1.5: 3, 2: 4, 2.5: 5, 3: 6}
8 | 0 | 5 | 1   | 6 | {0.5: -1, 0: 0, 1: 2, 1.5: 3, 2: 4, 2.5: 5, 3: 6}

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(n) -> In the worst case, `prefix_index` has n/2 elements.
