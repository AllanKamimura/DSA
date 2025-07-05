from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)

        max_heap = [(-count, letter) for letter, count in counter.items()]
        heapify(max_heap)

        result = ""

        last_count = 1
        last_letter = "?"

        curr_count, letter = max_heap[0]

        if ((curr_count) * -1) > (n + 1) // 2:
            return result

        while max_heap:
            curr_count, letter = heappop(max_heap)

            result += letter

            if (last_count + 1) < 0:
                heappush(max_heap, (last_count + 1, last_letter))

            last_count = curr_count
            last_letter = letter

        return result
