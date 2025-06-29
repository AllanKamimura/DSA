# 217. Contains Duplicate

[🔗 LeetCode Link](https://leetcode.com/problems/contains-duplicate/description/)

## Solution

### Hashmap counter

#### Explanation

Uses a hashmap with the number as a key
and a counter as value.
Each time we see the value we increase the counter by 1.

At the end, we iterate over all values
and if any counter is bigger than 1, we have a duplicate.

#### Manual Run

```python
nums = [1,2,3,1]

num = 1, counter = {1: 1}
num = 2, counter = {1: 1, 2: 1}
num = 3, counter = {1: 1, 2: 1, 3: 1}
num = 1, counter = {1: 2, 2: 1, 3: 1}

count = 2
count = 1
count = 1

return True
```

#### Time Complexity

- O(n) -> We transverse the array 1 time + counter array 1 time.

#### Space Complexity

- O(n) -> In the worst case, counter has the same size as array

### Sort array

#### Explanation

We first sort the array, 
so the duplicated numbers are going to be next to each other.

#### Manual Run

```python
nums = [1,2,3,1]
nums_sorted = [1,1,2,3]

nums[1] = 1
nums[0] = 1

return True
```

#### Time Complexity

- O(n * log(n)) -> Sorting part.

#### Space Complexity

- O(1) -> Inplace sort.
