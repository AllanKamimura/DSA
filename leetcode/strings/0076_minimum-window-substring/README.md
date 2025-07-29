# 76. Minimum Window Substring

[🔗 LeetCode Link](https://leetcode.com/problems/minimum-window-substring/description/)

## Solution

### Dynamic Sliding Window and Hashmap Counter

#### Explanation

First, we need to start by defining the problem.

Basically, we are going to have 2 hashmap counters, `to_find` and `already_found`.
`to_find` is static, counted over the target `t`, while `already_found` is the counter at the current window.

The objective is to find a window such that:

- All characters from `to_find` is in `already_found`.
- For each character, the count in `already_found` is greater or equal than in `to_find`.

The window is defined by 2 pointer, `left` and `right`.

The main loop is, we increment right step by step,
if the `curr_letter` is one we are looking for (if it is in `to_find`),
we update our `already_found`.

When we completely find all in `to_find`,
we shrink the window from the left,
to try and find a smaller window that satisfies the requirements.

To keep track of our progress,
we use 2 variables, `required_matches` and `formed_matches`,
the first is the number of characters we need to complete,
completed means that we found all the needed occurences of this character.

#### Manual Run

```python
s = "ADOBECODEBANC", t = "ABC"
to_find = {"A": 1, "B": 1, "C": 1}
```

left | right | curr_letter | already_found | min_size
--- | --- | ---- | ---- | ----
0 | 0  | "A" | {"A": 1} | n
0 | 1  | "D" | {"A": 1} | n
0 | 2  | "O" | {"A": 1} | n
0 | 3  | "B" | {"A": 1, "B": 1} | n
0 | 4  | "E" | {"A": 1, "B": 1} | n
0 | 5  | "C" | {"A": 1, "B": 1, , "C": 1} | 6
1 | 5  | "C" | {"B": 1, "C": 1} | 6
1 | 6  | "O" | {"B": 1, "C": 1} | 6
1 | 7  | "D" | {"B": 1, "C": 1} | 6
1 | 8  | "E" | {"B": 1, "C": 1} | 6
1 | 9  | "B" | {"B": 2, "C": 1} | 6
1 | 10 | "A" | {"A": 1, "B": 2, "C": 1} | 6
2 | 10 | "A" | {"A": 1, "B": 2, "C": 1} | 6
3 | 10 | "A" | {"A": 1, "B": 2, "C": 1} | 6
4 | 10 | "A" | {"A": 1, "B": 1, "C": 1} | 6
5 | 10 | "A" | {"A": 1, "B": 1, "C": 1} | 6
6 | 10 | "A" | {"A": 1, "B": 1} | 6
6 | 11 | "N" | {"A": 1, "B": 1} | 6
6 | 12 | "C" | {"A": 1, "B": 1, "C": 1} | 6
7 | 12 | "C" | {"A": 1, "B": 1, "C": 1} | 6
8 | 12 | "C" | {"A": 1, "B": 1, "C": 1} | 5
9 | 12 | "C" | {"A": 1, "B": 1, "C": 1} | 4

```python
return min_size = 4
```

#### Time Complexity

- O(n) -> We traverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables, the counters have at most 26 elements.
