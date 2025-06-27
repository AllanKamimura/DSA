# 2348. Number Of Zero Filled Subarrays

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-zero-filled-subarrays/description/)

## Solution

### Two pointers approach

#### Explanation

We initialize 2 pointers, `left` and `right`.
The `right` point has 2 functions:

1. When `left` value is 0, `right` looks for the next non 0
    1. This is inside the first if block
    2. So we know the size of the substring

2. When `left` value is not 0, `right` looks for the next 0
    1. This is inside the elif block
    2. So we can start counting our substring

To compute the size of the substring,
we can just take the `left_index` and subtract it from the `right_index`
when right finds a non zero (end of the substring).

Because of combinatories, the total number of zeros in each substring is
x * (x + 1) / 2, where x is the size of the substring.

The `nums.append(10)` is a magic trick to handle the case where
`nums[-1] = 0`, 
in which the loop would break before we find the end of the substring.

Additionally, this also handles the case where `len(nums) = 1`, 
in which there is no right pointer.

#### Manual Run

```python
nums = [1,3,0,0,2,0,0,4]
nums+[10] = [1,3,0,0,2,0,0,4, 10]
```

left | left_value | right | right_value | zeros
--- | --- | --- | --- | ---
0 | 1 | 1 | 3 | 0
0 | 1 | 2 | 0 | 0
2 | 0 | 3 | 0 | 0
2 | 0 | 4 | 2 | 3
4 | 2 | 5 | 0 | 3
5 | 0 | 6 | 0 | 3
5 | 0 | 7 | 4 | 6
7 | 4 | 8 | 10 | 6

```python
return zeros = 6
```

---

```python
nums = [0,0,0,2,0,0]
nums+[10] = [0,0,0,2,0,0, 10]
```

left | left_value | right | right_value | zeros
--- | --- | --- | --- | ---
0 | 0 | 1 | 0 | 0
0 | 0 | 2 | 0 | 0
0 | 0 | 3 | 0 | 0
0 | 0 | 4 | 2 | 6
4 | 2 | 5 | 0 | 6
5 | 0 | 6 | 0 | 6
5 | 0 | 7 | 10 | 9

```python
return zeros = 9
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
