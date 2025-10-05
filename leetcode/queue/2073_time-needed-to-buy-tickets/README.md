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

### Queue

#### Explanation

We can also simulate the queue,
where we go person by person buying a single ticket,
and going back to the end of the queue if they want to buy more tickets.

#### Manual Run

```python
tickets = [2,3,2], k = 2
```

index | tickets | queue
-- | ---
0 | [1, 3, 2] | [1, 2, 0]
1 | [1, 2, 2] | [2, 0, 1]
2 | [1, 2, 1] | [0, 1, 2]
0 | [0, 2, 1] | [1, 2]
1 | [0, 1, 1] | [2, 1]
2 | [0, 1, 0] | [1]


```python
return counter = 6
```

#### Time Complexity

- O(n * t) -> In the worst case, every person in the line buy a ticket `t` times.
  - O(n): for each person in the queue
  - O(t): each person in the queue goes back to the queue `t` times

#### Space Complexity

- O(n) -> We create a queue