# 205. Isomorphic Strings

[🔗 LeetCode Link](https://leetcode.com/problems/isomorphic-strings/description/)

## Solution

### Dictionary

#### Explanation

First, the description is wrong, we also need to consider the inverse map.

Two strings s and t are isomorphic if the characters in s can be replaced to get t
and the characters in t can be replaced to get s.

We can create a dict that maps each letter to the character in the other string.

If we have a character in the map and try to store a different character,
then the string can't be translated in the other.

#### Manual Run

```python
s = "badc", t = "baba"

translate = {}
retranslate = {}
```

i | s_letter | t_letter | translate | retranslate
-- | -- | -- | -- | --
0 | b | b | b -> b | b -> b
1 | a | a | a -> a | a -> a
2 | d | b | d -> b | b -> d
3 | c | a | c -> a | a -> c

```python
break
return False
```

Note that in the original problem statement,
this could be a True, because we can map s into t,
but not t into s.

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(1) -> We create 2 dicts with 26 elements at most.
