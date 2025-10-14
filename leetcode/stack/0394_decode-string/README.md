# 394. Decode String

[🔗 LeetCode Link](https://leetcode.com/problems/decode-string/description/)

## Solution

### Stack

#### Explanation

This question is pretty similar to [20. Valid Parentheses](../0020_valid-parentheses/).

Since we are already guaranteed to have valid square brackets with a number before,
we don't need to check this.

So we iterate over the string,
adding the chars to a stack,
when we find a closing square bracket,
we pop from the stack until we find the opening square bracket,
and apply the decoding rule to this segment.

#### Manual Run

```python
s = "3[a2[c]]"
```

char | stack
--- | ----
3 | (3)
[ | (3, [ )
a | (3, [, a )
2 | (3, [, a, 2 )
[ | (3, [, a, 2, [ )
c | (3, [, a, 2, [, c )
] | (3, [, a, cc)
] | (accaccacc)

```python
return accaccacc
```

#### Time Complexity

- O(n) -> Each element is popped and appended only once.

#### Space Complexity

- O(n) -> In the worst case, the stack has n elements.
