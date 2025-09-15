# 901. Online Stock Span

[🔗 LeetCode Link](https://leetcode.com/problems/online-stock-span/description/)

## Solution

### Monotonic Stack

#### Explanation

The core idea is to use 2 monotonic stacks,
one to keep track of the value and another for the streak.

This way we can have a quick look-up time for the next values.

When a new number comes up, we have 2 possible outcomes:

- The number is less than the value on top
  - So we get a 1 day streak and add the new number to the top
- The number is greater or equal the value on top
  - Since this number is greater than the top, that means we can extend the previous streak with the new day.
  - Then, we pop the old value
  - We repeat this logic until we fall to the first case.

#### Manual Run

```python
values = [[100], [80], [60], [70], [60], [75], [85]]
```

price | value_stack | streak_stack | curr_streak
--- | --- | --- | ----
100 | [100] | [1] | 1
80 | [100,80] | [1,1] | 1
60 | [100,80,60] | [1,1,1] | 1
70 | [100,80,70] | [1,1,2] | 2
60 | [100,80,70,60] | [1,1,2,1] | 1
75 | [100,80,75] | [1,1,4] | 4
85 | [100,85] | [1,6] | 6

```python
return streaks = [1,1,1,2,1,4,6]
```

#### Time Complexity

- O(n) -> We transverse the array a single time. Each value is only added once and removed at most once from the stack.

#### Space Complexity

- O(n) -> Each value is only added to the stack once.
