# 136. Single Number

[🔗 LeetCode Link](https://leetcode.com/problems/single-number/description/)

## Solution

### XOR Operator

#### Explanation

This is the most hackish 1 line solve question ever.
I spent hours thinking about this question 
and nothing was O(1) space and O(n) time.


The XOR Operator has the magic properties of:

- n == m -> n ^ m == 0
- n != m -> n ^ m != 0 (since we only have 0 and 1)
- the operator is commutative

#### Manual Run

```python
nums = [2,2,1]

num = 2, single = 2
num = 2, single = 0
num = 1, single = 1
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
