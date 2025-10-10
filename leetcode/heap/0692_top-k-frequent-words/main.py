import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = [(-1 * freq, word) for word, freq in count.items()]

        heapq.heapify(heap)

        output = []

        for _ in range(k):
            _, word = heapq.heappop(heap)

            output.append(word)

        return output
