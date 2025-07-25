# 424. Longest Repeating Character Replacement

[🔗 LeetCode Link](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

## Solution

### Sliding Window and Hashmap Counter

#### Explanation

The core idea to solve this problem is to, given a window,
compute the number of swaps needed to make it valid.

This is done by taking the total number of characters in the window
and subtracting the number of times the most frequent character shows.

`swaps_needed = len(window) - max_frequency <= k`

Now we have 2 points, how to know the `max_frequency`
and how the windows changes size.

The logic to move or shrink the window is very similar to
[3. Longest Substring Without Repeating Characters](../0003_longest-substring-without-repeating-characters).

To find the `max_frequency`,
we can use a hashmap counter to keep track of the frequency of each letter
at each step, we update this value.

#### Manual Run

```python
s = "AABABBA", k = 1
```

left | right | curr_letter | letter_counter | curr_size | max_frequency | swaps_needed
0 | 0 | A | {A: 1} | 1 | 1 | 0
0 | 1 | A | {A: 2} | 2 | 2 | 0
0 | 2 | B | {A: 2, B: 1} | 3 | 2 | 1
0 | 3 | A | {A: 3, B: 1} | 4 | 3 | 1
0 | 4 | B | {A: 3, B: 2} | 4 | 3 | 2
1 | 5 | B | {A: 2, B: 3} | 4 | 3 | 2
2 | 6 | A | {A: 2, B: 3} | 4 | 3 | 2

```python
return max_size = 4
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> Counter has at most 26 elements.
