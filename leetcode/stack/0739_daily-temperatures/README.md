# 739. Daily Temperatures

[🔗 LeetCode Link](https://leetcode.com/problems/daily-temperatures/description/)

## Solution

### Monotonic Stack

#### Explanation

The main idea is to use a monotonic stack to keep track of the past temperatures,
we keep the values there until we find a day with a higher temperature.

#### Manual Run

```python
temperatures = [73,74,75,71,69,72,76,73]
```

day | current | stack | output
0 | 73 | [73] | [0,0,0,0,0,0,0,0]
1 | 74 | [74] | [1,0,0,0,0,0,0,0]
2 | 75 | [75] | [1,1,0,0,0,0,0,0]
3 | 71 | [75,71] | [1,1,0,0,0,0,0,0]
4 | 69 | [75,71,69] | [1,1,0,0,0,0,0,0]
5 | 72 | [75,72] | [1,1,0,2,1,0,0,0]
6 | 76 | [] | [1,1,4,2,1,1,0,0]
7 | 73 | [] | [1,1,4,2,1,1,0,0] 

```python
return output = [1,1,4,2,1,1,0,0]
```

#### Time Complexity

- O(n) -> We transverse the array a single time. Each element is removed from the stack a single time.

#### Space Complexity

- O(n) -> In the worst case scenario, the stack has n elements.
