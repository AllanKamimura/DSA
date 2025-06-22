# 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


## Example 1

```shell
Input: nums = [3,2,3]
Output: 3
```

## Example 2

```shell
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Example 2

```shell
Input: nums = [2,2,1,1,1,2,1]
Output: 1
```

## Solution

### Boyer-Moore Voting Algorithm

#### Explaination
Since we know that the majority number appears at least (n//2 + 1) times in the list, all the other numbers are going to appear at most (n//2) times. So the algorithm is going to cancel out all candidates, but the one that appears at least (n//2 + 1).



#### Manual Run

Example 3:

i  |value | candidate | count | zeroed
--- | --- | ---- | ---- | ---
0 | 2 | 2 | 1 | True
1 | 2 | 2 | 2 | False
2 | 1 | 2 | 1 | False
3 | 1 | 1 | 1 | True
4 | 1 | 2 | 2 | False
5 | 2 | 2 | 1 | False
6 | 1 | 2 | 2 | False

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
