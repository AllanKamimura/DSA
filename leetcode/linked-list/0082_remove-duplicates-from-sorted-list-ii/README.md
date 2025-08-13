# 82. Remove Duplicates From Sorted List Ii

[🔗 LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

## Solution

### Rebuild the linked List

#### Explanation

We start by creating 3 pointers, `prev`, `right` and `right`.

The intuition behind this is that for a given number (`left`),
we need to look 1 step behind and 1 step ahead to know if it is a duplicate.

We also create 2 nodes.

- The `fake_head` is used to refer back to the start of the linked list.
- The `fake_head_add` is interactively updated to add the new nodes.


The main loop goes like this:

```shell
[prev] -> [left] -> [right] -> [] -> []
```

```python
if left.val == right.val:
    [] -> [] -> [prev] -> [left] -> [right]

if left.val != right.val:
    if prev.val != left.val:
        add(Node(left.val))
    [] -> [prev] -> [left] -> [right] -> []
```

We need to remove the next from left before adding it,
since we don't yet know where the next should be.

At the end, we need to check if the last `right` should be added.

#### Manual Run

```python
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

prev | left | right | add | list
--- | -- | -- | -- | --
-1 | 1 | 2 | True | [1]
1 | 2 | 3 | True | [1,2]
2 | 3 | 3 | False | [1,2]
3 | 4 | 4 | False | [1,2]
4 | 5 | None | a | [1,2]
4 | 5 | None | a | [1,2,5]

```python
return [1,2,5]
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create pointer values.
