# 3. Longest Substring Without Repeating Characters

[🔗 LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Solution

### Sliding window and Hashset Tracker

#### Explanation

We use a sliding window with increasing size to look for the substrings
and a hashset to keep track of the repeating characters.

The core logic is, starting from left and going right,
we start 2 pointers, left and right to mark the limits of the window.

If the new characters is not in the hashset,
we increase the window by moving right one step.

If it's a repeated character,
we move the window by moving the left pointer,
until the repeated character is out of the window.

Then, we keep track of the max_size by checking the size of the window.

#### Manual Run

```python
s = "abcabcbb"
```

left_letter | right_letter | unique_letters | repeated | substring 
--- | --- | --- | --- | ---
a | a | {a} | False | a
a | b | {a, b} | False | ab
a | c | {a, b, c} | False | abc
a | a | {a, b, c} | True | bca
b | b | {a, b, c} | True | cab
c | c | {a, b, c} | True | abc
b | b | {b, c} | True | cb
b | b | {b} | True | b

```python
return max_size = 3
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> In the worst case, unique_letters has all the unique characters.
