class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        look_ahead = {letter: i for i, letter in enumerate(s)}
        stack = []

        for i, letter in enumerate(s):
            if letter not in stack:
                while stack and stack[-1] > letter and look_ahead[stack[-1]] > i:
                    stack.pop()

                stack.append(letter)

        return "".join(stack)
