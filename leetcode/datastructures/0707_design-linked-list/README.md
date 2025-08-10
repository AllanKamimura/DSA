# 707. Design Linked List

[🔗 LeetCode Link](https://leetcode.com/problems/design-linked-list/description/)

## Solution

### Doubly Linked List

#### Explanation

The base element of a linked list is a Node.
Each Node has 3 basic attributes:

- `val`: The value stored at this Node
- `prev`: The previous node in the list, or `None`, if first
- `next`: The next node in the list, or `None`, if last

The linked list is formed by chaining together these nodes.

The linked list supports the basic operations of get, insertion and deletion.

Since we want to make the `addAtHead` and `addAtTail` operations O(1),
we need to keep track of the head_node, tail_node and list length.

The insertion and deletion operations are rather cumbersome,
because we always needs to use 3 pointers.

```shell
# insert
prev <-> next
prev <-> curr
curr <-> next
prev <-> curr <-> next

# delete
prev <-> curr <-> next
prev -> next
prev <- next
del curr
```

This leads to 2 attention points,
keeping tabs on boundaries
and having this look-ahead/look-behind tracking.

To make things easier, we use a fake head and fake tail,
to artificially "cut the edges",
so all operations are in the middle of the list.

#### Manual Run

```python
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
```

Operation | Linked List
-- | ---
MyLinkedList() | []
addAtHead(1) | [1]
addAtTail(3) | [1 <-> 3]
addAtIndex(1,2) | [1 <-> 2 <-> 3]
get(1) return 2 | [1 <-> 2 <-> 3]
deleteAtIndex(1) | [1 <-> 3]
get(1) return 3 | [1 <-> 3]

#### Time Complexity

- addAtHead O(1) -> Since we keep track of the head, we just need 2 swaps operations
- addAtTail O(1) -> Since we keep track of the tail, we just need 2 swaps operations
- get O(n) -> In the worst case we traverse the whole array.
- addAtIndex O(n) -> We need to first get to the index. The operation itself is 3 swaps (linear).
- deleteAtIndex O(n) -> We need to first get to the index. The operation itself is 3 swaps (linear).

#### Space Complexity

- O(n) -> For the nodes
- O(1) -> For the reference to tail and head nodes.
