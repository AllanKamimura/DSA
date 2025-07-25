from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_counter = Counter()

        left = 0
        max_frequency = 0
        max_size = 0

        for right in range(len(s)):
            curr_letter = s[right]

            letter_counter[curr_letter] += 1

            max_frequency = max(max_frequency, letter_counter[curr_letter])

            curr_size = (right - left) + 1

            swaps_needed = curr_size - max_frequency

            if swaps_needed > k:
                old_letter = s[left]
                letter_counter[old_letter] -= 1
                left += 1

            curr_size = (right - left) + 1

            max_size = max(max_size, curr_size)

        return max_size
