# 238. Product Of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Example 1

```shell
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

## Example 2

```shell
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints:

```shell
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
```

## Solution

### Precomputed prefix and suffix arrays

#### Explaination

We start by creating 2 auxiliaries array, prefix and suffix.
The prefix array has the property where,
prefix[i] = product of all numbers before the ith
While for the suffix array,
sufix[i] = product of all numbers after the ith

In such a way, the element product is:

prefix[i] * sufix[i] = product of all elements but the ith

#### Manual Run

```python
nums = [a,b,c,d]
prefix = [1, a, ab, abc]

sufix = [d, cd, bcd, abcd]
sufix.reverse() = [abcd, bcd, cd, d]
sufix.pop(0) = [bcd, cd, d]
sufix.append(1) = [bcd, cd, d, 1]

prefix * sufix = [bcd, acd, abd, abc]
```

#### Time Complexity

- O(n) -> We transverse the array 3 times.

#### Space Complexity

- O(n) -> We create 3 copies of the array.

### In-place prefix and suffix arrays

#### Explaination

The same as before, but instead of creating separated arrays,
we just compute the same values using the output array directly.

#### Manual Run

```python
nums = [a,b,c,d]

# first loop (same as before)
output = [1, a, ab, abc]

# instead of reversing it 2 times, just iterate from the end

i = -1
product = 1
output = [1, a, ab, abc]

i = -2
product = d
output = [1, a, abd, abc]

i = -3
product = cd
output = [1, acd, abd, abc]

i = -4
product = bcd
output = [bcd, acd, abd, abc]
```

#### Time Complexity

- O(n) -> We transverse the array 2 times.

#### Space Complexity

- O(1) -> Since we are using the outputs array directly.