class Solution:
    # Sliding window with increasing size
    ## Use a hashset to keep track of unique values
    ## Start from left and check right
    ### If right not in set, increase right
    ### If right in set, move left
    ### Size of window at end is the largest size.

    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_letters = set()
        left = 0
        max_size = 0

        for right in range(len(s)):
            while s[right] in unique_letters:
                unique_letters.remove(s[left])
                left += 1

            unique_letters.add(s[right])
            max_size = max(max_size, right - left + 1)

        return max_size
