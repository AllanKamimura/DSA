# 767. Reorganize String

[🔗 LeetCode Link](https://leetcode.com/problems/reorganize-string/description/)

## Solution

### Heap + Counter

#### Explanation

First, we start counting the frequency of each letter in the string.

To get an intuition of the impossible cases, we start by drawing some examples:

```python
s = "ab"
s = "aab"
s = "aabb"
s = "aaabb"
s = "aaabbb"
s = "aaaabbb"
```

Length | Max repeats
-- | --
2 | 1
3 | 2
4 | 2
5 | 3
6 | 3
7 | 4

If we want to have k repeated "a"'s, we must have at least (k-1) non "a"'s
So, we can generalize it to: `max_repeats <= (length + 1) // 2`

---

To solve the problem, we can think of starting with an empty string
and take letter by letter to create the final result.
At each step, we take the letter that we current have the most,
without taking the same letter as the previous step.

This really sounds like a heap, ordered by the frequency of the character.
To avoid taking the same character two times in a row,
we can simply keep track of the last picked value:

1. Pop last value
2. Pick new value
3. Put the popped value back

#### Manual Run

```python
s = "aaaabbbcc"
max_heap = [
    (-4, 'a'),
    (-3, 'b'),
    (-2, 'c')
]
```

heap_start| last_letter | curr_letter | curr_count | heap_after
--- | --- | --- | --- | ----
[(-4, 'a'), (-3, 'b'),(-2, 'c')] | ? | a | 4 | [(-3, 'b'),(-2, 'c')]
[(-3, 'b'),(-2, 'c')] | a | b | 3 | [(-3, 'a'),(-2, 'c')]
[(-3, 'a'),(-2, 'c')] | b | a | 3 | [(-2, 'b'),(-2, 'c')]
[(-2, 'b'),(-2, 'c')] | a | b | 2 | [(-2, 'a'),(-2, 'c')]
[(-2, 'a'),(-2, 'c')] | b | a | 2 | [(-2, 'c'),(-1, 'b')]
[(-2, 'c'),(-1, 'b')] | a | c | 2 | [(-1, 'a'),(-1, 'b')]
[(-1, 'a'),(-1, 'b')] | c | a | 1 | [(-1, 'b'),(-1, 'c')]
[(-1, 'b'),(-1, 'c')] | a | b | 1 | [(-1, 'c')]
[(-1, 'c')] | b | c | 1 | []

```python
return "ababacabc"
```

#### Time Complexity

- O(n log(n))
  - O(n): To count characters we iterate over the string
  - O(n): To create and heapfy the count list
  - O(n): Iterate over each character in the string
    - O(log(n)): Pop and Push the heap

#### Space Complexity

- O(n) -> Both Count and heap can have n elements
