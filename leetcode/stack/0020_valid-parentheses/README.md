# 20. Valid Parentheses

[🔗 LeetCode Link](https://leetcode.com/problems/valid-parentheses/description/)

## Solution

### Stacking

#### Explanation

The idea is to use a stack to hold the open symbols,
and each time we reach a closing symbol,
we need to check:

1. If there is an open symbol in the stack
2. If the last open symbol is the pair of the closing one

If we reach out the end of the string
with no symbol left in the stack,
then the string is valid.

#### Manual Run

```python
s = "()[]{}"
```

symbol | stack
-- | ---
( | (
) | -
[ | [
] | -
{ | {
} | -

```python
return (len(stack) == 0) = True
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(n) -> In the worst case scenario, the stack size is n.
