# 438. Find All Anagrams In A String

[🔗 LeetCode Link](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

## Solution

### Sliding window + Hashmap frequency counter

#### Explanation

To define an anagram, we use a Counter over the frequency of letters.

We use a slinding window approach over s.
This window has size len(p) and similarly we use a Counter to check for anagrams.

The main loop is:

- Add the new letter and remove the older letter
- Update the Counter
- compare the window Counter with the p Counter

#### Manual Run

```python
s = "cbaebabacd", p = "abc"

anagram = {"a": 1, "b": 1, "c": 1}
window = {"c": 1, "b": 1, "a": 1}

indices = [0]
```

i | letter_new | window | indices
4  | e | {"e": 1, "b": 1, "a": 1} | [0]
5  | b | {"e": 1, "b": 1, "a": 1} | [0]
6  | a | {"e": 1, "b": 1, "a": 1} | [0]
7  | b | {"b": 2, "a": 1} | [0]
8  | a | {"b": 1, "a": 2} | [0]
9  | c | {"c": 1, "b": 1, "a": 1} | [0, 6]
10 | d | {"c": 1, "d": 1, "a": 1} | [0, 6]

```python
return indices = [0,6]
```

#### Time Complexity

- O(n) -> We transverse the string a single time, each time we compare Counter.

#### Space Complexity

- O(1) -> Window and indices has 26 elements (number of unique letters)
