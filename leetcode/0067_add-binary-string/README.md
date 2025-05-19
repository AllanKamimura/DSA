# 283. Add Binary

Given two binary strings a and b, return their sum as a binary string.

## Example 1

```shell
Input: a = "11", b = "1"
Output: "100"
```

## Example 2

```shell
Input: a = "1010", b = "1011"
Output: "10101"
```

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