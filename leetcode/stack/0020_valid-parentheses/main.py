class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for symbol in s:
            if symbol in pairs:
                open_symbol = pairs[symbol]

                if not stack or stack[-1] != open_symbol:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(symbol)

        return len(stack) == 0
