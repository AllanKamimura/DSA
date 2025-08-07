# 78. Subsets

[🔗 LeetCode Link](https://leetcode.com/problems/subsets/description/)

## Solution

### Iterative Doubling

#### Explanation

The easiest way to get an intuition is to start with a sequence of length 0 and increase it 1 by 1.

```shell
[]
[1]
[2] [1,2]
[3] [1,3] [2,3] [1,2,3]
[4] [1,4] [2,4] [1,2,4] [3,4] [1,3,4] [2,3,4] [1,2,3,4]
```

Basically, at each step we double the quantity of subsets,
because you can just append the new number to each of the previous subsets to create a new subset.

#### Manual Run

Same as above

#### Time Complexity

- O(2^n) -> We transverse the array a single time.

#### Space Complexity

- O(2^n) -> The result has 2^n subsets.
