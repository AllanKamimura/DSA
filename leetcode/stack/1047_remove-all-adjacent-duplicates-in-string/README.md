# 1047. Remove All Adjacent Duplicates In String

[🔗 LeetCode Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

## Solution

### Stack

#### Explanation

Exactly ame idea from [20. Valid Parentheses](../0020_valid-parentheses/).

#### Manual Run

```python
s = "abbaca"
```

letter | Stack
--- | ---
a | a
b | ab
b | a
a | -
c | c
a | ca

```python
return stack = "ca"
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(n) -> In the worst case, the stack has n elements.
