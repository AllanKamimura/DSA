class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        track = 0
        best_track = track

        for symbol in s:
            match symbol:
                case "(":
                    stack.append(symbol)
                case ")":
                    if len(stack) == 0:
                        track = 0

                    elif stack.pop() == "(":
                        track += 2
                        if len(stack) == 0:
                            best_track += track
                            track = 0
                    else:
                        track = 0

        best_track = max(best_track, track)
        return best_track
