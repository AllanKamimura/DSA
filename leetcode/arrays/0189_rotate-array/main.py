from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # this handles the case where k > len(nums)
        n = len(nums)
        k %= n

        curr_index = 0
        curr_value = nums[curr_index]
        next_index = (curr_index + k) % n
        count = 0

        for start_point in range(n):
            if count >= n:
                break

            curr_index = start_point
            curr_value = nums[curr_index]

            while next_index != start_point:
                next_index = (curr_index + k) % n
                next_value = nums[next_index]

                nums[next_index] = curr_value
                curr_value = next_value
                curr_index = next_index

                count += 1

        return nums
