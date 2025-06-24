from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today = 0
        tommorow = 1

        profit = 0

        while tommorow < len(prices):
            today_value = prices[today]
            tommorow_value = prices[tommorow]

            curr_profit = tommorow_value - today_value

            if curr_profit <= 0:
                pass

            else:
                profit += curr_profit

            today = tommorow
            tommorow += 1

        return profit
