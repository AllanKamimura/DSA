# 202. Happy Number

[🔗 LeetCode Link](https://leetcode.com/problems/happy-number/description/)

## Solution

### Hashset with Seen Values

#### Explanation

We just use a hashset to store any already seen values,
if we see the same number 2 times,
it means we entered a cycle.

Since `1 <= n <= 2^31 - 1`, that means n has at most 10 digits.
The maximum digit is 9, therefore the maximum sum is 10 * 9 ** 2 = 810.

This means that any cycle must have less than 811 elements.

#### Manual Run

```python
n = 19
```

```python
seen = {
    19,
    82,
    68,
    100,
    1
}

return True
```

```python
n = 2
```

```python
seen = {
    2,
    4,
    16,
    37,
    58,
    145,
    42,
    20,
    4
}

return False
```

#### Time Complexity

- O(1) -> In the worst case, it takes 811 elements to find a cycle.

#### Space Complexity

- O(1) -> In the worst case, we store 811 values in seen.

### Cycle Detection with Fast and Slow

We can use the fast/slow pointer approach to detect cycles.
The faster pointer moves 2 steps at a time,
while the slow pointer moves 1 step at a time.

If there is a cycle,
at some point, fast and slow would be at the same position.

#### Time Complexity

- O(1) -> In the worst case, it takes 811 elements to find a cycle.

#### Space Complexity

- O(1) -> In the worst case, we store 811 values in seen.