# 283. Add Binary

[🔗 LeetCode Link](https://leetcode.com/problems/add-binary/description/)

## Solution

### Simple Sum

- Zero pad, so `len(a) == len(b)`
- Add a leading zero, to handle the case where the `len(answer) == max(len(a), len(b)) + 1`

#### Explanation

We simple iterate over all digits for both number and just sum it.

#### Time Complexity

- O(n) -> Iterate over all digits

#### Space Complexity

- O(n) -> The answer have size n
