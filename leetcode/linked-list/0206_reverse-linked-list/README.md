# 206. Reverse Linked List

[🔗 LeetCode Link](https://leetcode.com/problems/reverse-linked-list/description/)

## Solution

### Three Pointers Approach

#### Explanation

We use 3 pointers, prev, curr and curr.next to swap the node next position.

The main loop has 4 steps:

1. Store the next node, so we don't lose the reference `next_ = curr.next`
2. Assign the next value of the current node to the previous node `curr.next = prev`
3. Move the prev pointer 1 step forward `prev = curr`
4. Move the curr pointer 1 step forward `curr = next_`

#### Manual Run

```python
[head] -> [   1] -> [   2] -> [   3] -> [   4] -> [    5] -> None
[prev]    [curr]    [next]
```

```python
[None] <- [   1] -> [   2] -> [   3] -> [   4] -> [    5] -> None
          [prev]    [curr]    [next]
```

```python
[None] <- [   1] <- [   2] -> [   3] -> [   4] -> [    5] -> None
                    [prev]    [curr]    [next]
```

```python
[None] <- [   1] <- [   2] <- [   3] -> [   4] -> [    5] -> None
                              [prev]    [curr]    [next]
```

```python
[None] <- [   1] <- [   2] <- [   3] <- [   4] -> [    5] -> None
                                        [prev]    [curr]    [next]
```

```python
[None] <- [   1] <- [   2] <- [   3] <- [   4] <- [    5] -> None
                                                  [prev]    [curr]    [next]
```

```python
[None] <- [   1] <- [   2] <- [   3] <- [   4] <- [    5] <- [head]
                                                             [prev]    [curr]    [next]
```

#### Time Complexity

- O(n) -> We transverse the linked list a single time.

#### Space Complexity

- O(1) -> We only create pointer variables.
