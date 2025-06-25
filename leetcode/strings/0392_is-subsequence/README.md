# 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## Example 1

```shell
Input: s = "abc", t = "ahbgdc"
Output: true
```

## Example 2

```shell
Input: s = "axc", t = "ahbgdc"
Output: false
```


## Solution

### Two pointers approach

#### Explanation

We start 2 pointer, i and j, one at the start of `s` the other on `t`.
For each value that j points to, we check if i points to the same value
If it's a match, we move i to the next value.
While j always move forward.

This way, i acts as a counter of the number of matches,
so if number of matches equals to `len(s)`, so `s` is a subsequence of `t`.

#### Manual Run

```python
s = "abc", t = "ahbgdc"
```

j | i | t_value | s_value
--|--|--|--
0 | 0 | a | a
1 | 1 | h | b
2 | 1 | b | b
3 | 2 | g | c
4 | 2 | d | c
5 | 2 | c | c

```python
i == len(s) == 3
return True
```

#### Time Complexity

- O(n+m) -> We transverse each string a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
