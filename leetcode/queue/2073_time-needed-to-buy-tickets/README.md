# 2073. Time Needed To Buy Tickets

[🔗 LeetCode Link](https://leetcode.com/problems/time-needed-to-buy-tickets/description/)

## Solution

### Just do it

#### Explanation

This problem is pretty straightforward.

- All people in front of the queue needs to,
either buy all their tickets or `tickets[k]`, which ever comes first.
- All people behind needs to,
either buy all their tickets or `tickets[k] - 1`, which ever comes first.

#### Manual Run

```python
tickets = [2,3,2], k = 2
```

index | bought_tickets
-- | ---
0 | 2
1 | 2
2 | 2

```python
return counter = 6
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
