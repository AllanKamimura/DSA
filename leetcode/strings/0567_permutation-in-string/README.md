# 567. Permutation In String

[🔗 LeetCode Link](https://leetcode.com/problems/permutation-in-string/description/)

## Solution

### Sliding window + Letter Frequency hashmap

#### Explanation

This is very similar to [438. Find All Anagrams In A String](../0438_find-all-anagrams-in-a-string).

But instead of return the indices of the anagrams, we just return True or False.

#### Manual Run

```python
s1 = "ab", s2 = "eidbaooo"
count1 = {"a": 1, "b": 1}
window = {"e": 1, "i": 1}
```

i | letterwindow
-- | --
2  | {"e": 1, "i": 1}
3  | {"d": 1, "i": 1}
4  | {"d": 1, "b": 1}
5  | {"a": 1, "b": 1}

```python
{"a": 1, "b": 1} == {"a": 1, "b": 1}
return True
```

#### Time Complexity

- O(n) -> We transverse the string a single time, each time we compare Counter.

#### Space Complexity

- O(1) -> Window and indices has 26 elements (number of unique letters)
