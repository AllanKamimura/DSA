# 933. Number Of Recent Calls

[🔗 LeetCode Link](https://leetcode.com/problems/number-of-recent-calls/description/)

## Solution

### Queue

#### Explanation

The idea is to use a queue to store the requests,
when the current time exceeds 3000 + queue[0],
we expire the request at queue[0].

#### Manual Run

ping | queue
--- | ---
1 | [1]
100 | [1, 100]
3001 | [1, 100, 3001]
3002 | [100, 3001, 3002]

#### Time Complexity

- O(n) -> Since we pop the first value in the list, all values are shifted to the left.

#### Space Complexity

- O(1) -> The queue has at most 3000 elements.
