# 69. Sqrt(x)

[🔗 LeetCode Link](https://leetcode.com/problems/sqrtx/description/)

## Solution

### Binary Search Approach

```python
x = 8

...
# iter n-2
    # left = 0, right = 8 -> mid = 4
    # 4 > 8/4 -> go left
# iter n-1
    # left = 0, right = 4 -> mid = 2
    # 2 < 8/2 -> go right
# iter n
    # left = 2, right = 4 -> mid = 3
    # 3 > 8/3 -> go left

# left = 2, right = 3 -> break
# return 2
```

#### Explanation

We want to find a value where mid = sqrt(x) using a binary search over all integers.
I choose to compare mid < (x // mid) instead of mid ** 2 < x to avoid a potential integer overflow.

#### Time Complexity

- O(log(n)) -> At each step, the search space is halved

#### Space Complexity

- O(1) -> We only create integer variables
