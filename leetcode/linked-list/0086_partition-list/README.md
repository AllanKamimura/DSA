# 86. Partition List

[🔗 LeetCode Link](https://leetcode.com/problems/partition-list/description/)

## Solution

### Use 2 Heads to Split the List

#### Explanation

This problem is quite straightforward, there's no trick here.

We create 2 new heads, for less than x and greater than x,
and move the pointers accordingly.

#### Manual Run

```python
[1,4,3,2,5,2], x = 3
```

curr | less | great
-- | -- | --
1 | [1] | []
4 | [1] | [4]
3 | [1] | [4,3]
2 | [1,2] | [4,3]
5 | [1,2] | [4,3,5]
2 | [1,2,2] | [4,3,5]

```python
return [1,2,2] -> [4,3,5] = [1,2,2,4,3,5]
```

#### Time Complexity

- O(n) -> We transverse the linked list a single time.

#### Space Complexity

- O(1) -> We only create pointer variables.
