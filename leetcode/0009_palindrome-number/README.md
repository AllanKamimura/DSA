# 9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

## Example 1

```shell
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

## Example 2

```shell
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

## Example 3

```shell
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Solution

### Two pointers approach

```python
x = 1331

i = 0 # -> left = 1
j = 3 # -> right = 1
```

#### Explaination

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
