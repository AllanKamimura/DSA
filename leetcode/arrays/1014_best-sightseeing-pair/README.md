# 1014. Best Sightseeing Pair

[🔗 LeetCode Link](https://leetcode.com/problems/best-sightseeing-pair/description/)

## Solution

### Kadane's Algorithm Adapted

#### Explanation

The core idea is very similar to Kadane's Algorithm.

The problem, basically, is to find,
the score of the best sequence that ends at each index i.

The score of each ending is given by:

score = (start_value + start_index) + (curr_value - i)

Since for each value, `(curr_value - i)` is fixed,
we just need to keep track of the maximum
`(start_value + start_index)` seen so far.

#### Manual Run

```python
values = [7, 8, 8, 10]
```

i | curr_value | start_index | start_value | curr_result | max_result
--|----| ---- | ---- | ---- |---
1 | 8  | 0 | 7 | 14 | 14
2 | 8  | 1 | 8 | 15 | 15
3 | 10 | 2 | 8 | 17 | 17

```python
return max_value = 17
```

#### Time Complexity

- O(n) -> We traverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
