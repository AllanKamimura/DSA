# 19. Remove Nth Node From End Of List

[🔗 LeetCode Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## Solution

### Fast + Slow Pointer Approach

#### Explanation

The trick is to move the faster point (n+1) steps ahead,
the start moving the slower point.
By the time the faster point reaches the end of the list,
the slower point would be exactly (n+1) steps from the end of the list.

Since we want to remove the Nth node from the end,
it's basically `slow.next = slow.next.next`.

We need to handle one special edge case,
since the slow pointer needs to be 1 step before the node we want to remove,
there's the case when we want to remove the head itself.

For this we can use a dummy fake head,
in such a way that `slow` and `slow.next` are always defined.

#### Manual Run

```python
head = [1,2,3,4,5], n = 2
```

fast | slow
-- | --
dummy | dummy
1 | dummy
2 | dummy
3 | dummy
4 | 1
5 | 2
None | 3

```python
3 -> 5
return [1,2,3,5]
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create pointer variables.
