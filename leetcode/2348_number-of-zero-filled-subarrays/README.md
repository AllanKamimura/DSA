# 2348. Number Of Zero Filled Subarrays

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

## Example 1

```shell
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6

Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

## Example 2

```shell
Input: nums = [0,0,0,2,0,0]
Output: 9

Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
```

## Example 3

```shell
Input: nums = [2,10,2019]
Output: 0

Explanation: There is no subarray filled with 0. Therefore, we return 0.

```

## Solution

### Two pointers approach

#### Explaination

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
