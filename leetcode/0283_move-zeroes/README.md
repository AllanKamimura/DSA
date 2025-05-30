# 283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## Example 1

```shell
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

## Example 2

```shell
Input: nums = [0]
Output: [0]
```

## Solution

### Two pointers approach

```python
[0,1,0,3,12]

i = 0 # -> first = 0
j = 0 # -> second = 0
```

#### Explanation

While the first pointer keep track of the zeros, the second pointer looks for a non-zero value to swap.

#### Time Complexity

- O(n) -> In the worst case scenario,
    - The number of swaps is n/2
    - Consequently, the number of i steps is also n/2
    - j takes n steps

#### Space Complexity

- O(1) -> We only create integer variables
