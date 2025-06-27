# 6. Zigzag Conversion
[🔗 LeetCode Link](https://leetcode.com/problems/zigzag-conversion/description/)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```shell
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

## Example 1

```shell
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

## Example 2

```shell
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```


## Solution

### Just do it

#### Explanation

First, we need to identify the repetition pattern formed by the zigzag.
For this, we can think only about the index position instead of the actual letters,
The easiest way is to draw some base examples and inductively assume this is valid for n.

```shell
0     4     8     12
1  3  5  7  9  11 13
2     6     10    14
```

```shell
0        6          12
1     5  7      11  13
2  4     8  10      14
3        9          15
```

```shell
0           8           16
1        7  9        15 17
2     6    10     14    18
3  5       11  13       19
4          12           20
```

Immediately, we notice a visual pattern
with columnn going straight down, for numrows steps
then going up diagonally, for (numrows - 2) steps.

So to build the rows:

- First and last rows only has the numbers in the main column
- Mid rows also has the diagonal numbers
  - It starts at 1 before the next column
  - For each row it goes one step back

#### Manual Run

```python
s = [0, 1, 2, ..., 10, 11, 12]
numrows = 5
```

```python
magic_number = 5 + 5 - 2 = 8

i = 0
    j = 0 -> index = 0
    j = 1 -> index = 8

i = 1
    j = 0 -> index = 1, second_index = 7
    j = 0 -> index = 9, second_index = 15 (15 > 12 -> break)

i = 2
    j = 0 -> index = 2, second_index = 6
    j = 0 -> index = 10, second_index = 14 (14 > 12 -> break)

i = 3
    j = 0 -> index = 3, second_index = 5
    j = 0 -> index = 11, second_index = 13 (13 > 12 -> break)

i = 4
    j = 0 -> index = 4
    j = 1 -> index = 12

return [0, 8, 1, 7, 9, 2, 6, 10, 3, 5, 11, 4, 12]
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(n) -> We create a new string of the same size of s.
