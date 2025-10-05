from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        people_queue = deque(range(len(tickets)))

        counter = 0

        while tickets[k] != 0:
            curr_person = people_queue.popleft()

            curr_ticket = tickets[curr_person]

            if curr_ticket > 0:
                tickets[curr_person] -= 1
                counter += 1

                if tickets[curr_person] > 0:
                    people_queue.append(curr_person)

        return counter
