# 36. Valid Sudoku

[🔗 LeetCode Link](https://leetcode.com/problems/valid-sudoku/description/)

## Solution

### Hashsets

#### Explanation

This problem is pretty straightforward, no brain time.

Just create a hashset for each of the rows, cols and boxes.

Then iterate over the entire array
and check if the number is already in the hashset
or if we should add it to the hashset.

#### Manual Run

There is no secret here, just a 81 lines loop.

#### Time Complexity

- O(n²) -> We visit each number 1 time.

#### Space Complexity

- O(n²) -> We create 3 hashsets with the same size of the matrix.
