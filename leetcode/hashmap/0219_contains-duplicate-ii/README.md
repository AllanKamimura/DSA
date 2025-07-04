# 219. Contains Duplicate Ii

[🔗 LeetCode Link](https://leetcode.com/problems/contains-duplicate-ii/description/)

## Solution

### Hashmap

#### Explanation

Create a hashmap to keep track of the last time a number was seen.
Iterate over the nums, if we find a number that we already found in the past,
check the index it was last seen.

If the position it was previously seem is less than k,
then we found our number, otherwise, we update the last_seen position.

#### Manual Run

```python
nums = [1,2,3,1,2,3], k = 2
```

i | num | last_seen
--|--|--
0 | 1 | {1: 0}
1 | 2 | {1: 0, 2: 1}
2 | 3 | {1: 0, 2: 1, 3: 2}
3 | 1 | {1: 3, 2: 1, 3: 2}
4 | 2 | {1: 3, 2: 4, 3: 2}
5 | 3 |{1: 3, 2: 1, 3: 5}

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(n) -> In the worst case, the hashmap has n elements.
