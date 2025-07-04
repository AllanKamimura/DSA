# 1512. Number Of Good Pairs

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-good-pairs/description/)

## Solution

### Counter

#### Explanation

1. Count the instances of each number
2. The number of pairs is a combinatory problem
  1. Answer is binomial `C(n, 2) = n * (n-1) // 2`
3. Sum the result for each number

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
