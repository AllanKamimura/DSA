# 121. Best Time To Buy And Sell Stock

[🔗 LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Solution

### Two pointers approach

#### Explanation
We initialize 2 pointers, left and right, and a profit variable.
The left pointer is going to keep track of the lowest price found so far,
while the right pointer is going to "explore" the rest of the list.

Also, we are keeping track of the largest profit found so far, so we 
don't need to keep track of the right values.

When we calculate the curr_profit, if this is larger than the profit,
we update the max value.
If curr_profit is negative, it means we found a new lowest value,
so we move left to this value.

The right pointe always progress.

#### Manual Run

```python
prices = [7,1,5,3,6,4]
```

left | right | curr_profit | profit
---- | ----- | ----------- | ------
0 | 1 | -6 | 0
1 | 2 | 4 | 4
1 | 3 | 2 | 4
1 | 4 | 5 | 5
1 | 5 | 3 | 5

```python
return profit = 5
```
#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
