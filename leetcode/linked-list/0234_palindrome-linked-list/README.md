# 234. Palindrome Linked List

[🔗 LeetCode Link](https://leetcode.com/problems/palindrome-linked-list/description/)

## Solution

### Find Middle and Reverse

#### Explanation

The idea is quite simple.
A palindrome is a sequence that if we split it in half
and reverse one half, both halves are going to be equal.

#### Manual Run

```python
head = [1,1,2,1]
```

1. Find the middle node.

slow | fast | switch
---- | ---- | ------
head | head | True
1    | 1    | False
1    | 1    | True
1    | 2    | False
1    | 1    | True
2    | None | False

2. Reverse the second half.

prev | curr
---- | ----
None | 2
2    | 1 
1    | None

```python
reversed_head -> 1 -> 2 -> None
head -> 1 -> 1 -> 2 -> 1 -> None
```

left | right | equal
---  | ----- | ----
1    | 1     | True
1    | 2     | False

```python
return False
```


#### Time Complexity

- O(n) -> We traverse the linked list 2 times.

#### Space Complexity

- O(1) -> We only create pointer variables. Reverse is in-place.
