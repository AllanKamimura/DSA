# 92. Reverse Linked List Ii

[🔗 LeetCode Link](https://leetcode.com/problems/reverse-linked-list-ii/description/)

## Solution

### Three Pointers in-place Reverse

#### Explanation

This problem is very similar to [206. Reverse Linked List](../0206_reverse-linked-list/),
with 2 key points.

1. We have a new stop criterion: reverse only n nodes
2. We need to re-attach the reversed list later.

To grab an intuition about the links we are breaking and re-attaching,
let's think about an example.

```python
head = [1,2,3,4,5], left = 2, right = 4
```

```shell
1 -> 2 -> 3 -> 4 -> 5
```

When we reverse the segment, we are going to have this:

```shell
None <- 2 <- 3 <- 4
or
4 -> 3 -> 2 -> None
```

We need to attach 1 -> 4 and 2 -> 5

So we need to keep track of the node 1 step before left
and the node 1 step after right.

#### Manual Run


```python
head = [1,2,3,4,5], left = 2, right = 4
max_iter = 4 - 2 + 1 = 3
```

Main loop:

prev | curr | i
-- | -- | --
0 | 1 | 1
1 | 2 | 2

Reverse loop

prev | curr | j | next_ | curr.next
-- | --- | -- | -- | ---
None | 2 | 0 | 3 | 2 -> None
2 | 3 | 1 | 4 | 3 -> 2
3 | 4 | 2 | 5 | 4 -> 3
4 | 5 | 3 (break) | - | -

```shell
right_node = 4
right_next = 5
prev(main) = 1, 1 -> 4
curr(main) = 2, 2 -> 5
```

```python
return 1 -> 4 -> 3 -> 2 -> 5
```

#### Time Complexity

- O(n) -> We transverse the linked list a single time.

#### Space Complexity

- O(1) -> We only create pointer variables.
