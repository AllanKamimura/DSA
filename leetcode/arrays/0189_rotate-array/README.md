# 189. Rotate Array

[🔗 LeetCode Link](https://leetcode.com/problems/rotate-array/description/)

## Solution

### In-place swaps

#### Explanation

Just swap the balues 1 by 1. 
Each `curr_index` points to a `next_index` that is k steps ahead.
When we swap the values, we keep the next_value for the next swap.

The `next_value` to swap is naturally the value in `next_index` before the swap,
but sometimes (depending on the divisors of n and the value of k) a cycle can occur.

To handle these cases, we keep track of the starting point, so when `next_index` 
points to the starting point, we know that we closed the loop.
When this happens, we just move to 1 step ahead.


#### Manual Run

```python
nums = [-1,-100,3,99]
k = 2
```

`curr_index` | `curr_value` | `next_index` | `next_value` | `closed_loop`
--- | --- | --- | --- | ---
0 | -1 | 2 |  3 | False
2 | 3  | 0 | -1 | True
1 | -100 | 3 | 99 | False
3 | 99 | 1 | -100 | True

#### Time Complexity

- O(n) -> We transverse the array a single time
    - `count` keeps track of the number of swaps

#### Space Complexity

- O(1) -> We only create integer variables.

### Split and Concatenate

#### Explanation

Just split the list at k from the end,
then concatenate the first half +  second half


#### Manual Run

```python
nums = [-1,-100,3,99]
k = 2

k_to_the_end = nums[-k] = [3, 99]
second_half = nums[: len(nums) - k] = [-1, -100]

k_to_the_end + second_half = [3, 99, -1, -100]
```

#### Time Complexity

- O(n) -> We create 2 copies of the array with size k and (n - k)

#### Space Complexity

- O(n) -> We create 2 copies of the array with size k and (n - k)

### Reverse/Reverse

#### Explanation

Perform a sequence of clever reverses.

1. Reverse whole list.
    1. This puts the k values that "pass" to the other side at the start.
2. Reverse each part.
    1. This corrects the order of the elements.

#### Manual Run

```python
nums = [-1,-100,3,99]
k = 2

reverse_nums = [99, 3, -100, -1]
reverse_start = [3, 99, -100, -1]
reverse_end = [3, 99, -1, -100]

```

#### Time Complexity

- O(n) -> We create 2 copies of the array with size k and (n - k)

#### Space Complexity

- O(n) -> We create 2 copies of the array with size k and (n - k)
