# 128. Longest Consecutive Sequence

[🔗 LeetCode Link](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Solution

### Hashset

#### Explanation

Since the array is unordered
and we want to perform a lot of lookups, the ideal data structure is a set.

Given an arbitrary value in the set,
we want to know if this number is part of a sequence,
for this, we can just lookup if the adjacent numbers are part of the set.

Since we don't know at which point in the sequence is the position of this number,
we need to look back and forward.

So we can take anchor the number, then take 1 by 1 steps
and check if the previous or next values are in the set.

If we can't take anymore steps, we anchor another arbitrary number.

#### Manual Run

```python
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
```

anchor | next | prev | found | count | set
--- | --- | --- | --- | --- | ---
9 | 10 | 8 | prev | 2 | [1,4,7,3,-1,0,5,6]
9 | 10 | 7 | prev | 3 | [1,4,3,-1,0,5,6]
9 | 10 | 6 | prev | 4 | [1,4,3,-1,0,5]
9 | 10 | 5 | prev | 5 | [1,4,3,-1,0]
9 | 10 | 4 | prev | 6 | [1,3,-1,0]
9 | 10 | 3 | prev | 7 | [1,-1,0]
9 | 10 | 2 | no | 0 | [1,-1,0]
1 | 2 | 0 | prev | 2 | [-1]
1 | 2 | -1 | prev | 3 | []

```python
break
return biggest = 7
```

#### Time Complexity

- O(n)
  - We transverse the array a single time to create the set
  - Perform n pop and remove operations in the set in the worst case

#### Space Complexity

- O(n) -> In the worst case scenario, the set has length n
