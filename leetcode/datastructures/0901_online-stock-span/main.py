class StockSpanner:
    def __init__(self):
        self.values_stack = []
        self.streak_stack = []

    def next(self, price: int) -> int:
        curr_streak = 1

        while self.values_stack and self.values_stack[-1] <= price:
            self.values_stack.pop()
            prev_streak = self.streak_stack.pop()
            curr_streak += prev_streak

        self.values_stack.append(price)
        self.streak_stack.append(curr_streak)

        return curr_streak


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
