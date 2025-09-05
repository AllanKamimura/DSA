from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {}
        operators["+"] = lambda x, y: x + y
        operators["-"] = lambda x, y: x - y
        operators["*"] = lambda x, y: x * y
        operators["/"] = lambda x, y: x / y

        stack = []

        for token in tokens:
            if token in operators:
                y = int(stack.pop())
                x = int(stack.pop())

                stack.append(int(operators[token](x, y)))

            else:
                stack.append(token)

        return int(stack[0])
