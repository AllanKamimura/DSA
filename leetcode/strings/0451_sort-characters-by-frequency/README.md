# 451. Sort Characters By Frequency

[🔗 LeetCode Link](https://leetcode.com/problems/sort-characters-by-frequency/description/)

## Solution

### Counter + Sort

#### Explanation

This questions is pretty straightforward,
we can just directly count the occurrences of each letter,
then sort it and return it.

#### Manual Run

```python
s = "tree"
counter = {"t": 1, "r": 1, "e": 2}
return "eetr"
```

#### Time Complexity

- O(n) -> We traverse the string a single time.
  - O(n) -> Count the frequency of each letter
  - O(1) -> Since the counter dictionary has at most 52 elements, the sorting takes constant time.

#### Space Complexity

- O(n) -> The output have n letters
  - O(1) -> The counter dictionary has at most 52 elements
