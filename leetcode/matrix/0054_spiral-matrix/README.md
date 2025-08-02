# 54. Spiral Matrix

[🔗 LeetCode Link](https://leetcode.com/problems/spiral-matrix/description/)

## Solution

### Matrix traverse

#### Explanation

In this problem, basically we need to traverse the matrix step by step.

```shell
right → down → left → up
```

The core idea is to keep track of both
the move direction and the current boundaries.

Each time we "complete" a row or a column,
we move the boundaries by 1 step inwards.

#### Manual Run

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
```

steering_wheel | i | j | top | right | bottom | left | steering_wheel_new
-- | -- | -- | -- | -- | -- | -- | --
right | 0 | 0 | 2 | 3 | 0 | 0 | right
right | 0 | 1 | 2 | 3 | 0 | 0 | right
right | 0 | 2 | 2 | 3 | 0 | 0 | right
right | 0 | 3 | 2 | 2 | 0 | 0 | down
down | 1 | 3 | 2 | 2 | 0 | 0 | down
down | 2 | 3 | 2 | 2 | 1 | 0 | left
left | 2 | 2 | 2 | 2 | 1 | 0 | left
left | 2 | 1 | 2 | 2 | 1 | 0 | left
left | 2 | 0 | 2 | 2 | 1 | 1 | up
up | 2 | 0 | 2 | 2 | 1 | 1 | up
up | 1 | 0 | 1 | 2 | 1 | 1 | right
right | 1 | 1 | 1 | 2 | 1 | 1 | right
right | 1 | 2 | 1 | 2 | 1 | 1 | end


#### Time Complexity

- O(n * m) -> We traverse the matrix a single time.

#### Space Complexity

- O(m * n) -> The result array has m * n elements
- O(1) -> Extra space: We only create integer variables.
