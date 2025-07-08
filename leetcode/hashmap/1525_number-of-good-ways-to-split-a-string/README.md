# 1525. Number Of Good Ways To Split A String

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/)

## Solution

### Counter

#### Explanation

The core idea to solve the problem is to note that
we are spliting the string into 2 part:
the only way to add a letter to the right side
is to have it removed from the left side.

We can initialize an empty set and a counter.
The counter counts the occurence of each letter.

Then we iterate over each letter in the string.
for each letter, we add it to the set
and subtract one occurence from the counter.

When we pass over all occurences of a letter,
we remove it's key from the counter.

So the size of the set is going to keep track
how many unique letters we have on the right side.
And the size of the counter is going to keep track
how many letters we still have to see,
in another words, how many unique letters we have on the right side.

#### Manual Run

```python
s = "aacaba"
counter = {'a': 3, 'b': 1, 'c': 1}
```

letter | set | counter | result
--- | --- | --- | --- 
a | {a} | {'a': 2, 'b': 1, 'c': 1} | 0
a | {a} | {'a': 1, 'b': 1, 'c': 1} | 0
c | {a, c} | {'a': 2, 'b': 1} | 1
a | {a, c} | {'a': 1, 'b': 1} | 2
b | {a, b, c} | {'a': 1} | 2
a | {a, b, c} | {} | 2

```python
return result = 2
```

#### Time Complexity

- O(n) -> We transverse the array 2 times (counter + letter by letter).

#### Space Complexity

- O(1) -> Both set and counter has a maximum size of 26 (unique letters).
