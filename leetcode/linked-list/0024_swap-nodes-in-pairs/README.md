# 24. Swap Nodes In Pairs

[🔗 LeetCode Link](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

## Solution

### Just do it

#### Explanation

There's no secret here.
We just need to perform the swaps in the right order.

First, we create a `fake_head`, so we can refer to it later.

Then, we initializer 3 pointers.

- prev = fake_head, so we can swap the prev node to point to the right pair.
- curr = prev.next, the left node we are going to swap.
- next = curr.next, the right node we are going to swap.

```shell
[prev] -> [curr] -> [next] -> [aaaa] -> [    ]
```

1. `curr.next = next.next`

```shell
[prev] -> [curr] -> [aaaa] -> [    ]
[next] -> [aaaa] -> [    ]
```

2. `next.next = curr`

```shell
[prev] -> [curr] -> [aaaa] -> [    ]
[next] -> [curr] -> [aaaa] -> [    ]
```

3. `prev.next = next`

```shell
[prev] -> [next] -> [curr] -> [aaaa] -> [    ]
```

4. `prev = curr; curr = curr.next`

```shell
[    ] -> [    ] -> [prev] -> [curr] -> [next]
```

#### Manual Run

```python
head = [1,2,3,4]
```

```shell
[head] -> [  1 ] -> [  2 ] -> [  3 ] -> [  4 ]
[prev] -> [curr] -> [next] -> [aaaa] -> [    ]
```

##### First iteration

prev | prev.next | curr | curr.next | next | next.next
-- | -- | -- | -- | -- | --
0 | 1 | 1 | 2 | 2 | 3

```python
curr.next = next.next => 1.next = 3
next.next = curr = => 2.next = 1
prev.next = next = => 0.next = 2
prev = curr = 1
curr = curr.next = 3
```

```shell
[head] -> [  2 ] -> [  1 ] -> [  3 ] -> [  4 ]
[head] -> [    ] -> [prev] -> [curr] -> [    ]
```

##### Second iteration

prev | prev.next | curr | curr.next | next | next.next
-- | -- | -- | -- | -- | --
1 | 3 | 3 | 4 | 4 | None

```python
curr.next = next.next => 3.next = None
next.next = curr = => 4.next = 3
prev.next = next = => 1.next = 4
prev = curr = 3
curr = curr.next = None
```

```shell
[head] -> [  2 ] -> [  1 ] -> [  4 ] -> [  3 ] -> [None]
[head] -> [    ] -> [    ] -> [    ] -> [prev] -> [curr]
```

```python
break
return 2 -> 1 -> 4 -> 3
```


#### Time Complexity

- O(n) -> We traverse the linked list a single time.

#### Space Complexity

- O(1) -> We only create pointers variables.
