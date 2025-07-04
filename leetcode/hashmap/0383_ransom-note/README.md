# 383. Ransom Note

[🔗 LeetCode Link](https://leetcode.com/problems/ransom-note/description/)

## Solution

### Counter

#### Explanation

Just count the number of available letters in the magazine.
And the number of letters used in the note.

If the note use more letters than what's available,
we can't write.

#### Time Complexity

- O(n+m) -> We transverse both strings a single time.

#### Space Complexity

- O(1) -> We only 2 dicts with 26 elements at most.
