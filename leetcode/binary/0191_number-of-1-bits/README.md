# 191. Number Of 1 Bits

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-1-bits/description/)

## Solution

### Bit Manipulation

#### Explanation

We transverse the binary and count the 1 bits.

First, initialize counter = 0.

In the for loop, `(n >> i)` puts the "ith" bit counting from the right in the first position.

The `& 1` operation, returns 0 if the first bit is 0 and 1 if the first bit is 1.

#### Manual Run

```python
n = 11 -> 1011

i = 0, (n >> i) = 1011, last_bit = 1, counter = 1
i = 1, (n >> i) = 0101, last_bit = 1, counter = 2
i = 2, (n >> i) = 0010, last_bit = 0, counter = 2
i = 3, (n >> i) = 0001, last_bit = 1, counter = 3

# anything beyond this is 0

return counter = 3
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
