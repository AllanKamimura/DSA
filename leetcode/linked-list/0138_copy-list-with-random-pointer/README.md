# 138. Copy List With Random Pointer

[🔗 LeetCode Link](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

## Solution

### Linked List Inside a Linked List

#### Explanation

To grab an intuition about this problem,
we start by thinking about some points.

Suppose that we start by iterating over the linked list.

1. We can't assign the random pointers right way,
because the pointed node can be ahead of the iterator and,
thus not yet created.
1. We also can't go follow the random and create it because it could lead to a circular pattern.

So we are going to do 2 pass, one to create the new nodes and another to assign the random pointers.

We also need a way to map the nodes from the original list to it's respective clone node in the new list.

We could use a hashmap or maybe add a new pointer `new` to `ListNode`, but this would take O(n) space. Instead we are going to use the intertwined linked list approach.

```shell
head -> [0] -> [new 0] -> [1] -> [new 1] -> [2] -> [new 2]
```

This way, we are using the index position of the node to mark a node as part of the new linked list.

#### Manual Run

```python
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

1. Create the new nodes in-between the original nodes.

    ```python
    head = [[7,null],[7,null],[13,0],[13,null],[11,4],[11,null],[10,2],[10,null],[1,0],[1,null]]
    ```

1. Map the original random pointers to the nodes in the new list

    ```python
    head = [[7,null],[7,null(new)],[13,0],[13,0(new)],[11,4],[11,4(new)],[10,2],[10,2(new)],[1,0],[1,0(new)]]
    ```

1. Remove the original Nodes

    ```python
    head = [[7,null(new)],[13,0(new)],[11,4(new)],[10,2(new)],[1,0(new)]]
    ```

#### Time Complexity

- O(n) -> We transverse the linked list 3 times.

#### Space Complexity

- O(1) -> Aside from the output, we only create pointer variables.
