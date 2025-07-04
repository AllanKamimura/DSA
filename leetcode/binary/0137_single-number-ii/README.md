# 137. Single Number Ii

[🔗 LeetCode Link](https://leetcode.com/problems/single-number-ii/description/)

## Solution

### Bit Manipulation

#### Explanation

Basically, for each digit, we iterate over the list and count the number of 1 bits
for that digit.
Since all number are repetead 3 times, we expect this count to be a multiple of 3.

But because of the single number, some of the digits are going to have a count that
is `count % 3 == 1`.

We can then reconstruct the single number by looking at all digits with this count.


#### Manual Run

```python
nums = [2,2,3,2]
counts = [4, 1]

return 10 = bin(3) 
```


#### Time Complexity

- O(n) -> We transverse the array 32 times.

#### Space Complexity

- O(1) -> We only create a 32 lenght list and intereger variables.
