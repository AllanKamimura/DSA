# 14. Longest Common Prefix
[🔗 LeetCode Link](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Example 1

```shell
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

## Example 2

```shell
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Solution

### Just do it

#### Explanation

For each string in the list, iterate letter by letter,
until either a whole word is processed or
we find a letter that doesn't match.

#### Manual Run

```python
strs = ["flower","flow","flight"]
```

letter | string | common
--- | ---- | ----
f | flower | ""
f | flow | ""
f | flight | "f"
l | flower | "f"
l | flow | "f"
l | flight | "fl"
o | flower | "fl"
o | flow | "fl"
o | flight | "fl"

```python
break
return common = "fl"
```

#### Time Complexity

- O(n * m) -> We transverse the array a single time, and each time, we transverse all strings.

#### Space Complexity

- O(1) -> We only create integer variables.
