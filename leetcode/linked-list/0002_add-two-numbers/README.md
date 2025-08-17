# 2. Add Two Numbers

[🔗 LeetCode Link](https://leetcode.com/problems/add-two-numbers/description/)

## Solution

### Just do it

#### Explanation

This problem is quite straightforward, we just need to sum it.

One point of attention is the carry over number,
which we can get by taking the floor division by 10.

Also, since the lists can have different sizes,
we need to handle the loop after the short list is exhausted.

In the refined version,
we are able to fit all the logic into a single loop.

#### Manual Run

```python
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
```

n1 | n2 | n_new | over_number | new_list
-- | -- | ---   | ----
9 | 9 | 8 | 1 | [8]
9 | 9 | 9 | 1 | [8,9]
9 | 9 | 9 | 1 | [8,9,9]
9 | 9 | 9 | 1 | [8,9,9,9]

```python
head2.next == None: break
head1.next != None: if block
```

n | n_new | over_number | new_list
-- | ---   | ----
9 | 0 | 1 | [8,9,9,9,0]
9 | 0 | 1 | [8,9,9,9,0,0]
9 | 0 | 1 | [8,9,9,9,0,0,0]
9 | 0 | 1 | [8,9,9,9,0,0,0]

```python
remainder_head == None: break
over_number = 1: if block
add_head = [8,9,9,9,0,0,0,1]

return add_head = [8,9,9,9,0,0,0,1]
```

#### Time Complexity

- O(n) -> We traverse the linked list a single time.

#### Space Complexity

- O(n) -> The output linked list has size n or (n+1), where n is the longest input linked list.
- O(1) -> We only create integer and pointer variables.
