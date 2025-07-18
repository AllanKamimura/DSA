# 643. Maximum Average Subarray I

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-average-subarray-i/description/)

## Solution

### Sliding Window

#### Explanation

The sliding window works similarly to a FIFO queue,
for each new element, we append it to the end of the queue and remove the first element.

Since we are only interested in the sum of the numbers over the window,
we don't really need to create a queue,
instead we use a variable `sum` in which we add the new numbers
and subtract the first value.

So first we fill out the window by iterating over the first k elements,
computing our initial average.

The we iterate over the rest of elements after k,
use the add/subtract logic to compute the sum over the window,
and update the max_average value accordingly.

#### Manual Run

```python
nums = [1,12,-5,-6,50,3], k = 4
```

i | num | sum | average
--- | --- | --- | ---
0 | 1  | 1  | -
1 | 12 | 13 | -
2 | -5 | 8  | -
3 | -6 | 2  | 0.5
4 | 50 | 51 | 12.75
5 | 3  | 42 | 10.5

```python
return max_average = 12.75
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
