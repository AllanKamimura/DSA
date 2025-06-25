# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Example 1

```shell
Input: s = "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.
```

## Example 2

```shell
Input: s = "race a car"
Output: false

Explanation: "raceacar" is not a palindrome.
```

## Example 3

```shell
Input: s = " "
Output: true

Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Solution

### Two pointers approach

#### Explanation


We start 2 pointers, one at the start and one at the end.
At each step, we check if the letter it points are the same,
if yes, we move 1 step inwards, if not, the string is not a 
palindrome.

#### Manual Run

```python
s = "amanaplanacanalpanama"
```

start | end | start_value | end_value | match
--- | --- | ---- | ---- | ---
0 | 20 | a | a | True
1 | 19 | m | m | True
2 | 18 | a | a | True
3 | 17 | n | n | True
4 | 16 | a | a | True
5 | 15 | p | p | True
6 | 14 | l | l | True
7 | 13 | a | a | True
8 | 12 | n | n | True
9 | 11 | a | a | True

```python
return True
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
