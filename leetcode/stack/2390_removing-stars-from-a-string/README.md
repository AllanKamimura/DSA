# 2390. Removing Stars From A String

[🔗 LeetCode Link](https://leetcode.com/problems/removing-stars-from-a-string/description/)

## Solution

### Stack

#### Explanation

This question is actually quite easy.
We just iterate over the string
and use a stack to store the letters,
this way we can readily know the last added letter.

#### Manual Run

```python
Input: s = "leet**cod*e"
```

letter | stack
--- | ---
l | [l]
e | [le]
e | [lee]
t | [leet]
\* | [lee]
\* | [le]
c | [lec]
o | [leco]
d | [lecod]
\* | [leco]
e | [lecoe]

```python
return stack = ["lecoe"]
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(n) -> In the worst case scenario, the stack has n elements.
