# 260. Single Number Iii

[🔗 LeetCode Link](https://leetcode.com/problems/single-number-iii/description/)

## Solution

### XOR Operator

#### Explanation

When we apply the XOR Operator over all nums, `result = num1 ^ num2`, 
where `num1` and `num2` are the single numbers, since the duplicates
cancelts each other anyway.

To get the numbers separated, one approach is to split the nums array into 2 parts,
in such a way that `num1` and `num2` are in different splits.

We can use the `result` to find a digit where `num1` and `num2` are different,
in another words, find a `1` digit in `result`.

Then we can split the nums into groups based on this different digit.

#### Manual Run

```python
Input: nums = [1,2,1,3,2,5]
```

```python
001
010
001
011
010
101

resutl = 110
```

Then we split all nums that have the second digit 1.

```python
001 | 010
001 | 011
101 | 010
```

And apply the XOR inside each group.

```python
101 | 011

return [3, 5]
```

#### Time Complexity

- O(n) -> We transverse the array 2 times.

#### Space Complexity

- O(1) -> We only create integer variables.
