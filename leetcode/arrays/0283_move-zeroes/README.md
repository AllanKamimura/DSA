# 283. Move Zeroes

[🔗 LeetCode Link](https://leetcode.com/problems/move-zeroes/description/)

## Solution

### Two pointers approach

```python
[0,1,0,3,12]

i = 0 # -> first = 0
j = 0 # -> second = 0
```

#### Explanation

While the first pointer keep track of the zeros, the second pointer looks for a non-zero value to swap.

#### Time Complexity

- O(n) -> In the worst case scenario,
    - The number of swaps is n/2
    - Consequently, the number of i steps is also n/2
    - j takes n steps

#### Space Complexity

- O(1) -> We only create integer variables
