# 876. Middle Of The Linked List

[🔗 LeetCode Link](https://leetcode.com/problems/middle-of-the-linked-list/description/)

## Solution

### Fast and Slow Pointers

#### Explanation

This approach uses 2 pointers, one "fast" and the other "slow".
The core idea is that the "faster" moves 2 steps at a time,
while the "slow" moves a single step.

By the time the faster point reaches the end of the linked list,
the slow pointer would be in the middle of the linked list.

#### Manual Run

```python
head = [1,2,3,4,5]
```

fast | slow
-- | --
1 | 1
3 | 2
5 | 3

```python
return slow = 3
```

```python
head = [1,2,3,4,5,6]
```

fast | slow
-- | --
1 | 1
3 | 2
5 | 3

#### Time Complexity

- O(n) -> We transverse the linked list 2 times.

#### Space Complexity

- O(1) -> We only create pointer variables.
