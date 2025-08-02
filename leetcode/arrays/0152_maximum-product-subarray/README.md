# 152. Maximum Product Subarray

[🔗 LeetCode Link](https://leetcode.com/problems/maximum-product-subarray/description/)

## Solution

### Kadane's Algorithm Adapted

#### Explanation

Basically, we are going to use an approach similar to Kadane's Algorithm,
but with 2 accumulators, one for the `max_product` and another for the `min_product`.

The caveat here is that when `num < 0` and our `min_product` is negative,
the product `min_product * num` is going to be max,
and by the same logic,
the product `max_product * num` is going to be min.

So we can switch these values before accumulating.

#### Manual Run

```python
nums = [2,3,-2,4]
```

num | max_product | min_product | global_max
-- | --- | --- | ---
 2 | 2 | 2 | 2
 3 | 6 | 3 | 6
-2 | -2 | -12 | 6
 4 | 4 | -48 | 6

```python
return global_max = 6
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
