# 160. Intersection Of Two Linked Lists

[🔗 LeetCode Link](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

## Solution

### Cycle Around

#### Explanation

The solution is actually quite simple after you know what to do.

Let A and B be the linked lists.

A has (a + c) elements and B has (b + c) elements,
where c are the common elements,
and a exists only in A and b exists only in b.

Then we merge the 2 lists into A -> B and B -> A.

The total number of elements in each is (a + b + 2*c)

The elements in A are in this order (a -> c -> b -> c),
while in B it's (b -> c -> a -> c)

So if we traverse both linked lists at the same time,
with 2 pointer, `curr_a` and `curr_b`,
after (a + b + c) elements,
both are going to be at the same place,
and this place is exactly the start of the c sequence.

Also, this is going to be the first common element.

If the lists doesn't intersect,
both pointers are going to reach the end together.

#### Manual Run

```python
listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
AB = [4,1,8,4,5,5,6,1,8,4,5]
BA = [5,6,1,8,4,5,4,1,8,4,5]
```

curr_a | curr_b | same
-- | -- | --
4 | 5 | False
1 | 6 | False
8 | 1 | False
4 | 8 | False
5 | 4 | False
5 | 5 | False
6 | 4 | False
1 | 1 | False (not the same Node)
8 | 8 | True

```python
return curr_a = 8
```

#### Time Complexity

- O(n) -> We traverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
