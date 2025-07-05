# 49. Group Anagrams

[🔗 LeetCode Link](https://leetcode.com/problems/group-anagrams/description/)

## Solution

### String Enconding + Hashmap

#### Explanation

We want to count anagrams using a hashmap,
The first thing we need to think about is:

"How to represent each anagram in a hashable way?"

We can divide it into 2 steps:

1. Represent the anagram
  1. We can use a list with letters as index `List["letter"] = count`
2. Make it hashable (imutable)
  1. Using Tuples

Assuming only 26 common lowercase letters, 
we create a 26 elements list,
each index representing a letter
and each value is the counter.

Using ASCI representation, we can match the letter to the index by shifiting it by `ord(a)` (the first letter)

We then iterate over the word counting letters,
and then convert this "encoded" word into a hashable tuple.

We store these anagrams in a hashmap,
where the key is the anagram and the value is the index it appeared.

#### Manual Run

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

index | word | encoded
-- | -- | --
0 | eat | (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
1 | tea | (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
2 | tan | (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
3 | ate | (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
4 | nat | (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
5 | bat | (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)


```python
{
  (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): [0,1,3]
  (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): [2,4]
  (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): [5]
}

return [strs[0,1,3], strs[2,4], strs[5]]
```

#### Time Complexity

- O(n * m) -> For each word in strs, for each letter in word.

#### Space Complexity

- O(n) -> In the worst case, anagram_index has n elements.
