from typing import Tuple


class Solution:
    def baseSum(self, x: str, y: str, remainder: bool) -> Tuple[bool, str]:
        if remainder:
            if x == "1":
                if y == "1":
                    return True, "1"
                elif y == "0":
                    return True, "0"

            elif x == "0":
                if y == "1":
                    return True, "0"
                elif y == "0":
                    return False, "1"

        elif not remainder:
            if x == "1":
                if y == "1":
                    return True, "0"
                elif y == "0":
                    return False, "1"

            elif x == "0":
                if y == "1":
                    return False, "1"
                elif y == "0":
                    return False, "0"

    def addBinary(self, a: str, b: str) -> str:
        if (a == b) and (a == "0"):
            return "0"

        max_size = max(len(a), len(b))

        # left pad with 0 -> both same size
        a = a.zfill(max_size)
        b = b.zfill(max_size)

        # leading 0
        a = "0" + a
        b = "0" + b

        i = 0

        answer = ""
        remainder = False

        while i <= max_size:
            x = a[max_size - i]
            y = b[max_size - i]
            remainder, value = self.baseSum(x, y, remainder)

            answer = value + answer  # add new digit to the right
            i += 1

        return answer.lstrip("0")  # strip leading zero
