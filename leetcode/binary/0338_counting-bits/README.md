# 338. Counting Bits

[🔗 LeetCode Link](https://leetcode.com/problems/counting-bits/description/)

## Solution

### Naive Solution

#### Explanation

Use the `hammingWeight` solution from [0191 - Number of 1 bits](../0191_number-of-1-bits/README.md) to count the number of bits for each number.

#### Manual Run

```python
n = 5

number = 0, hammingWeight(0) = 0
number = 1, hammingWeight(0) = 1
number = 2, hammingWeight(0) = 1
number = 3, hammingWeight(0) = 2
number = 4, hammingWeight(0) = 1
number = 5, hammingWeight(0) = 2
```

#### Time Complexity

- O(n) -> We transverse the array a single time, and `hammingWeight` is O(1).

#### Space Complexity

- O(n) -> We create the `counter_list` array of size n.

---

### Dynamic Programming

#### Explanation

Start from a known value, n = 0 => countBits = 0, we compute the next value based on the last digit.

The numeric value and the index of the list matches, so `counter_list[number >> 1]` is going to take the count value at position `number // 2`.
Since we known the value for 0, and we transverse the range(1,n), the count value at position `number // 2` is already computed at each time.

`(number & 1)` is going to take the bit value of the last digit, this can be either 0 or 1.

Then, we sum the count value of the right shifted number and increase it by the bit value of the last digit.

#### Manual Run

```python
n = 5
```

number | `number // 2` | `number & 1` | `counter_list`
--- | --- | --- | --- 
0 | 0 | 0 | [0]
1 | 0 | 1 | [0, 1]
2 | 1 | 0 | [0, 1, 1]
3 | 1 | 1 | [0, 1, 1, 2]
4 | 2 | 0 | [0, 1, 1, 2, 1]
5 | 2 | 1 | [0, 1, 1, 2, 1, 2]


#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(n) -> We create the `counter_list` array of size n.

---
#### Final Consideraions

So even by taking a seemly smarter approach, 
which avoids unecessary recalculations,
we get no real gain in time or space complexity.