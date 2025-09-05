from typing import List


class Solution:
    operators = {}
    operators["+"] = lambda x, y: x + y
    operators["-"] = lambda x, y: x - y
    operators["*"] = lambda x, y: x * y
    operators["/"] = lambda x, y: x / y

    def calculate(self, s: str) -> int:
        stack = self.preprocess(s)
        stack = self.do_product(stack)
        stack = self.do_sum(stack)

        return int(stack[0])

    def preprocess(self, s: str) -> List:
        s = s.replace(" ", "")
        s = s.replace("+", " + ")
        s = s.replace("-", " - ")
        s = s.replace("*", " * ")
        s = s.replace("/", " / ")

        return s.split(" ")

    def do_product(self, s: List) -> List:
        stack = []

        i = 0

        while i < len(s):
            token = s[i]
            if token == "*" or token == "/":
                first = int(stack.pop())
                i += 1
                second = int(s[i])
                stack.append(int(self.operators[token](first, second)))

            else:
                stack.append(token)

            i += 1

        return stack

    def do_sum(self, s: List) -> List:
        stack = []

        i = 0

        while i < len(s):
            token = s[i]
            if token == "+" or token == "-":
                first = int(stack.pop())
                i += 1
                second = int(s[i])
                stack.append(int(self.operators[token](first, second)))

            else:
                stack.append(token)

            i += 1

        return stack
