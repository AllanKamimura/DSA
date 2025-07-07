# 792. Number Of Matching Subsequences

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-matching-subsequences/description/)

## Solution

### Hashmap

#### Explanation

The core idea is to use a hashmap
to map characters to a list of indices it appears.

For each word, we iterate over each character,
then, we check the possible positions for this character,
a valid position is greater than the position of the previous character.

If either, the character is not in the charmap
or we don't find a valid position for any character in the word,
the word is not a subsequence.

In this approach,
the index list in charmap is ordered,
since we add it by order it appears when we build the charmap,
so, we can leverage the valid index search with a bissect


#### Manual Run

```python
s = "dsahjpjauf"
s = "0123456789"
charmap = {
    d: [0],
    s: [1],
    a: [2,7],
    h: [3],
    j: [4,6],
    p: [5],
    u: [8],
    f: [9]
}
```

word | char | prev_index | valid_index
--- | --- | --- | ---
ahjpjau | a | -1 | 2
ahjpjau | h | 2 | 3
ahjpjau | j | 3 | 4
ahjpjau | p | 4 | 5
ahjpjau | a | 5 | 7
ahjpjau | u | 7 | 8
ja | j | -1 | 4
ja | a | -1 | 7
ahbwzgqnuk | a | -1 | 2
ahbwzgqnuk | h | 2 | 3
ahbwzgqnuk | b | 3 | break (not in charmap)
tnmlanowax | t | -1 | break (not in charmap)


```python
return 2
```

#### Time Complexity

- O(k  n  log(n))
  - We iterate over k words
  - In the worst case, k has n letters, we iterate over each letter
  - In the worst case, all letters are the same, so charmap[char] has n elements and bisect takes log(n)

#### Space Complexity

- O(n) -> Charmap has n elements
