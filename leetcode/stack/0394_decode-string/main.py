class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sequence = ""
                while stack and stack[-1] != "[":
                    sequence = stack.pop() + sequence

                stack.pop()  # '['

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(int(multiplier) * sequence)

        return "".join(stack)
