# 150. Evaluate Reverse Polish Notation

[🔗 LeetCode Link](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

## Solution

### Stack

#### Explanation

This problem is actually quite easy,
we just use a stack to stack values until we find an operator,
then we evaluate the numbers by popping the stack.

Things to pay attention:

- All operations are integer
- Operation order: [a,b,"/"] = stack[-2] / stack[-1]

#### Manual Run

```python
Input: tokens = ["2","1","+","3","*"]
```

token | stack
2 | [2]
1 | [2,1]
\+ | [3]
3 | [3,3]
\* | [9]

```python
return stack[0] = 9
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(n) -> In the worst case, we have ~ n/2 elements in the stack.
