# 316. Remove Duplicate Letters

[🔗 LeetCode Link](https://leetcode.com/problems/remove-duplicate-letters/description/)

## Solution

### Greedy Monotonic Stack + Look-Ahead

#### Explanation

To grab an intuition about this problem,
we can start by drawing some examples.

```python
s = "bcabc"
```

We can just add the letters until we reach this point.

output = "bca", next = "b"

Here we need to decide which "b" we are going to keep.

1. If we take the new "b", the resulting string "cab" is greater than "bca", which fails the lexicographical order requirement.
2. If we skip past and stay with the old "b", when we reach the next value "c", we are going to end with "bac", which is greater than "abc".

So, the conclusion is,
we need to have some sort of look-ahead information to decide which b to keep. If we just look at the immediate result,
we are going to miss the correct answer.

With this, we can use a greedy approach with a monotonic stack.
The greedy algorithm is going to check if the current letter is less than the last element, in another words, if starting a new sequence with the current letter
is going to wield a lexicographical lower string.

Before we decide if we should remove a letter from the stack,
we first need to check if this letter is going to come back later,
so we don't miss the popped letter.

#### Manual Run

```python
s = "cbacdcbc"
```

letter | stack
--- | ---
c | [c]
b | [b]
c | [b,c]
d | [b,c,d]
c | [b,c,d]
a | [b,c,d,a]
b | [b,c,d,a]
c | [b,c,d,a]

```python
return stack = [b,c,d,a]
```

#### Time Complexity

- O(n) -> In the worst case scenario, We transverse the string 2 times. The first to add the letters to the stack, the second to remove the letters from the stack.

#### Space Complexity

- O(1) -> If we are using only 26 letters, this is the max size of the look-ahead, stack.
