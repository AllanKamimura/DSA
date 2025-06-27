# 334. Increasing Triplet Subsequence

[🔗 LeetCode Link](https://leetcode.com/problems/increasing-triplet-subsequence/description/)

## Solution

### Greedy Capture Approach

#### Explanation

We create 2 variables, `first` and `second`, to keep track of possible candidates for `num_i` and `num_j`.

- `first`
  - it's the lowest number found so far, if we find a lower number, we update this value
  - it marks the lower bound for `num_j` candidates
- `second` 
  - it's the lowest number found so far that is greater than `first`
  - this value is only updated if there is a `num_i` candidate smaller than this.

If we are able to find candidates to both first and second,
and find a number that is greater than second, this number is a `num_k` candidate.
So we break the loop.

#### Manual Run

```python
nums = [2,1,5,0,6]
```

first | second | num | num_k
--- | --- | --- | ---
inf | inf | 2   | False
2   | inf | 1   | False
1   | inf | 5   | False
1   | 5   | 0   | False
0   | 5   | 6   | True

One important thing to note is that the final values for first and second
doesn't represents the triplet, but rather candidates for the triplet
and actually any value that comes before the number was update can be a valid triplet

(2,5,6) and (1,5,6) are both valid, but (0, 5, 6) is not.

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
