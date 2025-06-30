# 190. Reverse Bits

[🔗 LeetCode Link](https://leetcode.com/problems/reverse-bits/description/)

## Solution

### Bit Manipulation

#### Explanation

To reverse the binary number, we re-construct the number bit by bit.

- Initialize reverse = 0
- (num & 1): takes the right most bit
- (reverse << 1): left shift reverse, to make space for the new bit
- Use OR operator to add it
- (num >> 1): right shift the original number to grab the next bit

#### Manual Run

```python
n = 10111

reverse = 0
```

num | `reverse << 1` | `num & 1` | reverse
10111 | 0 | 1 | 1
1011 | 10 | 1 | 11
101 | 110 | 1 | 111
10 | 1110 | 0 | 1100
1  | 11100 | 1 | 11101

```python
return reverse = 11101
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
