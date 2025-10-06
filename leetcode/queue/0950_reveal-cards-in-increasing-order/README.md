# 950. Reveal Cards In Increasing Order

[🔗 LeetCode Link](https://leetcode.com/problems/reveal-cards-in-increasing-order/description/)

## Solution

### Queue

#### Explanation

We can just simulate the problem using a queue.
Since we want to reconstruct the input,
we go backwards.

First we sort the numbers

Starting with a deck with the last card.

1. Take the last card and put it on the top
2. Add the next card of the deck to the top.

#### Manual Run

```python
deck = [17,13,11,2,3,5,7]
deck.sort()
deck = [2,3,5,7,11,13,17]

queue = [17]
```

card | prev_card | queue
--- | --- | ----
13 | 17 | [13, 17]
11 | 17 | [11, 17, 13]
7 | 13 | [7, 13, 11, 17]
5 | 17 | [5, 17, 7, 13, 11]
3 | 11 | [3, 11, 5, 17, 7, 13]
2 | 13 | [2, 13, 3, 11, 5, 17, 7]

#### Time Complexity

- O(n ⋅ log(n)) -> We sort the array at the start.
  - O(n): For each card of the deck, we pop and left append twice.

#### Space Complexity

- O(n) -> The deck and queue are complementary and together has n elements.
