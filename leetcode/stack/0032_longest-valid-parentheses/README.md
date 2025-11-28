# 32. Longest Valid Parentheses

[🔗 LeetCode Link](https://leetcode.com/problems/longest-valid-parentheses/description/)

## Solution

#### Explanation



#### Manual Run

```python
Input: s = ")()())"
```

symbol | stack | track | best_track
-- | --- | --- | ---
) | [] | 0 | 0
( | ["("] | 0 | 0
) | [] | 2 | 2
( | ["("] | 2 | 2
) | [] | 4 | 4
) | [] | 4 | 4

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
