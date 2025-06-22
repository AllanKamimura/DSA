# 69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Hint: search all Integers.

## Example 1

```shell
Input: x = 8
Output: 2
```

## Example 2

```shell
Input: x = 9
Output: 3
```

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

#### Explaination

We want to find a value where mid = sqrt(x) using a binary search over all integers.
I choose to compare mid < (x // mid) instead of mid ** 2 < x to avoid a potential integer overflow.

#### Time Complexity

- O(log(n)) -> At each step, the search space is halved

#### Space Complexity

- O(1) -> We only create integer variables
