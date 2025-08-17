# 61. Rotate List

[🔗 LeetCode Link](https://leetcode.com/problems/rotate-list/description/)

## Solution

### Two Pointers Approach

#### Explanation

The core idea is to use the 2 pointers approach,
with the right point `k` steps ahead.
When the right pointer reaches the end,
the left point is going to be `k` steps from the end,
exactly at the split point.

We also need to take care of some edge cases,
`k` can be bigger than the length of the list.
To handle it, we first need to find the length of the list,
then we can take the modulo `k %= n`.

We also need to handle the case where either k or n is zero.
In this case, we don't need to change anything on the list,
so we can just return it as is.

#### Manual Run

```python
head = [1,2,3,4,5], k = 2
n = 5, k = 2
```

1. Advance right k=2 steps

right = 2

2. Create left and advance it until right.next == None

left | right 
-- | --
1 | 3
2 | 4
3 | 5

3. The head of the new list is left.next = 4
4. Close the cycle by adding right.next = head
5. Break the cycle at left by adding left.next = None

#### Time Complexity

- O(n) -> We transverse the list 2 times.

#### Space Complexity

- O(1) -> We only create integer and pointer variables.
