# 50. Powx N

[🔗 LeetCode Link](https://leetcode.com/problems/powx-n/description/)

## Solution

### Math?

#### Explanation

The idea is to use the mathematical property of exponentiation.

1. x^(2n) = x^n * x^n

With this, we can recursively compute the power operation in log(n) time.

#### Manual Run

```python
x = 2.00000, n = 10
```

n | call_stack
-- | ---
10 | [halfPow(2, 5)]
5 | [halfPow(2, 5), x * halfPow(2, 2)]
2 | [halfPow(2, 5), x * halfPow(2, 2), halfPow(2, 1)]

```python
halfPow(2, 1) = 2
halfPow(2, 2) = 2 ^ 2
halfPow(2, 5) = 2 ^ 4 * 2 = 2 ^ 5
halfPow(2, 10) = 2 ^ 10

return 1024
```

#### Time Complexity

- O(log(n)) -> At each recursion level, we half the value of n.

#### Space Complexity

- O(log(n)) -> At each recursion level, we half the value of n.
