from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            left_value = prices[left]
            right_value = prices[right]

            curr_profit = right_value - left_value
            if profit < curr_profit:
                profit = curr_profit

            if curr_profit < 0:
                left = right

            right += 1

        return profit
