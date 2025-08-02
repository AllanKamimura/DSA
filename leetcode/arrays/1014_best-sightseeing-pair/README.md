# 1014. Best Sightseeing Pair

[🔗 LeetCode Link](https://leetcode.com/problems/best-sightseeing-pair/description/)

## Solution

### Kadane's Algorithm Adapted

#### Explanation

The core idea is very similar to Kadane's Algorithm.

The problem, basically is to find the `start` and `end` pair.

At each value we need to decide if:

- We `end` the sequence.
- We `start` a new sequence
- Do nothing

The caveat here is that the score at each point
is the sum of the value AND index of the point.

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
