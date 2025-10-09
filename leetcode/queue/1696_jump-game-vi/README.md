# 1696. Jump Game Vi

[🔗 LeetCode Link](https://leetcode.com/problems/jump-game-vi/description/)

## Solution

### Sliding Window + Dequeue

#### Explanation

The core idea is to use a deque as sliding window with k steps look behind.
We use it to keep track of the possible previous spots.

So for each spot,
we need to compute the maximum score we can have when we get there.

For this, we look k steps behind
and try to find which previous step had the maximum score.

#### Manual Run

```python
nums = [1,-1,-2,4,-7,3], k = 2
```

index | num | score | behind_window
--- | --- | --- | ---
0 | 1 | 1 | [(0, 1)]
1 | -1 | 0 | [(0, 1), (1, 0)]
2 | -2 | -1 | [(1, 0), (2, -1)]
3 | 4 | 4 | [(3, 4)]
4 | -7 | -3 | [(3, 4), (4, -3)]
5 | 3 | 7 | [(5, 7)]

```python
return behind_window[-1][1] = 7
```

#### Time Complexity

- O(n) -> We append and pop each value at most 1 time.

#### Space Complexity

- O(1) -> The queue has at most k elements.
