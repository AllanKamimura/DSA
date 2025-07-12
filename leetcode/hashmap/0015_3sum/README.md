# 15. 3Sum

[🔗 LeetCode Link](https://leetcode.com/problems/3sum/description/)

## Solution

### Hashmap counter

#### Explanation

The approach is very similar to [0001 - Two Sum](../0001_two-sum/).

We want to find triplets (x,y,z) where x + y + z = 0.

If we call our target = - x, 
we get the exactly same problem as before, y + z = target.

One point of attention is handling the duplicated triplets,
For this, we can store the triplets in a set.

Additionally, we take `x <= y <= z`,
so we don't check repeteaded values.

#### Manual Run

```python
nums = [0,0,0]
```

```python
counter = {0: 3}

i = 0, x = 0
    target = 0
    y = 0
        z = 0
        counter[0] = 3 > 2:
            result.add((0,0,0))
```

#### Time Complexity

- O(n²)
  - O(n): counter
  - O(n log(n)): sorting counter
  - O(n²): double nested loop, in worst case scenario we have all unique values and do n²/2 loops

#### Space Complexity

- O(n²)
  - O(n): counter
  - O(n): sorted counter
  - O(n²): results, in the worst case scenario, for every (x,y) pair a matching z exists in the nums array. This, however, is highly improbable, since most (x,y) pairs doesn't have a valid z value.
