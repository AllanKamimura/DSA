class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr_url = homepage
        self.history_back = []
        self.history_forward = []

    def visit(self, url: str) -> None:
        self.history_back.append(self.curr_url)  # add the previous link to the hist
        self.history_forward.clear()
        self.curr_url = url

    def back(self, steps: int) -> str:
        i = 0
        while self.history_back and (i < steps):
            i += 1
            self.history_forward.append(self.curr_url)
            self.curr_url = self.history_back.pop()

        return self.curr_url

    def forward(self, steps: int) -> str:
        i = 0
        while self.history_forward and (i < steps):
            i += 1
            self.history_back.append(self.curr_url)
            self.curr_url = self.history_forward.pop()
        return self.curr_url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
