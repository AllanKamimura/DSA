# 155. Min Stack

[🔗 LeetCode Link](https://leetcode.com/problems/min-stack/description/)

## Solution

### Min Stack

#### Explanation

This is actually 2 stacks, one with values and one with mins.

The mins stack keep track of the minimum value so far,
We trade additional space for O(1) time getMin operation.

#### Manual Run

```python
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

action | stack | min_stack | output
--- | --- | ---- | ---
push(-2) | [-2] | [-2] | -
push(0) | [-2, 0] | [-2, -2] | -
push(-3) | [-2, 0, -3] | [-2, -2, -3] | -
getMin() | [-2, 0, 3] | [-2, -2, -3] | -3
pop() | [-2, 0] | [-2, -2] | -
top() | [-2, 0] | [-2, -2] | 0
getMin() | [-2, 0] | [-2, -2] | -2

#### Time Complexity

- O(1)
  - push: Insert at end into both stacks.
  - pop: Remove from the end in both stacks.
  - top: Retrieve from top the top of val stack
  - getMin: Retrieve from top the top of min stack

#### Space Complexity

- O(n) -> For each value, we have 2 elements in the stack, val and min.
