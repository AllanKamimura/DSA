from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        queue = deque([deck.pop()])

        while deck:
            card = deck.pop()
            prev_card = queue.pop()
            queue.appendleft(prev_card)
            queue.appendleft(card)

        return list(queue)
