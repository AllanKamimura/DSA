# 1189. Maximum Number Of Balloons

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-number-of-balloons/description/)

## Solution

### Counter

#### Explanation

We use a counter to count the number of instances of each letter in the string.

Since "l" and "o" appears twice in the word "ballon",
we need 2 of each for each word.

The upper limit of word instances is the character with lowest frequency,
thus we take the minimum of the counter for each letter.

#### Manual Run

```python
text = "nlaebolko"
Couter(text) = {'l': 2, 'o': 2, 'n': 1, 'a': 1, 'e': 1, 'b': 1, 'k': 1}

min(counter) = 1
return 1
```

#### Time Complexity

- O(n) -> We transverse the string a single time.

#### Space Complexity

- O(1) -> We create a dict with a maximum of 26 values.
