class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s_list = list(s)

        i = 0
        write_to = 0

        # find leading spaces
        while (i < n) and s_list[i] == " ":
            i += 1

        while i < n:
            curr_value = s_list[i]

            if s_list[i] == " ":
                if (write_to > 0) and s_list[write_to - 1] != " ":
                    s_list[write_to] = curr_value
                    write_to += 1
            else:
                s_list[write_to] = curr_value
                write_to += 1

            i += 1

        end = write_to - 1

        while (end >= 0) and s_list[end] == " ":
            end -= 1

        s_list = s_list[: end + 1]

        n = len(s_list)

        s_list.reverse()

        first, second = 0, 1

        while second <= n:
            if second == n or s_list[second] == " ":
                s_list[first:second] = reversed(s_list[first:second])
                first = second + 1
            second += 1

        return "".join(s_list)
