# 164. Maximum Gap

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-gap/description/)

## Solution

### Bucket sort

#### Explanation

The intuition behind this problem is really hard to grasp in the first time.

First, we need to start with some mathematics.

Let `min_value` and `max_value` be the min and max values in the nums list.

So all numbers are contained in the `range_ = [min_value, max_value]`.

If we have all numbers evenly distributed in this range,
the gap between any two adjacent numbers would be

`gap = range_ / (n - 1)`, where n is the length of the nums array.

Imagine that we try to decrease this gap by moving a number to the right. At the same time we would increase the gap between this number and the number to the left.

Intuitively, the evenly distributed numbers create the minimum "max gap". So, the following must be true.

`max_gap >= range_ / (n - 1)`

So if we use this size as the width size of the bucket, we guarantee that the max gap won't occur inside the buckets, but between 2 numbers in different buckets.

To map each value to its respective bucket, we use a simple logic. That is how many bucket widths are in between the current number and the min_value.

`bucket_index = (num - min_value) // bucket_size`



#### Manual Run

```python
nums = [21,9,25,3,37,43,49,29]
min_value = 3
n_buckets = 7
```

num | bucket_index | buckets
--- | ---- | ----
21 | 2 | [[],[],[21],[],[],[],[]]
9 | 0 | [[9],[],[21],[],[],[],[]]
25 | 3 | [[9],[],[21],[25],[],[],[]]
3 | 0 | [[3,9],[],[21],[25],[],[],[]]
37 | 4 | [[3,9],[],[21],[25],[37],[],[]]
43 | 5 | [[3,9],[],[21],[25],[37],[43],[]]
49 | 6 | [[3,9],[],[21],[25],[37],[43],[49]]
29 | 6 | [[3,9],[],[21],[25,29],[37],[43],[49]]

#### Time Complexity

- O(n) → We transverse the array a single time.
  - O(n) → Checking the min/max inside the buckets. Since each value can only be in 1 bucket, we only compare it once.

#### Space Complexity

- O(n) → The bucket holds n elements.
