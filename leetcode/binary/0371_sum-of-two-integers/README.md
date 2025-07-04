# 371. Sum Of Two Integers

[🔗 LeetCode Link](https://leetcode.com/problems/sum-of-two-integers/description/)

## Solution

### Bit Manipulation

#### Explanation

We iterate over each digit of number a and b.

Use the XOR operator to effective sum the digits.

Create an artificial `digit_c` to hold the "go up" value, after each sum.

#### Manual Run

```python
a = 2, b = 3
bin(a) = 10
bin(b) = 11
```


i | digit_a | digit_b | digit_c | result
--|--|--|--|--
0 | 0 | 1 | 0 | 1
1 | 1 | 1 | 0 | 01
2 | 0 | 0 | 1 | 101


```python
bin(5) = 101
return 5
```

#### Time Complexity

- O(1) -> We transverse the number's digits 32 times.

#### Space Complexity

- O(1) -> We only create integer variables.
