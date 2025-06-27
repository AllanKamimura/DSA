# 9. Palindrome Number

[🔗 LeetCode Link](https://leetcode.com/problems/palindrome-number/description/)

## Solution

### Two pointers approach

```python
x = 1331

i = 0 # -> left = 1
j = 3 # -> right = 1
```

#### Explanation

We start 2 pointers, one at the start and one at the end.
At each step, we check if the digit it points are the same,
if yes, we move 1 step inwards, if not, the number is not a 
palindrome.

#### Manual Run

```python
x = 1331

# iter 0
    # i = 0 -> left = 1
    # j = 3 -> right = 1
    # left == right -> i = 1, j = 2
    # i < j -> continue

# iter 1
    # i = 1 -> left = 3
    # j = 2 -> right = 3
    # left == right -> i = 2, j = 1
    # i > j -> break
    # return True

```

#### Time Complexity

- O(n) -> At the worst case scenario, we take n/2 steps to check all digits.

#### Space Complexity

- O(1) -> We only create integer variables
