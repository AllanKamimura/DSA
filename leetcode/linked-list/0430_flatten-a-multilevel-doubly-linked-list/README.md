# 430. Flatten A Multilevel Doubly Linked List

[🔗 LeetCode Link](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/)

## Solution

### Recursive Traverse

#### Explanation

From a first look at the problem, it seems to be a recursive pattern.
Basically, every time we go to a child node, we end up with the same problem.

So, the recursion ends when we reach a node that points to None next,
at this point, the recursive call should return this last node.

Then we need to perform 5 swaps:

1. `parent.next = child`
2. `child.prev = parent`
3. `child_tail.next = parent.next`
4. `parent.next.prev = child_tail`
5. `parent.child = None`

#### Manual Run

The multi-layer doubly linked list was a bit hard to model in my local tests.

```python
head = [
    1   ,2   ,3   ,4   ,5   , 6  ,null,
    null,null,7   ,8   ,9   ,10  ,
              null,null,11  ,12  ]
```

```shell
[1]
[1] <-> [2]
[1] <-> [2] <-> [3]
```

First recursion

```shell
[7]
[7] <-> [8]
[7] <-> [8] <-> [9]
```

Second recursion

```shell
[11]
[11] <-> [12] -> None
```

Resolve Second recursion

```python
parent_curr = 9
child = 11
child_tail = 12
next_ = 10

parent.next = child        # 9 -> 11
child.prev = parent        # 11 <- 9
parent.child = None        # detach
child_tail.next = next_    # 12 -> 10
next_.prev = child_tail    # 10 <- 12
```

```python
head = [
    1   ,2   ,3   ,4   ,5   , 6  , null,
    null,null,7   ,8   ,9   ,11  , 12  , 10]
```

Resolve First recursion

```python
parent = 3
child = 7
child_tail = 10
next_ = 4

parent.next = child        # 3 -> 7
child.prev = parent        # 7 <- 3
parent.child = None        # detach
child_tail.next = next_    # 10 -> 4
next_.prev = child_tail    # 4 <- 10
```

```python
head = [
    1   ,2   ,3   ,7   ,8   ,9   ,11  , 12  , 10,    4   ,5   , 6  , null]
```

#### Time Complexity

- O(n) -> We traverse over all nodes a single time.

#### Space Complexity

- O(d) -> We create a recursive stack that, in the worst case, has depth (d) = n.
