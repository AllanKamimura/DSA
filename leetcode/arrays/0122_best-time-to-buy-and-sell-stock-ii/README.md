# 122. Best Time To Buy And Sell Stock Ii

[🔗 LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

## Solution

### 2 pointers approach

#### Explanation
We start 2 pointers, today and tomorrow. 
Today is going to point to the current price,
while tomorrow is going to point to the price in the next day.

Basically, since we can buy and sell as many times we want,
we buy every time when the price is going to raise in the following day.
This is going to effectivelly wield the maximum profit, since we are
garanteed to sell at every local maximum.


#### Manual Run

```python
prices = [1,2,3,4,5]
profit = 0

today_value = 1, tomorrow_value = 2, profit += 1
today_value = 2, tomorrow_value = 3, profit += 1
today_value = 3, tomorrow_value = 4, profit += 1
today_value = 4, tomorrow_value = 5, profit += 1

total_profit = 4
```


#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
