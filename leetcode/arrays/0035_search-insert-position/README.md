# 35. Search Insert Position

[🔗 LeetCode Link](https://leetcode.com/problems/search-insert-position/description/)

## Solution

### Binary Search Approach

```python
nums = [1,3,5,6]
target = 4

i = 0
j = 3

i = 0, j = 3, middle = 1, val = 3
i = 1, j = 3, middle = 2, val = 5
i = 1, j = 2, middle = 1, val = 3
break

return i = 2
```

#### Explanation

While the value is not found or the 2 points are not on the same number,
get 1 step closer to the desired value, until it is found.

If we don't found the value, the insert position is going to be exactly i,
because i is going to point to one position to the right of the last
searched small value.

#### Time Complexity

- O(log(n)) -> At each step, the search space is halved

#### Space Complexity

- O(1) -> We only create integer variables
