from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        biggest = 0

        if not num_set:
            return biggest

        anchor = num_set.pop()
        counter = 1

        if not num_set:
            return counter

        next_steps = 1
        prev_steps = 1

        while num_set:
            next = anchor + next_steps
            prev = anchor - prev_steps
            if next in num_set:
                num_set.remove(next)
                counter += 1
                next_steps += 1
                if counter > biggest:
                    biggest = counter
            elif prev in num_set:
                num_set.remove(prev)
                counter += 1
                prev_steps += 1
                if counter > biggest:
                    biggest = counter
            else:
                anchor = num_set.pop()
                counter = 1
                next_steps = 1
                prev_steps = 1

        return biggest
