# 201. Bitwise And Of Numbers Range

[🔗 LeetCode Link](https://leetcode.com/problems/bitwise-and-of-numbers-range/description/)

## Solution

### Bit Manipulation

#### Explanation

First, we need to build an intuition about this problem, we start with a simple example.

```shell
10000
10001  --- left
10010
10011
10100
10101
10110
10111
11000
11001
11010
11011
11100
11101 --- right
11110
11111
```

By moving around the left and right pointers, we get the intuition behind this question.

```shell
1 | 0001  --- left
1 | 0010
1 | 0011
1 | 0100
1 | 0101
1 | 0110
1 | 0111
1 | 1000
1 | 1001
1 | 1010
1 | 1011
1 | 1100
1 | 1101 --- right
```

Any sequence formed by `[left, right]` can be divided into 2 parts. The "**prefix**", it's the digits that are common to all numbers in this sequence. And the "**flips**", which are the digits that needs to be flipped at some point to get to one side to the other of the range.

Since we are applying the bitwise **AND**, any "**flips**" digits is going to be a 0, while any "**prefix**" digit is going to keep their original value.

So our problem narrows down to finding said "**prefix**", in other words, we need to find how many digits doesn't "**flips**".

#### Solution

So we go digit by digit starting from the end.

```shell
1000 | 0
1000 | 1  --- left 
1001 | 0
```

From this small example, it's intuitive that the only way for the end digit to not flip is if left == right.

So if it is a flip, we increase or `i` counter by 1, and right shift left and right, to get to the next digit.

```shell
100 | 0  --- left
100 | 1
101 | 0
101 | 1
110 | 0
110 | 1
111 | 0 --- right
```

#### Manual Run

i | left | right | equal
--|--|--| --
0 | 10001 | 11101 | False
1 | 1000 | 1110 | False
2 | 100 | 111 | False
3 | 10 | 11 | False
4 | 1 | 1 | True

```python
i = 4 (we have 4 flipped digits)
return left << 4 = 10000
```

#### Time Complexity

- O(1) -> In the worst case scenario, we iterate 32 times.

#### Space Complexity

- O(1) -> We only create integer variables.
