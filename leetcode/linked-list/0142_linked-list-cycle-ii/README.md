# 142. Linked List Cycle Ii

[🔗 LeetCode Link](https://leetcode.com/problems/linked-list-cycle-ii/description/)

## Solution

### Fast and Slow Pointers

#### Explanation

The idea is to use the Fast/Slow Pointers approach,
similar to [876. Middle Of The Linked List](../0876_middle-of-the-linked-list/).

1. Find if there is a cycle.
2. Find the "length" of the cycle.

To find the "length" (or a multiple of the length),
we count the steps taken,
the idea is that the number of steps is equal
to the distance between slow and fast.

Since, at the end,
both pointers are at the same node,
this distance is a multiple of the length of the cycle.

Finally, to find the start of the cycle,
we can, starting from the head and check at each node,
we check "length of the cycle" steps ahead,
if we end up at the same place, it means we walked a whole cycle.

#### Manual Run

```python
head = [3,2,0,-4], pos = 1
```

iter 1

```shell
[   3] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4]
[slow] -> [fast] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ]
```

iter 2

```shell
[   3] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4]
[    ] -> [slow] -> [    ] -> [fast] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ]
```

iter 3

```shell
[   3] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4]
[    ] -> [    ] -> [slow] -> [    ] -> [    ] -> [fast] -> [    ] -> [    ] -> [    ] -> [    ]
```

```python
fast == slow: cycle_found
lenght = 3
```

```shell
[   3] -> [   2] -> [   0] -> [    4] -> [   2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4]
[head] -> [    ] -> [    ] -> [ahead] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ]
```

```shell
[   3] -> [   2] -> [   0] -> [    4] -> [    2] -> [   0] -> [   4] -> [   2] -> [   0] -> [   4]
[    ] -> [head] -> [    ] -> [     ] -> [ahead] -> [    ] -> [    ] -> [    ] -> [    ] -> [    ]
```

```python
head = ahead
return cycle_start_index = 1
```

#### Time Complexity

- O(n) -> We transverse the linked list 3 times.

#### Space Complexity

- O(1) -> We only create pointer variables.
