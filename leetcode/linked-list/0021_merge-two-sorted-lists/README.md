# 21. Merge Two Sorted Lists

[🔗 LeetCode Link](https://leetcode.com/problems/merge-two-sorted-lists/description/)

## Solution

### Just do it

#### Explanation

This problem is quite straightforward,
we can just reconstructed the linked list
by iterating over the 2 linked lists,
comparing each value and moving the pointers accordingly.

#### Manual Run

```python
list1 = [1,2,4], list2 = [1,3,4]
```

val1 | val2 | new_list 
--- | --- | ----
1 | 1 | [1]
2 | 1 | [1,1]
2 | 3 | [1,1,2]
4 | 3 | [1,1,2,3]
4 | 4 | [1,1,2,3,4]
None | 4 | [1,1,2,3,4,4]

```python
return new_list = [1,1,2,3,4,4]
```

#### Time Complexity

- O(n + m) -> We transverse the arrays a single time.

#### Space Complexity

- O(1) -> We only create reference variables.

### Recursion

#### Explanation

We can also think this problem backwards with recursion.

The base case is when either of the lists are empty,
this way we can just append the non empty list.

#### Manual Run

```python
list1 = [1,2,4], list2 = [1,3,4]
```

val1 | val2 | new_list | resolve
--- | --- | ---- | 
1 | 1 | mergeTwoLists(list1, list2.next) | 1
1 | 3 | mergeTwoLists(list1.next, list2) | 1
2 | 3 | mergeTwoLists(list1.next, list2) | 2
4 | 3 | mergeTwoLists(list1, list2.next) | 3
4 | 4 | mergeTwoLists(list1, list2.next) | 4

```python
return new_list = [1,1,2,3,4,4]
```

#### Time Complexity

- O(n + m) -> We transverse the arrays a single time.

#### Space Complexity

- O(n + m) -> In the worst case, the recursion stack have (n + m) calls.