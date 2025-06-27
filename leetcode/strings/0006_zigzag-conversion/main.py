class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        magic_number = 2 * (numRows - 1)

        n = len(s)

        output = ""

        for i in range(numRows):
            j = 0

            while True:
                index = j * magic_number + i

                if index >= n:
                    break
                output += s[index]

                # For middle rows, add the second character in the zigzag pattern
                if i != 0 and i != numRows - 1:
                    second_index = (j + 1) * magic_number - i
                    if second_index >= n:
                        break
                    output += s[second_index]

                j += 1

        return output
