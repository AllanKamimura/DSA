from typing import List


class Solution:
    """
    - i < j < k
        - Not necessary consecutive sequence

    - num_i < num_k < num_j

    """

    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False

        stack = []
        k_candidate = float("-Inf")

        for num in nums[::-1]:
            if len(stack) >= 2 and num not in stack and num < k_candidate:
                return True

            while stack and stack[-1] >= num:
                stack.pop()

            stack.append(num)
            k_candidate = max(stack[0], k_candidate)

        return False
